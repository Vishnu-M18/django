from django.shortcuts import render
import requests

# Create your views here.

def index(request):



    url = 'https://newsapi.org/v2/everything?q=Phones&from=2023-05-02&sortBy=popularity&apiKey=e93f017e55374b668dbbe11301c4b5d2'

    crypto_news = requests.get(url).json()

    a = crypto_news['articles']
    desc =[]
    title =[]
    img =[]

    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(title, desc, img)

    context = {'mylist': mylist}

    return render(request, 'index.html', context)
