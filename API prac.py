import requests
from bs4 import BeautifulSoup
import re

session = requests.session()
resp = session.get("https://opensource-demo.orangehrmlive.com/")

soup = BeautifulSoup(resp.text, 'lxml')
# csrf = soup.select("#csrf_token")[0].get("value")
# print(csrf)

parser = re.compile(r'<input type="hidden" name="_csrf_token" value="(.+)?" id="csrf_token"')
csrf = re.search(parser, resp.text)
#print(csrf.group(1))