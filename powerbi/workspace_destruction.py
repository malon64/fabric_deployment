import argparse
from powerbi.api_calls import get_capacities, get_capacity_id_by_name, delete_workspace, get_capacity_workspaces

parser = argparse.ArgumentParser(description="A program for destroying workspaces and users in a given capacity", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-t', '--token')
parser.add_argument('-c', '--capacity')

args = parser.parse_args()
token = "Bearer " + args.token

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


capacities = get_capacities(token).json()
print("Capacities : ")
for capacity in capacities['value']:
    printCapacity(capacity)

capacityId = get_capacity_id_by_name(capacities['value'], args.capacity)

workspaces = get_capacity_workspaces(capacityId, token).json()
print("Workspaces linked to the capacity " + capacityId + " : ")
for workspace in workspaces['value']:
    printWorkspace(workspace)
print("///")

print("Deleting all workspaces in the Capacity : ")
for workspace in workspaces['value']:
    delWs = delete_workspace(workspace['id'], token)
    print(delWs)
    print("///")
print("Workspaces deleted successfuly !")