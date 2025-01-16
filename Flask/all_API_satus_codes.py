import requests

# run the creating_APIs.py first


response = requests.get("http://127.0.0.1:5000")


if response.status_code == 200 :
    
    data = response.json()
    
    print("\nmessage recived sucessfully !\n")
    
    print(data)
    
    
elif response.status_code == 404 :
    
    print("The requested url dosen't exist")
    
elif response.status_code == 400 :
    
    print("Bad request !, The client sent a mailformed request")
    
elif response.status_code == 503 :
    
    print("Service Unavailable !, the requested server is unavailable")
    
elif response.status_code == 502 :
    
    print("Bad Gateway !, The server recived an invalid response ")

elif response.status_code == 504 :
    
    print("Gateway Timeout !, The server coudn't filfill the request in time due to technical deffculties")
    
elif response.status_code == 401 :
    
    print("Gone !, The resource the client wants to access has been permanently deleted ")
    
elif response.status_code == 501 :
    
    print("Not impelmented !, The server dosen't support the requested facility ")
    
elif response.status_code == 412 :
    
    print("Precondition failed !, The server dosen't meet one or more preconditions ")
    
elif response.status_code == 500 :
    
    print("Internal server error !, An error occured while processing the call ")