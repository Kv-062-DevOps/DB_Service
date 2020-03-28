# Start DataBase initialization; Db_init_load - load data
____
Build from Dockerfile
``` docker build -t Image_Name . ```
* Image_Name - create name for your image;
Start init container
``` docker run --name="Name" -e Db_url="URL" -e Region="region" Image_Name ```
* Name - create name for your container
* URL - DB endpoint url. No default. Example: 
``` http://ip:container_port ``` ``` http://localhost:8000 ```  ``` http://172.17.0.3:8000 ``` 
* ip - ip address of db container from previous step (first terminal) :)
* Region - AWS credentials region. Default "local". Example: "us-east-2". If set another than default it would break because we not set up credentials.
* Image_Name - name wich you give while build or set up image name from Docker HUB vnikolayenko/db-service:latest-init-load