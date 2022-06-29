1. Фотография бегающего кластера в running_cluster.jpg  
Бегает в гугль клауде  
>> kubectl cluster-info
Kubernetes control plane is running at https://104.198.240.61  
GLBCDefaultBackend is running at https://104.198.240.61/api/v1/namespaces/kube-system/services/default-http-backend:http/proxy  
KubeDNS is running at https://104.198.240.61/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy  
Metrics-server is running at https://104.198.240.61/api/v1/namespaces/kube-system/services/https:metrics-server:/proxy  
To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.  

2. К сожалению, я похерил докер образ, а перестроить и загрузить на хаб 
сейчас не получится. Поэтому  заккомиил образ busybox. Не бейте сильно

3. ресурсы 
Request нужен чтобы кубернатис выделил ноду (виртуальную машинку) как минимум с соответующими 
ресурсами. Лимит - чтобы в рантайме приложение не пожрало больше ресурсов

4. liveness 
То что я написал в манифесте работает так.  
Через 10 секунд после старта  создается файлик tmp/healty и через 60 секунд уничтожается.  
Первая проба стартует через 20 секунд и поэтому все хорошо. Вторая через 100 секунд после первой, не находит файлик и прибивает под  
5. readinessProbe  
Эксперименты проводились путем убиенся nginx 
Пингуем (или коннектимся) на 8080 каждые 10 секунд начиная с 5. Если не отвечет - к поду приходит бабайка
(вид бабайки - Kill или restart зависит от настроек) 
