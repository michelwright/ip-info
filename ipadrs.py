from bs4 import BeautifulSoup
import re
import requests

class IP:
    def __init__(self):
        self.url = "https://www.whatismybrowser.com/detect/"
        self.chrome_win10 = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
        self.safari_mac = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
        #pick default headers chrome_win10 or safari_mac
        self.headers = self.safari_mac
        self.refresh()

    def refresh(self):
        try:
            r = requests.get(self.url+'ip-address-location', headers=self.headers)
            self.IPLocation = BeautifulSoup(r.text, 'html.parser')
            r = requests.get(self.url+'what-is-my-ip-address', headers=self.headers)
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
        