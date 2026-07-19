import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Data Preprocessing Pipeline", layout="wide")
st.title("⚙️ AI Data Preprocessing Pipeline")
st.markdown("Clean, normalize, and validate datasets for model ingestion.")

uploaded_file = st.sidebar.file_uploader("Upload Raw CSV Dataset", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Raw Dataset Preview")
    st.dataframe(df.head())

    # Automated Validation Checks
    st.subheader("🔍 Automated Validation Summary")
    
    missing_values = df.isnull().sum().sum()
    duplicate_rows = df.duplicated().sum()
    
    col1, col2 = st.columns(2)
    col1.metric("Missing Values Flagged", missing_values)
    col2.metric("Duplicate Rows Found", duplicate_rows)

    # Preprocessing pipeline options
    st.subheader("🛠️ Run Pipeline Operations")
    
    clean_missing = st.checkbox("Handle Missing Values (Drop rows)")
    drop_dupes = st.checkbox("Remove Duplicate Rows")
    normalize_text = st.checkbox("Lowercase & Strip Text Data")

    if st.button("Execute Pipeline"):
        processed_df = df.copy()
        
        if clean_missing:
            processed_df = processed_df.dropna()
        if drop_dupes:
            processed_df = processed_df.drop_duplicates()
        if normalize_text:
            for col in processed_df.select_dtypes(include=['object']).columns:
                processed_df[col] = processed_df[col].astype(str).str.lower().str.strip()
                
        st.success("Pipeline executed successfully!")
        st.subheader("Processed Dataset Preview")
        st.dataframe(processed_df.head())
        
        # Download Cleaned Data
        csv_data = processed_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Cleaned Dataset",
            data=csv_data,
            file_name="cleaned_dataset.csv",
            mime="text/csv"
        )
else:
    st.info("Upload a dataset to run validation checks and trigger the preprocessing pipeline.")
