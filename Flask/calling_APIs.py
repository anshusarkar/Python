import requests

# Run creating_APIs.py first 

response = requests.get("http://127.0.0.1:5000")

response2 = requests.get("http://127.0.0.1:5000/hello")

print(response)

print(response2)

if response.status_code == 200 :
    
    data = response.json()
    
    print(data)
    
    
if response2.status_code == 200 :
    
    data2 = response2.json()
    
    print(data2)