import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)
q=0
""" for i in data:
    if 2018 > (data[q]['year']) > 2015:
        print (data[q]['title'])
    q=q+1 """

""" for i in data:
    if (data[q]['year']) == 2019:
        print (data[q]['title'])
    q=q+1 """

def rickyissmart():
    for i in data:
        print (data[q]['title'])
    q=q+1
    x = input("")

