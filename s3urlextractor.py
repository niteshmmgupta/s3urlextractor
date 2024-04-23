import sys
import requests
from bs4 import BeautifulSoup

def extractkeyValues(domain):
    response = requests.get(url=domain).text
    soup = BeautifulSoup(response, 'xml')
    ipaddr = []
    for key in soup.find_all('Key'):
        ipaddr.append(key.get_text())
    return ipaddr

def urlCreator(url,paths):
    complete_urls = [url + path for path in paths]
    return complete_urls


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    url_argument = sys.argv[1]

    # Check if the provided URL starts with "https://"
    if url_argument.startswith("https://"):
        url = url_argument
        domain = url.split("//")[1].split("/")[0]
    else:
        domain = url_argument
        url = "https://" + domain
    
    path = extractkeyValues(url)
    complete_urls = (urlCreator(url,path))
    with open("urls.txt", "w") as file:
        for url in complete_urls:
            file.write(url + "\n")

main()

