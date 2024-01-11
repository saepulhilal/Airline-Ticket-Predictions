import streamlit as st
import pandas as pd
import joblib

def run():
# Load All Files

    with open('model.pkl', 'rb') as file:
        model = joblib.load(file)

    st.title('Predict your ticket price')

    airline = st.selectbox(label='choose your airline',options=['SpiceJet', 'AirAsia', 'Vistara', 'GO_FIRST', 'Indigo',
       'Air_India'])

    source_city = st.selectbox(label='choose departure city',options=['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'])

    departure_time = st.selectbox(label='choose departure time',options=['Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night',
       'Late_Night'])

    stops = st.selectbox(label='how many times did it stop?',options=['zero', 'one', 'two_or_more'])
    
    arrival_time = st.selectbox(label='choose arrival time',options=['Night', 'Morning', 'Early_Morning', 'Afternoon', 'Evening',
       'Late_Night'])

    destination_city = st.selectbox(label='choose departure city',options=['Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai', 'Delhi'])

    type = st.selectbox(label='choose your class',options=['Economy', 'Business'])

    duration = st.number_input(label='input your duration here',min_value=0.83,max_value=49.83)

    days_left = st.number_input(label='input your duration here',min_value=1,max_value=49)
    
    # distance = st.number_input(label='input your distance here',min_value=0.0,max_value=7.5)
    # surge_multiplier = st.selectbox(label='choose your surge_multiplier here',options=[1.  , 1.25, 2.5 , 2.  , 1.75, 1.5 , 3.  ])
    # name = st.selectbox(label='choose your cab name here',options=['Shared', 'Lux', 'Lyft', 'Lux Black XL', 'Lyft XL', 'Lux Black',
    #    'UberXL', 'Black', 'UberX', 'WAV', 'Black SUV', 'UberPool'])
    # product_id = st.selectbox(label='choose your product id here',options=['lyft_line', 'lyft_premier', 'lyft', 'lyft_luxsuv', 'lyft_plus',
    #    'lyft_lux', 'uber_line', 'uber_premier', 'uber', 'uber_luxsuv',
    #    'uber_plus', 'uber_lux'])
    
    # st.write('In the following is the result of the data you have input : ')
    
    data_inf = pd.DataFrame({

        'airline' : airline,
        'source_city' : source_city,
        'departure_time' : departure_time,
        'stops' : stops ,
        'arrival_time' : arrival_time,
        'destination_city' : destination_city,
        'type' : type,
        'duration' : duration,
        'days_left' : days_left,
        }, index=[0])

    st.table(data_inf)


    if st.button(label='predict'):
    
        # Melakukan prediksi data dummy
        y_pred_inf = model.predict(data_inf)

        
        st.metric(label="Here is a prediction of your ticket price : ", value = round(y_pred_inf[0]))

    # If your data is a classification, you can follow the example below 
        # if y_pred_inf[0] == 0:
        #     st.write('Pasien tidak terkena jantung')
        #     st.markdown("[Cara Cegah Serangan Jantung](https://www.siloamhospitals.com/informasi-siloam/artikel/cara-cegah-serangan-jantung-di-usia-muda)")

        # else:
        #     st.write('Pasien kemungkinan terkena jantung')
        #     st.markdown("[Cara Hidup Sehat Sehabis Terkena Serangan Jantung](https://lifestyle.kompas.com/read/2021/11/09/101744620/7-pola-hidup-sehat-setelah-mengalami-serangan-jantung?page=all)")
