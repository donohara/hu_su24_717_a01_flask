import requests

print('starting')
files = {'file': open('./cat_1.jpg','rb')}
url = "http://127.0.0.1:5000/predict"

# resp = requests.post("http://127.0.0.1:5000/predict",
# headers = {'accept': 'application/json'}
# r = requests.post(url, files=files, headers=headers)
r = requests.post(url, files=files)
print(r.text)


# resp = requests.post("http://127.0.0.1:5000/predict",
#                      files={"file":
#                                 open('','rb')})
# print(f'response: {resp.text}')
