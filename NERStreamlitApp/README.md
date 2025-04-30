# 🔥 NER Streamlit App

## 📚 Overview  
Welcome to the **NER Streamlit App**! This interactive tool allows you to perform Named Entity Recognition (NER) using **spaCy** and **Streamlit**. You can input custom text, define entity rules, and instantly visualize the results. This project was developed as part of my Elements of Computing II portfolio.

---

## ✨ Features  
- **Flexible Text Input**  
  Type/paste your own text, upload a `.txt` file, or use one of the built-in sample texts.

- **Custom Entity Rules**  
  Add custom rules by specifying an entity label (e.g., `PERSON`, `ORG`) and a matching pattern (e.g., `"Barack Obama"`).  
  Rules are displayed in an expandable list and can be cleared at any time.

- **Interactive Visualizations**  
  View recognized entities in a clean two-column layout, along with a color-highlighted version of your text.

- **Entity Statistics**  
  See a count of all detected entities, with a breakdown by type (e.g., PERSON, ORG, GPE).

- **Built-in Help & Documentation**  
  The sidebar includes instructions and external links to spaCy and Streamlit documentation.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/GooboGobbo/NERStreamlitApp.git
cd NERStreamlitApp
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```
## 3. Install Dependencies  
Make sure you have the required libraries installed:

- `streamlit`
- `spacy`

Install them with:
```bash
pip install -r requirements.txt
```

## 4. Download spaCy's English Model
```bash
python -m spacy download en_core_web_sm
```
## 🏃‍♂️ Running the Application  
To launch the app locally, run:
```bash
streamlit run app.py
```

## 🌐 Deployment  
The app is deployed on Streamlit Community Cloud. You can view it live here:  
[https://nergoobogobbo.streamlit.app/](https://nergoobogobbo.streamlit.app/)

## 🎓 How to Use

### 📄 Input Your Text
- Use the radio buttons to select between typing, pasting, or uploading text.
- Load a sample text from the sidebar for quick testing.

### 🏷️ Add Custom Entity Rules
- Input a label (like `PERSON`) and a pattern (like `"Notre Dame"`).
- Click **Add Custom Rule** to save it.
- View current rules by expanding the **Current Custom Rules** section.
- Use **Clear Custom Rules** to reset.

### 🧠 Run the NER Model
- Click **Run NER** to process the text.
- Results will display:
  - ✅ A list of recognized entities  
  - 📊 A breakdown of entity counts by type  
  - 🖍️ The text with highlighted entities

## 📖 References  
- [spaCy Documentation](https://spacy.io/usage)  
- [spaCy EntityRuler](https://spacy.io/usage/rule-based-matching)  
- [Streamlit Documentation](https://docs.streamlit.io/)


## 📬 Contact  
For feedback or inquiries, please contact me at: [jedge@nd.edu](mailto:jedge@nd.edu)

