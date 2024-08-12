import streamlit as st
import random

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Streamlit app title
st.title("Prime Number Identifier")

# Slider Input Method
st.write("### Use the slider to select a number.")
number = st.slider(
    "Choose your number:",
    min_value=1,
    max_value=100,
    value=10,
    step=1,
    format="Number: %d",
    key="unique_number_slider"
)

if is_prime(number):
    st.write(f"**{number}** is a prime number!")
else:
    st.write(f"**{number}** is not a prime number.")

# Separator
st.write("---")

# Random Number Method
st.write("### Or use this method to generate and check a random number.")

# Generate a random number
if st.button("Generate Random Number"):
    random_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    st.session_state.random_number = random_number  # Store the number in session state
    st.write(f"Random Number Generated: {random_number}")

# Check if the number is prime
if 'random_number' in st.session_state:
    if st.button("Check if Prime"):
        number_to_check = st.session_state.random_number
        if is_prime(number_to_check):
            st.write(f"**{number_to_check}** is a prime number!")
        else:
            st.write(f"**{number_to_check}** is not a prime number.")
else:
    st.write("Please generate a random number first.")
