import requests

def get_capacities(token):
    return requests.get(
        'https://api.powerbi.com/v1.0/myorg/capacities', 
        headers={'Authorization': 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiJodHRwczovL2FuYWx5c2lzLndpbmRvd3MubmV0L3Bvd2VyYmkvYXBpIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvZThiODhmM2QtMjIyYi00Y2U1LWI5ZDEtNDZiMGZmOTQ2NmEwLyIsImlhdCI6MTY5NTgyNTcyMiwibmJmIjoxNjk1ODI1NzIyLCJleHAiOjE2OTU4MzEwMzgsImFjY3QiOjAsImFjciI6IjEiLCJhaW8iOiJBVlFBcS84VUFBQUF2cVRUdmt2RWhBb3dZZ0VBd2lPUVlhTmdvQ0pKbFRFVDVTdXNqemN6UEUwb0ZhYTRyNzFTeWYreUtuYWQxaW1JcjhpMlMyeUlvM3lnaXFLSCtVakI3TDNCMm1UUGhxRXl5dk5EQ3B2cVB3UT0iLCJhbXIiOlsicHdkIiwibWZhIl0sImFwcGlkIjoiMThmYmNhMTYtMjIyNC00NWY2LTg1YjAtZjdiZjJiMzliM2YzIiwiYXBwaWRhY3IiOiIwIiwiZmFtaWx5X25hbWUiOiJNRVRXQUxMSSIsImdpdmVuX25hbWUiOiJBbGV4aXMiLCJpcGFkZHIiOiIzNy43MS4xMjYuMTMyIiwibmFtZSI6IkFsZXhpcyBNRVRXQUxMSSIsIm9pZCI6ImUzNDliMzc3LTYwMzctNGJmNC05ODZkLTQ1ZGE3NmFjNTAxZCIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0yNjQxNTExNDQ4LTE4MzQyOTMzNjctNjIyNTg0NTk1LTYzNzc3IiwicHVpZCI6IjEwMDMyMDAyNkM3MTU1OUUiLCJyaCI6IjAuQVRFQVBZLTQ2Q3NpNVV5NTBVYXdfNVJtb0FrQUFBQUFBQUFBd0FBQUFBQUFBQUF4QUNnLiIsInNjcCI6IkFwcC5SZWFkLkFsbCBDYXBhY2l0eS5SZWFkLkFsbCBDYXBhY2l0eS5SZWFkV3JpdGUuQWxsIENvbnRlbnQuQ3JlYXRlIERhc2hib2FyZC5SZWFkLkFsbCBEYXNoYm9hcmQuUmVhZFdyaXRlLkFsbCBEYXRhZmxvdy5SZWFkLkFsbCBEYXRhZmxvdy5SZWFkV3JpdGUuQWxsIERhdGFzZXQuUmVhZC5BbGwgRGF0YXNldC5SZWFkV3JpdGUuQWxsIEdhdGV3YXkuUmVhZC5BbGwgR2F0ZXdheS5SZWFkV3JpdGUuQWxsIFBpcGVsaW5lLkRlcGxveSBQaXBlbGluZS5SZWFkLkFsbCBQaXBlbGluZS5SZWFkV3JpdGUuQWxsIFJlcG9ydC5SZWFkLkFsbCBSZXBvcnQuUmVhZFdyaXRlLkFsbCBTdG9yYWdlQWNjb3VudC5SZWFkLkFsbCBTdG9yYWdlQWNjb3VudC5SZWFkV3JpdGUuQWxsIFRlbmFudC5SZWFkLkFsbCBUZW5hbnQuUmVhZFdyaXRlLkFsbCBVc2VyU3RhdGUuUmVhZFdyaXRlLkFsbCBXb3Jrc3BhY2UuUmVhZC5BbGwgV29ya3NwYWNlLlJlYWRXcml0ZS5BbGwiLCJzaWduaW5fc3RhdGUiOlsiaW5rbm93bm50d2siLCJrbXNpIl0sInN1YiI6IkdPMW1mRTJobldFMnVyblFqSUpQaWVJVjNmRV9YVFFmUVRLN0lPazFqaUEiLCJ0aWQiOiJlOGI4OGYzZC0yMjJiLTRjZTUtYjlkMS00NmIwZmY5NDY2YTAiLCJ1bmlxdWVfbmFtZSI6ImEubWV0d2FsbGlAZ3JvdXBlb25lcG9pbnQuY29tIiwidXBuIjoiYS5tZXR3YWxsaUBncm91cGVvbmVwb2ludC5jb20iLCJ1dGkiOiJCZ2tQNF9SWXRrMkI2RzdtU2d4YkFBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX3BsIjoiZnIifQ.WO4jRp31noNTqxhqMC-UMMRtfyA1Y_v6jyCyZaGrxISzkIXOPS62krNMeWb66kMJDF77U5zH-ryJnXjP5lKJwh-P3UhrAZRXhr3u3OyBpa5cZlFE-tvzjBY4MXfsqFAII6JAC4meGDDyWYOX7DtrXHTiJy8J0UK0zA0S2RM6K4SYmaGUgoP1buDTN5f_0gj9KbYKYiTjB0vDgtFjB-OiJPIqL7rTity1KzvwTfJfo0wzsqohT_df8nkDGy-w9BxbWUh8ngHR_FIHpEKfpECkN13huGGXhMTrybBM3UgkdylXOFNyahHwhgAVjzrGMEhw4eoGWHVCxjwG7p9w38jiEA'}
    )

def get_capacity_id_by_name(capacities, capacityName):
    for capacity in capacities:
        if capacity['displayName'] == capacityName:
            return capacity['id']

def get_all_workspaces(token):
    return requests.get(
        "https://api.powerbi.com/v1.0/myorg/groups",
        headers={'Authorization': token}
    )

def get_capacity_workspaces(capacityId, token):
    return requests.get(
        "https://api.powerbi.com/v1.0/myorg/groups?$filter=contains(capacityId,'{}')".format(capacityId),
        headers={'Authorization': token}
    )

def create_workspace(workspaceName, token):
    return requests.post(
        'https://api.powerbi.com/v1.0/myorg/groups?workspaceV2=true',
        data={'name': workspaceName},
        headers={'Authorization': token}
    )

def delete_workspace(workspaceId, token):
    return requests.delete(
        'https://api.powerbi.com/v1.0/myorg/groups/{}'.format(workspaceId),
        headers={'Authorization': token}
    )

def assign_workspace(workspaceId, capacityId, token):
    return requests.post(
        'https://api.powerbi.com/v1.0/myorg/groups/{}/AssignToCapacity'.format(workspaceId),
        data={'capacityId': capacityId},
        headers={'Authorization': token}
    )

def create_user(workspaceId, token):
    return requests.post(
        'https://api.powerbi.com/v1.0/myorg/groups/{}/users'.format(workspaceId),
        data=
        {
            'groupUserAccessRight': "",
            'identifier': "",
            'principalType': ""
        },
        headers={'Authorization': token}
    )
