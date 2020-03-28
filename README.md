____
# 1. Start DynamoDN;
____
Download image from Docker Hub.
``` docker pull amazon/dynamodb-local ```
Start DynamoDb container.
``` docker run -p container_port:host_port amazon/dynamodb-local ```
* Example: 
``` docker run --name=DB -d -p 8000:8000 amazon/dynamodb-local ```
Get know container IP address: 
``` docker ps -l - container id ```
``` docker inspect --format '{{ .NetworkSettings.IPAddress }}' container_id ```
(new terminal)- for next step :)
____
# 2. Start DataBase initialization; First Db_init_create - create Table; Second Db_init_load - load data
____
Build from Dockerfile. Db_init_create directory or from Db_init_load.  
``` docker build -t Image_Name . ```
* Image_Name - create name for your image;
Start init containers. First init_create to Create Table. Second init_load to load Data.
``` docker run --name="Name" -e Db_url="URL" -e Region="region" Image_Name ```
* Name - create name for your container
* URL - DB endpoint url. No default. Example: 
``` http://ip:container_port ``` ``` http://localhost:8000 ```  ``` http://172.17.0.3:8000 ``` 
* ip - ip address of db container from previous step (first terminal) :)
* Region - AWS credentials region. Default "local". Example: "us-east-2". If set another than default it would break because we not set up credentials.
* Image_Name - name wich you give while build or set up image name from Docker HUB vnikolayenko/db_service:latest_init_create or :latest_init_load
____
# 3. Start Db_service
____
Build from Dockerfile. Db_service directory.
``` docker build -t Image_Name . ```
* Image_Name - give name for your image.
To start Docker Image:
 ```docker run -p container_port:host_port --name="Name" -e Db_url="URL" -e Server_port="Port" -e  Region="region" Image_Name ```
* Name - give name to your container
* URL - DB endpoint url. No default. Example: 
``` http://ip:container_port ``` ``` http://localhost:8000 ``` ``` http://172.17.0.3:8000 ``` 
* ip - ip address of db container from 1 step (first terminal);
* Port - flask run port(server port), should be the same as container listening port. By default 8083. Example: "8083"
* Region - AWS region wich specified in credentials. By default "local". Example "us-east-2".If set another than default it would break because we not set up credentials.
* Image_Name - name wich you give while build or set up image name from Docker HUB vnikolayenko/db_service:latest_db_service

