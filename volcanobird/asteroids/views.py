from datetime import datetime, timedelta
import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from volcanobird.volcanobird.settings import NASA_NEO_URL, NASA_API_KEY

def index(request):
    start_date = datetime.now().strftime("%Y-%m-%d")
    end_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    url = f"{NASA_NEO_URL}start_date={start_date}&end_date={end_date}&api_key={NASA_API_KEY}"
    r = requests.get(url)
    j_response = r.json()
    print(j_response['near_earth_objects'][start_date])

    template = loader.get_template('asteroids/index.html')
    context = {
        'element_count': j_response['element_count'],
        'objects_today': j_response['near_earth_objects'][start_date],
        'start_date': start_date,
        'end_date': end_date
    }
    return HttpResponse(template.render(context, request))