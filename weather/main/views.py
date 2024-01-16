from django.shortcuts import render
from os import getenv
from dotenv import load_dotenv

# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request

load_dotenv()

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = getenv('api_key')

        # Constructing the URL with f-string
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        # Making a request to the API
        source = urllib.request.urlopen(url).read()

        # Converting JSON data to a dictionary
        list_of_data = json.loads(source)

        # Extracting data from the dictionary
        data = {
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": f"{list_of_data['coord']['lon']} {list_of_data['coord']['lat']}", 
            "temp": f"{list_of_data['main']['temp']}k", 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']),
        }
    
    else:
        data = {}

    return render(request, "main/index.html", data)

