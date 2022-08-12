from flask import request, Flask
import feedparser # we can use that library for parsing url and extract articles informations 
import socket
from db import *
import json

app = Flask(__name__)

@app.route("/parse_url", methods=["POST"])
def data():
    if request.method == "POST":
        data = request.get_json()
        url = str(data["url"])
        print(url)
        feeds = feedparser.parse(url) # for exapmle, we can use ny times rss feed as url url = https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml

        json_list = []

        for feed in feeds["entries"]:

            article_link = feed.link
            title = feed.title
            description = feed.description    

            save_to_db(article_link, title, description)

            item = {"article_link": article_link,
                    "title": title,
                    "description": description}

            json_list.append(item)            

            #print("00000000000", link)
            #print("***********", title)
            #print("-----------", description)

        return json.dumps(json_list, indent="\t")

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print(s.getsockname()[0])
    return s.getsockname()[0]

if __name__ == '__main__':	
    app.run(debug = True, host = get_ip_address(), port = 3002)


