import argparse
import yaml

from powerbi.api_calls import get_all_workspaces, get_capacities, get_capacity_id_by_name, get_capacity_workspaces, create_workspace, create_user, assign_workspace, delete_workspace

# https://learn.microsoft.com/en-us/rest/api/power-bi/capacities

parser = argparse.ArgumentParser(description="A program for creating workspaces in a given capacity", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-t', '--token')
parser.add_argument('-c', '--capacity_name')
parser.add_argument('-a', '--capacity_azure_id')


args = parser.parse_args()
token = f'Bearer {args.token}'

def printCapacity(capacity):
    print("Capacity {}".format(capacity['id']))
    print("Display name : {}".format(capacity['displayName']))
    print("SKU : {}".format(capacity['sku']))
    print("State : {}".format(capacity['state']))
    print("Admins : ")
    print(capacity['admins'])
    print("Region : {}".format(capacity['region']))
    print("---------------")

def printWorkspace(workspace):
    print("Workspace {}".format(workspace['id']))
    print("Name : {}".format(workspace['name']))
    print("Is read only ? -> {}".format(workspace['isReadOnly']))
    print("Is on dedicated capacity ? -> {}".format(workspace['isOnDedicatedCapacity']))
    if 'capacityId' in workspace:
        print("Capacity ID : {}".format(workspace['capacityId']))
    if 'defaultDatasetStorageFormat' in workspace:
        print("Default Dataset Storage : {}".format(workspace['defaultDatasetStorageFormat']))
    print("---------------")

# This script finds the capacity by its name, create a workspace and assign it to the capacity

capacities = get_capacities(token).json()
print("Capacities : ")
for capacity in capacities['value']:
    printCapacity(capacity)

#This capacity id is not the same Id given by Azure so we need to retrieve it with the capacity name (which is unique)
capacityId = get_capacity_id_by_name(capacities['value'], args.capacity_name)


workspaces = get_all_workspaces(token).json()
print("Workspaces existing : ")
for workspace in workspaces['value']:
    printWorkspace(workspace)
print("///")

# Deleting all the workspaces, this part is here to avoid bugs but needs to be removed
for workspace in workspaces['value']:
    delWs = delete_workspace(workspace['id'], token)
    print(delWs)
    print("///")

with open('../capacity_config.yml', 'r+') as file:
    config = yaml.safe_load(file)
    config["capacity"]["azure_id"] = args.capacity_azure_id
    config["capacity"]["powerbi_id"] = capacityId
    config["capacity"]["name"] = args.capacity_name
    # Create workspaces
    for workspace in config["capacity"]["workspaces"]:
        workspace_created = create_workspace(workspace["name"], token).json()
        print("Workspace created : ")
        printWorkspace(workspace_created)
        workspace["id"] = workspace_created['id']

    # Assign the created workspace
    aw = assign_workspace(workspace["id"], capacityId, token)
    print("Assigned workspace : ")
    print(aw)
    
yaml.dump(config, file)

# Print the capacity assigned workspaces
# workspaces = get_capacity_workspaces(capacityId, token).json()
# print("Workspaces linked to capacity :")
# for workspace in workspaces['value']:
#     printWorkspace(workspace)