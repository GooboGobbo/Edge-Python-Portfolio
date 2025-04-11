import streamlit as st
import spacy

# =============================================================================
# Custom CSS Styling
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
    </style>
    """,
    unsafe_allow_html=True
)

# =============================================================================
# Sidebar Content Setup
# =============================================================================
st.sidebar.markdown("## Navigation")
st.sidebar.markdown(
    """
    - **Home:** Main NER application.
    - **Documentation:** [spaCy EntityRuler](https://spacy.io/usage/rule-based-matching)
    - **Portfolio:** [My GitHub Portfolio](https://github.com/yourusername)
    """
)
st.sidebar.markdown("---")

st.sidebar.expander("Help / Documentation", expanded=True).markdown(
    """
    **Overview:**  
    This app uses spaCy's Named Entity Recognition (NER) along with custom rules from 
    the EntityRuler to highlight named entities in the text you provide.

    **How It Works:**  
    1. **Input:** You can type/paste text, upload a .txt file, or load one of the sample texts.  
    2. **Custom Rules:** Optionally, add custom entity rules by specifying a label (e.g., PERSON, ORG) 
       and a pattern (e.g., Barack Obama).  
    3. **Processing:** Click "Run NER" to analyze the text. Custom rules (if any) are integrated into 
       spaCy's pipeline.
    4. **Output:** View the recognized entities, a breakdown of entity statistics, and the text with highlighted annotations.

    **Notes:**  
    - Please ensure custom rules are entered correctly for the expected results.
    """
)
st.sidebar.markdown("---")

sample_texts = {
    "Sample 1 - Obama & Politics": (
        "Barack Obama, the 44th President of the United States, delivered a stirring speech "
        "at Harvard University in Cambridge, Massachusetts. During his term, he focused on topics "
        "like healthcare reform and economic recovery in cities like Chicago and New York. His efforts "
        "sparked conversations globally, influencing political debates in countries such as Canada and Germany."
    ),
    "Sample 2 - Sports & Entertainment": (
        "At the Los Angeles Lakers game, star players like LeBron James and Anthony Davis showcased "
        "their incredible skills. The match was held at the Staples Center, drawing fans from across California. "
        "Later that evening, the New York Yankees celebrated a spectacular win in baseball, highlighted by the performance "
        "of their top hitters in a packed stadium in New York City."
    ),
    "Sample 3 - Mixed Domains": (
        "In a remarkable event in London, tech giant Google announced its latest innovations in artificial intelligence. "
        "The conference, which also featured keynote speeches by Elon Musk and Satya Nadella, blended technology, politics, "
        "and entertainment. Meanwhile, the local football team, Manchester United, enjoyed unprecedented support as they clinched "
        "an important victory, making headlines worldwide."
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
# =============================================================================
if "custom_patterns" not in st.session_state:
    st.session_state["custom_patterns"] = []

if "user_text" not in st.session_state:
    st.session_state["user_text"] = ""

# =============================================================================
# Main Page Title and Header
# =============================================================================
st.markdown('<div class="big-header">🧠 Custom Named Entity Recognition App</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Built with spaCy and Streamlit</div>', unsafe_allow_html=True)

# =============================================================================
# Layout: Two Columns for Input & Custom Rules
# =============================================================================
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Text Input")
    st.markdown('<p class="instruction">Enter or load text to run Named Entity Recognition.</p>', unsafe_allow_html=True)
    input_method = st.radio("Choose Input Method", ["Type or Paste Text", "Upload Text File (.txt)"])
    if input_method == "Type or Paste Text":
        user_text = st.text_area(
            "Enter Text Here",
            height=300,
            placeholder="Paste or type your text here...",
            value=st.session_state["user_text"],
            key="user_text"
        )
    else:
        uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
        if uploaded_file is not None:
            user_text = uploaded_file.read().decode("utf-8")
            st.session_state.user_text = user_text
        else:
            user_text = st.session_state.user_text

with col2:
    st.markdown("### Custom Entity Rules (Optional)")
    st.markdown('<p class="instruction">Add custom rules to supplement the default NER. '
                'Enter an entity label (e.g., PERSON, ORG) and a pattern (e.g., Barack Obama) below.</p>',
                unsafe_allow_html=True)
    rule_label = st.text_input("Entity Label (e.g., PERSON, ORG)", key="rule_label")
    rule_pattern = st.text_input("Entity Pattern (e.g., Barack Obama, Notre Dame)", key="rule_pattern")
    if st.button("Add Custom Rule"):
        if rule_label.strip() and rule_pattern.strip():
            new_rule = {"label": rule_label.strip(), "pattern": rule_pattern.strip()}
            st.session_state.custom_patterns.append(new_rule)
            st.success(f"Added custom rule: {new_rule}")
        else:
            st.error("Please provide both a label and a pattern.")
    if st.session_state.custom_patterns:
        with st.expander("Current Custom Rules"):
            st.json(st.session_state.custom_patterns)
    if st.button("Clear Custom Rules"):
        st.session_state.custom_patterns = []
        st.success("Cleared all custom rules.")

# =============================================================================
# Load spaCy Model
# =============================================================================
def load_model():
    return spacy.load("en_core_web_sm")

# =============================================================================
# Add Entity Ruler
# =============================================================================
def add_entity_ruler(nlp, patterns):
    if "entity_ruler" in nlp.pipe_names:
        nlp.remove_pipe("entity_ruler")
    ruler = nlp.add_pipe("entity_ruler", before="ner")
    ruler.add_patterns(patterns)
    return nlp

# =============================================================================
# Run NER
# =============================================================================
if st.button("Run NER"):
    if not st.session_state.user_text.strip():
        st.warning("Please enter some text before running NER.")
    else:
        try:
            nlp = load_model()
            if st.session_state.custom_patterns:
                nlp = add_entity_ruler(nlp, st.session_state.custom_patterns)
            with st.spinner("Processing text with spaCy..."):
                doc = nlp(st.session_state.user_text)
            st.markdown("### Recognized Entities")
            if doc.ents:
                entities = [f"**{ent.text}** — {ent.label_}" for ent in doc.ents]
                mid_index = (len(entities) + 1) // 2
                col_entities1, col_entities2 = st.columns(2)
                with col_entities1:
                    for ent_info in entities[:mid_index]:
                        st.write(ent_info)
                with col_entities2:
                    for ent_info in entities[mid_index:]:
                        st.write(ent_info)
                stats = {}
                for ent in doc.ents:
                    stats[ent.label_] = stats.get(ent.label_, 0) + 1
                st.markdown("#### Entity Statistics")
                st.write("Total entities recognized:", len(doc.ents))
                st.table(stats)
            else:
                st.info("No entities recognized in the provided text.")
            st.markdown("### Highlighted Text")
            html = spacy.displacy.render(doc, style="ent", jupyter=False)
            st.markdown(html, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"An error occurred: {e}")

# =============================================================================
# Footer
# =============================================================================
st.markdown('<div class="footer">Developed as part of the Elements of Computing II course.</div>', unsafe_allow_html=True)
