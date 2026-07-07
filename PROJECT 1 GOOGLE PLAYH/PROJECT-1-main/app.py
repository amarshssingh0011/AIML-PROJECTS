import streamlit as st
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Airbnb Outlier Detection",
    page_icon="🏠",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("🏠 Airbnb Price Outlier Detection")
st.write("This app detects and removes outliers from the **Price** column using the **Percentile Method**.")

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("AB_NYC_2019.csv")   # Replace with your dataset name if different

# -----------------------------
# Display Dataset
# -----------------------------
st.header("📋 Original Dataset")

st.dataframe(df)

st.write("**Dataset Shape:**", df.shape)

# -----------------------------
# Outlier Detection
# -----------------------------
st.header("📊 Outlier Detection Using Percentile Method")

# Calculate thresholds
min_threshold, max_threshold = df["price"].quantile([0.01, 0.999])

st.subheader("Threshold Values")

st.write("**Minimum Threshold:**", min_threshold)
st.write("**Maximum Threshold:**", max_threshold)

# Lower outliers
st.subheader("Lower Outliers")

lower_outliers = df[df["price"] < min_threshold]

st.write("Number of Lower Outliers:", lower_outliers.shape[0])

st.dataframe(lower_outliers)

# Remove outliers
df2 = df[
    (df["price"] > min_threshold) &
    (df["price"] < max_threshold)
]

# -----------------------------
# Cleaned Dataset
# -----------------------------
st.subheader("Dataset After Removing Outliers")

st.write("**Shape of Cleaned Dataset:**", df2.shape)

st.dataframe(df2.sample(5))

# -----------------------------
# Summary Statistics
# -----------------------------
st.subheader("Price Summary Statistics")

st.dataframe(df2["price"].describe())

# -----------------------------
# Comparison
# -----------------------------
st.subheader("Dataset Comparison")

st.write("Original Dataset Shape:", df.shape)
st.write("Cleaned Dataset Shape:", df2.shape)
st.write("Rows Removed:", df.shape[0] - df2.shape[0])

st.success("✅ Outliers removed successfully using the Percentile Method.")
