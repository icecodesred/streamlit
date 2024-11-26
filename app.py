import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# App Title
st.title("My First Streamlit App")

# Text Input
user_text = st.text_input("Enter some text:", "Hello, Streamlit!")

# Slider Input
number = st.slider("Pick a number:", min_value=1, max_value=100, value=50)

# Display User Input
st.write(f"You entered: **{user_text}**")
st.write(f"Your selected number is: **{number}**")

# Generate Data for Plot
x = np.linspace(0, 10, 100)
y = np.sin(x * number / 10)

# Plot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title(f"Sine Wave (Frequency Multiplier: {number / 10})")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Display Plot
st.pyplot(fig)

# Checkbox Example
if st.checkbox("Show a surprise message"):
    st.write("🎉 Congratulations on building your first Streamlit app!")
