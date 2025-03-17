# 🐧 Palmer's Penguins - Interactive Data App  

## 📌 Project Overview  
This project is an **interactive web application** built with **Streamlit**, allowing users to explore the **Palmer's Penguins dataset**. The dataset contains measurements of three penguin species from different islands in Antarctica.  

Through this app, users can filter penguins based on **species** and **body mass**, gaining insights into their characteristics.  

---

## 🚀 How to Run This Project  

### 1️⃣ Install Dependencies  
Ensure you have **Python 3.7+** and the required packages installed:  
```sh
pip install streamlit pandas
```
### 2️⃣ Run the Streamlit App  
Clone this repository and navigate to the project folder. Then, run the following command:  

```sh
streamlit run penguins_app.py
```
---

## 📊 Dataset Description  
**Dataset:** `penguins.csv`

The dataset includes the following attributes for each penguin:
- **Species** (Adelie, Chinstrap, or Gentoo)
- **Island** where the penguin was observed
- **Body mass** (grams)
- **Bill length & depth**
- **Flipper length**

---

## 🔍 Key Features
- **Dropdown Selection:** Choose a species to filter penguins.
- **Interactive Slider:** Adjust body mass range to filter results.
- **Live Data Updates:** View updated penguin data instantly.

This project showcases data visualization, interactive UI design, and real-world dataset exploration.

---

## 📁 Project Organization
- `penguins_app.py` → Main Streamlit app
- `penguins.csv` → Dataset
- `README.md` → Project documentation
- `Images/` → Screenshots for documentation
