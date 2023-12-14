export $(egrep -v '^#' .env | xargs)
export CAPACITY_BASENAME=testcapa
export SKU=F2
export LOCATION=francecentral
export ADMIN_EMAIL=a.metwalli@groupeonepoint.com

python3 powerbi/workspace_destruction.py -t $POWERBI_TOKEN -c $CAPACITY_NAME

cd terraform
az login
terraform destroy --auto-approve -var="capacity_name=$CAPACITY_BASENAME" -var="capacity_sku=$SKU" -var="location=$LOCATION" -var="admin_email=$ADMIN_EMAIL"