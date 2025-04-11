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
### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

