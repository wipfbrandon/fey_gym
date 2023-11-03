import pandas as pd
import streamlit as st
from datetime import date


st.header("Fey's Super Awesome Gym Adventure!")
st.subheader('OPERATIONS')
weekly_classes = st.slider('Number of Weekly Classes:', 0, 40, 24, 1)
total_coaches = st.slider('Total Coaches per Class:', 0, 5, 1, 1)
salary_per_class = st.slider('Coach Compensation per Class:', 20, 50, 25, 5)
coach_sal = (weekly_classes * total_coaches * salary_per_class) * 52

st.write('---')
st.subheader('EXPENSES:')
rent_sq_ft = st.slider('Base Rent / Sq Ft (4,000)', 4.0, 10.00, 7.5, 0.25)
total_rent = int(rent_sq_ft * 4_000)
util_cost = st.slider('Annual Utilities', 1000, 10000, 5000, 500)
cams = st.slider('Common Area Maintenance', 1000, 10000, 5000, 500)
ann_expense = total_rent + util_cost + cams + coach_sal

st.write(f'Annual Coach Salary: {int(coach_sal)}')
st.write(f'Annual Base Rent: {total_rent}') 
st.write(f'Annual Building Cost: {int(total_rent + util_cost + cams)}')
st.write(f'ANNUAL EXPENSES: {int(ann_expense)}')

st.write('---')
st.subheader('REVENUE:')
athletes = st.slider('Total Athletes', 30, 200, 45, 5)
price_per_ath = st.slider('Monthly Price Per Athlete', 100, 200, 130, 10)
mon_rev = athletes * price_per_ath
ann_rev = mon_rev * 12
st.write(f'Monthly Revenue: {int(mon_rev)}')
st.write(f'ANNUAL REVENUE: {int(ann_rev)}')

st.write('---')
st.subheader('PROFIT & LOSS')
profit = ann_rev - ann_expense
st.write(f'ANNUAL PROFIT/(LOSS): {int(profit)}')
