# DB_Service
## DynamoDB & Python
### init manual:
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
docker run --name="Name" -e db_url="URL" -e region="region" Image_Name
```