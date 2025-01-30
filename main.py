from IPython.display import HTML
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("model_final.pkl")

#Load the encoder & scaler
encoder0=joblib.load("enco.pkl")
encoder1=joblib.load("InternetService.pkl")
encoder2=joblib.load("Contract.pkl")
encoder3=joblib.load("PaymentMethod.pkl")

scaler0 = joblib.load("tenure.pkl")
scaler1 = joblib.load("MonthlyCharges.pkl")
scaler2= joblib.load("TotalCharges.pkl")


# Define function to make predictions

def predict(input_features):

    # Perform any necessary preprocessing on the input_features

    # Make predictions using the loaded model

    prediction = model.predict(input_features)
    return prediction[0]
# Create the web interface

def main():

    st.title("Model for predicting the renewal of a phone subscription")

    st.write("Fill in the fields to get the prediction")

    # Create input fields for user to enter data

    tenure = st.number_input("How many months has the customer been with us (tenure)", min_value=1.0, step=1.0)
    encodedtenure=scaler0.transform([[tenure]])[0][0]
    st.write(encodedtenure)

    MultipleLines=st.selectbox("Multiple phone lines ?",["Yes","No","No phone service"])
    encodedMultipleLines=encoder0.transform([MultipleLines])[0]
    st.write(encodedMultipleLines)

    InternetService=st.selectbox("internet service ?",["DSL","Fiber optic","No"])
    encodedInternetService=encoder1.transform([InternetService])[0]
    st.write(encodedInternetService)

    OnlineSecurity = st.selectbox("Online security ?",["Yes","No","No internet service"])
    encodedOnlineSecurity=encoder0.transform([OnlineSecurity])[0]
    st.write(encodedOnlineSecurity)

    OnlineBackup = st.selectbox("Online backup ?",["Yes","No","No internet service"])
    encodedOnlineBackup=encoder0.transform([OnlineBackup])[0]
    st.write(encodedOnlineBackup)


    DeviceProtection = st.selectbox("Does he have equipment protection?",["Yes","No","No internet service"])
    encodedDeviceProtection=encoder0.transform([DeviceProtection])[0]
    st.write(encodedDeviceProtection)

    TechSupport = st.selectbox("Does he have TechSupport ?",["Yes","No","No internet service"])
    encodedTechSupport=encoder0.transform([TechSupport])[0]
    st.write(encodedTechSupport)

    StreamingTV=st.selectbox('Streaming TV ?',["Yes","No","No internet service"])
    encodedStreamingTV=encoder0.transform([StreamingTV])[0]
    st.write(encodedStreamingTV)

    StreamingMovies=st.selectbox('Streaming Movies ?',["Yes","No","No internet service"])
    encodedStreamingMovies=encoder0.transform([StreamingMovies])[0]
    st.write(encodedStreamingMovies)

    Contract=st.selectbox('Type of contract ?',["Month-to-month","One year","Two year"])
    encodedContract=encoder2.transform([Contract])[0]
    st.write(encodedContract)

    PaymentMethod=st.selectbox('Payment method ?',["Electronic check","Mailed check","Bank transfer (automatic)","Credit card (automatic)"])
    encodedPaymentMethod=encoder3.transform([PaymentMethod])[0]
    st.write(encodedPaymentMethod)


    MonthlyCharges = st.number_input("Monthly charges (amount) ?", min_value=0.0)
    encodedMonthlyCharges=scaler1.transform([[MonthlyCharges]])[0][0]
    st.write(encodedMonthlyCharges)

    TotalCharges = st.number_input("Total charges (amount) ?", min_value=0.0)
    encodedTotalCharges=scaler2.transform([[TotalCharges]])[0][0]
    st.write(encodedTotalCharges)

    gender_Male=st.selectbox('Gender',['Homme','Femme'])
    if gender_Male=="Homme":
       encodedgender_Male=True
    else:
       encodedgender_Male=False
    st.write(encodedgender_Male)

    Partner_Yes=st.selectbox('Is he a partner?',['Yes', 'No'])
    if Partner_Yes=="Yes":
       encodedPartner_Yes=True
    else:
       encodedPartner_Yes=False
    st.write(encodedPartner_Yes)

    Dependents_Yes=st.selectbox('Is he dependent?',['Yes', 'No'])
    if Dependents_Yes=="Yes":
       encodedDependents_Yes=True
    else:
       encodedDependents_Yes=False
    st.write(encodedDependents_Yes)

    PhoneService_Yes=st.selectbox('Does he have a telephone service?',['Yes', 'No'])
    if PhoneService_Yes=="Yes":
       encodedPhoneService_Yes=True
    else:
       encodedPhoneService_Yes=False
    st.write(encodedPhoneService_Yes)

    PaperlessBilling_Yes=st.selectbox('Paperless billing ?',['Yes', 'No'])
    if PaperlessBilling_Yes=="Yes":
       encodedPaperlessBilling_Yes=True
    else:
       encodedPaperlessBilling_Yes=False
    st.write(encodedPaperlessBilling_Yes)

    SeniorCitizen_1=st.selectbox('Is he a senior citizen ?',['Yes', 'No'])
    if SeniorCitizen_1=="Yes":
       encodedSeniorCitizen_1=True
    else:
       encodedSeniorCitizen_1=False
    st.write(encodedSeniorCitizen_1)

    # Combine input features into a DataFrame



    input_data = pd.DataFrame({'tenure': [encodedtenure],"MultipleLines":[encodedMultipleLines],'InternetService': [encodedInternetService],'OnlineSecurity': [encodedOnlineSecurity],
                               "OnlineBackup":[encodedOnlineBackup],"DeviceProtection":[encodedDeviceProtection],"TechSupport":[encodedTechSupport],"StreamingTV":[encodedStreamingTV],
                               "StreamingMovies":[encodedStreamingMovies],"Contract":[encodedContract],"PaymentMethod":[encodedPaymentMethod],"MonthlyCharges":[encodedMonthlyCharges],
                               "TotalCharges":[encodedTotalCharges],"gender_Male":[encodedgender_Male],"Partner_Yes":[encodedPartner_Yes],"Dependents_Yes":[encodedDependents_Yes],
                               "PhoneService_Yes":[encodedPhoneService_Yes],"PaperlessBilling_Yes":[encodedPaperlessBilling_Yes],"SeniorCitizen_1":[encodedSeniorCitizen_1]})
    st.write(input_data)

    # Add more features as needed

    if st.button('Predictions'):

        predictions = predict(input_data)
        st.write(predictions)
        if predictions==False:
          emoji='''<div style="font-size: 200px; text-align: center;">😍</div>'''
          st.markdown(emoji, unsafe_allow_html=True)
          text = """<div style="text-align: center; font-size: 60px;color: green;">Congratulation ! He will either become a new customer or continue with us.</div>"""
          st.markdown(text, unsafe_allow_html=True)
        else:
          emoji='''<div style="font-size: 200px; text-align: center;">😅</div>'''
          st.markdown(emoji, unsafe_allow_html=True)
          text = """<div style="text-align: center; font-size: 60px;color: red;">The offer needs to be reviewed, as the subscriber has no intention of renewing.</div>"""
          st.markdown(text, unsafe_allow_html=True)





if __name__ == '__main__':

    main()
