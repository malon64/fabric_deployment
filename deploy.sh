export $(egrep -v '^#' .env | xargs)
az login # Connect to your Azure account using web browser

cd terraform
terraform init
terraform plan -var="location=$AZURE_REGION" -out=plan
terraform apply --auto-approve "plan"
export CAPACITY_AZURE_ID=$(terraform output -raw capacity_id)
export CAPACITY_NAME=$(terraform output -raw capacity_name)

cd ../powerbi
python3 workspace_creation.py -t $POWERBI_TOKEN -c $CAPACITY_NAME -a $CAPACITY_AZURE_ID