import streamlit as st
import spacy

# =============================================================================
# CUSTOM CSS STYLING
# -----------------------------------------------------------------------------
# This block injects custom HTML and CSS styling into the app.
# It enhances the visual hierarchy by styling headers, footers, and hints.
# Useful for a cleaner, more professional UI.
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
st.markdown(
    """
    <style>
    /* Make Streamlit buttons gold and clean */
    div.stButton > button:first-child {
        background-color: #C99700;
        color: black;
        font-weight: 600;
        border-radius: 5px;
        border: none;
    }
    div.stButton > button:first-child:hover {
        background-color: #b58900;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =============================================================================
# SIDEBAR CONTENT
# -----------------------------------------------------------------------------
# This section populates the sidebar with:
# - Creator bio
# - Helpful navigation links
# - Embedded help section
# - Sample text options
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
    - **Home:** Main NER app  
    - **Documentation:** [spaCy EntityRuler](https://spacy.io/usage/rule-based-matching)  
    - **Portfolio:** [GitHub Portfolio](https://github.com/GooboGobbo/Edge-Python-Portfolio)
    """
)
st.sidebar.markdown("---")

# Collapsible help guide to assist users.
st.sidebar.expander("Help / Documentation", expanded=True).markdown(
    """
    **App Overview:**  
    This app uses spaCy's Named Entity Recognition (NER) and rule-based EntityRuler 
    to highlight named entities in your custom or uploaded text.

    **Steps to Use:**  
    1. Enter or upload text (or load a sample).  
    2. Optionally define custom entity rules.  
    3. Click "Run NER" to analyze the text.  
    4. View extracted entities, statistics, and highlighted output.
    """
)

# =============================================================================
# SAMPLE TEXT OPTIONS
# -----------------------------------------------------------------------------
# These are pre-loaded samples users can select to quickly test the app.
# Each one covers a different topic domain (e.g., politics, sports, tech).
# =============================================================================
sample_texts = {
    "Sample 1 - Obama & Politics": (
        "Barack Obama, the 44th President of the United States, delivered a stirring speech at Harvard University "
        "in Cambridge, Massachusetts. During his presidency, he focused heavily on healthcare reform and economic recovery, "
        "especially in urban centers like Chicago and New York City. In 2009, he received the Nobel Peace Prize."
    ),
    "Sample 2 - Sports & Entertainment": (
        "LeBron James led the Los Angeles Lakers to a win at Crypto.com Arena. Meanwhile, Taylor Swift performed in a sold-out "
        "concert at Madison Square Garden. Tom Brady made headlines as he announced his retirement from the NFL."
    ),
    "Sample 3 - Business & Tech": (
        "Google revealed a $2B investment in AI, partnering with Oxford University. Elon Musk and Satya Nadella gave talks at "
        "the TechFuture Summit, and Apple announced the Vision Pro headset from its Cupertino HQ."
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
# SESSION STATE INITIALIZATION
# -----------------------------------------------------------------------------
# These keys are used to persist user input and custom rules across interactions.
# They ensure the app doesn't lose data when it reruns after a button is clicked.
# =============================================================================
if "custom_patterns" not in st.session_state:
    st.session_state["custom_patterns"] = []

if "user_text" not in st.session_state:
    st.session_state["user_text"] = ""

# =============================================================================
# MAIN APP HEADER
# -----------------------------------------------------------------------------
# Displays the main title and subtitle with enhanced formatting.
# =============================================================================
st.markdown('<div class="big-header">🧠 Custom Named Entity Recognition App</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Built with spaCy and Streamlit</div>', unsafe_allow_html=True)

# =============================================================================
# MAIN INTERFACE: TWO-COLUMN LAYOUT
# -----------------------------------------------------------------------------
# Column 1: Input for user text (typed or uploaded)
# Column 2: Interface for defining and managing custom entity rules
# =============================================================================
col1, col2 = st.columns(2)

# ---------------- TEXT INPUT SECTION (LEFT COLUMN) ----------------
with col1:
    st.markdown("### Text Input")
    st.markdown('<p class="instruction">Enter or upload your text below.</p>', unsafe_allow_html=True)
    
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

# ---------------- CUSTOM RULES SECTION (RIGHT COLUMN) ----------------
with col2:
    st.markdown("### Custom Entity Rules (Optional)")
    st.markdown('<p class="instruction">Define a label and a matching phrase (e.g., "ORG" + "Notre Dame").</p>', unsafe_allow_html=True)
    
    rule_label = st.text_input("Entity Label", key="rule_label")
    rule_pattern = st.text_input("Entity Pattern", key="rule_pattern")

    # Add custom rule to session state
    if st.button("Add Custom Rule"):
        if rule_label.strip() and rule_pattern.strip():
            st.session_state.custom_patterns.append({"label": rule_label.strip(), "pattern": rule_pattern.strip()})
            st.success(f"Added rule: {rule_label.strip()} — {rule_pattern.strip()}")
        else:
            st.error("Both label and pattern fields are required.")

    # Display current rules in a collapsible section
    if st.session_state.custom_patterns:
        with st.expander("Current Custom Rules"):
            st.json(st.session_state.custom_patterns)

    # Clear all custom rules
    if st.button("Clear Custom Rules"):
        st.session_state.custom_patterns = []
        st.success("Cleared all custom rules.")

# =============================================================================
# SPA-CY MODEL LOADER
# -----------------------------------------------------------------------------
# This function loads the pre-trained English model.
# It assumes the model is already available (or will be downloaded via your deployment logic).
# =============================================================================
def load_model():
    return spacy.load("en_core_web_sm")

# =============================================================================
# ADD ENTITY RULER TO PIPELINE
# -----------------------------------------------------------------------------
# This function injects custom rules into the spaCy NLP pipeline.
# It first removes any existing EntityRuler, then adds a fresh one.
# =============================================================================
def add_entity_ruler(nlp, patterns):
    if "entity_ruler" in nlp.pipe_names:
        nlp.remove_pipe("entity_ruler")
    ruler = nlp.add_pipe("entity_ruler", before="ner")
    ruler.add_patterns(patterns)
    return nlp

# =============================================================================
# MAIN BUTTON: Run NER and Display Results
# -----------------------------------------------------------------------------
# When "Run NER" is clicked:
# - The model is loaded
# - Custom rules are applied (if any)
# - The text is processed
# - Entities and visualizations are displayed
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

            # ---- Display Recognized Entities (Split into Columns) ----
            st.markdown("### Recognized Entities")
            if doc.ents:
                entity_lines = [f"**{ent.text}** — `{ent.label_}`" for ent in doc.ents]
                mid = (len(entity_lines) + 1) // 2
                col1, col2 = st.columns(2)
                with col1:
                    for line in entity_lines[:mid]:
                        st.markdown(line)
                with col2:
                    for line in entity_lines[mid:]:
                        st.markdown(line)

                # ---- Entity Frequency Statistics (Sorted by Count Descending) ----
                stats = {}
                for ent in doc.ents:
                    stats[ent.label_] = stats.get(ent.label_, 0) + 1

                # Sort the stats dictionary by frequency (value) in descending order
                sorted_stats = dict(sorted(stats.items(), key=lambda item: item[1], reverse=True))

                # Convert to a format Streamlit can display cleanly as a table
                st.markdown("#### Entity Statistics")
                st.write(f"Total entities recognized: {len(doc.ents)}")
                st.table({"Entity Type": list(sorted_stats.keys()), "Count": list(sorted_stats.values())})

            else:
                st.info("No named entities were found.")

            # ---- Visualize Highlighted Text ----
            st.markdown("### Highlighted Text")
            html = spacy.displacy.render(doc, style="ent", jupyter=False)
            st.markdown(html, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"An error occurred while processing: {e}")

# =============================================================================
# FOOTER
# -----------------------------------------------------------------------------
# A simple footer to credit the course context.
# =============================================================================
st.markdown('<div class="footer">Developed as part of the Elements of Computing II course.</div>', unsafe_allow_html=True)
