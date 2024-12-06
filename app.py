import streamlit as st
import datetime
import requests
import pandas as pd

'''
# TaxiFareModel
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')


## Please complete the field hereafter:

date = st.date_input('Enter date')
time = st.time_input('Enter time')
pickup_longitude = st.number_input('Enter pickup longitude')
pickup_latitude = st.number_input('Enter pickup latitude')
dropoff_longitude = st.number_input('Enter dropoff longitude')
dropoff_latitude = st.number_input('Enter dropoff latitude')
passenger_count = st.number_input('Enter the number of passenger')


## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡

url = 'https://taxifare.lewagon.ai/predict'

if st.button('predict fare'):
    if all([date, time,pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude,passenger_count ]):
        params = {'date':date, 'time':time, 'pickup_longitude' :float(pickup_longitude),'pickup_latitude' :float(pickup_latitude),
                  'dropoff_longitude' :float(dropoff_longitude),'dropoff_latitude' :float(dropoff_latitude),
                  'passenger_count' : int(passenger_count)}

    try:
        reponse = requests.get(url, params=params)

        reponse.raise_for_status()

        prediction = response.json().get("fare", "No fare returned")
            st.success(f"The predicted fare is: ${prediction:.2f}")

    except Exception as e:
        st.error(f"Error calling the API: {e}")
    else:
        st.error("Please fill in all fields before predicting!")
