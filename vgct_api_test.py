import requests, json



def vgct():
    url = 'http://127.0.0.1:8000/api/members/'
    headers = {'Content-Type': 'application/json'}
    # data = json.dumps({"party": 1,})



    req = requests.get(url, headers = headers)
    response = req.json()
    # year = response[0]['release_dates'][0]['y']
    print(response[0])

    return response

vgct()