
### Configuration  
Change model_dir/ in docker-compose.yml  
`AIRFLOW_VAR_MODELPATH=/data/models/2022-07-06`  

### Run app

`export FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")`  
`sudo docker-compose up --build`