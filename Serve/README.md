# DB_Service
## Python
### dbservice manual:
**Pull** image:
```
docker pull delaskoff/dbservice
```
Start Docker Image: 
```
docker run --name="Name" -e db_url="URL" -e host_port="port" -e region="region" delaskoff/dbservice
```

Give name to your container URL - endpoint url to DynamoDB service with port. Example: "http://localhost:8000" Port - flask run port(host port), also used as container listening port. By default 8080.