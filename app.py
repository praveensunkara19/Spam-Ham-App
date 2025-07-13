import streamlit as st
from huggingface_hub import hf_hub_download
import joblib


st.set_page_config(page_title="Spam-Ham Classifier", page_icon="📝")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton button {
        background-color: #227ae6;
        color: white;
        font-size: 16px;
        border-radius: 8px;
        padding: 10px 24px;
    }
    .stButton button:hover {
        background-color: #b5ccb5;
    }
    .prediction-box {
        border: 2px solid #e6c522;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📝 SPAM - HAM CLASSIFIER")



model_path = hf_hub_download(repo_id="praveensunkara/spam-ham-model", filename="spam-ham")
text_model = joblib.load(model_path)


# Sample test messages
st.markdown("### ✉️ Sample Test Messages")
col1, col2 = st.columns(2)
with col1:
    if st.button("🔴✗ Test SPAM"):
        st.session_state['input_text'] = "Congratulations! You've won a free lottery ticket. Click here to claim."
with col2:
    if st.button("🟢✔ Test HAM"):
        st.session_state['input_text'] = "Hi John, I will meet you at the cafe by 5 PM today."

# Input box with default or selected value
default_text = st.session_state.get('input_text', "Winner! you won lottery ticket. Click the below link!")
ip = st.text_input("Or enter your own message below:", value=default_text)

# Button to predict
if st.button("🔍 Predict"):
    op = text_model.predict([ip])   # predict only when button is clicked
    result = op[0]

    # Display entered message
    st.markdown("#### 🗒️ Your Entered Message:")
    st.write(ip)

    # Color-coded prediction result
    if result.lower() == 'spam':
        color = "#ff4d4d"  # red for spam
    else:
        color = "#4CAF50"  # green for ham

    st.markdown("#### 🤖 Prediction Result:")
    st.markdown(
        f"<div class='prediction-box' style='background-color:{color}; color:white;'>{result.upper()}</div>",
        unsafe_allow_html=True
    )

# Footer or credits
st.markdown("---")
st.markdown("*Made with ❤️ using Streamlit*", unsafe_allow_html=True)
