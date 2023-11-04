import pandas as pd
import streamlit as st
from datetime import date


st.header(":fire: Fey-ered Up Crossfit :fire:")
st.subheader('OPERATIONS')
weekly_classes = st.slider('Number of Weekly Classes:', 0, 40, 24, 1)
total_coaches = st.slider('Total Coaches per Class:', 0, 5, 1, 1)
salary_per_class = st.slider('Coach Compensation per Class:', 20, 50, 25, 5)
coach_sal = (weekly_classes * total_coaches * salary_per_class) * 52
st.write(f'Annual Coach Salary: {int(coach_sal)}')

st.write('---')
st.subheader('REVENUE:')
athletes = st.slider('Total Athletes', 30, 200, 45, 5)
price_per_ath = st.slider('Monthly Price Per Athlete', 100, 200, 160, 10)
mon_rev = athletes * price_per_ath
ann_rev = mon_rev * 12
st.write(f'Monthly Revenue: {int(mon_rev)}')
st.write(f'ANNUAL REVENUE: {int(ann_rev)}')


st.write('---')
st.subheader('EXPENSES:')
st.write(f'Annual Coach Salary: {int(coach_sal)}')

col_lease, col_buy = st.columns(2)

with col_lease:
    st.subheader('LEASE:')
    square_footage = 4_000
    lease_sq_ft = st.slider('Base Rent / Sq Ft (4,000)', 4.0, 10.00, 7.5, 0.25)
    cam_sq_ft = st.slider('CAM Expense / Sq Ft (RE tax, Insurance, common area maintenance)', 1.0, 10.00, 2.20, 0.10)
    
    base_rent_exp = int(lease_sq_ft * square_footage)
    cam_exp = int(cam_sq_ft * square_footage)

    lease_expense = base_rent_exp + cam_exp

    st.write(f'Annual Base Rent: {base_rent_exp}')
    st.write(f'Annual CAMs: {cam_exp}')
    st.write(f'TOTAL ANNUAL LEASE: {lease_expense}')

with col_buy:
    st.subheader('BUY:')
    purchase_price = st.slider('Purchase Price:', 300_000, 500_000, 400_000, 25_000)
    down_payment_pct = st.slider('Down Payment Percent:', 5.0, 30.0, 20.0, 1.0)
    cal_dp = down_payment_pct / 100
    loan = int(purchase_price * (1-cal_dp))
    st.write(f'Loan Amount: {loan}')

    int_rate = st.slider('Interest Rate:', 4.00, 10.00, 7.50, 0.25)
    term = st.slider('Loan Term (Yrs)', 5, 30, 15, 1)
    
    calc_int_rate = (int_rate / 100)
    calc_term = term * 12

    monthly_payment = int(round((calc_int_rate/12) * (1/(1-(1+calc_int_rate/12)**(-calc_term)))*loan, 0))
    annual_payments = monthly_payment * 12

    st.write(f'Monthly Principal & Interest Payment: {monthly_payment}')
    st.write(f'Annual P&I Payment: {annual_payments}')

    annual_tax = st.slider('Real Estate Taxes:', 500, 15_000, 5_000, 500)
    annual_prop_ins = st.slider('Property Insurance:', 500, 10_000, 3_000, 500)

    escrow_pay = int(annual_tax + annual_prop_ins)

    annual_mortgage_cost = int(annual_payments + escrow_pay)

    st.write(f'Monthly Escrow Payment: {int(escrow_pay / 12)}')
    st.write(f'Annual Escrow Payment: {int(escrow_pay)}')

    st.write(f'TOTAL ANNUAL MORTGAGE: {annual_mortgage_cost}')


st.subheader('Operating Expenses:')
utility_cost = st.slider('Annual Utilities', 1000, 10000, 5000, 500)
software = st.slider('Software', 100, 6000, 3600, 100)
liab_insurance = st.slider('Liability Insurance', 1000, 15000, 10000, 500)
misc_costs = st.slider('Other Costs (supplies, maintenance, bookkeeping)', 1000, 10000, 1500, 500)

operating_costs = int(utility_cost + software + liab_insurance + misc_costs)
monthly_op_costs = int(operating_costs / 12)

st.write(f'Monthly Operating Cost: {monthly_op_costs}') 
st.write(f'ANNUAL OPERATING COSTS: {operating_costs}')

st.write('---')
st.subheader('PROFIT & LOSS')
st.caption('Expenses include: Lease/Mortgage + Coach + Operating')
col_lease_pl, col_buy_pl = st.columns(2)

with col_lease_pl:
    st.subheader('LEASE:')
    annual_lease_cost = int(lease_expense + operating_costs + coach_sal)
    monthly_lease_cost = int(annual_lease_cost / 12)

    lease_profit = ann_rev - annual_lease_cost
    st.write(f'LEASE REVENUE: {ann_rev}')
    st.write(f'LEASE EXPENSES: {annual_lease_cost}')
    st.write(f'LEASE PROFIT/(LOSS): {lease_profit}')
    st.write(f'Taxable Income (100%): {lease_profit}')
    st.write(f'Taxes (25%): {lease_profit * 0.25}')

with col_buy_pl:
    st.subheader('BUY:')
    annual_buy_cost = int(annual_mortgage_cost + operating_costs + coach_sal)
    monthly_buy_cost = int(annual_buy_cost / 12)

    buy_profit = ann_rev - annual_buy_cost
    st.write(f'BUY REVENUE: {ann_rev}')
    st.write(f'BUY EXPENSES: {annual_buy_cost}')
    st.write(f'BUY PROFIT/(LOSS): {buy_profit}')
    st.write(f'Taxable Income (60%): {buy_profit * 0.60}')
    st.write(f'Taxes (25%): {buy_profit * 0.60 * 0.25}')


if buy_profit > lease_profit:
    best_option = 'PURCHASING'
    difference = buy_profit - lease_profit
    comment = 'and you are building equity and can expense Depreciation on TR'
else:
    best_option = 'LEASING'
    difference = lease_profit - buy_profit
    comment = 'but... you are NOT building equity, nor can you expense Depreciation on TR'



st.write('---')
st.subheader('FINAL THOUGHTS:')
st.write(f'Given the above inputs, your best option is {best_option}, by {difference} dollars annually, {comment}.')
