# Igor Itkin (Made)
В конфигах по прежнему гидра

Чтобы запустить сборку и имадж в докере (будет открыт 5000 порт) 

`docker-compose up -d --build`

Чтобы собрать докер образ без композера (легкие пути!? Мы не ищем легких путей!)  
`docker build -t yehudaitkin/ml-in-prod .`


Чтобы запушить на докер-хаб (предположим, что мы уже залогинились)  
Если не существует репы  
`docker build -t yehudaitkin/ml-in-prod`  
и  
`docker push  yehudaitkin/ml-in-prod`  
а если у нас какая то свой террариум образов  
`docker push  terrarium/yehudaitkin/ml-in-prod`


Скрипты работают понятно и просто (как то исторически тоже на 5000) 
./scripts/alive.sh
./scripts/health.sh
./scripts/predict.sh
