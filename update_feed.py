import urllib.request
import json
from datetime import datetime

url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"

try:
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    
    # Get the top 10 most recently added vulnerabilities
    vulnerabilities = sorted(data['vulnerabilities'], key=lambda x: x['dateAdded'], reverse=True)[:10]
    
    with open("README.md", "w") as file:
        file.write("# 🚨 CISA Known Exploited Vulnerabilities (Automated Feed)\n\n")
        file.write(f"*Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC*\n\n")
        file.write("This repository automatically tracks the latest vulnerabilities added to the CISA KEV catalog using a scheduled GitHub Actions workflow.\n\n")
        file.write("| CVE ID | Vulnerability Name | Date Added | Action Due |\n")
        file.write("|--------|--------------------|------------|------------|\n")
        
        for vuln in vulnerabilities:
            file.write(f"| {vuln['cveID']} | {vuln['vulnerabilityName']} | {vuln['dateAdded']} | {vuln['dueDate']} |\n")
            
except Exception as e:
    print(f"Error fetching data: {e}")
