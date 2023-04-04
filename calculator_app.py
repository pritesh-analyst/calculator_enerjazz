import streamlit as st

# Define the layout
st.title("Salary Calculator")
salary = st.number_input("Enter your monthly salary", min_value=0.0, step=1000.0, format="%f")
days_in_month = st.number_input("No. of days in month", min_value=1, step=1, format="%d")
duties_per_month = st.number_input("Enter the number of duties in a month", min_value=0, step=1, format="%d")
overtime_hours = st.number_input("Enter the number of overtime hours", min_value=0.0, step=0.5, format="%f")

# Write the app logic
# regular_hours = (days_in_month * 30 * 8) - (duties_per_month * 8)
# regular_rate = salary / (months_worked * 30 * 8)
# overtime_rate = regular_rate * 1.5
# overtime_pay = overtime_hours * overtime_rate
# total_pay = (regular_hours * regular_rate) + overtime_pay

Daily_salary = salary/days_in_month
total_salary_without_ot = Daily_salary*duties_per_month + (Daily_salary/9)*overtime_hours
# total_salary_with_ot = (total_salary_without_ot )+ 


# Display the output
st.write("Your monthly salary is: ", round(total_salary_without_ot, 2), )
