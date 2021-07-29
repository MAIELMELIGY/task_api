import urllib.request
from django.shortcuts import render
from datetime import datetime, timedelta
from collections import Counter
import json
import requests
def index(request):
    if request.method == 'POST':
        search = request.POST['search']
        today = datetime.now()    
        date = today - timedelta(days=10)
        url = "https://api.github.com/search/repositories?q={search}:>{date}z&sort=stars&order=desc"
        response = requests.get(url)
        data_of_repo= response.json()
        data_list = data_of_repo['items']
        data_slice = data_list[:3]
        language = []
        url = []
        lang_num =[]
        for repo in data_slice:
            language.append(repo['language'])
            url.append(repo['url'])
       
        for repolang in data_list:

            if repolang['language'] in language:
                lang_num.append(repolang['language'])
        final_lang = Counter(lang_num)
        repo = {
            'language':language,
            'url':url,
            'final_lang':final_lang,
        }
        print(repo)
    else:
        repo={}
        


    
    return render(request, 'repo.html',repo)
'''
def tryfun(request):
    if request.method == 'POST':
        search = request.POST['search']
        today = datetime.now()    
        date = today - timedelta(days=10)
        url = "https://api.github.com/search/repositories?q={search}:>{date}z&sort=stars&order=desc"
        response = requests.get(url)
        data= response.json()
        data_list = data['items']
        data_slice = data_list[:3]
        language = []
        url = [] 
        for repo in data_slice:
            language.append(repo['language'])
            url.append(repo['url'])

       
    return render(request, 'repo.html', language,url,)

'''
