import streamlit as st

st.write(""" 
# Find whether the given number is odd or even.
""")
num = st.number_input("Enter a number", step=1)
if num % 2 == 0:
    st.write("The given number is even")
else:
    st.write("The given number is odd")
