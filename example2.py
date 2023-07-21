import streamlit as st

st.set_page_config(
    page_title="GW Quickview", page_icon=":eyeglasses:", layout="centered"
)

st.title("Model Endpoint Viewer")
st.write("Automated endpoint controller with parameter selection.")

col1, col2, col3 = st.columns(3)
with col1:
    ticker = st.selectbox('Choose an input device:',
                        ['All', 'Parking Lot 1A'])
with col2:
    ticker_dx = st.slider(
        "Confidence", min_value=0.1, max_value=1.0, step=0.1, value=0.1
    )
with col3:
    ticker_dy = st.slider(
        "Minimum Target Latency (ms)", min_value=50, max_value=3000, step=10, value=250
    )
for _ in range(0, 25):
    st.write("\n")
st.write("## Metrics")
for _ in range(0, 25):
    st.write("\n")