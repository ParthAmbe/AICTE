import streamlit as st
import pickle

st.set_page_config(page_title="Disease Prediction", page_icon="⚕️")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stAppViewContainer"] {
        background-image: url("data:image/jpeg;base64,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");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    [data-testid="stAppViewContainer"]::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
       
    }
    </style>
""", unsafe_allow_html=True)

models = {
    'diabetes': pickle.load(open('D:\AICTE\Medical\Trained-models\diabetes_model.sav', 'rb')),
    'heart_disease': pickle.load(open('D:\AICTE\Medical\Trained-models\heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('D:\AICTE\Medical\Trained-models\parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('D:\AICTE\Medical\Trained-models\lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('D:\AICTE\Medical\Trained-models\Thyroid_model.sav', 'rb'))
}

selected = st.selectbox("Select a Disease to Predict", [
    'Diabetes Prediction',
    'Heart Disease Prediction',
    "Parkinsons Prediction",
    "Lung Cancer Prediction",
    "Hypo-Thyroid Prediction"
])

def display_input(label, key, type="number"):
    return st.number_input(label, key=key, step=1) if type == "number" else st.text_input(label, key=key)

if selected == 'Diabetes Prediction':
    st.title('Diabetes')
    Pregnancies = display_input('Number of Pregnancies', 'Pregnancies')
    Glucose = display_input('Glucose Level', 'Glucose')
    BloodPressure = display_input('Blood Pressure', 'BloodPressure')
    SkinThickness = display_input('Skin Thickness', 'SkinThickness')
    Insulin = display_input('Insulin Level', 'Insulin')
    BMI = display_input('BMI value', 'BMI')
    DiabetesPedigreeFunction = display_input('Diabetes Pedigree Function', 'DiabetesPedigreeFunction')
    Age = display_input('Age', 'Age')
    
    if st.button('Diabetes Test Result'):
        diab_prediction = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        st.success('The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic')

if selected == 'Heart Disease Prediction':
    st.title('Heart Disease')
    inputs = [display_input(label, key) for label, key in [
        ('Age', 'age'), ('Sex (1 = male; 0 = female)', 'sex'), ('Chest Pain types (0-3)', 'cp'),
        ('Resting Blood Pressure', 'trestbps'), ('Serum Cholesterol', 'chol'), ('Fasting Blood Sugar > 120 mg/dl', 'fbs'),
        ('Resting ECG results (0-2)', 'restecg'), ('Max Heart Rate', 'thalach'), ('Exercise Induced Angina', 'exang'),
        ('ST depression', 'oldpeak'), ('Slope of ST segment (0-2)', 'slope'), ('Major vessels (0-3)', 'ca'),
        ('Thal (0-2)', 'thal')]]
    if st.button('Heart Disease Test Result'):
        heart_prediction = models['heart_disease'].predict([inputs])
        st.success('The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease')

if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease")
    inputs = [display_input(label, key) for label, key in [
        ('MDVP:Fo(Hz)', 'fo'), ('MDVP:Fhi(Hz)', 'fhi'), ('MDVP:Flo(Hz)', 'flo'),
        ('MDVP:Jitter(%)', 'Jitter_percent'), ('MDVP:Jitter(Abs)', 'Jitter_Abs'),
        ('MDVP:RAP', 'RAP'), ('MDVP:PPQ', 'PPQ'), ('Jitter:DDP', 'DDP'),
        ('MDVP:Shimmer', 'Shimmer'), ('MDVP:Shimmer(dB)', 'Shimmer_dB'),
        ('Shimmer:APQ3', 'APQ3'), ('Shimmer:APQ5', 'APQ5'), ('MDVP:APQ', 'APQ'),
        ('Shimmer:DDA', 'DDA'), ('NHR', 'NHR'), ('HNR', 'HNR'),
        ('RPDE', 'RPDE'), ('DFA', 'DFA'), ('Spread1', 'spread1'),
        ('Spread2', 'spread2'), ('D2', 'D2'), ('PPE', 'PPE')]]
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = models['parkinsons'].predict([inputs])
        st.success("The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease")

if selected == "Lung Cancer Prediction":
    st.title("Lung Cancer")
    inputs = [display_input(label, key) for label, key in [
        ('Gender (1 = Male; 0 = Female)', 'GENDER'), ('Age', 'AGE'), ('Smoking', 'SMOKING'),
        ('Yellow Fingers', 'YELLOW_FINGERS'), ('Anxiety', 'ANXIETY'), ('Peer Pressure', 'PEER_PRESSURE'),
        ('Chronic Disease', 'CHRONIC_DISEASE'), ('Fatigue', 'FATIGUE'), ('Allergy', 'ALLERGY'),
        ('Wheezing', 'WHEEZING'), ('Alcohol Consuming', 'ALCOHOL_CONSUMING'), ('Coughing', 'COUGHING'),
        ('Shortness Of Breath', 'SHORTNESS_OF_BREATH'), ('Swallowing Difficulty', 'SWALLOWING_DIFFICULTY'),
        ('Chest Pain', 'CHEST_PAIN')]]
    if st.button("Lung Cancer Test Result"):
        lungs_prediction = models['lung_cancer'].predict([inputs])
        st.success("The person has lung cancer" if lungs_prediction[0] == 1 else "The person does not have lung cancer")

if selected == "Hypo-Thyroid Prediction":
    st.title("Hypo-Thyroid")
    inputs = [display_input(label, key) for label, key in [
        ('Age', 'age'), ('Sex (1 = Male; 0 = Female)', 'sex'), ('On Thyroxine', 'on_thyroxine'),
        ('TSH Level', 'tsh'), ('T3 Measured', 't3_measured'), ('T3 Level', 't3'), ('TT4 Level', 'tt4')]]
    if st.button("Thyroid Test Result"):
        thyroid_prediction = models['thyroid'].predict([inputs])
        st.success("The person has Hypo-Thyroid" if thyroid_prediction[0] == 1 else "The person does not have Hypo-Thyroid")
