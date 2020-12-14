from bs4 import BeautifulSoup
import re
import requests

class IP:
    def __init__(self):
        self.url = "https://www.whatismybrowser.com/detect/"
        self.mozilla = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
        try:
            r = requests.get(self.url+'ip-address-location', headers=self.mozilla)
            self.IPLocation = BeautifulSoup(r.text, 'html.parser')
            r = requests.get(self.url+'what-is-my-ip-address', headers=self.mozilla)
            self.IPAddress = BeautifulSoup(r.text, 'html.parser')
        except:
            print('Error getting IP information') 

    def info(self):
        print('-------------------------')
        print('')
        print('IP Address: '+self.IPAddress.body.find_all(id=re.compile('detected_value'))[0].get_text())
        print('')
        print('-------------------------')
        print('')
        print('Location: '+self.IPLocation.body.find_all(id=re.compile('detected_value'))[0].get_text())
        print('')
        print('-------------------------')
        print('')
        