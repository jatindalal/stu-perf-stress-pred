import streamlit as st
from performance_prediction_page import show_performance_prediction_page
from stress_prediction_page import show_stress_prediction_page


page = st.sidebar.selectbox("Performance prediction, Stress prediction or Explore", ("Performance prediction", "Stress prediction"))

if page == "Performance prediction":
    show_performance_prediction_page()
elif page == "Stress prediction":
    show_stress_prediction_page()
