# DB_Service
DynamoDB, Flask, Yaml, Python
Build: 
docker build -t Image_Name .
Image_Name - give name for your image.
To start Docker Image:
docker run --name="Name" -e Db_url="URL" -e Server_port="Port" -e  Region="region" Image_Name
Name - give name to your container
URL - endpoint url to DynamoDB service with port. No default.Example: "http://localhost:8000" "http://172.17.0.3:8000"
Port - flask run port(server port), also useed as container listening port. By default 8083. Example: "8083"
Region - AWS region wich specified in credentials. By default "local". Example "us-east-2"
Image_Name - name wich you give while build or set up image name from Docker HUB vnikolayenko/db_service
