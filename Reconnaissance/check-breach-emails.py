# Author:      Md Ali 
# Description: This python script will utilize Have I Been Pwn to see if an email has been 
#              been part of a data breach. You will need to have a valid api-key, and this 
#              script will wait due to the lowest subscription for rate limits.
# Version:     1.0
# Date:        08/01/2024

import requests
import time

def check_email(email, api_key):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        "hibp-api-key": api_key,
        "User-Agent": "email-checker-script"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json() # Breach data
    elif response.status_code == 404:
        return None # No breach data
    else:
        return f"Error: {response.status_code}"
    
# Load emails from file (Please do one email per line in a file calleed emails.txt)
with open("emails.txt", "r") as file:
    emails = [line.strip() for line in file]

api_key = "ENTER API KEY"

with open("breach_results.txt", "w") as output_file:
    for index, email in enumerate(emails):
        result = check_email(email, api_key)
        if result:
            output_file.write(f"Breach found for {email}: {result}\n")
            print(f"Breach found for {email}: {result}")
        else:
            output_file.write(f"No breach found for {email}\n")
            print(f"No breach found for {email}")
        
        if(index + 1) % 10:
            print("Pausing for rate limit...")
            time.sleep(60)
        else:
            time.sleep(6)