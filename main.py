from IPython.display import HTML
import streamlit as st
import pandas as pd
import joblib


model = joblib.load("model_final.pkl")


encoder0=joblib.load("enco.pkl")
encoder1=joblib.load("InternetService.pkl")
encoder2=joblib.load("Contract.pkl")
encoder3=joblib.load("PaymentMethod.pkl")

scaler0 = joblib.load("tenure.pkl")
scaler1 = joblib.load("MonthlyCharges.pkl")
scaler2= joblib.load("TotalCharges.pkl")




def predict(input_features):

   

    

    prediction = model.predict(input_features)
    return prediction[0]


def main():

    st.title("Model for predicting the renewal of a phone subscription")

    st.write("Fill in the fields to get the prediction")

    

    tenure = st.number_input("How many months has the customer been with us (tenure)", min_value=1.0, step=1.0)
    encodedtenure=scaler0.transform([[tenure]])[0][0]
    

    MultipleLines=st.selectbox("Multiple phone lines ?",["Yes","No","No phone service"])
    encodedMultipleLines=encoder0.transform([MultipleLines])[0]
    

    InternetService=st.selectbox("internet service ?",["DSL","Fiber optic","No"])
    encodedInternetService=encoder1.transform([InternetService])[0]
    

    OnlineSecurity = st.selectbox("Online security ?",["Yes","No","No internet service"])
    encodedOnlineSecurity=encoder0.transform([OnlineSecurity])[0]
    st.write(encodedOnlineSecurity)

    OnlineBackup = st.selectbox("Online backup ?",["Yes","No","No internet service"])
    encodedOnlineBackup=encoder0.transform([OnlineBackup])[0]
    


    DeviceProtection = st.selectbox("Does he have equipment protection?",["Yes","No","No internet service"])
    encodedDeviceProtection=encoder0.transform([DeviceProtection])[0]
    

    TechSupport = st.selectbox("Does he have TechSupport ?",["Yes","No","No internet service"])
    encodedTechSupport=encoder0.transform([TechSupport])[0]
    

    StreamingTV=st.selectbox('Streaming TV ?',["Yes","No","No internet service"])
    encodedStreamingTV=encoder0.transform([StreamingTV])[0]
    

    StreamingMovies=st.selectbox('Streaming Movies ?',["Yes","No","No internet service"])
    encodedStreamingMovies=encoder0.transform([StreamingMovies])[0]
    

    Contract=st.selectbox('Type of contract ?',["Month-to-month","One year","Two year"])
    encodedContract=encoder2.transform([Contract])[0]
    

    PaymentMethod=st.selectbox('Payment method ?',["Electronic check","Mailed check","Bank transfer (automatic)","Credit card (automatic)"])
    encodedPaymentMethod=encoder3.transform([PaymentMethod])[0]
    


    MonthlyCharges = st.number_input("Monthly charges (amount) ?", min_value=0.0)
    encodedMonthlyCharges=scaler1.transform([[MonthlyCharges]])[0][0]
    

    TotalCharges = st.number_input("Total charges (amount) ?", min_value=0.0)
    encodedTotalCharges=scaler2.transform([[TotalCharges]])[0][0]
    

    gender_Male=st.selectbox('Gender',['Homme','Femme'])
    if gender_Male=="Homme":
       encodedgender_Male=True
    else:
       encodedgender_Male=False
    

    Partner_Yes=st.selectbox('Is he a partner?',['Yes', 'No'])
    if Partner_Yes=="Yes":
       encodedPartner_Yes=True
    else:
       encodedPartner_Yes=False
    

    Dependents_Yes=st.selectbox('Is he dependent?',['Yes', 'No'])
    if Dependents_Yes=="Yes":
       encodedDependents_Yes=True
    else:
       encodedDependents_Yes=False
    

    PhoneService_Yes=st.selectbox('Does he have a telephone service?',['Yes', 'No'])
    if PhoneService_Yes=="Yes":
       encodedPhoneService_Yes=True
    else:
       encodedPhoneService_Yes=False
    

    PaperlessBilling_Yes=st.selectbox('Paperless billing ?',['Yes', 'No'])
    if PaperlessBilling_Yes=="Yes":
       encodedPaperlessBilling_Yes=True
    else:
       encodedPaperlessBilling_Yes=False
    

    SeniorCitizen_1=st.selectbox('Is he a senior citizen ?',['Yes', 'No'])
    if SeniorCitizen_1=="Yes":
       encodedSeniorCitizen_1=True
    else:
       encodedSeniorCitizen_1=False
    

    



    input_data = pd.DataFrame({'tenure': [encodedtenure],"MultipleLines":[encodedMultipleLines],'InternetService': [encodedInternetService],'OnlineSecurity': [encodedOnlineSecurity],
                               "OnlineBackup":[encodedOnlineBackup],"DeviceProtection":[encodedDeviceProtection],"TechSupport":[encodedTechSupport],"StreamingTV":[encodedStreamingTV],
                               "StreamingMovies":[encodedStreamingMovies],"Contract":[encodedContract],"PaymentMethod":[encodedPaymentMethod],"MonthlyCharges":[encodedMonthlyCharges],
                               "TotalCharges":[encodedTotalCharges],"gender_Male":[encodedgender_Male],"Partner_Yes":[encodedPartner_Yes],"Dependents_Yes":[encodedDependents_Yes],
                               "PhoneService_Yes":[encodedPhoneService_Yes],"PaperlessBilling_Yes":[encodedPaperlessBilling_Yes],"SeniorCitizen_1":[encodedSeniorCitizen_1]})
    

    

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
        st.write("Copyrights tidjaha jan-2025 !")
        st.image("cv_qr_code.png")





if __name__ == '__main__':

    main()
