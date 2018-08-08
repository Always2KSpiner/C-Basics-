'''
Created on 15-Jun-2018

@author: anitr
'''
def check_baggage (baggage_weight):
    if (baggage_weight>=0) & (baggage_weight<=40):
        return True
    else:
        return False
def check_immigration(expiry_year):
    if (expiry_year>=2001) & (expiry_year<=2025):
        return True
    else:
        return False
def check_security(noc_status):
    if (noc_status=='valid') | (noc_status=='VALID'):
        return True
    else:
        return False
def traveler():
    try:
        traveler_id=int(input("ENTER TRAVELER ID \n"))
    except ValueError:
        print("VALUE ERROR!!!\n NUMBER ONLY")
    traveler_name=input("ENTER TRAVELER NAME \n")
    try:
        baggage_weight=int(input("ENETR BAG WEIGHT\n"))
    except ValueError:
        print("VALUE ERROR!!!\n NUMBER ONLY")
    try:
        expiry_year=int(input("ENETR TRAVEL YEAR\n"))
    except ValueError:
        print("VALUE ERROR!!!\n NUMBER ONLY")
    noc_status=input("ENETR NOC STATUS(VALID)\n")
    if(check_baggage (baggage_weight) is True)&(check_immigration(expiry_year) is True)&(check_security(noc_status) is True):
        print("CUSTOMER ID: ",traveler_id)
        print("CUSTOMER NAME: ",traveler_name)
        print("ALLOW TO FLY")
    else:
        print("CUSTOMER ID: ",traveler_id)
        print("CUSTOMER NAME: ",traveler_name)
        print("DETAIN TRAVELER FOR RE-CHECK")
traveler()
