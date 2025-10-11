import streamlit as st
from src.data_loader import load_financial_data
from src.ratio_calculator import calculate_ratios
from src.score_engine import generate_health_score
from src.visualizer import plot_ratios

st.set_page_config(page_title="Financial Health Scoring System", layout="wide")

st.title("💼 Financial Health Scoring System for SMEs")
st.write("Upload a company's financial statements and get a calculated Financial Health Score instantly.")

uploaded_file = st.file_uploader("📤 Upload your financial data (Excel or CSV)", type=["csv", "xlsx"])

if uploaded_file:
    df = load_financial_data(uploaded_file)
    if isinstance(df, str):
        st.error(df)
    else:
        st.success("✅ File uploaded successfully!")
        st.subheader("📄 Data Preview")
        st.dataframe(df.head(), use_container_width=True)

        ratios = calculate_ratios(df)
        if "error" in ratios:
            st.error(ratios["error"])
        else:
            st.subheader("📊 Financial Ratios")
            st.json(ratios)

            score = generate_health_score(ratios)
            st.metric("🏆 Financial Health Score", f"{score} / 100")

            st.subheader("📈 Ratio Visualization")
            st.pyplot(plot_ratios(ratios))
else:
    st.info(" Upload your financial file to get started.")

