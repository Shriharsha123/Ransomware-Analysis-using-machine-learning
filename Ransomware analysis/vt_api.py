#! /usr/bin/python3

import requests
import sys

API_KEY = "01c254aff43bce182b5dca6057355189c0c43e1a21b755e96ca2f1f53a9a25bc"  #<--- Put your API key here

class VirusTotal:
    def __init__(self):
        self.headers = {"accept": "application/json","X-Apikey": API_KEY}
        self.url = "https://www.virustotal.com/api/v3/"

    def upload_hash(self, hash):
        url = self.url + "search?query=" + hash
        response = requests.get(url, headers=self.headers)
        result = response.json()
        
        if response.status_code == 200 and len(result['data']) > 0:
            try:
                malicious = result['data'][0]['attributes']['last_analysis_stats']['malicious']
            except:
                malicious = 0
        else:
            malicious = 0
        
        if len(sys.argv) > 2:
            if malicious > int(sys.argv[2]):
                print(hash + " " + str(malicious))
        else:
            if malicious > 1:
                print(hash + " " + str(malicious))

if __name__ == "__main__":
    try:
        file = open('hashes.txt', 'r')
        lines = file.readlines()
        for line in lines:
            virustotal = VirusTotal()
            virustotal.upload_hash(line[:-1])
    except:
        None