import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.title("Solar Energy Data Analysis Dashboard")

# Sidebar for country selection
country = st.sidebar.selectbox("Select a Country", ["Benin", "Sierra Leone", "Togo"])

# Load the appropriate data
@st.cache_data
def load_data(country):
    if country == "Benin":
        return pd.read_csv("data/benin-malanville.csv")
    elif country == "Sierra Leone":
        return pd.read_csv("data/sierraleone-bumbana.csv")
    else:
        return pd.read_csv("data/togo-dapaong.csv")

df = load_data(country)
st.write(f"## Preview of {country} Dataset")
st.dataframe(df.head())

# Show a correlation heatmap
st.write("### Correlation Heatmap")
fig, ax = plt.subplots()
sns.heatmap(df[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']].corr(), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Optional: Show time series
st.write("### GHI Over Time")
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
fig, ax = plt.subplots()
df.plot(x='Timestamp', y='GHI', ax=ax, figsize=(10,4))
st.pyplot(fig)
