Recursice apply from each directory:
* db
* db-service 
* ``` kubectl apply -f ./db --recursive ```
* Port forwarding for outbound(local) connection
* ``` kubectl port-forward service/back 8083:8083 ```
* Now you can connect to ``` http://127.0.0.1:8083 ```
* Example:
* ``` http://127.0.0.1:8083/hello ```
* ``` http://127.0.0.1:8083/list ```

