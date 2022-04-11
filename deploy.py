import streamlit as st
import pickle
import numpy as np
import sklearn

st.title('Deploying Example for HDSC Capstone')
# page_bg_img = '''
# <style>
# body {
# background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXbmoubmlcnm83vFUWe4QDOjgP02RxWXnUcQ&usqp=CAU");
# background-size: cover;
# }
# </style>
# '''
#
# st.markdown(page_bg_img, unsafe_allow_html=True)

# with open('divorce_model.pkl', 'rb') as f:
#     model = pickle.load(f)
with open('model_pkl' , 'rb') as f:
    lr = pickle.load(f)
#model = pickle.load(pickle_in)

#@st.cache()
#model = pickle.load('divorce_model')

# Making predictions
#model = /home/kehindebello/HDSC_Capstone/divorce_model

No_home_time = st.selectbox('Rate your home time',(1,2,3,4,5))
Compatible_dreams = st.slider('Similar and harmonious dreams', 1, 5)
Happy = st.slider('Same view about happiness',1,5)
Similar_role_idea = st.slider('Similar role idea', 1, 5)
trust = st.slider('Similar values in trust', 1, 5)
anxieties = st.slider('Knowledge of partners anxieties', 1, 5)
hopes_wishes = st.slider('Knowledgeof partners hope and wishes', 1, 5)
Aggro_argue = st.slider('Aggressiveness during argument', 1, 5)
idk_whats_going_on = st.slider('I dont know whats going on', 1, 5)
accusations = st.slider("I have nothing to do with what i'm accused of", 1, 5)


#st.write(No_home_time, Compatible_dreams, Happy, Similar_role_idea, trust,anxieties,hopes_wishes,Aggro_argue,idk_whats_going_on,accusations)

#print(type(model))
if st.button('Predict'):
    prediction = lr.predict(np.array([[No_home_time, Compatible_dreams, Happy, Similar_role_idea, trust,anxieties,hopes_wishes,Aggro_argue,idk_whats_going_on,accusations]]))
    if prediction == 0:
        st.write('More likely to stay together')
    else:
        st.write('More like to Divorce')


# array(['No_home_time', 'dreams', 'happy', 'roles', 'trust', 'anxieties',
#        'hopes_wishes', 'Aggro_argue', "idk_what's_going_on",
#        'accusations']
#st.write(f'Level of home time:{No_home_time}')
