import requests
from bs4 import BeautifulSoup

requests.get("http://stackoverflow.com/questions")
soup = BeautifulSoup(requests.get, "html.parser")

questions = soup.select(".question-summary")
print(questions[0].attrs)
