from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount

MOUNT_SOURCE = Mount(
    source="/home/yehuda/garbage/hw3data",
    target="/data",
    type='bind'
)

FAKE_DATA_DIR = "/data/models/{{ ds }}"
RAW_DATA_DIR = "/data/raw/{{ ds }}"
PP_DATA_DIR = "/data/processed/{{ ds }}"
MODEL_DIR = "/data/models/{{ ds }}"
PREDICT_DIR = "/data/predictions/{{ ds }}"


NUM_SAMPLES = 100
SAMPLE_FILE = "data_sample.csv"

default_args = {
    "owner": "Igor Itkin aka BukaByaka",
    "email": ["ig.itkin@gmail.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
        "data_generator",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=days_ago(0),
) as dag:
    generate = DockerOperator(
        image="airflow-generate-fake",
        command=f"--date-sample /data/{SAMPLE_FILE} --out_dir {FAKE_DATA_DIR} --number-of-samples {NUM_SAMPLES}",
        task_id="docker-airflow-generate-fake",
        do_xcom_push=False,
        network_mode="bridge",
        mounts=[Mount(source="/home/yehuda/garbage/data/fake", target="/data", type='bind')]
    )

    move = DockerOperator(
        image="airflow-move",
        command=f"--input-dir {FAKE_DATA_DIR} --output-dir {RAW_DATA_DIR}",
        task_id="docker-airflow-move",
        do_xcom_push=False,
        network_mode="bridge",
        # Do we need mount here?
        mounts=[Mount(source="/home/yehuda/garbage/data/fake", target="/data", type='bind')]
    )

    # Here the model is the preprocessor!
    preprocess = DockerOperator(
        image="airflow-preprocess",
        command=f"--model_dir {MODEL_DIR} --input-dir {RAW_DATA_DIR}--output_dir {PP_DATA_DIR}",
        task_id="docker-airflow-preprocess",
        do_xcom_push=False,
        network_mode="bridge",
        mounts=[MOUNT_SOURCE])

    predict = DockerOperator(
        image="airflow-predict",
        command=f"--model_dir {MODEL_DIR} --input-dir {PP_DATA_DIR}--output_dir {PREDICT_DIR}",
        task_id="docker-airflow-predict",
        do_xcom_push=False,
        network_mode="bridge",
        mounts=[MOUNT_SOURCE]
    )

    generate >> move >> preprocess >> predict
