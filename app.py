import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
date = st.date_input(
    "Enter date",
    datetime.date(6, 12,2024 ))
time = st.time_input('Enter time', datetime.time(8, 45))
pickup_longitude = st.number_input('Enter pickup longitude')
pickup_latitude = st.number_input('Enter pickup latitude')
dropoff_longitude = st.number_input('Enter dropoff longitude')
dropoff_latitude = st.number_input('Enter dropoff latitude')
passenger_count = st.number_input('Enter the number of passenger')

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Complete the missing information')

'''
2. Let's build a dictionary containing the parameters for our API...'''

dict = dict(
        pickup_datetime=[pd.Timestamp(f'{date}&{time}', tz='UTC')],
        pickup_longitude=[pickup_longitude],
        pickup_latitude=[pickup_latitude],
        dropoff_longitude=[dropoff_longitude],
        dropoff_latitude=[dropoff_latitude],
        passenger_count=[passenger_count],
    )
'''
3. Let's call our API using the `requests` package...'''
st.markdown(dict)

url = f'https://taxifare.lewagon.ai/predict?{dict}'

reponse = requests.get(url)

st.markdown(reponse)

'''
4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user



'''
