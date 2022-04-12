import streamlit as st
import pickle
import numpy as np
import sklearn

st.title('Deploying Example for HDSC Capstone')

with open('model_pkl' , 'rb') as f:
    lr = pickle.load(f)

No_home_time = st.slider('Rate your home time', 1, 5))
Compatible_dreams = st.slider('Similar and harmonious dreams', 1, 5)
Happy = st.slider('Same view about happiness',1,5)
Similar_role_idea = st.slider('Similar role idea', 1, 5)
trust = st.slider('Similar values in trust', 1, 5)
anxieties = st.slider('Knowledge of partners anxieties', 1, 5)
hopes_wishes = st.slider('Knowledgeof partners hope and wishes', 1, 5)
Aggro_argue = st.slider('Aggressiveness during argument', 1, 5)
idk_whats_going_on = st.slider('I dont know whats going on', 1, 5)
accusations = st.slider("I have nothing to do with what i'm accused of", 1, 5)


if st.button('Predict'):
    prediction = lr.predict(np.array([[No_home_time, Compatible_dreams, Happy, Similar_role_idea, trust,anxieties,hopes_wishes,Aggro_argue,idk_whats_going_on,accusations]]))
    if prediction == 0:
        st.write('More likely to stay together')
    else:
        st.write('More likely to Divorce')

