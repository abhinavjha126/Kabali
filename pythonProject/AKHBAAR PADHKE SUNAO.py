#AKHBAAR PADHKE SUNAO
import pyttsx3
import requests
import json
engine=pyttsx3.init()


if __name__ == '__main__':
    engine.say("News for Today.....Let's begin")
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=0802e28604054be9a3d3e7cd498d46d9"
    r=requests.get(url).text
    news=json.loads(r)
    n=news["articles"]
    for articles in n:
        engine.say(articles["title"])
        print(articles["title"])
        engine.say("Next news")
print("Thanks for Listening")
engine.runAndWait()

