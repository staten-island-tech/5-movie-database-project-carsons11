import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)



""" for i in data:
    if 2018 > (data[q]['year']) > 2015:
        print (data[q]['title'])
    q=q+1 """

""" for i in data:
    if (data[q]['year']) == 2019:
        print (data[q]['title'])
    q=q+1 """

""" def movies():
    q=0
    for i in data:
        print (data[q]['title'])
        q=q+1
    x = input("What movie do you want?: ")
    w=0
    for i in data:
        if x == data[w]['title']:
            print (data[w])
    w=w+1
movies()  """

""" def genre():
    q=0
    for i in data:
        print (data[q]['genres'])
        q=q+1
    x = input ("What genre of movies do you want to watch?")
    w=0 
    v=0
    for i in data:
        for j in data[w]["genres"]:
            if x == data[w]["genres"][v]:
                print(data[w]["title"])
            v+=1
        v=0
        w+=1
genre() """


# class Hero:
#     def _init_(self,name,money,inventory):
#         self.name = name 
#         self.money = money
#         self.inventory = inventory
#     def buy(self,item):
#         self.inventory.appen(item)
#         print(f"{self.name} purchased {item} and has {self.inventory}")
# Nathan = Hero("Nathan", 0, ["Pencil"])
# print(Nathan._dict_)
# Nathan.buy("Xi Yang")