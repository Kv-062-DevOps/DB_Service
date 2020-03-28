# Start Db_service
____
Build from Dockerfile
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