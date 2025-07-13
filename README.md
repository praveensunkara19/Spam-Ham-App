---
title: SPAM-HAM-CLASSIFIER
emoji: ✉️
colorFrom: pink
colorTo: red
sdk: streamlit
sdk_version: "1.25.0"
app_file: app.py
pinned: false
---

# 📝 **SPAM - HAM CLASSIFIER**

[![Hugging Face Spaces](https://img.shields.io/badge/HuggingFace-SpamHamApp-yellow?logo=huggingface)](https://huggingface.co/spaces/praveensunkara/Spam-Ham-App)
[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/praveensunkara19/Spam-Ham-App)

This is a **Streamlit web application** that classifies a given message as **SPAM** or **HAM (Not Spam)** using a trained machine learning model.

---

## 🚀 **Features**

✅ Classifies messages into Spam or Ham using **Naive Bayes**  
✅ Color-coded prediction output (**Red for Spam, Green for Ham**)  
✅ Sample test messages for easy testing  
✅ Clean and interactive UI with emojis  
✅ Built using **Streamlit**, **joblib**, and **scikit-learn**

---

## 🌐 **Live Demo**

▶️ Check out the app on [Hugging Face Spaces](https://huggingface.co/spaces/praveensunkara/Spam-Ham-App).

---

## 🛠️ **Setup Instructions**

```bash
# 1. Clone the repository
git clone https://github.com/praveensunkara19/Spam-Ham-App.git
cd Spam-Ham-App

# 2. Create a virtual environment and activate it
python -m venv myenv

# On Windows
myenv\Scripts\activate

# On Mac/Linux
source myenv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py
