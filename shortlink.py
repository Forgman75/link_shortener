import requests
import sys
url = 'https://api-ssl.bitly.com/v4/shorten'
def shorten_link(link):
    token = "17c09e22ad155405159ca1977542fecf00231da7"
    bearer = "Bearer {t}".format(t=token)
    headers = {
        "Authorization": bearer 
    }
    payload = {
        "long_url": link 
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['link']

if __name__ == "__main__":
 link = input("Введите ссылку, которую нужно сократить:") 
 try:  
    bitlink = shorten_link(link)
 except requests.exceptions.HTTPError:
     print("Вы ввели не корректную ссылку")
     sys.exit()
 print('Битлинк', bitlink)