#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import pandas as pd
import csv
from datetime import datetime

# Sample lists for topics and subtopics
topics = ["Technology", "Health", "Education", "Business"]
subtopics = {
    "Technology": ["AI", "Cybersecurity", "Blockchain"],
    "Health": ["Nutrition", "Exercise", "Mental Health", "Clinics and Hospitals"],
    "Education": ["Online Learning", "STEM", "Early Childhood"],
    "Business": ["Marketing", "Finance", "Entrepreneurship"]
}

# CSV file to store prompts
FILE_PATH = "prompts.csv"

# Sidebar for topic selection
st.sidebar.header("Prompt Generator")
selected_topic = st.sidebar.selectbox("Select a Topic", topics)
selected_subtopic = st.sidebar.selectbox("Select a Subtopic", subtopics[selected_topic])
prompt = st.text_area("Write your prompt here:", "")

# Button to create and save prompt
if st.button("Create Prompt"):
    if prompt.strip() != "":
        # Add timestamp for tracking
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(FILE_PATH, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, selected_topic, selected_subtopic, prompt])
        st.success("Prompt saved!")
    else:
        st.error("Please write a prompt before saving.")

# Button to view all saved prompts
if st.button("View All Prompts"):
    try:
        df = pd.read_csv(FILE_PATH, names=["Timestamp", "Topic", "Subtopic", "Prompt"])
        st.write(df)
    except FileNotFoundError:
        st.write("No prompts have been saved yet.")


# In[5]:


if st.button("Download Prompts as CSV"):
    try:
        df = pd.read_csv(FILE_PATH, names=["Timestamp", "Topic", "Subtopic", "Prompt"])
        st.download_button("Download CSV", df.to_csv(index=False), "prompts.csv", "text/csv")
    except FileNotFoundError:
        st.write("No prompts available to download.")


# In[ ]:




