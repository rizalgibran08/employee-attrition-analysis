import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model, scaler, dan encoder
try:
    model = joblib.load("model/model_svm.joblib")
    scaler = joblib.load("model/scaler.joblib")
    encoders = joblib.load("model/encoders.joblib")
except Exception as e:
    st.error(f"Gagal memuat model atau tools: {e}")
    st.stop()

# Form input
st.title("Employee Attrition Prediction")

age = st.number_input("Age", min_value=18, max_value=60, value=30)
department = st.selectbox(
    "Department", ["Sales", "Research & Development", "Human Resources"])
distance = st.number_input(
    "Distance From Home", min_value=0, max_value=100, value=5)
education = st.selectbox(
    "Education Level (1= Below College, 2= College, 3= Bachelor, 4= Master, 5= Doctor)", [1, 2, 3, 4, 5])
education_field = st.selectbox("Education Field", [
                               "Life Sciences", "Medical", "Marketing", "Technical Degree", "Human Resources", "Other"])
env_satisfaction = st.selectbox(
    "Environment Satisfaction (1=Low, 2=Medium, 3=High, 4=Very High)", [1, 2, 3, 4])
gender = st.selectbox("Gender", ["Male", "Female"])
job_involvement = st.selectbox(
    "Job Involvement (1=Low, 2=Medium, 3=High, 4=Very High)", [1, 2, 3, 4])
job_level = st.selectbox("Job Level", [1, 2, 3, 4, 5])
job_role = st.selectbox("Job Role", ["Sales Executive", "Research Scientist", "Laboratory Technician", "Manufacturing Director",
                                     "Healthcare Representative", "Manager", "Sales Representative", "Research Director", "Human Resources"])
job_satisfaction = st.selectbox(
    "Job Satisfaction (1=Low, 2=Medium, 3=High, 4=Very High)", [1, 2, 3, 4])
marital_status = st.selectbox(
    "Marital Status", ["Single", "Married", "Divorced"])
monthly_income = st.number_input(
    "Monthly Income", min_value=1000, max_value=20000, value=5000)
num_companies = st.number_input(
    "Number of Companies Worked", min_value=0, max_value=10, value=1)
overtime = st.selectbox("OverTime", ["Yes", "No"])
percent_salary_hike = st.number_input(
    "Percent Salary Hike", min_value=0, max_value=100, value=15)
performance_rating = st.selectbox("Performance Rating", [1, 2, 3, 4])
relationship_satisfaction = st.selectbox(
    "Relationship Satisfaction (1=Low, 2=Medium, 3=High, 4=Very High)", [1, 2, 3, 4])
stock_option = st.selectbox("Stock Option Level", [0, 1, 2, 3])
total_working_years = st.number_input(
    "Total Working Years", min_value=0, max_value=40, value=5)
training_times = st.selectbox(
    "Training Times Last Year", [0, 1, 2, 3, 4, 5, 6])
work_life_balance = st.selectbox(
    "Work Life Balance (1=Low, 2=Good, 3=Excellent, 4=Outstanding)", [1, 2, 3, 4])
years_at_company = st.number_input(
    "Years At Company", min_value=0, max_value=40, value=3)
years_since_promo = st.number_input(
    "Years Since Last Promotion", min_value=0, max_value=15, value=1)

# Mapping input ke dictionary
input_data = {
    'Age': age,
    'Department': department,
    'DistanceFromHome': distance,
    'Education': education,
    'EducationField': education_field,
    'EnvironmentSatisfaction': env_satisfaction,
    'Gender': gender,
    'JobInvolvement': job_involvement,
    'JobLevel': job_level,
    'JobRole': job_role,
    'JobSatisfaction': job_satisfaction,
    'MaritalStatus': marital_status,
    'MonthlyIncome': monthly_income,
    'NumCompaniesWorked': num_companies,
    'OverTime': overtime,
    'PercentSalaryHike': percent_salary_hike,
    'PerformanceRating': performance_rating,
    'RelationshipSatisfaction': relationship_satisfaction,
    'StockOptionLevel': stock_option,
    'TotalWorkingYears': total_working_years,
    'TrainingTimesLastYear': training_times,
    'WorkLifeBalance': work_life_balance,
    'YearsAtCompany': years_at_company,
    'YearsSinceLastPromotion': years_since_promo
}

input_df = pd.DataFrame([input_data])

if st.button("Prediksi"):
    try:
        # Encode kategorik dengan pengecekan
        for col in input_df.columns:
            if input_df[col].dtype == 'object':
                if col in encoders:
                    le = encoders[col]
                    try:
                        input_df[col] = le.transform(input_df[col])
                    except ValueError as e:
                        st.error(
                            f"Nilai '{input_df[col].values[0]}' di kolom '{col}' tidak dikenali oleh encoder.")
                        st.stop()
                else:
                    st.error(
                        f"Kolom kategorikal '{col}' tidak memiliki encoder. Harap pastikan encoder dibuat dan disimpan saat training.")
                    st.stop()

        # Scaling
        input_scaled = scaler.transform(input_df)

        # Prediksi
        prediction = model.predict(input_scaled)[0]
        proba = model.predict_proba(input_scaled)[0][1]

        if prediction == 1:
            st.error(f"Karyawan berisiko keluar")
        else:
            st.success(f"Karyawan tidak berisiko keluar")

    except Exception as e:
        st.error(f"Terjadi error saat prediksi: {e}")
