____
Backend service: 
Helm chart, Terraform for creating AWS DynamoDB, Docker for ECR, Workflow for GitHub Actions.
____
* 1. Create own DynamoDB if you want (you can edit file for 'region' parameter). If you want to use existed - ask owner of DB for credentials and go to step 3.
``` terraform init ```
``` terraform plan -out=filepath ```
``` terraform apply ```
* 2. Create IAM role for all access to DB.(You can add such feature to your terraform). 
* 3. Start Kubernetes cluster.
* 4. Create own ECR or use existed. Manual to use existed 'https://github.com/Kv-062-DevOps/k8s-deploy/blob/master/ecr.md'. For own use dynamodb_web branch.
* 5. Let's deploy. Happy helming!
* * At first, let's check if all is correct. Default only is tag=latest
 ``` helm install --dry-run --debug  --set secretFile=ImagePullSecretCredFile --set registry=ecrAddress --ser tag=registryTag --set Region="dynamodb-region" --set secret_key="dynamodb-secret-key" --set access_key="dynamodb-access-key" helm-chart-specific-name ./helm-chart-dir ```
* secretFile - by default = awsecr-cred.
* registry - by default = 074368059797.dkr.ecr.eu-central-1.amazonaws.com/back.
* tag - by default = latest.
* region - by default = "local".
* secret and acess key - by default = "anything"
``` helm install --set secretFile=ImagePullSecretCredFile --set registry=ecrAddress --ser tag=registryTag --set Region="dynamodb-region" --set secret_key="dynamodb-secret-key" --set access_key="dynamodb-access-key" helm-chart-specific-name ./helm-chart-dir ```
* 6. Check for working.
``` kubectl get all``` &&
``` kubectl port-forward service/back-srv 8083:8083 ```
* 7. Go to browser and enter "http://127.0.0.1:8083/list".
