import requests
import re
import getpass
import sys
import time
import ctypes
from tkinter import *
tries = 3

def weapon():
    WEAPON = input("Weapon name: ")
    SKIN = input("Skin: ")
    EXTERIOR = input("Exterior type (FN/MW/FT/WW/BS): ")
    WEAPON = re.sub(r"\s+", '%20', WEAPON)
    d = {
        "FN": "Factory New",
        "MW": "Minimal Wear",
        "FT": "Field-Tested",
        "WW": "Well-Worn", 
        "BS": "Battle-Scarred"                     
    }
    EXTERIOR = d[EXTERIOR]
    responsew = requests.get("https://steamcommunity.com/market/priceoverview/?appid=730&market_hash_name=" + WEAPON + "%20%7C%20" + SKIN + "%20" + "%28" + EXTERIOR + "%29" + "&currency=24")   
    print(responsew.json())
    print(responsew.json()['lowest_price'])
    print(responsew.json()['volume'])

def agent():
    AGENT = input("Agent: ")
    GROUP = input("GROUP: ")
    responsea = requests.get("https://steamcommunity.com/market/priceoverview/?currency=24&appid=730&market_hash_name=" + AGENT + "%20%7C%20" + GROUP)
    print(responsea.json())
    print(responsea.json()['lowest_price'])
    print(responsea.json()['volume'])

def case():
    CASE = input("Case: ")
    responsec = requests.get("https://steamcommunity.com/market/priceoverview/?currency=24&appid=730&market_hash_name=" + CASE)
    print(responsec.json())
    print(responsec.json()['lowest_price'])
    print(responsec.json()['volume'])

def weaponexc():
    WEAPON = input("Weapon name: ")
    SKIN = input("Skin: ")
    EXTERIOR = input("Exterior type (FN/MW/FT/WW/BS): ")
    WEAPON = re.sub(r"\s+", '%20', WEAPON)
    d = {
            "FN": "Factory New",
            "MW": "Minimal Wear",
            "FT": "Field-Tested",
            "WW": "Well-Worn",
            "BS": "Battle-Scarred"
            }
    EXTERIOR = d[EXTERIOR]
    responsew = requests.get("https://steamcommunity.com/market/priceoverview/?appid=730&market_hash_name=" + WEAPON + "%20%7C%20" + SKIN + "%20" + "%28" + EXTERIOR + "%29" + "&currency=24")
    print(responsew.json()['lowest_price'])
    

def agentexc():
    print()

def caseexc():
    print()

def inv():
    print()

def exc():
    global tries
    una = input("\nUsername: ")
    pas = getpass.getpass()  
    if una == "root" and pas == "NoPe":
        TYPEn = input("\nChoose type from (Weapon/Agent/Case/Inv): ")
        if TYPEn == "weapon":
            waeponexc()    
        if TYPEn == "agent":
            agentexc()
        if TYPEn == "case":
            caseexc()
        if TYPEn == "inv":
            inv()
    else:
        if tries > 1:
            tries-=1   
            print('Wrong username or password')
            exc()
        else:  
            print("\nWe couldn't verify if you're an account holder. Kindly contact the owner for help. :) ")
            time.sleep(2)
            sys.exit()
def init_input():   
    TYPE = input("Choose type from (Weapon/Agent/Case): ")
    if TYPE == "weapon":
        weapon()
    elif TYPE == "agent":
        agent()
    elif TYPE == "case":
        case()
    elif TYPE == "exc":
        exc()
    else:
        ctypes.windll.user32.MessageBoxW(0, "Please enter a valid option", "INCORRECT RESPONSE !", 0)
        init_input()
