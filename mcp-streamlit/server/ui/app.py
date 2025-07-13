import streamlit as st
import json

# Read the JSON data from file
with open("../json_data/data.json", "r") as f:
    data = json.load(f)

# Display data in Streamlit
st.title("Student Info")

st.write("### Name:")
st.write(data["name"])

st.write("### Class:")
st.write(data["class"])
