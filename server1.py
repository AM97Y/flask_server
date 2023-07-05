import requests
if __name__ == '__main__':
    elem = requests.get('http://127.0.0.1:5000/detect/', params= {'img': [1,1,1]})
    print(elem.json())
