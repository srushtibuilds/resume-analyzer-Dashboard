import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Load Data
df = pd.read_csv("skills.csv")

st.title("Skills Analytics Dashboard")

st.subheader("Raw Data")
st.dataframe(df)

# Count skills
skill_counts = df["Skills_Name"].value_counts()

st.subheader("Skill Frequency")
st.bar_chart(skill_counts)

# Pie Chart
fig, ax = plt.subplots()
ax.pie(skill_counts, labels=skill_counts.index, autopct="%1.1f%%")
st.subheader("Skill Distribution")

fig2, ax2 = plt.subplots()
ax2.pie(skill_counts, labels=skill_counts.index, autopct='%1.1f%%')
ax2.axis("equal")

st.pyplot(fig2)

st.metric("Total Unique Skills", len(skill_counts))
top_skill = skill_counts.idxmax()
st.metric("Most Common Skill", top_skill)


search = st.text_input("Search Skill")
filtered_df = df[df["Skills_Name"].str.contains(search, case=False)]
st.dataframe(filtered_df)


