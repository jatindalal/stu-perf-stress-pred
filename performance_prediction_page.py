import streamlit as st
import pickle

def load_model(model_type):
    with open("trained_performace_models/" + model_type + '.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

# Load label encoded dictonaries
dicts = pickle.load(open("dictonaries/performance_model_dict.pkl", "rb"))
gender_dict, ethnicity_dict, parental_edu_level_dict = dicts[0], dicts[1], dicts[2]

# print(gender_dict, ethnicity_dict, parental_edu_level_dict)

def show_performance_prediction_page():
    st.title("Student Performance Prediction")

    st.write("""### Enter information to predict the performance""")

    gender_options = (
        "male",
        "female"
    )

    ethnicity_options = (
        "group A",
        "group B",
        "group C",
        "group D",
        "group E",
    )
    parentel_level_of_education_options = (
        "bachelor's degree",
        "some college",
        "master's degree",
        "associate's degree",
        "high school",
        "some high school"
    )

    model_options = (
        "Linear Regression",
        "Lasso Regression",
        "Random Forest Regressor",
        "Support Vector Regression"
    )

    selected_gender = st.selectbox("Gender", gender_options)
    selected_ethnicity = st.selectbox("Race/Ethnicity", ethnicity_options)
    selected_parentel_level_of_education = st.selectbox("Race/Ethnicity", parentel_level_of_education_options)
    selected_model = st.selectbox("Regression Model to Use", model_options)

    selected_math_score = st.slider("Maths Score", 0, 100, 0)
    selected_reading_score = st.slider("Reading Score", 0, 100, 0)

    ok = st.button("Calculate Writing Score")

    if ok:
        if selected_model == "Linear Regression":
            model = load_model("linear_regression_model")
        elif selected_model == "Random Forest Regressor":
            model = load_model("random_forest_model")
        elif selected_model == "Support Vector Regression":
            model = load_model("svr_model") 
        else:
            model = load_model("lasso_model")
        
        selected_features = [
                                gender_dict[selected_gender],
                                ethnicity_dict[selected_ethnicity], 
                                parental_edu_level_dict[selected_parentel_level_of_education],
                                selected_math_score,
                                selected_reading_score
                            ]

        predicted_writing_score = model.predict([selected_features])

        st.subheader(f"The estimated writing score is {predicted_writing_score[0]:.2f}")