import streamlit as st
import pickle

def load_model(model_type):
    with open("trained_Stress_models/" + model_type + '.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

# Load label encoded dictonaries
dicts = pickle.load(open("dictonaries/stress_model_dict.pkl", "rb"))
gender_dict, ethnicity_dict, country_dict, pg_study_dict = dicts[0], dicts[1], dicts[2], dicts[3]

#print(gender_dict, ethnicity_dict, country_dict, pg_study_dict)

def show_stress_prediction_page():
    st.title("Student Stress Prediction")

    st.write("""### Enter information to predict the stress level""")

    gender_options = (
        'Male',
        'Female',
        'Prefer not to say'
    )

    ethnicity_options = (
        'White',
        'Mixed / Multiple Ethnic Groups',
        'Asian / Asian British',
        'Black / African / Caribbean / Black British',
        'Other'
    )

    country_options = (
        'International',
        'EU',
        'UK'
    )

    pg_study_options = (
        "PhD",
        "Research master's degree",
        "Taught master's degree",
        "Other"
    )

    model_options = (
        "Decision Tree",
        "K Nearest Neighbours",
        "Naive Bayes (Categorical)",
        "Support Vector Machine"
    )

    selected_gender = st.selectbox("Gender", gender_options)
    selected_ethnicity = st.selectbox("Race/Ethnicity", ethnicity_options)
    selected_country = st.selectbox("Country", country_options)
    selected_pg_study = st.selectbox("PG Study", pg_study_options)
    selected_model = st.selectbox("Classification Model to Use", model_options)

    selected_age = st.slider("Age", 21, 63, 21)

    ok = st.button("Calculate Stress Level")

    if ok:
        if selected_model == "Decision Tree":
            model = load_model("decision_tree_model")
        elif selected_model == "K Nearest Neighbours":
            model = load_model("knn_model")
        elif selected_model == "Naive Bayes (Categorical)":
            model = load_model("knn_model") 
        else:
            model = load_model("svm_model")
        
        selected_features = [
                                gender_dict[selected_gender],
                                ethnicity_dict[selected_ethnicity],   
                                selected_age,
                                country_dict[selected_country],
                                pg_study_dict[selected_pg_study]
                            ]

        predicted_stress_level = model.predict([selected_features])

        st.subheader(f"The estimated stress level is '{predicted_stress_level[0]}'")