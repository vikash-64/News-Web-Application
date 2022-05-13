from django.shortcuts import loader , HttpResponse , render 
import requests

API_KEY = '3518f7d019594a4bb16b96ae5ce52a83'
def index(request):

    country = 'in'
    country_codes = Countries() 
    box_data = request.GET.get('country')
    box_data = str(box_data)
    box_data = box_data.capitalize()
    catagories = request.GET.get('catagoriess')
    if box_data in country_codes:
 
        country = country_codes[box_data] 
    
    
    urlss = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
    
    if catagories != None :

        urlss = f'https://newsapi.org/v2/top-headlines?category={catagories}&apiKey={API_KEY}'


    response = requests.get(urlss)

    data = response.json()
    
    articles = data['articles']

    context = {
        'articles': articles
    }
   
    return render(request, 'index.html' , context)
 

def Countries(): 
    return {'Argentina':'ar', 
    'Australia': 'au',
    'Austria': 'at',
    'Belgium': 'be',
    'Brazil': 'br',
    'Bulgaria': 'bg',
    'Canada': 'ca',
    'China': 'cn',
    'Colombia': 'co',
    'Cuba': 'cu',
    'Czech Republic': 'cz',
    'Egypt': 'eg',
    'France': 'fr',
    'Germany': 'de',
    'Greece' : 'gr',
    'Hong Kong': 'hk',
    'Hungary': 'hu',
    'India': 'in',
    'Indonesia': 'id',
    'Ireland': 'ie',
    'Israel': 'il', 
    'Italy': 'it',
    'Japan': 'jp',   
    'Latvia': 'lv',
    'Lithuania': 'lt',
    'Malaysia': 'my',
    'Mexico': 'mx',
    'Morocco': 'ma',
    'Netherlands': 'nl',
    'New Zealand': 'nz',
    'Nigeria': 'ng',
    'Norway': 'no',
    'Philippines':'ph',
    'Poland': 'pl',
    'Portugal': 'pt',
    'Romania': 'ro',
    'Russia': 'ru',
    'Saudi Arabia': 'sa',
    'Serbia': 'rs',
    'Singapore': 'sg',
    'Slovakia': 'sk',
    'Slovenia': 'si',
    'South Africa': 'za',
    'South Korea': 'kr',
    'Sweden': 'se',
    'Switzerland': 'ch',
    'Taiwan': 'tw',
    'Thailand': 'th',
    'Turkey': 'tr',
    'UAE': 'ae',
    'Ukraine': 'ua',
    'United Kingdom': 'uk',
    'United States': 'us',
    'America' : 'us',
    'Us': 'us',
    'Uk': 'uk',
    
    'Venuzuela': 've',            
    }
