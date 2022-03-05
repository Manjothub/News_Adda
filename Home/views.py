from django.shortcuts import render
import requests

API_KEY = 'fb7227bb6f194b8895f5058a48156819'
def HOME(request):
    country = request.GET.get('country')
    if country:
        url =  f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url =  f' https://newsapi.org/v2/everything?domains=wsj.com&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    context ={
            'articles':articles
    }
    return render(request,'user/home.html',context)