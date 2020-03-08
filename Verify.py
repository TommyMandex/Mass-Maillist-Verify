#Change Or Edit Author COPYRIGHT Never Make You Coder, Don't Be A Bastard Dude!
#Coded By Wissem Mahfoud
#OwnerTN
import threading
from multiprocessing.dummy import Pool
import os,sys,time
from bs4 import BeautifulSoup
from platform import system
import random
import datetime
import cookielib
import os
import re
from colorama import Fore								
from colorama import Style								
from colorama import init												
import requests, re, os, base64;
import urllib, httplib, urllib2										
from urlparse import urlparse, parse_qs
import requests, re, urllib2, os, sys, codecs, random                                       
from time import time as timer  
import time
import json
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
try:
    os.system('title MASS MAILLIST VERIFY')
except:
    pass
if system() == 'Windows':
    os.system('cls')
elif system() == 'Linux':
    os.system('clear')
else:
    pass    
########### COLOR ############ 
fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT										
##############################  
print ('''{}{}
              ________
            /'        /|
           /         / |_
          /         /  //|
         /_________/  ////|
        |   _ _    | 8o////|
        | /'// )_  |   8///|
        |/ // // ) |   8o///|
        / // // //,|  /  8//|
       / // // /// | /   8//|      MASS MAILLIST VERIFY
      / // // ///__|/    8//|      CODED BY WISSEM MAHFOUD 
     /.(_)// /// |       8///|     THINK TWICE, CODE ONCE
    (_)' `(_)//| |       8////|___________ 
   (_) /_\ (_)'| |        8///////////////
   (_) \"/ (_)'|_|         8/////////////
    (_)._.(_) d' Hb         8oooooooopb'
      `(_)'  d'  H`b
            d'   `b`b
           d'     H `b
          d'      `b `b
         d'           `b
        d'             `b  
		
''').format(fr,sb)
now = datetime.datetime.now()
print('\n\033[92m                        STARTED AT: ' + str(now))       
Maillist = raw_input("\n\033[92m[!]\033[91m WELCOME TO HELL ENTER LIST OF EMAILS : ")
try:
    from os import system as sy, path; sy("cls||clear");import requests,socket,optparse,re   
except ImportError:
    print(fw+"["+fg+"*"+fw+"] Use This Command :"+fg+" pip install requests"+fw)
    exit(1)
def conection():
    try:
        ip = socket.gethostbyname("www.google.com")
        con = socket.create_connection((ip, 80), 2)
        return True
    except socket.error:
        pass
    return False
def Louis(email):
    try:
        data = {"email": email}
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24'}
        response = requests.post("https://verifyemailaddress.com/result", headers=headers, data=data).text
        if "is valid" in response:
            print(fc+"["+fc+">"+fc+"] "+fg+email+fw+" .... "+fg+" Verified "+fw+"")
            open('Verified.txt', 'a').write(email+'\n')
        else:
            response = requests.post("https://www.infobyip.com/verifyemailaccount.php", headers=headers, data=data).text
            if "Email account exists." in response:
                print(fc+"["+fc+">"+fc+"] "+fg+email+fw+" .... "+fg+" Verified "+fw+"")
                open('Verified.txt', 'a').write(email+'\n')
            else:
                print(fc+"["+fc+">"+fc+"] "+fr+email+fw+" .... "+fr+" Not Verified "+fw+""+fw)
                open('Not-Verified.txt', 'a').write(email+'\n')
    except(KeyboaredInterrupt,EOFError):
        print(fw+" ")
        exit(1)
def Main():
    if Maillist !=None:
        luci = Maillist
        if not path.isfile(luci):
            print(fr+"\n["+fr+"!"+fr+"]"+fr+" Wrong:"+fc+" Please Use Your Mind"+fr+luci+fc+""+fr+" !"+fw)
            print(fw+"["+fc+"!"+fw+"]"+fc+" Wrong:"+fw+" Open Your Fucking EYES"+fc+" !"+fw)
            exit(1)
        try:
            with open(luci) as fop:
                for email in fop:
                    if not email.strip():continue
                    if not "@" in email : print(fc+"["+fr+"!"+fc+"]"+fr+" ERROR"+fc+": Email["+fr+email.strip()+fc+"] .... ["+fr+" Invalid "+fc+"]"+fw);continue
                    email = email.strip()
                    Louis(email)
            fop.close()
        except (KeyboaredInterrupt,EOFError):
            print(fr+"\n["+fc+"!"+fc+"] Cancel..."+fr+"!")
            exit(1)
    else:
        print(parse.usage)
        exit(1)
if __name__=="__main__":
    Main()
############# Owner TN #########
