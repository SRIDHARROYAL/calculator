import streamlit as st

# App Title
st.title("Simple Python Calculator")

# Inputs
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)
operation = st.selectbox("Select an operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform the calculation
result = None
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero!"

# Display the result
if result is not None:
    st.write(f"Result: {result}")
