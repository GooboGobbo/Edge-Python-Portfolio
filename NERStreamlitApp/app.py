import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
import pandas as pd
import json

# --- Title ---
st.title("🧠 Custom Named Entity Recognition App")
st.subheader("Built with spaCy and Streamlit")

# --- Sidebar: Input method ---
input_method = st.sidebar.radio("Choose Input Method", ["Type or Paste Text", "Upload Text File (.txt)"])

# --- Upload or input text ---
if input_method == "Type or Paste Text":
    user_text = st.text_area("Enter Text Here", height=300, placeholder="Paste or type your text here...")
else:
    uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
    if uploaded_file is not None:
        user_text = uploaded_file.read().decode("utf-8")
    else:
        user_text = ""

# --- Pattern Input ---
st.markdown("### 🔧 Add Custom Entity Patterns")
st.markdown("Patterns should be in this format:")
st.code('[{"label": "ORG", "pattern": "Notre Dame"}, {"label": "SPORT", "pattern": "swimming"}]', language="json")

pattern_input = st.text_area("Paste pattern list (JSON format)", height=200)

# --- Load spaCy + Apply Patterns ---
if st.button("Run NER"):
    if user_text and pattern_input:
        try:
            # Load spaCy model
            nlp = spacy.load("en_core_web_sm")

            # Add EntityRuler
            ruler = nlp.add_pipe("entity_ruler", before="ner")
            patterns = json.loads(pattern_input)
            ruler.add_patterns(patterns)

            # Process text
            doc = nlp(user_text)

            # Display results
            st.markdown("### 📍 Recognized Entities")
            for ent in doc.ents:
                st.write(f"**{ent.text}** — `{ent.label_}`")

            # Display with highlight
            st.markdown("### 🎨 Highlighted Text")
            st.markdown(spacy.displacy.render(doc, style="ent", jupyter=False), unsafe_allow_html=True)

        except Exception as e:
            st.error(f"⚠️ Error: {e}")
    else:
        st.warning("Please enter both text and entity patterns.")

# --- Sample patterns ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Example Patterns")
st.sidebar.code('[{"label": "PERSON", "pattern": "Barack Obama"}]')
