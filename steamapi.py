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
    root = Tk()
    root.title(WEAPON +" "+ SKIN + " | " + EXTERIOR)
    lbl = Label(root, font = ('source code pro', 20, 'bold'), background = 'black', foreground = 'pink')
    lbl.config(text = 'Prices start at ' + requests.get("https://steamcommunity.com/market/priceoverview/?appid=730&market_hash_name=" + WEAPON + "%20%7C%20" + SKIN + "%20" + "%28" + EXTERIOR + "%29" + "&currency=24").json()['lowest_price']+ "\n" + 'Currently '+ requests.get("https://steamcommunity.com/market/priceoverview/?appid=730&market_hash_name=" + WEAPON + "%20%7C%20" + SKIN + "%20" + "%28" + EXTERIOR + "%29" + "&currency=24").json()['volume'] + ' units are available in the market')
    lbl.pack(anchor = 'center')
    root.mainloop()

def agent():
    AGENT = input("Agent: ")
    GROUP = input("Group: ")
    root = Tk()
    root.title(AGENT + " | " + EXTERIOR)
    lbl = Label(root, font = ('source code pro', 20, 'bold'), background = 'black', foreground = 'pink')
    lbl.config(text = 'Prices start at '+ requests.get("https://steamcommunity.com/market/priceoverview/?currency=24&appid=730&market_hash_name=" + AGENT + "%20%7C%20" + GROUP).json()['lowest_price']+ "\n" + 'Currently '+ requests.get("https://steamcommunity.com/market/priceoverview/?currency=24&appid=730&market_hash_name=" + AGENT + "%20%7C%20" + GROUP).json()['volume'] + ' units are available in the market')
    lbl.pack(anchor = 'center')
    root.mainloop()

def case():
    CASE = input("Case: ")
    root = Tk()
    root.title(CASE + " Case")
    lbl = Label(root, font = ('source code pro', 20, 'bold'), background = 'black', foreground = 'pink')
    lbl.config(text = 'Prices start at '+ requests.get("https://steamcommunity.com/market/priceoverview/?currency=24&appid=730&market_hash_name=" + CASE).json()['lowest_price'] + "\n" + 'Currently '+ requests.get("https://steamcommunity.com/market/priceoverview/?currency=24&appid=730&market_hash_name=" + CASE).json()['volume'] + ' units are available in the market')    
    lbl.pack(anchor = 'center')    
    root.mainloop()

def init_input():   
    TYPE = input("Choose type from (Weapon/Agent/Case): ")
    if TYPE == "weapon":
        weapon()
    elif TYPE == "agent":
        agent()
    elif TYPE == "case":
        case()
    else:
        root = Tk()
        root.title('INCORRECT RESPONSE !')
        lbl = Label(root, font = ('source code pro', 20, 'bold'), background = 'black', foreground = 'pink') 
        lbl.config(text = 'Please enter a valid response.')
        lbl.pack(anchor = 'center')
        root.mainloop()
        init_input()

init_input()
