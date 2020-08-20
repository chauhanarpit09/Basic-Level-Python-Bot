
import os
import webbrowser
import re
import smtplib
import wikipedia

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 

def menu():
    print("\n\n Hello , I can do these things .")
    print("-> Open Chrome")
    print("-> Open VS code")
    print("-> Open window media Player")
    print("-> Get Wikipedia result or open any website")
    print("-> send mail")
    print("-> Basic Chatting\n\t")
    prCyan("So, tell me how may I help you")

      
def open(text,name):
    if not os.system(text):
        a = "{} opened succesfully".format(name)
        prGreen(a)
        print("\n\t")
        prCyan("Any other Help You Need ?")

def search(url):
    if bool(re.search(".com",url)):  
        webbrowser.register('chrome',
            None,
            webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
        prGreen("Your URL was Opened")
        print()
        prCyan("Need Any other Help ? ")
    else:
        try:
            ny = wikipedia.page(url)
            webbrowser.register('chrome',
                None,
                webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(ny.url)
            prCyan("Need Any other Help ? ")
        except:
            prRed("Sorry I din't found Something on Wikipedia")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('prasad111suresh@gmail.com', 'Arpit9945')
    server.sendmail('prasad111suresh@gmail.com', to, content)
    server.close()




menu()
while True:
    print()
    i = input().lower()
    if bool(re.search("search",i)) :
        print("enter  " , end = " : ")
        a = input()
        search(a)
    elif bool(re.search("chrome",i)):
        open("chrome","Google Chrome")
    elif bool(re.search("code",i)):
        open("code","Visual Studio Code")
    elif bool(re.search("player",i)):
        open("wmplayer","Windows Media Player")
    elif bool(re.search("thank",i)):
        prCyan("ohh..no any need of this i was only develop to help you")
        break
    elif bool(re.search("mail",i)):
        print("Enter Email : ",end = " : ")
        e = input()
        while True:
            if bool(re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',e)):
                print("Enter body : ",end = " : ")
                b = input()
                break
            else:
                prRed("Email Enterd was Incorrect")
                print("\nEnter Email again : ",end = " : ")
                e = input()
        try:
            sendEmail(e,b)
            prGreen("Email was Sent")
        except:
            prRed("There Was a problem please try after sometime or check is email u entered is correct")
        prCyan("Anything Else")
    elif i in ["yes","yup","yes ofcs","yes yes","yes!","yes ofcourse"]:
        prCyan("Enter what other help you need : ")
        continue
    elif bool(re.search("exit",i)):
        prGreen("Thank You For using me")
        break
    else:
        prRed("Sorry i Didn't Get What You said")
    
