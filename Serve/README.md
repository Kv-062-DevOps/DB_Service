# DB_Service
## DynamoDB & Python
### dbservice manual:
Build image:
```
docker build -t Image_Name
```
Or **pull** image:
```
docker pull 
```
Start Docker Image: 
```
docker run --name="Name" -e db_url="URL" -e host_port="port" -e region="region" Image_Name
```

Give name to your container URL - endpoint url to DynamoDB service with port. Example: "http://localhost:8000" Port - flask run port(server port), also useed as container listening port. By default 8080. Example: "8080" Image_Name - name wich you give while build