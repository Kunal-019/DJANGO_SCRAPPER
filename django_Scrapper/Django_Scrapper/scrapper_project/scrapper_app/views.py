# views.py
from django.shortcuts import render
from .models import Country
import requests
from bs4 import BeautifulSoup

def fetch_country_data(country):
    base_link = f'https://countrycode.org/{country}'
    response = requests.get(base_link)
    soup = BeautifulSoup(response.text, 'html.parser')

    details_xpath = {
        'capital': 'li:has(i.fa-university) ul li',
        'population': 'li:has(i.fa-user) ul li',
        'area': 'li:has(i.fa-superscript) ul li',
        'gdp': 'li:has(i.fa-usd) ul li',
        'country_code': 'div.box-blue h2',
        'iso2': 'div.box-green h3#iso2',
        'iso3': 'div.box-green h4',
    }
    
    details = {}
    for name, selector in details_xpath.items():
        element = soup.select_one(selector)
        if element:
            value = element.get_text().strip()
            details[name] = value

    iso_formatted = f"{details.get('iso2', '')}/{details.get('iso3', '')}"

    return {
        'name': country,
        'capital': details.get('capital', ''),
        'population': details.get('population', ''),
        'area': details.get('area', ''),
        'gdp': details.get('gdp', ''),
        'country_code': details.get('country_code', ''),
        'iso': iso_formatted
    }

def country_info(request):
    if request.method == 'POST':
        selected_country = request.POST.get('selected_country')
        
        country = Country.objects.filter(name=selected_country).first()
        
        if country is None:

            country_data = fetch_country_data(selected_country)
            country_name = country_data.pop('name', None)
            
            country = Country.objects.create(name=country_name, **country_data)
        
        return render(request, 'index.html', {'selected_country': selected_country, 'country_data': country})
    
    return render(request, 'index.html')
