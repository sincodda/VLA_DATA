import requests
import pandas as pd
from datetime import datetime, timezone, timedelta
import time
import os
import pytz
import json

# Tu clave de API de OpenWeatherMap
API_KEY = "a6b3b4b263a24fe98a3212845241604"
CITY = "Villa La Angostura, AR"  # Cambia esto a la ciudad de tu elección
#DATE = "2024-04-16" # yyyy-mm-dd
Latitud = -40.7836167
Longitud = -71.6596111

def obtener_datos_clima(fecha):
    url = (f"https://api.weatherapi.com/v1/history.json?key={API_KEY}&q={Latitud},{Longitud}&dt={fecha}&lang=sp&aqi=no&alerts=no")
    response = requests.get(url)
    data = response.json()

    # Extraer los datos relevantes (por ejemplo, temperatura, humedad, etc.)
    latitud = data["location"]["lat"]
    longitud = data["location"]["lon"]
    avgtemp_c = data["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
    maxtemp_c = data["forecast"]["forecastday"][0]["day"]["maxtemp_c"]
    mintemp_c = data["forecast"]["forecastday"][0]["day"]["mintemp_c"]
    humidity = data["forecast"]["forecastday"][0]["day"]["avghumidity"]
   # fells_like = data["main"]["feels_like"]
    totalprecip_mm = data["forecast"]["forecastday"][0]["day"]["totalprecip_mm"]
    totalsnow = data["forecast"]["forecastday"][0]["day"]["totalsnow_cm"]
    forecast_time = data["location"]["localtime"]
    forecast = data["forecast"]["forecastday"][0]["day"]["condition"]["text"]
    #forecast_detailed = data["weather"][0]["description"]
    wind_speed = data["forecast"]["forecastday"][0]["day"]["maxwind_kph"] #data["wind"]
    #wind_deg = data["wind"]["deg"]
    #clouds = data["clouds"]["all"]
    #pressure = data["main"]["pressure"]
    visibility = data["forecast"]["forecastday"][0]["day"]["avgvis_km"]
    amanecer = data["forecast"]["forecastday"][0]["astro"]["sunrise"]
    atardecer = data["forecast"]["forecastday"][0]["astro"]["sunset"]


    df = pd.DataFrame({
        "Ciudad": [CITY],
        "Latitud": [latitud],
        "Longitud": [longitud],
        "Fecha": [fecha],
        "Forecast":[forecast],
        "Temperatura Promedio (°C)": [avgtemp_c],  
        "Temperatura Maxima (°C)": [maxtemp_c],
        "Temperatura Minima (°C)": [mintemp_c],
        "Precipitación (mm)": [totalprecip_mm],
        "Nieve (cm)": [totalsnow],
        "Humedad(%)": [humidity],
        "Visibilidad (km)": [visibility],
        "Velocidad Viento(m/s)": [wind_speed],
        "Amanecer (s)": [amanecer],
        "Atardecer (s)": [atardecer],
        "Forecast Time":[forecast_time]
    })

    # Guardar los datos en un archivo CSV
    if not os.path.exists("datos_clima_history_lt.csv"):
        df.to_csv("datos_clima_history_lt..csv", index=False)
    else:
        df.to_csv("datos_clima_history_lt..csv", index=False, mode="a", header=False)  # No incluir el encabezado

    print(f"Datos guardados en datos_clima_history_lt..csv para la fecha {fecha}")

    datos_clima = "datos_clima_history_lt..json"
    with open(datos_clima, "w") as archivo:
        json.dump(data, archivo, indent=4)

if __name__ == "__main__":
    # Obtener datos climáticos para un rango de 7 días
    fecha_actual = datetime.now().date()
    for i in range(21):
        fecha = (fecha_actual - timedelta(days=i)).strftime("%Y-%m-%d")
        obtener_datos_clima(fecha)
        # Esperar 1 hora antes de tomar más datos
        time.sleep(10)  # 3600 segundos = 1 hora