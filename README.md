____
Backend service: 
Helm chart, Terraform for creating AWS Dynamodb, Docker for ECR, Workwlow for GitHub Actions, Example File of default reply from DB.
____
* 1. Create if you want own DynamoDB with predifined (you can edit file for change such parameters like 'region' ). If you want to use existed - ask owner of DB for credentials and goes to 3. step
``` terraform init ```
``` terraform plan -out=filepath ```
``` terraform apply ```
* 2. Create IAM role for all access to DB.(You can add such feature to your terraform)
* 3. Change GitHub actions if you want to use your own images. If you want to use existed - ask owner of ECR repo for credentials and create it in Settings/Secret. If you my coleg - just use this workflow and never mind (but don't forget that Docker should be in the same directory or change docker build path in workflow .yaml file)
* 4. Do you have Kubernetes? Yes...Go ahead.
* 5. Let's deploy. Happy helming!
* * At first, let's check if all is correct. Default only Tag=latest
``` helm install --dry-run --debug --set imageCredentials.registry=ecr-address --set imageCredentials.username=username-for-ecr --set imageCredentials.password=password-for-ecr --set Region="dynamodb-region" --set Secret_key="dynamodb-secret-key" --set Access_key="dynamodb-access-key" --set Tag="ecr-image-tag" helm-chart-specific-name ./helm-chart-dir ```
* * 
``` helm install --set imageCredentials.registry=ecr-address --set imageCredentials.username=username-for-ecr --set imageCredentials.password=password-for-ecr --set Region="dynamodb-region" --set Secret_key="dynamodb-secret-key" --set Access_key="dynamodb-access-key" --set Tag="ecr-image-tag" helm-chart-specific-name ./helm-chart-dir ```
* 6. Check for working. If you want, you can even set port for your service (check ./chart/values and ./chart/templates/...service.yaml)
``` kubectl get all```
``` helm ls ``` 
``` kubectl port-forward service/back-srv 8083:8083 ```
* 7. Go to browser and enter "http://127.0.0.1:8083/list". You should see reply like in get_response file.