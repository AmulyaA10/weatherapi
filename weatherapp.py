import streamlit as st
import requests
import pandas as pd
import json
import plotly.graph_objs as go

# Page config
st.set_page_config(page_title="Weather Forecast App", layout="wide")
st.title("🌦️ Weather Forecast with RapidAPI")

# Sidebar controls
st.sidebar.header("Weather Controls")
city = st.sidebar.text_input("City Name", value="Dallas")
lang = st.sidebar.selectbox("Language", options=["EN", "ES", "FR", "HI"], index=0)

# API call function
def get_weather_data(city, lang):
    url = "https://open-weather13.p.rapidapi.com/city"
    querystring = {"city": city, "lang": lang}

    headers = {
        "x-rapidapi-key": "2e3186bb1emsh173af87ec363d8ep1332b3jsn84d96973212d",
        "x-rapidapi-host": "open-weather13.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"API Error {response.status_code}: Could not retrieve data.")
        return None

# Fetch and display data
if st.sidebar.button("Fetch Weather"):
    weather = get_weather_data(city, lang)

    if weather:
        st.subheader(f"🌍 Current Weather in {weather.get('name', 'Unknown')}, {weather.get('sys', {}).get('country', '')}")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Temperature (°C)", f"{weather['main']['temp']} °C")
            st.metric("Feels Like", f"{weather['main']['feels_like']} °C")
        with col2:
            st.metric("Humidity", f"{weather['main']['humidity']}%")
            st.metric("Pressure", f"{weather['main']['pressure']} hPa")
        with col3:
            st.metric("Wind Speed", f"{weather['wind']['speed']} m/s")
            st.metric("Weather", f"{weather['weather'][0]['description'].capitalize()}")

        # Display JSON (optional for debugging)
        with st.expander("🔍 Raw Weather Data (JSON)"):
            st.json(weather)

        # Map (if coordinates available)
        if 'coord' in weather:
            lat = weather['coord']['lat']
            lon = weather['coord']['lon']
            st.subheader("📍 Location on Map")
            st.map(pd.DataFrame([[lat, lon]], columns=['lat', 'lon']))
    else:
        st.warning("No data available for the specified city.")
