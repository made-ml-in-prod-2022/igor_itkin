from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable
from docker.types import Mount


DIR_PROCESSED = "/data/processed/{{ ds }}"
MODEL_PATH = Variable.get("MODELPATH")
PREDICTIONS_PATH = "/data/predictions/{{ ds }}"
MOUNT_SOURCE = Mount(
    source="/home/yehuda/garbage/hw3data",
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
        "predict",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=days_ago(0),
) as dag:
    preprocess = DockerOperator(
        image="airflow-preprocess",
        command="--in_dir {} --model_dir {} --pred_dir {}".format(DIR_PROCESSED, MODEL_PATH, PREDICTIONS_PATH),
        task_id="docker-airflow-preprocess",
        do_xcom_push=False,
        network_mode="bridge",
        mounts=[MOUNT_SOURCE])

    predict = DockerOperator(
        image="airflow-predict",
        command="--in_dir {} --model_dir {} --pred_dir {}".format(DIR_PROCESSED, MODEL_PATH, PREDICTIONS_PATH),
        task_id="docker-airflow-predict",
        do_xcom_push=False,
        network_mode="bridge",
        mounts=[MOUNT_SOURCE]
    )

    preprocess >> predict
