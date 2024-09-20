#!/usr/bin/env python
# coding: utf-8
# %%

# %%


import numpy as np
import pickle
import streamlit as st
import joblib




loaded_model = pickle.load(open(r'C:\\Users\\DELL\\Desktop\\Sanjana\\itvedant\\ML_Project\\rf_model1.sav','rb'))

def AirlineSatisfaction_function(input_data):
    

# changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'Passenger is neutral/dissatisfied'
    else:
        return 'Passenger is satisfied'
    

def main():
    
    st.markdown('<h1 class="title">Airline Passenger Satisfaction Prediction Web App</h1>', unsafe_allow_html=True)
    
    st.markdown(
        
    """
    <style>
    .main {
        background-color: #ADD8E6;
        padding: 20px;
        border-radius: 10px;
    }
    .title {
        font-size: 50px;
        color: maroon;
        text-align: center;
    }
    .stTextInput>label {
        color: maroon;
        font-weight: bold;
        font-size: 20px;
    }
    </style>
    """,    unsafe_allow_html = True)
    
    Gender= st.text_input("Gender: ")
    Customer_Type= st.text_input("Customer Type: ")
    Age= st.text_input("Age: ")
    Type_Of_Travel= st.text_input("Type of Travel: ")
    Customer_Class= st.text_input("Customer Class: ")
    Flight_Distance= st.text_input("Flight Distance: ")
    Inflight_Wifi_Service = st.text_input("Inflight Wifi Service: ")
    Departure_Arrival_Time_Convenient = st.text_input("Departure Arrival Time Convenient: ")
    Ease_of_online_booking = st.text_input("Ease of online booking: ")
    Food_And_Drink = st.text_input("Food and Drink: ")
    Online_Boarding = st.text_input("Online boarding: ")
    Seat_Comfort = st.text_input("Seat comfort: ")
    Inflight_Entertainment = st.text_input("Inflight Entertainment: ")
    Onboard_service = st.text_input("Onboard service: ")
    leg_room_service = st.text_input("Legroom service: ")
    baggage_handling = st.text_input("Baggage Handling: ")
    checkin_service = st.text_input("Checkin service: ")
    inflight_service = st.text_input("Inflight service: ")
    cleanliness = st.text_input("Cleanliness: ")
    departure_delay = st.text_input("Departure Delay: ")
    arrival_delay = st.text_input("Arrival Delay: ")
    
    
    
    result=""
    if st.button("Click here for result"):
        result= AirlineSatisfaction_function([Gender,Customer_Type, Age, Type_Of_Travel,Customer_Class,
                                      Flight_Distance, Inflight_Wifi_Service,Departure_Arrival_Time_Convenient,
                                      Ease_of_online_booking,Food_And_Drink, Online_Boarding, Seat_Comfort,
                                      Inflight_Entertainment, Onboard_service,  leg_room_service,
                                      baggage_handling, checkin_service, inflight_service, cleanliness, departure_delay, arrival_delay])
    st.success(result)
    
    st.write(f'''
        <a target="_self" href="/">
        <button id= "clear-data">
        Clear form
        </button>
        </a>
''',unsafe_allow_html=True)
    
if __name__=='__main__':
    main()


