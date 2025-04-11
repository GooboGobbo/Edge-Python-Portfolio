import streamlit as st
import spacy

import os
os.environ["SPACY_DATA"] = "/tmp"

import spacy
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")


# =============================================================================
# Custom CSS Styling
# -----------------------------------------------------------------------------
# The following markdown block injects custom CSS into your app.
# This CSS customizes the header fonts, subtitle colors, instruction text,
# and the footer appearance.
# =============================================================================
st.markdown(
    """
    <style>
    .big-header {
        font-size: 2.5em;         /* Makes the main header large and bold */
        font-weight: bold;
        margin-bottom: 0;         /* No margin below the header */
    }
    .sub-header {
        font-size: 1.2em;         /* Slightly smaller subtitle text */
        color: #555;              /* A medium gray for the subtitle */
        margin-bottom: 20px;      /* Space below the subtitle */
    }
    .instruction {
        font-size: 0.9em;         /* Smaller text for instructions */
        color: #666;              /* A slightly lighter gray */
    }
    .footer {
        text-align: center;       /* Center-align footer text */
        font-size: 0.8em;         /* Small text in the footer */
        color: #aaa;              /* Light gray color for footer */
        margin-top: 40px;         /* Space above the footer */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =============================================================================
# Sidebar Content Setup
# -----------------------------------------------------------------------------
# The sidebar includes navigation, external links, a help/documentation section,
# sample texts for testing the app, and a version indicator.
#
# Benefits of having help in the sidebar:
# - It's always visible (or easily expandable), so users can refer to it
#   without scrolling away from the main interface.
# - It keeps the main page less cluttered.
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

# -----------------------------------------------------------------------------
# Help / Documentation in the Sidebar
# -----------------------------------------------------------------------------
# The help documentation is included inside an expander in the sidebar so it
# can be collapsed when not needed.
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
    - The spaCy model is cached to improve performance.
    """
)
st.sidebar.markdown("---")

# -----------------------------------------------------------------------------
# Sample Texts for Testing
# -----------------------------------------------------------------------------
# Here, we provide three sample texts containing several Named Entities.
# Users can choose a sample from the selectbox and load it into the text input.
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
# -----------------------------------------------------------------------------
# We use Streamlit's session_state to maintain the current text input (user_text)
# and any custom entity rules (custom_patterns) the user adds. This ensures 
# consistency when refreshing the page or updating inputs.
# =============================================================================
if "custom_patterns" not in st.session_state:
    st.session_state["custom_patterns"] = []

if "user_text" not in st.session_state:
    st.session_state["user_text"] = ""

# =============================================================================
# Main Page Title and Header
# -----------------------------------------------------------------------------
# Display the main title and a subtitle using HTML for styling.
# =============================================================================
st.markdown('<div class="big-header">🧠 Custom Named Entity Recognition App</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Built with spaCy and Streamlit</div>', unsafe_allow_html=True)

# =============================================================================
# Layout: Two Columns for Input & Custom Rules
# -----------------------------------------------------------------------------
# The main interface is split into two columns:
# - Left Column: Text input area for entering or uploading text.
# - Right Column: Input fields for adding custom entity rules.
# =============================================================================
col1, col2 = st.columns(2)

# ---------------------------- Left Column: Text Input ----------------------
with col1:
    st.markdown("### Text Input")
    st.markdown('<p class="instruction">Enter or load text to run Named Entity Recognition.</p>', unsafe_allow_html=True)
    
    # Radio buttons allow the user to choose between entering text directly or uploading a file.
    input_method = st.radio("Choose Input Method", ["Type or Paste Text", "Upload Text File (.txt)"])
    
    if input_method == "Type or Paste Text":
        # The text area shows the current text stored in session_state.
        user_text = st.text_area(
            "Enter Text Here",
            height=300,
            placeholder="Paste or type your text here...",
            value=st.session_state["user_text"],
            key="user_text"
        )
    else:
        # If the user selects file upload, read the file and update the session state's user_text.
        uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
        if uploaded_file is not None:
            user_text = uploaded_file.read().decode("utf-8")
            st.session_state.user_text = user_text
        else:
            user_text = st.session_state.user_text

# ---------------------------- Right Column: Custom Entity Rules -----------------
with col2:
    st.markdown("### Custom Entity Rules (Optional)")
    st.markdown('<p class="instruction">Add custom rules to supplement the default NER. '
                'Enter an entity label (e.g., PERSON, ORG) and a pattern (e.g., Barack Obama) below.</p>',
                unsafe_allow_html=True)
    
    # Text input fields to capture the entity label and pattern.
    rule_label = st.text_input("Entity Label (e.g., PERSON, ORG)", key="rule_label")
    rule_pattern = st.text_input("Entity Pattern (e.g., Barack Obama, Notre Dame)", key="rule_pattern")
    
    # When the "Add Custom Rule" button is clicked, check that both inputs are non-empty,
    # then add the new rule to session_state.custom_patterns.
    if st.button("Add Custom Rule"):
        if rule_label.strip() and rule_pattern.strip():
            new_rule = {"label": rule_label.strip(), "pattern": rule_pattern.strip()}
            st.session_state.custom_patterns.append(new_rule)
            st.success(f"Added custom rule: {new_rule}")
        else:
            st.error("Please provide both a label and a pattern.")
    
    # Display the current custom rules in a collapsible (expander) section.
    if st.session_state.custom_patterns:
        with st.expander("Current Custom Rules"):
            st.json(st.session_state.custom_patterns)
    
    # Button to clear all custom rules.
    if st.button("Clear Custom Rules"):
        st.session_state.custom_patterns = []
        st.success("Cleared all custom rules.")

# =============================================================================
# Load spaCy Model with Caching
# -----------------------------------------------------------------------------
# The following function loads the spaCy model and caches it to improve performance.
# This avoids reloading the model on every run.
# =============================================================================
@st.cache_resource
def load_model():
    """
    Load and return the English spaCy model.
    This model is cached to improve performance across app reruns.
    """
    return spacy.load("en_core_web_sm")

# =============================================================================
# Update spaCy Pipeline with Custom EntityRuler
# -----------------------------------------------------------------------------
# If the user has added custom rules, this function adds an EntityRuler component
# to the spaCy pipeline with the specified patterns.
# =============================================================================
def add_entity_ruler(nlp, patterns):
    """
    Add an EntityRuler to the spaCy pipeline using user-defined patterns.
    
    Parameters:
        nlp (Language): The loaded spaCy model.
        patterns (list): A list of dictionaries where each dictionary contains
                         a "label" and a "pattern" key.
    
    Returns:
        The updated spaCy model with the custom EntityRuler added.
    """
    if "entity_ruler" in nlp.pipe_names:
        nlp.remove_pipe("entity_ruler")
    ruler = nlp.add_pipe("entity_ruler", before="ner")
    ruler.add_patterns(patterns)
    return nlp

# =============================================================================
# Main Execution Block: Running Named Entity Recognition
# -----------------------------------------------------------------------------
# When the "Run NER" button is clicked:
# 1. It verifies that text has been entered.
# 2. Loads the spaCy model (with caching).
# 3. Integrates any custom entity rules via the EntityRuler.
# 4. Processes the input text to recognize entities.
# 5. Displays the recognized entities in two columns.
# 6. Computes and displays statistics (counts per entity type).
# 7. Shows the annotated text with highlighted entities.
# =============================================================================
if st.button("Run NER"):
    if not st.session_state.user_text.strip():
        st.warning("Please enter some text before running NER.")
    else:
        try:
            # Load the spaCy model.
            nlp = load_model()
            
            # Integrate custom entity rules if any exist.
            if st.session_state.custom_patterns:
                nlp = add_entity_ruler(nlp, st.session_state.custom_patterns)
            
            # Process the input text using spaCy.
            with st.spinner("Processing text with spaCy..."):
                doc = nlp(st.session_state.user_text)
            
            # -------------------- Display Recognized Entities --------------------
            st.markdown("### Recognized Entities")
            if doc.ents:
                # Prepare a list of strings for each recognized entity.
                entities = [f"**{ent.text}** — `{ent.label_}`" for ent in doc.ents]
                # Calculate the midpoint to split the list into two nearly equal halves.
                mid_index = (len(entities) + 1) // 2
                # Create two columns to display the entities side-by-side.
                col_entities1, col_entities2 = st.columns(2)
                with col_entities1:
                    for ent_info in entities[:mid_index]:
                        st.write(ent_info)
                with col_entities2:
                    for ent_info in entities[mid_index:]:
                        st.write(ent_info)
                
                # ---------------- Responsive Feedback: Entity Statistics ----------------
                # Count the number of occurrences for each entity type.
                stats = {}
                for ent in doc.ents:
                    stats[ent.label_] = stats.get(ent.label_, 0) + 1
                st.markdown("#### Entity Statistics")
                st.write("Total entities recognized:", len(doc.ents))
                st.table(stats)
            else:
                st.info("No entities recognized in the provided text.")
            
            # -------------------- Display Highlighted Text --------------------
            # Use spaCy's displaCy to generate HTML with highlighted entities.
            st.markdown("### Highlighted Text")
            html = spacy.displacy.render(doc, style="ent", jupyter=False)
            st.markdown(html, unsafe_allow_html=True)
        
        except Exception as e:
            st.error(f"An error occurred: {e}")

# =============================================================================
# Footer
# -----------------------------------------------------------------------------
# Finally, the footer credits the course and provides a final visual cue.
# =============================================================================
st.markdown('<div class="footer">Developed as part of the Elements of Computing II course.</div>', unsafe_allow_html=True)
