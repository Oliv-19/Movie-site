from django.shortcuts import render
import json
import requests
import random
from django.http import HttpResponse

# Create your views here.
def index(request):
    # url = "https://moviesdatabase.p.rapidapi.com/titles/x/titles-by-ids"
    url = "https://moviesdatabase.p.rapidapi.com/titles/x/titles-by-ids"

    querystring = {"idsList":"tt4154664,tt10676048,tt0371746,tt1228705,tt1300854,tt0458339,tt1843866,tt3498820,tt0800080,tt0848228,tt2395427,tt4154756,tt4154796,tt0800369,tt1981115,tt3501632,tt10648342,tt10648342,tt9376612,tt5095030,tt9032400,tt1211837,tt9419884,tt0478970,tt1825683","info":"base_info"}
    
    querystring2 ={"idsList":'tt6320628,tt2250912,tt10872600,tt2015381,tt6791350,tt3896198,tt9114286,tt1431045,tt5463162,tt3480822,',"info":"base_info"}
    headers = {
        "X-RapidAPI-Key": "306b3eab4cmshfe2bb7966afe897p10cf3ajsnb0f6770d59a4",
        "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
    }

    res = requests.get(url, headers=headers, params=querystring)
    res2 = requests.get(url, headers=headers, params=querystring2)

    json_data = json.loads(res.text)['results']
    json_data2 = json.loads(res2.text)['results']
    # data ={'titles': [], 'img':[], 'year':[], 'rating':[], 'plot':[]}
    indexes= 0
    data = []
    
    
    for i in json_data:
        data.append({'id':i['id'],'titles':i['titleText']['text'], 'img':i['primaryImage']['url'], 'year':i['releaseYear']['year'],
                     'rating':i['ratingsSummary']['aggregateRating'],
                     'plot':i['plot']['plotText']['plainText']})
        # data['titles'].append(i['titleText']['text'])  
        # data['img'].append(i['primaryImage']['url'])  
        # data['year'].append(i['releaseYear']['year'])  
        # data['rating'].append(i['ratingsSummary']['aggregateRating'])  
        # data['plot'].append(i['plot']['plotText']['plainText'])  
        
    for e in json_data2:
        data.append({'id':e['id'],'titles':e['titleText']['text'], 'img':e['primaryImage']['url'], 'year':e['releaseYear']['year'],
                     'rating':e['ratingsSummary']['aggregateRating'],
                     'plot':e['plot']['plotText']['plainText']})
        # data['titles'].append(e['titleText']['text'])  
        # data['img'].append(e['primaryImage']['url'])  
        # data['year'].append(e['releaseYear']['year'])  
        # data['rating'].append(e['ratingsSummary']['aggregateRating'])  
        # data['plot'].append(e['plot']['plotText']['plainText'])  
        
    

    value = random.choices([i['img'] for i in data], k=5)

    ids = ['slide_1','slide_2','slide_3','slide_4','slide_5']
     
    idDict = {ids[0]:value[0], ids[1]:value[1], ids[2]:value[2], ids[3]:value[3], ids[4]:value[4]}

    # if request.method == 'POST':

    #     movieTitle =  request.POST['search_bar']
    #     url = f"https://moviesdatabase.p.rapidapi.com/titles/search/title/{movieTitle}"

    #     querystring = {"exact":"false","info":"base_info","titleType":"movie","limit":"25"}

    #     headers = {
    #         "X-RapidAPI-Key": "306b3eab4cmshfe2bb7966afe897p10cf3ajsnb0f6770d59a4",
    #         "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
    #     }

    #     response = requests.get(url, headers=headers, params=querystring)

    #     json_data = json.loads(response.text)['results']

    #     # data = []
    #     # for j in json_data:
    #     #     data.append({'id':j['id'], 
    #     #             'titles':j['titleText']['text'], 
    #     #             #'img':j['primaryImage']['url'],
    #     #             'caption': j['primaryImage']['caption']['plainText'],
    #     #             'year':j['releaseYear']['year'],
    #     #             'rating':j['ratingsSummary']['aggregateRating'],
    #     #             #'plot':j['plot']['plotText']['plainText']
    #     #             })
    #     return render(request, 'search.html', {'data':json_data})

    
    
    
    return render(request, 'index.html', {'data':data,'idDict':idDict})


def search(request):
    if request.method == 'GET':

        movieTitle =  request.GET['search_bar']

        url = f"https://moviesdatabase.p.rapidapi.com/titles/search/title/{movieTitle}"

        querystring = {"exact":"false","info":"base_info","titleType":"movie","limit":"25"}

        headers = {
            "X-RapidAPI-Key": "306b3eab4cmshfe2bb7966afe897p10cf3ajsnb0f6770d59a4",
            "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        json_data = json.loads(response.text)['results']

        # for j in json_data:
        #     if j['primaryImage']['url'] == None:
        #         print('not image')

        # data = []
        # for j in json_data:
        #     data.append({'id':j['id'], 
        #             'titles':j['titleText']['text'], 
        #             'img':j['primaryImage']['url'],
        #             'year':j['releaseYear']['year'],
        #             'rating':j['ratingsSummary']['aggregateRating'],
        #             'plot':j['plot']['plotText']['plainText']
        #             })
        # print(data)

        return render(request, 'search.html', {'data':json_data})


def movieInfo(request, movieId):
    url = f"https://moviesdatabase.p.rapidapi.com/titles/{movieId}"

    querystring = {"info":"base_info"}

    headers = {
        "X-RapidAPI-Key": "306b3eab4cmshfe2bb7966afe897p10cf3ajsnb0f6770d59a4",
        "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    json_data = json.loads(response.text)['results']
    

    return render(request, 'info.html', {'json_data':json_data})