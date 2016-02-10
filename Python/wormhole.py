import json
import requests

def signup(emailAddress):
    return requests.post('https://wormhole.network/api/signup/', headers={'Content-Type': 'application/json'}, data=json.dumps({'email': emailAddress}))

## Read-only operations

def getHubs(authToken):
    return requests.get('https://wormhole.network/api/hubs/', headers={'Authorization':'Token ' + authToken})
    
def getHubdetails(authToken, hubName):
    return requests.get('https://wormhole.network/api/hubs/'+hubName+"/", headers={'Authorization':'Token ' + authToken})
        
def getHubusers(authToken, hubName):
    return requests.get('https://wormhole.network/api/hubs/'+hubName+"/users/", headers={'Authorization':'Token ' + authToken})
    
def getHubuserdetails(authToken, hubName, hubUser):
    return requests.get('https://wormhole.network/api/hubs/'+hubName+"/users/"+hubUser+"/", headers={'Authorization':'Token ' + authToken})
    
def getConfig(authToken, hubName, hubUser):
    return requests.get('https://wormhole.network/api/hubs/'+hubName+"/users/"+hubUser+"/configfile/", headers={'Authorization':'Token ' + authToken})
    
def getConfig(authToken, hubName, hubUser):
    return requests.get('https://wormhole.network/api/hubs/'+hubName+"/users/"+hubUser+"/configfile/", headers={'Authorization':'Token ' + authToken})

def getLinuxconfig(authToken, hubName, hubUser):
    return requests.get('https://wormhole.network/api/hubs/'+hubName+"/users/"+hubUser+"/linuxconfig/", headers={'Authorization':'Token ' + authToken})

## Write operations

def newHub(authToken, hubName, serverName):
    return requests.post('https://wormhole.network/api/hubs/', headers={'Content-Type': 'application/json', 'Authorization':'Token ' + authToken}, data=json.dumps({'name': hubName, 'server': serverName}))
    
def newHubuser(authToken, hubName, username, userpassword):
    return requests.post('https://wormhole.network/api/hubs/'+hubName+'/users/', headers={'Content-Type': 'application/json', 'Authorization':'Token ' + authToken}, data=json.dumps({'username': username, 'password': userpassword}))