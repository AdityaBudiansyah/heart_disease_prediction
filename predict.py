import streamlit as st

from web_fungtions import predict

def app(df, x, y):
    st.title("Halaman Prediksi")

    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.number_input('Input usia')
    with col1:
        Sex = st.number_input('Input jenis kelamin')
    with col1:
        Chest_pain_type = st.number_input('Input jenis nyeri dada')
    with col1:
        BP = st.number_input('Input tekanan darah')
    with col2:
        Cholesterol = st.number_input('Input kadar kolesterol')
    with col2:
        FBS_over_120 = st.number_input('Input gula darah')
    with col2:
        EKG_results	 = st.number_input('Input hasil elektrokardiogram')
    with col2:
        Max_HR = st.number_input('Input Denyut jantung maksimum yang dicapai')
    with col3:
        Exercise_angina = st.number_input('Input Angina akibat olahraga')
    with col3:
        ST_depression = st.number_input('Input ST Depression')
    with col3:
        Slope_of_ST = st.number_input('Input Kemiringan')
    with col3:
        Number_of_vessels_fluro = st.number_input('Input Jumlah pembuluh darah utama')
    with col3:
        Thallium = st.number_input('Input tipe thalassemia')

    features = [Age,Sex,Chest_pain_type,BP,Cholesterol,FBS_over_120,EKG_results,Max_HR,Exercise_angina,ST_depression,Slope_of_ST,Number_of_vessels_fluro,Thallium]

    if st.button("Prediksi"):
        prediction, score = predict(x,y,features)
        score = score
        st.info("Prediksi Sukses...")

        if (prediction == 1):
            st.warning("Orang tersebut rentan terkena penyakit jantung")
        else: 
            st.success("Orang tersebut relatif aman dari penyakit jantung")

        st.write("Model yang digunakan memiliki tingkat akurasi", (score*100),"%")