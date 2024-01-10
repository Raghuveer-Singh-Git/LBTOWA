from helperFunctions import *
from pprint import pprint
import sys

#---------------- Account Details -----------------#
cold_wallet_seed = "sEd7hk1DEWYEC21EiDUmwJUUWfT4diN"
hot_wallet_seed = "sEdVwioBsaM9gEZyVxzij7tMuH3yvAU"

#---------------- Currency Details -----------------#
currency_code = "TST" # 3 letter code
issue_quantity = 1000

#---------------- Create Wallets -----------------#
cold_wallet = wallet_from_seed(cold_wallet_seed)
hot_wallet = wallet_from_seed(hot_wallet_seed)

#-------- Configure Cold Wallet Settings ---------#
response = conf_cold_settings(cold_wallet)
if response.status._value_ != "success":
    print("Error: Could not configure cold wallet settings")
    pprint(response)
    sys.exit(1)
print("Info: Cold wallet settings configured")

#--------- Configure Hot Wallet Settings ----------#
response = conf_hot_settings(hot_wallet)
if response.status._value_ != "success":
    print("Error: Could not configure hot wallet settings")
    pprint(response)
    sys.exit(1)
print("Info: Hot wallet settings configured")

#------- Create Trust Line to Cold wallet --------#
response = create_trust_line(cold_wallet.address,currency_code,hot_wallet_seed)
if response.status._value_ != "success":
    print("Error: Could not create trust line")
    pprint(response)
    sys.exit(1)
print("Info: Trust Line Created")

#------------------ Issue Tokens-------------------#
response = issue_tokens(issue_quantity,currency_code,cold_wallet,hot_wallet)
if response.status._value_ != "success":
    print("Error: Could not issue tokens")
    pprint(response)
    sys.exit(1)
print("Info: Tokens Issued")
