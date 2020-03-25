# DB_Service
DynamoDB, Flask, Yaml, Python
Build: 
docker build -t Image_Name .
Image_Name - give name for your image.
To start Docker Image:
docker run --name="Name" -e Db_url="URL" -e Server_port="Port" Image_Name
Name - give name to your container
URL - endpoint url to DynamoDB service with port. Example: "http://localhost:8000"
Port - flask run port(server port), also useed as container listening port. By default 8083. Example: "8083"
Image_Name - name wich you give while build or set up image name from Docker HUB.(in progress)
