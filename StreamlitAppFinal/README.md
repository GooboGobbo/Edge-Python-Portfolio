# 🇰🇷 Learn Korean: Mini Games Hub 🎮

Welcome to the **Learn Korean Mini Games Hub**, an interactive web-based platform that helps beginner Korean learners improve their language skills through a variety of fun and focused mini-games.

This project was created as part of my final assignment for *Elements of Computing II*. I built it because I found it surprisingly difficult to find Korean learning apps that combine multiple game modes in one place. Most apps only focus on flashcards or grammar — so I set out to build something better.

---

## 📌 Features

The app is designed with a clean multi-tab layout and includes four engaging mini-games:

| Game | Description |
|------|-------------|
| ✍️ **Romanization ➔ Hangul** | Practice typing correct Hangul based on the Romanized Korean word. Tracks progress and streaks. |
| 📝 **Vocabulary Quiz** | Pick the correct Korean word for a given English prompt from multiple choices. Fully randomized. |
| 🏎️ **Korean TypeRacer** | Choose between Easy or Hard difficulty and test your typing speed in Korean. Tracks best times. |
| ⏳ **Tense Selector** | Choose the correct Korean verb tense (past, present, future) based on the English sentence. Includes grammar sidebar guide. |

Each game is self-contained and allows you to reset for a new challenge at any time. Feedback, streaks, and total correct/attempts are tracked per game.

---

## 💻 Technologies Used

- **Python 3.10+**
- [**Streamlit**](https://streamlit.io/) — for building the interactive web app
- Custom layout and styling using `st.markdown()` with inline CSS

---

## 🚀 Running the App Locally

Make sure Python and pip are installed, then:

```bash
# Clone the repo
git clone https://github.com/your-username/learn-korean-hub.git
cd learn-korean-hub

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

## 🌐 Deployment

This app can be deployed for free using [**Streamlit Community Cloud**](https://streamlit.io/cloud).  
You can also host it yourself using services like **PythonAnywhere** or **Replit**.

---

## 📂 Project Structure

learn-korean-hub/ ├── app.py # Main Streamlit app ├── README.md # Project documentation (you're reading it!) ├── requirements.txt # Python dependencies