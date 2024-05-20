
from weather import app
from flask import render_template, redirect, url_for, request
import requests
from datetime import date
from weather.weather import *

@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
def home_page():
  if request.method == "POST":
    print(1)
    search = request.form['search']
    city = search
  
    key='API_KEY'
    url = f'https://api.weatherapi.com/v1/current.json?key={key}&q={city}&aqi=yes'

    #Handle error coming from API response 
    try:
      response = requests.get(url)
      response.raise_for_status()
    except requests.exceptions.HTTPError as err:
      raise SystemExit(err)

    json = response.json()
    print(json)

    #Location details
    Town      = json["location"]["name"]
    Region    = json["location"]["region"]
    Country   = json["location"]["country"]
    Time_Zone = json["location"]["tz_id"]

    #Current weather conditions 
    Temperature    = json ["current"]["temp_c"]
    Condition      = json ["current"]["condition"]["text"]

    # URL used to display what kind of weather we have
    Icon           = json ["current"]["condition"]["icon"]
    Wind_speed     = json ["current"]["wind_kph"]
    Wind_direction = json ["current"]["wind_dir"]
    Humidity       = json ["current"]["humidity"]
    Feels_like     = json ["current"]["feelslike_c"]
    Pressure       = json ["current"]["pressure_mb"]
    Precipitation  = json ["current"]["precip_mm"]
    Cloud_cover    = json ["current"]["cloud"]

    #Air quality
    Carbon         = json ["current"]["air_quality"]["co"]
    Nitrogen_oxide = json ["current"]["air_quality"]["no2"]
    Ozone          = json ["current"]["air_quality"]["o3"]
    Sulphur_dio    = json ["current"]["air_quality"]["so2"]
    US_EPA_Index   = json ["current"]["air_quality"]["us-epa-index"]
    EPA            =  us_epa_index_description(US_EPA_Index)
    
    #Display Weather Conditions:
    return render_template('home.html', Time_Zone=Time_Zone, Country=Country, Region=Region, Town=Town,Temperature=Temperature,Condition=Condition,Wind_speed=Wind_speed,Wind_direction=Wind_direction,Feels_like=Feels_like,Humidity=Humidity,Icon=Icon,Carbon=Carbon,Nitrogen_oxide=Nitrogen_oxide,Ozone=Ozone,Sulphur_dio=Sulphur_dio,US_EPA_Index=US_EPA_Index, Cloud_cover=Cloud_cover,Precipitation=Precipitation, Pressure=Pressure, EPA=EPA)
  else:
    return render_template('home.html')


 