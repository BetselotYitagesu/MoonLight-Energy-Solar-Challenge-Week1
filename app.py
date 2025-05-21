import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="Solar Data Comparison", layout="wide")
st.title("🌞 Solar Energy Data Comparison Dashboard")

# Load and combine cleaned datasets
@st.cache_data
def load_clean_data():
    benin = pd.read_csv("E:/Tenx/data/benin_clean.csv")
    sierraleone = pd.read_csv("E:/Tenx/data/sierraleone_clean.csv")
    togo = pd.read_csv("E:/Tenx/data/togo_clean.csv")

    benin['Country'] = 'Benin'
    sierraleone['Country'] = 'Sierra Leone'
    togo['Country'] = 'Togo'

    df_all = pd.concat([benin, sierraleone, togo], ignore_index=True)
    return df_all


df = load_clean_data()

# Sidebar - select metrics to compare
st.sidebar.header("🔧 Options")
metric = st.sidebar.selectbox("Select Metric", ["GHI", "DNI", "DHI"])

# Tabs for comparison views
tab1, tab2, tab3 = st.tabs(["📊 Boxplot Comparison", "📋 Summary Table", "📈 GHI Trends"])

# ---- Tab 1: Boxplot Comparison ----
with tab1:
    st.subheader(f"{metric} Distribution Across Countries")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(data=df, x='Country', y=metric, palette='Set2', ax=ax)
    ax.set_ylabel(f"{metric} (W/m²)")
    st.pyplot(fig)

# ---- Tab 2: Summary Statistics Table ----
with tab2:
    st.subheader("Summary Statistics (GHI, DNI, DHI)")
    summary = df.groupby('Country')[['GHI', 'DNI', 'DHI']].agg(['mean', 'median', 'std'])
    summary.columns = ['_'.join(col) for col in summary.columns]
    st.dataframe(summary.style.format("{:.2f}"))

    # Bar chart of average GHI
    st.subheader("Average GHI by Country")
    avg_ghi = df.groupby('Country')['GHI'].mean().sort_values(ascending=False)
    fig, ax = plt.subplots()
    avg_ghi.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_ylabel("Average GHI (W/m²)")
    st.pyplot(fig)

# ---- Tab 3: GHI Time Series (Optional) ----
with tab3:
    st.subheader("GHI Over Time by Country")
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    fig, ax = plt.subplots(figsize=(12, 5))
    for country in df['Country'].unique():
        subset = df[df['Country'] == country]
        subset = subset.sort_values('Timestamp').groupby('Timestamp')['GHI'].mean()
        subset.plot(label=country, ax=ax)
    ax.set_ylabel("GHI (W/m²)")
    ax.legend()
    st.pyplot(fig)

st.markdown("---")
st.caption("0Academy AI Mastery Program | Data from MoonLight Energy Solutions")
