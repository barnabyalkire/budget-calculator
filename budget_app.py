
# budget_app.py

import streamlit as st

st.title("💰 Simple Budget Calculator")

st.header("Enter your monthly income and expenses:")

income = st.number_input("Monthly Income ($)", min_value=0.0, format="%.2f")
rent = st.number_input("Rent ($)", min_value=0.0, format="%.2f")
utilities = st.number_input("Utilities ($)", min_value=0.0, format="%.2f")
groceries = st.number_input("Groceries ($)", min_value=0.0, format="%.2f")
transportation = st.number_input("Transportation ($)", min_value=0.0, format="%.2f")
other = st.number_input("Other Expenses ($)", min_value=0.0, format="%.2f")

total_expenses = rent + utilities + groceries + transportation + other
remaining = income - total_expenses

st.subheader("📊 Summary:")
st.write(f"**Total Expenses:** ${total_expenses:,.2f}")
st.write(f"**Remaining Balance:** ${remaining:,.2f}")

if remaining < 0:
    st.error("⚠️ You're overspending! Try adjusting your expenses.")
elif remaining == 0:
    st.warning("⚠️ You have no money left over this month.")
else:
    st.success("✅ Good job! You have money left over.")
