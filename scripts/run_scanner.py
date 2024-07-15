import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from vulnerability_scanner.domain_check import Domain_Check
from vulnerability_scanner.email_validation import Email_Validation
from vulnerability_scanner.ip_check import IP_Check
from vulnerability_scanner.text_check import Text_Check

prompt_message = (
    '\nPick the type of verification service you are looking for:' + '\n'
    'Options are:' + '\n'
    '1 - Domain - Check if a domain is valid and exists.' + '\n'
    '2 - Email - Validate an email address.' + '\n'
    '3 - IP - Check if an IP address is a known threat.' + '\n'
    '4 - Text - Detect various threats in a text input.' + '\n'
    'To see examples, type "examples".' + '\n'
    'Please enter the number corresponding to your choice:' + '\n'
)

examples_message = (
    'Examples:' + '\n'
    '1. Domain: google.com' + '\n'
    '2. Email: samsmith@gmail.com' + '\n'
    '3. IP: 81.79.7.198 (find your IP at https://www.whatismyip.com/)' + '\n'
    '4. Text: "Your account has been compromised. Please visit http://phishing-site.com to reset your password."' + '\n'
)

while True:
    service = input(prompt_message).lower()
    if service == 'exit':
        print('Closing the program.')
        break
    elif service == 'examples':
        print(examples_message)
        continue

    try:
        if service == '1':
            domain = input('Please enter the domain you would like to verify: ')
            Domain_Check(domain)
        elif service == '2':
            email = input('Please enter the email address you would like to verify: ')
            Email_Validation(email)
        elif service == '3':
            ip_address = input('Please enter the IP address you would like to verify: ')
            IP_Check(ip_address)
        elif service == '4':
            text_input = input('Please enter the text you would like to verify: ')
            Text_Check(text_input)
        else:
            print("Invalid entry or the email address does not exist. Please check and try again.")
    except (ValidateApiException, SecurityApiException) as e:
        if isinstance(e, ValidateApiException) and e.status == 401:
            print("Unauthorised request. Please check your API key and/or your input.")
        elif isinstance(e, ValidateApiException) and e.status == 503:
            print("Unauthorised request. Please check your API key and/or your input.")
        else:
            print(f"Exception when calling the API: {e}")