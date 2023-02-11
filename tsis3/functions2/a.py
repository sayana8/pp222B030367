# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#Write a function that takes a single movie and returns True if its IMDB score is above 5.5

a=input("enter the movie name: ")
def score(a):
    for m in movies:
        if(m["name"] == a and m["imdb"]>5.5):
            print("good")
            return True
    print("not good")
score(a)

#Write a function that returns a sublist of movies with an IMDB score above 5.5.

def movies_list(movies):
    for m in movies:
        if m["imdb"] > 5.5:
            print(m["name"])
movies_list(movies)

#Write a function that takes a category name and returns just those movies under that category.

a=input("Enter the category: ")
def categoryy(a):
    for m in movies:
        if(m["category"]==a):
            print(m["name"])
categoryy(a)

#Write a function that takes a list of movies and computes the average IMDB score.
sum=0
def average(movies, sum):
    for m in movies:
        sum+=m["imdb"]
    print("THe average value is : " ,round(float(sum/15), 2))
average(movies,sum)

#Write a function that takes a category and computes the average IMDB score.

a=input("Enter the category : ")
sum=0
cnt=0
def avcat(a,cnt, sum):
    for m in movies:
        if(m["category"]==a):
            cnt+=1
            sum+=m["imdb"]
    print("THe average value of the category is : ", round(float(sum/cnt), 2))
avcat(a, cnt, sum) 



