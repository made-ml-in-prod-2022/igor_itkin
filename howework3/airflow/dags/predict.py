from datetime import timedelta

from airflow import DAG
from airflow.models import Variable
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount

MOUNT_SOURCE = Mount(
    source="/home/yehuda/garbage/hw3data",
    target="/data",
    type='bind'
)

FAKE_DATA_DIR = "/data/models/{{ ds }}"
REAL_DATA = "/data/real/{{ ds }}"
RAW_DATA_DIR = "/data/raw/{{ ds }}"
PP_DATA_DIR = "/data/processed/{{ ds }}"
MODEL_DIR = Variable.get("MODELPATH")
PREDICT_DIR = "/data/predictions/{{ ds }}"
LOCAL_DIR = "/home/yehuda/garbage/h3hw"

NUM_SAMPLES = 100
SAMPLE_FILE = "data_sample.csv"

default_args = {
    "owner": "Igor (Yehuda) Itkin aka BukaByaka",
    "email": ["ig.itkin@gmail.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
        "predict",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=days_ago(0),
) as dag:
    move = DockerOperator(
        image="airflow-move",
        command=f"--input-dir {REAL_DATA} --output-dir {RAW_DATA_DIR}",
        task_id="docker-airflow-move",
        do_xcom_push=False,
        network_mode="bridge",
        # Do we need mount here?
        mounts=[Mount(source=f"{LOCAL_DIR}/data/fake", target=FAKE_DATA_DIR, type='bind')]
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

    move >> preprocess >> predict
