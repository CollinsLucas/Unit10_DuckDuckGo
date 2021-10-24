import pytest
import requests

api_url = "https://api.duckduckgo.com/?q="
@pytest.mark.parametrize("us_presidents",
    ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Jackson", "Van Buren", "Harrison",
    "Tyler", "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant",
    "Hayes", "Garfield", "Arthur", "Cleveland", "Harrison", "McKinley", "Roosevelt", "Taft",
    "Wilson", "Harding", "Coolidge", "Hoover", "Roosevelt", "Truman", "Eisenhower", "Kennedy",
    "Johnson", "Nixon", "Ford", "Carter", "Reagan", "Bush", "Clinton", "Obama", "Trump", "Biden"])

def test_president_search(us_presidents):
    req = requests.get(api_url+ "presidents of the united states&format=json")

    data = req.json()

    topics_list = data["RelatedTopics"]

    topics_text = []

    for topic in topics_list:
        topics_text.append(topic['Text'])

    assert us_presidents in str(topics_text)
