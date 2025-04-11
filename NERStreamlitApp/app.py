import streamlit as st
import spacy

# =============================================================================
# Custom CSS Styling
# -----------------------------------------------------------------------------
# This section customizes the visual style of your app, including headers,
# instructions, footer, and a green highlight for recognized named entities.
# =============================================================================
st.markdown(
    """
    <style>
    .big-header {
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 0;
    }
    .sub-header {
        font-size: 1.2em;
        color: #555;
        margin-bottom: 20px;
    }
    .instruction {
        font-size: 0.9em;
        color: #666;
    }
    .footer {
        text-align: center;
        font-size: 0.8em;
        color: #aaa;
        margin-top: 40px;
    }
    .ner-highlight {
        background-color: #d4edda;
        border-radius: 4px;
        padding: 2px 6px;
        margin-bottom: 4px;
        display: inline-block;
        font-weight: 600;
        color: #155724;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =============================================================================
# Sidebar: Creator Info & Navigation
# -----------------------------------------------------------------------------
# This section personalizes the app and provides helpful links and documentation.
# =============================================================================
st.sidebar.markdown("## 👤 Creator")
st.sidebar.markdown("""
**James Edge**  
University of Notre Dame  
Studying Finance and Real Estate
""")
st.sidebar.markdown("---")

st.sidebar.markdown("## Navigation")
st.sidebar.markdown(
    """
    - **Home:** Main NER application  
    - **Documentation:** [spaCy EntityRuler](https://spacy.io/usage/rule-based-matching)  
    - **Portfolio:** [My GitHub Portfolio](https://github.com/GooboGobbo/Edge-Python-Portfolio)
    """
)
st.sidebar.markdown("---")

st.sidebar.expander("Help / Documentation", expanded=True).markdown(
    """
    **Overview:**  
    This app uses spaCy's Named Entity Recognition (NER) along with custom rules from 
    the EntityRuler to highlight named entities in your text.

    **Steps:**  
    1. Input text manually, upload a .txt file, or load a sample  
    2. Optionally define custom entity rules  
    3. Click "Run NER"  
    4. View recognized entities and statistics  
    """
)
st.sidebar.markdown("---")

# =============================================================================
# Sidebar: Sample Texts
# -----------------------------------------------------------------------------
# Predefined sample texts for quick testing and demonstration.
# =============================================================================
sample_texts = {
    "Sample 1 - Obama & Politics": (
        "Barack Obama, the 44th President of the United States, delivered a stirring speech at Harvard University "
        "in Cambridge, Massachusetts. During his presidency, Obama focused heavily on healthcare reform and economic recovery, "
        "especially in urban centers such as Chicago and New York City. He also met with leaders from countries like Germany, "
        "Canada, and Japan to discuss international diplomacy. In 2009, he was awarded the Nobel Peace Prize. His administration's "
        "initiatives were frequently covered by media outlets like CNN, The Washington Post, and BBC News."
    ),

    "Sample 2 - Sports & Entertainment": (
        "At the Los Angeles Lakers' home game at the Crypto.com Arena, LeBron James and Anthony Davis led a thrilling comeback "
        "against the Golden State Warriors. ESPN commentators praised their teamwork and leadership. Earlier that weekend, "
        "Taylor Swift performed at Madison Square Garden in New York City as part of her sold-out Eras Tour, drawing fans from "
        "across the globe. Meanwhile, Tom Brady officially announced his retirement from the NFL during a live interview with NBC Sports."
    ),

    "Sample 3 - Business & Tech": (
        "In London, Google announced a $2 billion investment in AI research, partnering with Oxford University and several British tech firms. "
        "The announcement was made at the TechFuture Global Summit, where CEOs like Elon Musk (Tesla, SpaceX) and Satya Nadella (Microsoft) "
        "shared their visions for ethical innovation. Apple also unveiled its new Vision Pro headset during a livestream from Cupertino, "
        "California. The event trended globally on Twitter and LinkedIn, with analysts at Bloomberg predicting a surge in market valuation."
    )
}
st.sidebar.markdown("## Sample Texts")
selected_sample = st.sidebar.selectbox("Choose a sample text", list(sample_texts.keys()))
if st.sidebar.button("Load Sample Text"):
    st.session_state["user_text"] = sample_texts[selected_sample]
    st.sidebar.success("Sample text loaded!")

st.sidebar.markdown("---")
st.sidebar.markdown("**App Version 1.0**")

# =============================================================================
# Session State Setup
# -----------------------------------------------------------------------------
# Used to persist text input and custom rules across reruns.
# =============================================================================
if "custom_patterns" not in st.session_state:
    st.session_state["custom_patterns"] = []

if "user_text" not in st.session_state:
    st.session_state["user_text"] = ""

# =============================================================================
# Main Title
# -----------------------------------------------------------------------------
st.markdown('<div class="big-header">🧠 Custom Named Entity Recognition App</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Built with spaCy and Streamlit</div>', unsafe_allow_html=True)

# =============================================================================
# Layout: Text Input (Left) + Entity Rule Builder (Right)
# =============================================================================
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Text Input")
    st.markdown('<p class="instruction">Enter or upload the text you want to analyze.</p>', unsafe_allow_html=True)
    
    input_method = st.radio("Choose Input Method", ["Type or Paste Text", "Upload Text File (.txt)"])
    
    if input_method == "Type or Paste Text":
        user_text = st.text_area("Enter Text Here", height=300, value=st.session_state["user_text"], key="user_text")
    else:
        uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
        if uploaded_file:
            user_text = uploaded_file.read().decode("utf-8")
            st.session_state.user_text = user_text
        else:
            user_text = st.session_state.user_text

with col2:
    st.markdown("### Custom Entity Rules (Optional)")
    st.markdown('<p class="instruction">Define your own label (e.g., PERSON) and text pattern.</p>', unsafe_allow_html=True)

    rule_label = st.text_input("Entity Label (e.g., PERSON, ORG)", key="rule_label")
    rule_pattern = st.text_input("Entity Pattern (e.g., Barack Obama)", key="rule_pattern")

    if st.button("Add Custom Rule"):
        if rule_label.strip() and rule_pattern.strip():
            st.session_state.custom_patterns.append({"label": rule_label.strip(), "pattern": rule_pattern.strip()})
            st.success(f"Added rule: {rule_label.strip()} — {rule_pattern.strip()}")
        else:
            st.error("Both fields are required.")
    
    if st.session_state.custom_patterns:
        with st.expander("Current Custom Rules"):
            st.json(st.session_state.custom_patterns)

    if st.button("Clear Custom Rules"):
        st.session_state.custom_patterns = []
        st.success("Cleared all custom rules.")

# =============================================================================
# Load spaCy model (No caching used)
# =============================================================================
def load_model():
    return spacy.load("en_core_web_sm")

# =============================================================================
# Add custom patterns to spaCy's EntityRuler
# =============================================================================
def add_entity_ruler(nlp, patterns):
    if "entity_ruler" in nlp.pipe_names:
        nlp.remove_pipe("entity_ruler")
    ruler = nlp.add_pipe("entity_ruler", before="ner")
    ruler.add_patterns(patterns)
    return nlp

# =============================================================================
# NER Execution and Display
# =============================================================================
if st.button("Run NER"):
    if not st.session_state.user_text.strip():
        st.warning("Please enter some text.")
    else:
        try:
            nlp = load_model()
            if st.session_state.custom_patterns:
                nlp = add_entity_ruler(nlp, st.session_state.custom_patterns)
            with st.spinner("Analyzing text..."):
                doc = nlp(st.session_state.user_text)
            
            st.markdown("### Recognized Entities")
            if doc.ents:
                entities = [f'<span class="ner-highlight">{ent.text}</span> <code>{ent.label_}</code>' for ent in doc.ents]
                mid = (len(entities) + 1) // 2
                col1, col2 = st.columns(2)
                with col1:
                    for ent in entities[:mid]:
                        st.markdown(ent, unsafe_allow_html=True)
                with col2:
                    for ent in entities[mid:]:
                        st.markdown(ent, unsafe_allow_html=True)

                # Show entity statistics
                stats = {}
                for ent in doc.ents:
                    stats[ent.label_] = stats.get(ent.label_, 0) + 1
                st.markdown("#### Entity Statistics")
                st.write("Total entities recognized:", len(doc.ents))
                st.table(stats)
            else:
                st.info("No entities recognized.")

            # DisplaCy Highlighted Text
            st.markdown("### Highlighted Text")
            html = spacy.displacy.render(doc, style="ent", jupyter=False)
            st.markdown(html, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"An error occurred: {e}")

# =============================================================================
# Footer
# =============================================================================
st.markdown('<div class="footer">Developed as part of the Elements of Computing II course.</div>', unsafe_allow_html=True)

