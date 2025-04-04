import whois
import time
import sys
import os

print("Tool made by: https://github.com/GabrielConforto")
divider = "---------------------------------------------"

while type !=1 or type !=2:
    
    print("What kind of information are you looking for?")
    print(divider)
    type = int(input("1-Domain / 2-IP Address"))

    if type == 1:
        print(divider)
        print("Domain lookup")
        domain = input("Which domain do you want to lookup?")
        domainlookup = whois.whois(domain)
        print(domainlookup)
        sys.exit()

    elif type == 2:
        print(divider)
        print("IP lookup")
        IP = input("Which IP do you want to lookup?")
        IPlookup = whois.whois(IP)
        print(IPlookup)
        sys.exit()

    else:
        print(divider)
        print("PLEASE PROVIDE A VALID LOOKUP")
        time.sleep(1.5)
        print(divider)

