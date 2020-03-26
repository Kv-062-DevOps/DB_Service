1. Start DynamoDN 
docker pull amazon/dynamodb-local;
docker run -p container_port:host_port amazon/dynamodb-local;
Example: docker run --name=DB -d -p 8000:8000 amazon/dynamodb-local;
Get know container IP address: 
docker ps -l - container id
docker inspect --format '{{ .NetworkSettings.IPAddress }}' container_id
(new terminal)
2. Start Db_init 
docker build -t Image_Name .;
Image_Name - create name for your image;
docker run --name="Name" -e Db_url="URL" -e Region="region" Image_Name;
Name - create name for your container
URL - DB endpoint url. No default. Example: http://ip:container_port ;"http://localhost:8000" "http://172.17.0.3:8000"; ip - ip address of db container from previous step (first terminal);
Region - AWS credentials region. Default "local". Example: "us-east-2"
Image_Name - name wich you give while build or set up image name from Docker HUB vnikolayenko/db_service:latest_db_init
3. Start Db_service
Build: 
docker build -t Image_Name .
Image_Name - give name for your image.
To start Docker Image:
docker run -p container_port:host_port --name="Name" -e Db_url="URL" -e Server_port="Port" -e  Region="region" Image_Name
Name - give name to your container
URL - DB endpoint url. No default. Example: http://ip:container_port ;"http://localhost:8000" "http://172.17.0.3:8000"; ip - ip address of db container from previous step (first terminal);
Port - flask run port(server port), also useed as container listening port. By default 8083. Example: "8083"
Region - AWS region wich specified in credentials. By default "local". Example "us-east-2"
Image_Name - name wich you give while build or set up image name from Docker HUB vnikolayenko/db_service:latest_db_service

