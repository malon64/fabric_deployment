export $(egrep -v '^#' .env | xargs)

cd terraform
az login
terraform init
terraform plan -var="location=$AZURE_REGION" -out=plan
terraform apply --auto-approve "plan" 
export CAPACITY_NAME=$(terraform output -raw capacity_name)

cd ../powerbi
python3 workspace_creation.py -t $POWERBI_TOKEN -c $CAPACITY_NAME