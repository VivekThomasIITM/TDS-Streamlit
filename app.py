import streamlit as st

st.title("TDS Assignment 8")
st.header("App to find the largest number among three numbers.")
st.caption("By Vivek Thomas - 21f1005436@student.onlinedegree.iitm.ac.in")
a = st.number_input("Enter your first number")
b = st.number_input("Enter your second number")
c = st.number_input("Enter your third number")
_max = max([a,b,c])
st.subheader("The largest number is : {}".format(_max))
