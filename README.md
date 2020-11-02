# Folding@Home Client REST API Server

Users who want to monitor the progress and status of their Folding@Home client do not have the option of doing this particularly easily - there is a Third Party API available for the Folding@Home client, however it is quite difficult to integrate with to answer simple questions, like whether the client is working or not, and the progress and phase of it's current Work Unit(s).  

The purpose of this server is primarily to monitor clients, rather than control them.  However, a limit set of commands may be implemented later which allow clients to be paused and unpaused via the API.  

## Usage

This server runs inside a docker container, which listens on port 8000 by default.  

### Reference
https://github.com/FoldingAtHome/fah-control/wiki/3rd-party-FAHClient-API
https://docs.python-guide.org/writing/structure/

### API

#### Status
* **URL**: /status
* **Method**: GET
* Success Response:
* * Code: 200
* * Content: 
```
{
    "status": "ok",
    "version": {
        "release": "0.1.0",
        "commit": "abc234"
    }
}
```
* Error Response:
* * Code: 500
* * Content: 
```
{
    "status": "error",
    "message": "Human friendly error message to show to a user",
    "version": {
        "release": "0.1.0",
        "commit": "abc234"
    }
}
```

#### Clients
* **URL**: /clients
* **Method**: GET
* Success Response:
* * Code: 200
* * Content: 
```
{
    "clients": [
        {
            "hostname":"example-hostname",
            "id": "ac8f597a-4d9c-49bb-bc40-6829970e9e36",
            "status": "paused",
            "slots": [
                
            ]
        }
    ]
}
```
* Error Response:
* * Code: 500
* * Content:
```
{
    "error": "Cannot connect to clients"
}
```

# Development

Dependencies are managed with Pipenv. 