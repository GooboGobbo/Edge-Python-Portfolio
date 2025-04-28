# ---------------------------------------------------------------------------------------------------------------------------
# Learn Korean Mini Games Hub 🇰🇷
# Streamlit App
# ---------------------------------------------------------------------------------------------------------------------------

import streamlit as st
import random
import time

# ---------------------------------------------------------------------------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------------------------------------------------------------------------

st.set_page_config(page_title="Learn Korean Hub 🇰🇷", layout="centered")
st.title("Learn Korean: Mini Games Hub 🇰🇷🎮")

# ---------------------------------------------------------------------------------------------------------------------------
# Datasets for All Mini-Games
# ---------------------------------------------------------------------------------------------------------------------------

# Dataset for Romanization ➔ Hangul
romanization_words = [
    {"romanization": "annyeong", "hangul": "안녕", "english": "Hi / Hello"},
    {"romanization": "gamsahamnida", "hangul": "감사합니다", "english": "Thank you"},
    {"romanization": "saranghae", "hangul": "사랑해", "english": "I love you"},
    {"romanization": "jal jinae", "hangul": "잘 지내", "english": "Doing well"},
    {"romanization": "chingu", "hangul": "친구", "english": "Friend"},
    {"romanization": "eomma", "hangul": "엄마", "english": "Mother"},
    {"romanization": "appa", "hangul": "아빠", "english": "Father"},
    {"romanization": "hangugeo", "hangul": "한국어", "english": "Korean language"},
    {"romanization": "mashisseoyo", "hangul": "맛있어요", "english": "It's delicious"},
    {"romanization": "bogosipeo", "hangul": "보고싶어", "english": "I miss you"},
    {"romanization": "gaja", "hangul": "가자", "english": "Let's go"},
    {"romanization": "meogeoyo", "hangul": "먹어요", "english": "Eat / Eating"},
    {"romanization": "isseoyo", "hangul": "있어요", "english": "There is / I have"},
    {"romanization": "eodieyo", "hangul": "어디에요", "english": "Where is it?"},
    {"romanization": "jal isseo", "hangul": "잘 있어", "english": "Stay well"},
    {"romanization": "saengil chukhahae", "hangul": "생일 축하해", "english": "Happy birthday"},
    {"romanization": "jal ja", "hangul": "잘 자", "english": "Sleep well"},
    {"romanization": "annyeonghaseyo", "hangul": "안녕하세요", "english": "Hello (formal)"},
    {"romanization": "byeonhada", "hangul": "변하다", "english": "To change"},
    {"romanization": "sseuda", "hangul": "쓰다", "english": "To write / To use"},
    {"romanization": "juseyo", "hangul": "주세요", "english": "Please give me"},
    {"romanization": "gamsahaeyo", "hangul": "감사해요", "english": "Thanks (polite)"},
    {"romanization": "je ireumeun", "hangul": "제 이름은", "english": "My name is..."},
    {"romanization": "jal meokkesseumnida", "hangul": "잘 먹겠습니다", "english": "I will eat well"},
    {"romanization": "jal meogeosseumnida", "hangul": "잘 먹었습니다", "english": "I ate well"},
    {"romanization": "chogiyo", "hangul": "저기요", "english": "Excuse me"},
    {"romanization": "juseyo", "hangul": "주세요", "english": "Please"},
    {"romanization": "aneyo", "hangul": "아니요", "english": "No"},
    {"romanization": "ne", "hangul": "네", "english": "Yes"},
    {"romanization": "mianhamnida", "hangul": "미안합니다", "english": "Sorry"},
    {"romanization": "sillyehapnida", "hangul": "실례합니다", "english": "Excuse me (formal)"},
    {"romanization": "oneul", "hangul": "오늘", "english": "Today"},
    {"romanization": "naeil", "hangul": "내일", "english": "Tomorrow"},
    {"romanization": "eoneu", "hangul": "어느", "english": "Which"},
    {"romanization": "eodiseo", "hangul": "어디서", "english": "Where (from)"},
    {"romanization": "mwo", "hangul": "뭐", "english": "What"},
    {"romanization": "eotteoke", "hangul": "어떻게", "english": "How"},
    {"romanization": "wa", "hangul": "와", "english": "And (casual)"},
    {"romanization": "geurigo", "hangul": "그리고", "english": "And (formal)"},
    {"romanization": "ttatteuthae", "hangul": "따뜻해", "english": "It's warm"},
    {"romanization": "chuwo", "hangul": "추워", "english": "It's cold"},
    {"romanization": "tteugeoun", "hangul": "뜨거운", "english": "Hot"},
    {"romanization": "sigan", "hangul": "시간", "english": "Time"},
    {"romanization": "sigan isseo", "hangul": "시간 있어", "english": "Do you have time?"},
    {"romanization": "pyeonhage", "hangul": "편하게", "english": "Comfortably"},
    {"romanization": "cheoncheonhi", "hangul": "천천히", "english": "Slowly"},
    {"romanization": "ppalli", "hangul": "빨리", "english": "Quickly"},
    {"romanization": "jeoneun", "hangul": "저는", "english": "I am..."},
    {"romanization": "dangsin", "hangul": "당신", "english": "You"},
    {"romanization": "geunyeo", "hangul": "그녀", "english": "She"},
    {"romanization": "geu", "hangul": "그", "english": "That"},
]



# Dataset for Vocabulary Quiz
vocab_questions = [
    {"english": "Thank you", "choices": ["감사합니다", "사랑해", "친구", "잘 지내"], "answer": "감사합니다"},
    {"english": "Friend", "choices": ["엄마", "친구", "아빠", "한국어"], "answer": "친구"},
    {"english": "Mother", "choices": ["엄마", "아빠", "친구", "안녕"], "answer": "엄마"},
    {"english": "Father", "choices": ["사랑해", "감사합니다", "아빠", "친구"], "answer": "아빠"},
    {"english": "Korean language", "choices": ["맛있어요", "보고싶어", "한국어", "잘 지내"], "answer": "한국어"},
    {"english": "It's delicious", "choices": ["맛있어요", "먹어요", "있어요", "어디에요"], "answer": "맛있어요"},
    {"english": "I miss you", "choices": ["가자", "맛있어요", "보고싶어", "안녕하세요"], "answer": "보고싶어"},
    {"english": "Let's go", "choices": ["가자", "먹어요", "사랑해", "안녕"], "answer": "가자"},
    {"english": "Where is it?", "choices": ["있어요", "어디에요", "가자", "잘 자"], "answer": "어디에요"},
    {"english": "Goodbye (stay well)", "choices": ["잘 자", "잘 있어", "안녕", "친구"], "answer": "잘 있어"},
    {"english": "Happy birthday", "choices": ["잘 자", "잘 있어", "생일 축하해", "감사합니다"], "answer": "생일 축하해"},
    {"english": "Sleep well", "choices": ["잘 자", "잘 지내", "친구", "감사합니다"], "answer": "잘 자"},
    {"english": "Hello (formal)", "choices": ["감사합니다", "안녕하세요", "사랑해", "가자"], "answer": "안녕하세요"},
    {"english": "To change", "choices": ["변하다", "쓰다", "맛있어요", "친구"], "answer": "변하다"},
    {"english": "To write / To use", "choices": ["쓰다", "가자", "친구", "감사합니다"], "answer": "쓰다"},
    {"english": "Please give me", "choices": ["주세요", "미안합니다", "네", "아니요"], "answer": "주세요"},
    {"english": "Thanks (polite)", "choices": ["감사해요", "감사합니다", "사랑해", "어디에요"], "answer": "감사해요"},
    {"english": "My name is...", "choices": ["제 이름은", "어디에요", "잘 있어", "사랑해"], "answer": "제 이름은"},
    {"english": "I will eat well", "choices": ["잘 먹겠습니다", "잘 먹었습니다", "먹어요", "친구"], "answer": "잘 먹겠습니다"},
    {"english": "I ate well", "choices": ["잘 먹겠습니다", "잘 먹었습니다", "맛있어요", "감사합니다"], "answer": "잘 먹었습니다"},
    {"english": "Excuse me", "choices": ["저기요", "어디에요", "감사합니다", "잘 자"], "answer": "저기요"},
    {"english": "No", "choices": ["네", "아니요", "감사합니다", "친구"], "answer": "아니요"},
    {"english": "Yes", "choices": ["네", "아니요", "감사합니다", "사랑해"], "answer": "네"},
    {"english": "Sorry", "choices": ["미안합니다", "감사합니다", "친구", "잘 지내"], "answer": "미안합니다"},
    {"english": "Excuse me (formal)", "choices": ["실례합니다", "감사합니다", "잘 있어", "잘 자"], "answer": "실례합니다"},
    {"english": "Today", "choices": ["오늘", "내일", "어디에요", "가자"], "answer": "오늘"},
    {"english": "Tomorrow", "choices": ["내일", "오늘", "감사합니다", "잘 지내"], "answer": "내일"},
    {"english": "Which", "choices": ["어느", "뭐", "어디에요", "감사합니다"], "answer": "어느"},
    {"english": "What", "choices": ["뭐", "어느", "감사합니다", "친구"], "answer": "뭐"},
    {"english": "How", "choices": ["어떻게", "어디에요", "감사합니다", "친구"], "answer": "어떻게"},
    {"english": "And (casual)", "choices": ["와", "그리고", "맛있어요", "잘 자"], "answer": "와"},
    {"english": "And (formal)", "choices": ["그리고", "와", "감사합니다", "친구"], "answer": "그리고"},
    {"english": "It's warm", "choices": ["따뜻해", "추워", "뜨거운", "감사합니다"], "answer": "따뜻해"},
    {"english": "It's cold", "choices": ["추워", "따뜻해", "뜨거운", "친구"], "answer": "추워"},
    {"english": "Hot", "choices": ["뜨거운", "추워", "맛있어요", "친구"], "answer": "뜨거운"},
    {"english": "Time", "choices": ["시간", "어디에요", "감사합니다", "친구"], "answer": "시간"},
    {"english": "Do you have time?", "choices": ["시간 있어", "시간", "어디에요", "친구"], "answer": "시간 있어"},
    {"english": "Comfortably", "choices": ["편하게", "천천히", "빨리", "감사합니다"], "answer": "편하게"},
    {"english": "Slowly", "choices": ["천천히", "편하게", "빨리", "잘 자"], "answer": "천천히"},
    {"english": "Quickly", "choices": ["빨리", "편하게", "천천히", "잘 있어"], "answer": "빨리"},
    {"english": "I am...", "choices": ["저는", "당신", "그녀", "그"], "answer": "저는"},
    {"english": "You", "choices": ["당신", "저는", "그녀", "그"], "answer": "당신"},
    {"english": "She", "choices": ["그녀", "당신", "저는", "그"], "answer": "그녀"},
    {"english": "He", "choices": ["그", "그녀", "당신", "저는"], "answer": "그"},
    {"english": "Food", "choices": ["음식", "친구", "학교", "감사합니다"], "answer": "음식"},
    {"english": "School", "choices": ["학교", "음식", "친구", "사랑해"], "answer": "학교"},
    {"english": "Water", "choices": ["물", "학교", "음식", "친구"], "answer": "물"},
    {"english": "Book", "choices": ["책", "음악", "학교", "친구"], "answer": "책"},
    {"english": "Music", "choices": ["음악", "책", "학교", "친구"], "answer": "음악"}
]


# Dataset for Korean TypeRacer
typing_sentences_easy = [
    {"hangul": "오늘 날씨가 정말 좋아요.", "english": "The weather is really nice today."},
    {"hangul": "저는 한국어를 공부하고 있어요.", "english": "I am studying Korean."},
    {"hangul": "내일은 친구를 만날 거예요.", "english": "I will meet a friend tomorrow."},
    {"hangul": "이 음식은 정말 맛있어요.", "english": "This food is really delicious."},
    {"hangul": "지금 어디에 가고 있어요?", "english": "Where are you going now?"},
    {"hangul": "저는 서울에 살고 있어요.", "english": "I live in Seoul."},
    {"hangul": "학교에 가야 해요.", "english": "I have to go to school."},
    {"hangul": "커피를 마시고 싶어요.", "english": "I want to drink coffee."},
    {"hangul": "좋은 하루 보내세요.", "english": "Have a good day."},
    {"hangul": "오늘도 수고했어요.", "english": "You worked hard today too."},
    {"hangul": "운동을 하고 싶어요.", "english": "I want to exercise."},
    {"hangul": "책을 읽고 있어요.", "english": "I am reading a book."},
    {"hangul": "음악을 듣고 있어요.", "english": "I am listening to music."},
    {"hangul": "집에 가고 싶어요.", "english": "I want to go home."},
    {"hangul": "영화를 보고 싶어요.", "english": "I want to watch a movie."},
    {"hangul": "어제는 정말 추웠어요.", "english": "It was really cold yesterday."},
    {"hangul": "새로운 친구를 사귀었어요.", "english": "I made a new friend."},
    {"hangul": "저는 매일 아침에 운동해요.", "english": "I exercise every morning."},
    {"hangul": "오늘은 숙제가 많아요.", "english": "I have a lot of homework today."},
    {"hangul": "가족과 시간을 보내고 싶어요.", "english": "I want to spend time with my family."},
    {"hangul": "저녁에 공원에 갔어요.", "english": "I went to the park in the evening."},
    {"hangul": "주말에 바다를 보러 갔어요.", "english": "I went to see the sea on the weekend."},
    {"hangul": "한국 음식을 좋아해요.", "english": "I like Korean food."},
    {"hangul": "생일 파티에 갔어요.", "english": "I went to a birthday party."},
    {"hangul": "새로운 직장을 찾고 있어요.", "english": "I am looking for a new job."},
    {"hangul": "요즘 너무 바빠요.", "english": "I am very busy these days."},
    {"hangul": "오늘은 일찍 일어났어요.", "english": "I woke up early today."},
    {"hangul": "비가 와서 집에 있었어요.", "english": "It rained so I stayed at home."},
    {"hangul": "여름 방학이 기다려져요.", "english": "I am looking forward to summer vacation."},
    {"hangul": "운전하는 것을 배우고 있어요.", "english": "I am learning how to drive."}
]

typing_sentences_hard = [
    {
        "hangul": "오늘은 정말 바빴어요. 회사에서 회의가 많았어요. 그래서 점심도 늦게 먹었어요.",
        "english": "Today was really busy. There were many meetings at work. So I ate lunch late."
    },
    {
        "hangul": "주말에 여행을 갔어요. 친구들과 바다를 보러 갔어요. 날씨가 정말 좋았어요.",
        "english": "I went on a trip over the weekend. I went to see the ocean with friends. The weather was really nice."
    },
    {
        "hangul": "어제는 비가 많이 왔어요. 우산을 안 가져와서 많이 젖었어요. 그래서 감기에 걸렸어요.",
        "english": "It rained a lot yesterday. I didn’t bring an umbrella and got really wet. So I caught a cold."
    },
    {
        "hangul": "오늘 아침에 운동을 했어요. 조깅을 하고 스트레칭을 했어요. 몸이 상쾌했어요.",
        "english": "I exercised this morning. I went jogging and did some stretching. My body felt refreshed."
    },
    {
        "hangul": "저는 새로운 취미를 시작했어요. 그림 그리기를 배우고 있어요. 정말 재미있어요.",
        "english": "I started a new hobby. I am learning to draw. It's really fun."
    },
    {
        "hangul": "이번 주말에는 영화를 볼 거예요. 가족과 함께 영화관에 갈 거예요. 팝콘도 먹을 거예요.",
        "english": "I will watch a movie this weekend. I will go to the movie theater with my family. We will eat popcorn too."
    },
    {
        "hangul": "오늘은 친구 생일이에요. 우리는 맛있는 음식을 먹을 거예요. 그리고 노래방에 갈 거예요.",
        "english": "Today is my friend's birthday. We will eat delicious food. And we will go to karaoke."
    },
    {
        "hangul": "어제 새로운 책을 샀어요. 오늘 아침에 조금 읽었어요. 이야기 내용이 정말 흥미로워요.",
        "english": "I bought a new book yesterday. I read a little this morning. The story is really interesting."
    },
    {
        "hangul": "학교에서 시험을 봤어요. 시험이 생각보다 쉬웠어요. 좋은 점수를 받을 것 같아요.",
        "english": "I took a test at school. The test was easier than I thought. I think I will get a good score."
    },
    {
        "hangul": "이번 여름에 한국에 갈 거예요. 친구들을 만나고 맛있는 음식을 먹을 거예요. 그리고 여러 곳을 여행할 거예요.",
        "english": "I will go to Korea this summer. I will meet friends and eat delicious food. And I will travel to many places."
    }
]


# Dataset for Tense Selector
tense_questions = [
    {"english": "I eat rice.", "choices": ["먹어요", "먹었습니다", "먹을 거예요"], "answer": "먹어요"},
    {"english": "I ate rice.", "choices": ["먹어요", "먹었습니다", "먹을 거예요"], "answer": "먹었습니다"},
    {"english": "I will eat rice.", "choices": ["먹어요", "먹었습니다", "먹을 거예요"], "answer": "먹을 거예요"},
    
    {"english": "I study Korean.", "choices": ["공부해요", "공부했어요", "공부할 거예요"], "answer": "공부해요"},
    {"english": "I studied Korean.", "choices": ["공부해요", "공부했어요", "공부할 거예요"], "answer": "공부했어요"},
    {"english": "I will study Korean.", "choices": ["공부해요", "공부했어요", "공부할 거예요"], "answer": "공부할 거예요"},

    {"english": "I meet a friend.", "choices": ["만나요", "만났어요", "만날 거예요"], "answer": "만나요"},
    {"english": "I met a friend.", "choices": ["만나요", "만났어요", "만날 거예요"], "answer": "만났어요"},
    {"english": "I will meet a friend.", "choices": ["만나요", "만났어요", "만날 거예요"], "answer": "만날 거예요"},

    {"english": "I go to school.", "choices": ["가요", "갔어요", "갈 거예요"], "answer": "가요"},
    {"english": "I went to school.", "choices": ["가요", "갔어요", "갈 거예요"], "answer": "갔어요"},
    {"english": "I will go to school.", "choices": ["가요", "갔어요", "갈 거예요"], "answer": "갈 거예요"},

    {"english": "I drink coffee.", "choices": ["마셔요", "마셨어요", "마실 거예요"], "answer": "마셔요"},
    {"english": "I drank coffee.", "choices": ["마셔요", "마셨어요", "마실 거예요"], "answer": "마셨어요"},
    {"english": "I will drink coffee.", "choices": ["마셔요", "마셨어요", "마실 거예요"], "answer": "마실 거예요"},

    {"english": "I buy a book.", "choices": ["사요", "샀어요", "살 거예요"], "answer": "사요"},
    {"english": "I bought a book.", "choices": ["사요", "샀어요", "살 거예요"], "answer": "샀어요"},
    {"english": "I will buy a book.", "choices": ["사요", "샀어요", "살 거예요"], "answer": "살 거예요"},

    {"english": "I sleep early.", "choices": ["일찍 자요", "일찍 잤어요", "일찍 잘 거예요"], "answer": "일찍 자요"},
    {"english": "I slept early.", "choices": ["일찍 자요", "일찍 잤어요", "일찍 잘 거예요"], "answer": "일찍 잤어요"},
    {"english": "I will sleep early.", "choices": ["일찍 자요", "일찍 잤어요", "일찍 잘 거예요"], "answer": "일찍 잘 거예요"},

    {"english": "I watch a movie.", "choices": ["영화 봐요", "영화 봤어요", "영화 볼 거예요"], "answer": "영화 봐요"},
    {"english": "I watched a movie.", "choices": ["영화 봐요", "영화 봤어요", "영화 볼 거예요"], "answer": "영화 봤어요"},
    {"english": "I will watch a movie.", "choices": ["영화 봐요", "영화 봤어요", "영화 볼 거예요"], "answer": "영화 볼 거예요"},

    {"english": "I walk in the park.", "choices": ["공원에서 걸어요", "공원에서 걸었어요", "공원에서 걸을 거예요"], "answer": "공원에서 걸어요"},
    {"english": "I walked in the park.", "choices": ["공원에서 걸어요", "공원에서 걸었어요", "공원에서 걸을 거예요"], "answer": "공원에서 걸었어요"},
    {"english": "I will walk in the park.", "choices": ["공원에서 걸어요", "공원에서 걸었어요", "공원에서 걸을 거예요"], "answer": "공원에서 걸을 거예요"},
]

# ---------------------------------------------------------------------------------------------------------------------------
# Create Tabs
# ---------------------------------------------------------------------------------------------------------------------------

tab_home, tab1, tab2, tab3, tab4 = st.tabs([
    "🏠 Home", 
    "✍️ Romanization ➔ Hangul", 
    "📝 Vocabulary Quiz", 
    "🏎️ Korean TypeRacer", 
    "⏳ Tense Selector"
])



# ---------------------------------------------------------------------------------------------------------------------------
# Home Screen
# ---------------------------------------------------------------------------------------------------------------------------
with tab_home:

    st.subheader("Welcome!")

    st.write("""
    This app is designed to help **beginner Korean learners** improve their language skills through interactive games.
    It is inspired by my desire to learn more about my mother's Korean heritage and to connect with my family's roots. 🇰🇷✨
    """)
    st.write("If you want some additional information on Romanization and tenses, check the sidebar! Have fun!")

    st.markdown("---")

    st.subheader("Mini-Games Overview")

    # Romanization to Hangul
    st.markdown("### ✍️ Romanization ➔ Hangul")
    st.write("""
    Practice typing Hangul by seeing Romanized Korean words.
    Type the correct Hangul spelling based on the Romanization.
    Press **Enter** or **Submit** to check your answer.
    """)

    # Vocabulary Quiz
    st.markdown("### 📝 Vocabulary Quiz")
    st.write("""
    Test your Korean vocabulary knowledge!
    You will be shown an English word and must pick the correct Korean translation from multiple choices.
    """)

    # Korean TypeRacer
    st.markdown("### 🏎️ Korean TypeRacer")
    st.write("""
    Improve your typing speed and accuracy in Hangul!
    Type full Korean sentences as fast as you can based on what you see. Your time will be recorded.
    """)

    # Tense Selector
    st.markdown("### ⏳ Tense Selector")
    st.write("""
    Strengthen your understanding of Korean verb tenses!
    Choose the correct Korean verb form (present, past, or future) based on the given English sentence.
    """)

    st.markdown("---")
    st.caption("Good luck and have fun learning Korean! 🌟")


# ---------------------------------------------------------------------------------------------------------------------------
# Mini-Game 1: Romanization ➔ Hangul
# ---------------------------------------------------------------------------------------------------------------------------

with tab1:
    st.header("Romanization ➔ Hangul Practice ✍️")

    # --- Sidebar for Romanization Game ---
    with st.sidebar:
        st.header("✍️ Romanization ➔ Hangul Guide")
        st.write("""
Romanization is the representation of Korean words using the Latin alphabet.  
Your goal is to correctly type the Hangul (Korean script) based on the Romanized hint!

### 📚 Quick Tips:
- Each Romanized syllable maps to a Hangul block.
- Pay attention to double consonants (e.g., 'kk', 'tt') and vowel sounds (e.g., 'eo', 'ae').

### 🛠️ Common Romanization to Hangul Equivalents:
| Romanization | Hangul | Example |
|:--|:--|:--|
| a | 아 | 가 (ga) |
| eo | 어 | 서 (seo) |
| o | 오 | 도 (do) |
| u | 우 | 수 (su) |
| eu | 으 | 그 (geu) |
| i | 이 | 미 (mi) |
| ae | 애 | 새 (sae) |
| e | 에 | 네 (ne) |
| k/g | ㄱ | 고 (go) |
| n | ㄴ | 나 (na) |
| d/t | ㄷ | 다 (da) |
| r/l | ㄹ | 라 (ra) |
| m | ㅁ | 마 (ma) |
| b/p | ㅂ | 바 (ba) |
| s | ㅅ | 사 (sa) |
| j | ㅈ | 자 (ja) |
| ch | ㅊ | 차 (cha) |
| k | ㅋ | 카 (ka) |
| t | ㅌ | 타 (ta) |
| p | ㅍ | 파 (pa) |
| h | ㅎ | 하 (ha) |

### 🔗 Learn more about Romanization:
[Korean Romanization Guide - How to Study Korean](https://www.howtostudykorean.com/unit-0-lesson-1/)
        
---------------
                 
                 """)

    # --- Small Description Under Title ---
    st.caption("Type the correct Hangul spelling based on the Romanized word shown. Press Enter or click Submit!")

    # Initialize session state
    if "rom_current_word" not in st.session_state:
        st.session_state.rom_current_word = random.choice(romanization_words)

    if "rom_user_input" not in st.session_state:
        st.session_state.rom_user_input = ""

    if "rom_flash" not in st.session_state:
        st.session_state.rom_flash = False  # control color flashing

    if "rom_correct_count" not in st.session_state:
        st.session_state.rom_correct_count = 0

    if "rom_total_attempts" not in st.session_state:
        st.session_state.rom_total_attempts = 0

    if "rom_streak" not in st.session_state:
        st.session_state.rom_streak = 0

    # --- Handle Next Word button first ---
    col1, col2, col3 = st.columns([2, 4, 1])
    with col1:
        if st.button("🔄 Next Word"):
            st.session_state.rom_current_word = random.choice(romanization_words)
            st.session_state.rom_user_input = ""
            st.session_state.rom_flash = True
            st.rerun()

    # --- Display Word and Input Form ---
    if st.session_state.rom_flash:
        st.markdown(
            f"<h2 style='color: #C60C30;'>{st.session_state.rom_current_word['romanization']}</h2>",
            unsafe_allow_html=True
        )
        st.session_state.rom_flash = False
    else:
        st.subheader(f"Romanized Word: {st.session_state.rom_current_word['romanization']}")

    # Create the input form
    with st.form(key="rom_form"):
        user_input = st.text_input(
            "Type the Hangul version:",
            key="rom_user_input"
        )
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            st.session_state.rom_total_attempts += 1

            if user_input.strip() == st.session_state.rom_current_word['hangul']:
                st.session_state.rom_correct_count += 1
                st.session_state.rom_streak += 1
                st.success(f"✅ Correct!\n\n**Meaning:** {st.session_state.rom_current_word['english']}")
            else:
                st.session_state.rom_streak = 0
                st.error(f"❌ Incorrect. Correct answer: {st.session_state.rom_current_word['hangul']}")

    # --- Show Progress and Streak at the Bottom ---
    st.markdown("---")
    st.markdown(f"**Progress:** {st.session_state.rom_correct_count} correct out of {st.session_state.rom_total_attempts} attempts")
    st.markdown(f"🔥 **Current Streak:** {st.session_state.rom_streak}")



# ---------------------------------------------------------------------------------------------------------------------------
# Mini-Game 2: Vocabulary Quiz
# ---------------------------------------------------------------------------------------------------------------------------

with tab2:
    st.header("Vocabulary Quiz 📝")

    # --- Add Small Description Under Title ---
    st.caption("Choose the correct Korean translation for the given English word. Press Submit to check your answer!")

    # Initialize session state
    if "vocab_current_question" not in st.session_state:
        st.session_state.vocab_current_question = random.choice(vocab_questions)

    if "vocab_shuffled_choices" not in st.session_state:
        st.session_state.vocab_shuffled_choices = st.session_state.vocab_current_question['choices'].copy()
        random.shuffle(st.session_state.vocab_shuffled_choices)

    if "vocab_user_choice" not in st.session_state:
        st.session_state.vocab_user_choice = None

    if "vocab_correct_count" not in st.session_state:
        st.session_state.vocab_correct_count = 0

    if "vocab_total_attempts" not in st.session_state:
        st.session_state.vocab_total_attempts = 0

    if "vocab_streak" not in st.session_state:
        st.session_state.vocab_streak = 0

    # --- Handle Next Question button FIRST ---
    col1, col2, col3 = st.columns([2, 4, 1])
    with col1:
        if st.button("🔄 Next Question (Vocab Quiz)"):
            st.session_state.vocab_current_question = random.choice(vocab_questions)
            st.session_state.vocab_user_choice = None
            st.session_state.vocab_shuffled_choices = st.session_state.vocab_current_question['choices'].copy()
            random.shuffle(st.session_state.vocab_shuffled_choices)
            st.rerun()

    # --- Display Current Question ---
    st.subheader(f"English Word: **{st.session_state.vocab_current_question['english']}**")

    # Use the SHUFFLED copy stored in session state
    st.radio(
        "Pick the correct Korean word:",
        options=st.session_state.vocab_shuffled_choices,
        key="vocab_user_choice"
    )

    # --- Submit Answer Button ---
    if st.button("✅ Submit (Vocab Quiz)"):
        if st.session_state.vocab_user_choice:
            st.session_state.vocab_total_attempts += 1

            if st.session_state.vocab_user_choice == st.session_state.vocab_current_question['answer']:
                st.session_state.vocab_correct_count += 1
                st.session_state.vocab_streak += 1
                st.success(f"✅ Correct!\n\n**English Word:** {st.session_state.vocab_current_question['english']}\n**Korean Word:** {st.session_state.vocab_user_choice}")
            else:
                st.session_state.vocab_streak = 0
                st.error(f"❌ Incorrect.\n\n**English Word:** {st.session_state.vocab_current_question['english']}\n**Correct Korean Word:** {st.session_state.vocab_current_question['answer']}")

    # --- Show Progress and Streak at the Bottom ---
    st.markdown("---")
    st.markdown(f"**Progress:** {st.session_state.vocab_correct_count} correct out of {st.session_state.vocab_total_attempts} attempts")
    st.markdown(f"🔥 **Current Streak:** {st.session_state.vocab_streak}")


# ---------------------------------------------------------------------------------------------------------------------------
# Mini-Game 3: Korean Typeracer
# ---------------------------------------------------------------------------------------------------------------------------

# --- Helper function to highlight differences ---
def highlight_differences(correct, user):
    output = ""
    for i in range(max(len(correct), len(user))):
        correct_char = correct[i] if i < len(correct) else ""
        user_char = user[i] if i < len(user) else ""
        if correct_char == user_char:
            output += f"<span style='color:black;'>{correct_char}</span>"
        else:
            output += f"<span style='color:red;'>{correct_char}</span>"
    return output

with tab3:
    st.header("Korean TypeRacer 🏎️⌨️")

    # --- Add Small Description Under Title ---
    st.caption("Choose Easy or Hard mode. Type the full Korean sentence(s) exactly as shown. Timer starts when a new sentence appears!")

    # Initialize session state
    if "typeracer_mode" not in st.session_state:
        st.session_state.typeracer_mode = "Easy"

    if "typeracer_current_sentence" not in st.session_state:
        st.session_state.typeracer_current_sentence = random.choice(typing_sentences_easy)

    if "typeracer_user_input" not in st.session_state:
        st.session_state.typeracer_user_input = ""

    if "typeracer_start_time" not in st.session_state:
        st.session_state.typeracer_start_time = time.time()

    if "typeracer_best_time_easy" not in st.session_state:
        st.session_state.typeracer_best_time_easy = None

    if "typeracer_best_time_hard" not in st.session_state:
        st.session_state.typeracer_best_time_hard = None

    # --- Handle Mode Switching ---
    mode = st.radio(
        "Select Difficulty:",
        options=["Easy", "Hard"],
        index=0 if st.session_state.typeracer_mode == "Easy" else 1
    )

    if mode != st.session_state.typeracer_mode:
        st.session_state.typeracer_mode = mode
        if mode == "Easy":
            st.session_state.typeracer_current_sentence = random.choice(typing_sentences_easy)
        else:
            st.session_state.typeracer_current_sentence = random.choice(typing_sentences_hard)
        st.session_state.typeracer_user_input = ""
        st.session_state.typeracer_start_time = time.time()
        st.rerun()

    # --- Handle Next Sentence Button FIRST ---
    col1, col2, col3 = st.columns([2, 4, 1])
    with col1:
        if st.button("🔄 Next Sentence (TypeRacer)"):
            if st.session_state.typeracer_mode == "Easy":
                st.session_state.typeracer_current_sentence = random.choice(typing_sentences_easy)
            else:
                st.session_state.typeracer_current_sentence = random.choice(typing_sentences_hard)
            st.session_state.typeracer_user_input = ""
            st.session_state.typeracer_start_time = time.time()
            st.rerun()

    # --- Display Sentence to Type (Large, Cleanly Formatted) ---
    if st.session_state.typeracer_mode == "Easy":
        # Easy mode: one big centered sentence
        st.markdown(
            f"<h2 style='text-align: center; font-size: 36px;'>{st.session_state.typeracer_current_sentence['hangul']}</h2>",
            unsafe_allow_html=True
        )
    else:
        # Hard mode: split paragraph into 3 separate lines
        sentences = st.session_state.typeracer_current_sentence['hangul'].split('. ')
        formatted_sentences = "<br>".join(
            f"<div style='text-align: center; font-size: 30px;'>{s.strip()}.</div>"
            for s in sentences if s
        )
        st.markdown(formatted_sentences, unsafe_allow_html=True)

    # --- Typing input box ---
    user_input = st.text_area(
        "Type the full sentence(s) exactly here:",
        value=st.session_state.typeracer_user_input,
        key="typeracer_user_input",
        height=150
    )

    # --- Submit Button ---
    if st.button("✅ Submit (TypeRacer)"):
        if st.session_state.typeracer_user_input:
            end_time = time.time()
            total_time = round(end_time - st.session_state.typeracer_start_time, 2)

            if st.session_state.typeracer_user_input.strip() == st.session_state.typeracer_current_sentence['hangul'].strip():
                st.success(f"✅ Correct! You typed it in **{total_time} seconds**.")
                st.info(f"**English Translation:** {st.session_state.typeracer_current_sentence['english']}")

                # Update best time based on mode
                if st.session_state.typeracer_mode == "Easy":
                    if (st.session_state.typeracer_best_time_easy is None) or (total_time < st.session_state.typeracer_best_time_easy):
                        st.session_state.typeracer_best_time_easy = total_time
                        st.balloons()
                else:
                    if (st.session_state.typeracer_best_time_hard is None) or (total_time < st.session_state.typeracer_best_time_hard):
                        st.session_state.typeracer_best_time_hard = total_time
                        st.balloons()

            else:
                st.error("❌ Incorrect! Check your spelling and spacing carefully.")

                # Highlight incorrect characters FIRST
                highlighted = highlight_differences(
                    st.session_state.typeracer_current_sentence['hangul'].strip(),
                    st.session_state.typeracer_user_input.strip()
                )
                st.markdown("### 🔎 Correct Sentence with Mistakes Highlighted:")
                st.markdown(highlighted, unsafe_allow_html=True)

                # Then show English translation SECOND
                st.info(f"**English Translation:** {st.session_state.typeracer_current_sentence['english']}")

    # --- Show Best Times ---
    st.markdown("---")
    if st.session_state.typeracer_mode == "Easy" and st.session_state.typeracer_best_time_easy:
        st.markdown(f"🏆 **Best Easy Mode Time:** {st.session_state.typeracer_best_time_easy} seconds")
    if st.session_state.typeracer_mode == "Hard" and st.session_state.typeracer_best_time_hard:
        st.markdown(f"🏆 **Best Hard Mode Time:** {st.session_state.typeracer_best_time_hard} seconds")



# ---------------------------------------------------------------------------------------------------------------------------
# Mini-Game 3: Korean Typeracer
# ---------------------------------------------------------------------------------------------------------------------------

with tab4:
    st.header("Tense Selector 🕰️")

    # --- Sidebar Explanation for Tenses ---
    with st.sidebar:
        st.header("📚 Korean Verb Tenses Overview")
        st.write("""
In Korean, verbs change depending on when an action happens: past, present, or future.

- **Present Tense (현재형)**:  
  Verb stem + 아요 / 어요  
  Example: 먹어요 (I eat), 가요 (I go)

- **Past Tense (과거형)**:  
  Verb stem + 았어요 / 었어요  
  Example: 먹었어요 (I ate), 갔어요 (I went)

- **Future Tense (미래형)**:  
  Verb stem + ㄹ 거예요 / 을 거예요  
  Example: 먹을 거예요 (I will eat), 갈 거예요 (I will go)

👉 Look carefully at the verb endings to choose the correct form!
        """)
        st.markdown("---")
        st.markdown("[🔗 Learn more about Korean tenses here](https://www.howtostudykorean.com/unit-1-lesson-5/)")

    # --- Small Description under Title ---
    st.caption("Choose the correct Korean verb form (present, past, future) for the given English sentence.")

    # Initialize session state
    if "tense_current_question" not in st.session_state:
        st.session_state.tense_current_question = random.choice(tense_questions)

    if "tense_user_choice" not in st.session_state:
        st.session_state.tense_user_choice = None

    if "tense_correct_count" not in st.session_state:
        st.session_state.tense_correct_count = 0

    if "tense_total_attempts" not in st.session_state:
        st.session_state.tense_total_attempts = 0

    if "tense_streak" not in st.session_state:
        st.session_state.tense_streak = 0

    # --- Handle Next Question button FIRST ---
    col1, col2, col3 = st.columns([2, 4, 1])
    with col1:
        if st.button("🔄 Next Question (Tense Selector)"):
            st.session_state.tense_current_question = random.choice(tense_questions)
            st.session_state.tense_user_choice = None
            st.rerun()

    # --- Display Current Question ---
    st.subheader(f"English Sentence: **{st.session_state.tense_current_question['english']}**")

    # No shuffling — show choices in dataset order
    st.radio(
        "Pick the correct Korean verb form:",
        options=st.session_state.tense_current_question['choices'],
        key="tense_user_choice"
    )

    # --- Submit Answer Button ---
    if st.button("✅ Submit (Tense Selector)"):
        if st.session_state.tense_user_choice:
            st.session_state.tense_total_attempts += 1

            if st.session_state.tense_user_choice == st.session_state.tense_current_question['answer']:
                st.session_state.tense_correct_count += 1
                st.session_state.tense_streak += 1
                st.success(f"✅ Correct! **{st.session_state.tense_user_choice}** is the right form.")
            else:
                st.session_state.tense_streak = 0
                st.error(f"❌ Incorrect. Correct answer was: **{st.session_state.tense_current_question['answer']}**")

    # --- Show Progress and Streak at the Bottom ---
    st.markdown("---")
    st.markdown(f"**Progress:** {st.session_state.tense_correct_count} correct out of {st.session_state.tense_total_attempts} attempts")
    st.markdown(f"🔥 **Current Streak:** {st.session_state.tense_streak}")
