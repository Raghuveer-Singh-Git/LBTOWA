from helperFunctions import create_trust_line
from pprint import pprint
import sys

#---------- Details Requried ----------#
issuer_address = "##################################"
currency_code = input("Please Enter The Currency Code: ")
reciver_seed = input("Please Enter your wallet seed: ")

response = create_trust_line(issuer_address,currency_code,reciver_seed)
if response.status._value_ != "success":
    print("Error: Could not create trust line")
    pprint(response)
    sys.exit(1)
print("Info: Trust Line Created")
