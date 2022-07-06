from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount

FAKE_DATA_DIR = "/data/models/{{ ds }}"
REAL_DATA = "/data/real/{{ ds }}"
RAW_DATA_DIR = "/data/raw/{{ ds }}"
PP_DATA_DIR = "/data/processed/{{ ds }}"
MODEL_DIR = "/data/models/{{ ds }}"
PREDICT_DIR = "/data/predictions/{{ ds }}"
LOCAL_DIR = "/home/yehuda/garbage/h3hw"

MOUNT_SOURCE = Mount(
    source=f"{LOCAL_DIR}/data/train",
    target="/data",
    type='bind'
)

default_args = {
    "owner": "Igor (Yehuda) Itkin aka BykaByaka",
    "email": ["ig.itkin@gmail.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
        "train",
        default_args=default_args,
        schedule_interval="@weekly",
        start_date=days_ago(0),
) as dag:
    preprocess = DockerOperator(
        image="airflow-preprocess",
        command=f"--model_dir {MODEL_DIR} --input-dir {RAW_DATA_DIR}--output_dir {PP_DATA_DIR}",
        task_id="docker-airflow-preprocess",
        do_xcom_push=False,
        network_mode="bridge",
        mounts=[MOUNT_SOURCE])

    train = DockerOperator(
        image="airflow-train",
        command=f"--model_dir {MODEL_DIR} --predict_dir {PREDICT_DIR}",
        task_id="docker-airflow-train",
        do_xcom_push=False,
        network_mode="bridge",
        mounts=[MOUNT_SOURCE]
    )

    preprocess >> train
