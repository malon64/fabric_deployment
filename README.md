# Fabric Deployment automation

This project is used to deploy a Microsoft Fabric capacity and fill it with workspaces and users. All you have to do is editing the capacity_config.yml file and create your capacity hierarchy in it.

## Login and credentials

First of all you need to create a `.env` file and write in it the powerbi token to use in the API and the Azure region where you want to store your capacity :
```bash
POWERBI_TOKEN='<Your PowerBI API Token>'
AZURE_REGION='<Your Azure Region>'
```
Use this `.env` with Azure credentials if you don't want to use the az login command line

## Configuration file

In the `capacity_config.yml` you have to custom your capacity, its workspaces and their users :
```yaml
capacity: # your main capacity
  admin_email: # REQUIRED: the administrator email (ex: admin@email.com)
  basename:  # REQUIRED: the base name that will be added to a unique complete name on Azure (ex: test_capacity)
  sku: # REQUIRED: capacity size (ex: F2)
  tags: # OPTIONAL: Add additional metadata on the resource
  workspaces: # Now add all your workspaces that will be affected to the capacity
  - 
    name: # REQUIRED: the workspace name (ex: test_workspace)
    users: # Add in your workspace all your users
    - 
        groupUserAccessRight: # REQUIRED: the user access right (either Admin/Contributor/Member/None/Viewer)
        principalType: # REQUIRED: type of service principal (either App/Group/None/User)
        identifier:  # REQUIRED: user identifier (Pattern : xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx)
        displayName: # OPTIONAL: the user name (ex: John Doe)
        emailAddres: # OPTIONAL: the user email (ex: j.doe@email.com)
        profile: # OPTIONAL: type of identification (either id/displayName)
        userType: # OPTIONAL: type of user (ex: Data Analyst)
```
For more information about Workspaces (aka Groups also in powerBI) check the official documentation :
https://learn.microsoft.com/fr-fr/rest/api/power-bi/groups

## Deployment and destruction

For deploying the capacity use :
```bash
./deploy.sh
```
Your `capacity_config.yml` will be updated when the capacity is created with the `capacity_azure_id` and `capacity_powerbi_id`

For destroying your resources use : 
```bash
./destroy.sh
```