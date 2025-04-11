# 🔥 NER Streamlit App

## 📚 Overview  
Welcome to the **NER Streamlit App**! This interactive application lets you perform Named Entity Recognition using **spaCy** and **Streamlit**. You can enter your own text or load a sample, define custom entity rules, and see real-time results with intuitive visualizations. This project is part of my Elements of Computing II portfolio.

---

## ✨ Features  
- **Flexible Text Input:**  
  Choose to type/paste text, upload a `.txt` file, or load one of the sample texts from the sidebar.
- **Custom Entity Rules:**  
  Easily add custom rules by specifying an entity label (e.g., `PERSON`, `ORG`) and a corresponding pattern (e.g., "Barack Obama").  
  View current custom rules in a collapsible section and clear them if needed.
- **Interactive Visualization:**  
  Recognized entities are displayed in two columns for clarity, and the app shows highlighted text annotated with entities.
- **Responsive Feedback:**  
  Get detailed entity statistics (total count and breakdown by type) right after processing.
- **Integrated Help:**  
  Access usage instructions and documentation through the sidebar for a smooth user experience.

---

## 🚀 Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/NERStreamlitApp.git
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
[https://share.streamlit.io/yourusername/NERStreamlitApp](https://share.streamlit.io/yourusername/NERStreamlitApp)

## 🎓 Usage Instructions

### Text Input  
- **Choose Input Method:**  
  Use the radio buttons to select whether you want to type/paste your text or upload a `.txt` file.

- **Load Sample Text:**  
  Pick a sample from the sidebar and click **"Load Sample Text"** to quickly populate the text area.

### Custom Entity Rules  
- **Add a Rule:**  
  Enter an entity label (like `PERSON` or `ORG`) and a pattern (such as "Barack Obama") to create a custom rule.

- **View Current Rules:**  
  Expand the **"Current Custom Rules"** section to see all added rules.

- **Clear Rules:**  
  Click **"Clear Custom Rules"** to remove all custom rules if needed.

### Run NER  
Once your text and custom rules (if any) are set:
- Click the **Run NER** button.
- The app processes your text with spaCy, displaying recognized entities in two columns.
- You'll also see a breakdown of entity statistics (total and per label) and a version of your text with highlighted entities.

## 📖 References  
- [spaCy Documentation](https://spacy.io/usage)  
- [spaCy EntityRuler](https://spacy.io/usage/rule-based-matching)  
- [Streamlit Documentation](https://docs.streamlit.io/)


## 📬 Contact  
For feedback or inquiries, please contact me at: [jedge@nd.edu](mailto:jedge@nd.edu)

