import streamlit as st
import spacy

# =============================================================================
# Session State Setup for Custom Patterns
# -----------------------------------------------------------------------------
# We use Streamlit's session_state to keep track of all custom patterns added 
# by the user. This allows the list to persist during the session.
# =============================================================================
if "custom_patterns" not in st.session_state:
    st.session_state["custom_patterns"] = []

# =============================================================================
# Title and Header
# -----------------------------------------------------------------------------
# These lines set up the main heading and subheading of the application.
# =============================================================================
st.title("🧠 Custom Named Entity Recognition App")
st.subheader("Built with spaCy and Streamlit")

# =============================================================================
# Sidebar: Input Method Selection
# -----------------------------------------------------------------------------
# This sidebar lets users choose between typing/pasting text or uploading
# a .txt file. The selected method determines how text is provided.
# =============================================================================
input_method = st.sidebar.radio("Choose Input Method", 
                                ["Type or Paste Text", "Upload Text File (.txt)"])

# =============================================================================
# Text Input Section
# -----------------------------------------------------------------------------
# Depending on the selected method, this part either displays a text area or
# a file uploader. The text from the file (if uploaded) is read and decoded.
# =============================================================================
if input_method == "Type or Paste Text":
    user_text = st.text_area("Enter Text Here", height=300, 
                             placeholder="Paste or type your text here...")
else:
    uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
    if uploaded_file is not None:
        user_text = uploaded_file.read().decode("utf-8")
    else:
        user_text = ""

# =============================================================================
# Custom Entity Patterns Section (Interactive)
# -----------------------------------------------------------------------------
# Instead of forcing the user to type a full JSON list, we provide individual
# input fields for the entity label and its respective pattern.
#
# The inputs are wrapped in an expander for a cleaner interface. Users can:
# - Enter a label and pattern.
# - Click "Add Custom Rule" to append this rule to the stored list.
# - View the current list of custom rules.
# - Optionally clear all rules with "Clear Custom Rules".
# =============================================================================
st.markdown("### 🔧 Add Custom Entity Patterns (Optional)")
with st.expander("Add Custom Entity Rules"):
    # Input for the entity label (e.g., PERSON, ORG)
    rule_label = st.text_input("Entity Label (e.g., PERSON, ORG)", key="rule_label")
    # Input for the entity pattern (e.g., Barack Obama, Notre Dame)
    rule_pattern = st.text_input("Entity Pattern (e.g., Barack Obama, Notre Dame)", key="rule_pattern")
    
    # When the "Add Custom Rule" button is clicked, add the new rule if both inputs
    # are provided. Otherwise, display an error message.
    if st.button("Add Custom Rule", key="add_rule_button"):
        if rule_label.strip() and rule_pattern.strip():
            new_rule = {"label": rule_label.strip(), "pattern": rule_pattern.strip()}
            st.session_state.custom_patterns.append(new_rule)
            st.success(f"Added custom rule: {new_rule}")
        else:
            st.error("Please provide both a label and a pattern.")
    
    # Display the current list of custom rules, if any, as a JSON for clarity.
    if st.session_state.custom_patterns:
        st.markdown("#### Current Custom Rules")
        st.json(st.session_state.custom_patterns)
    
    # Optional button to clear all custom rules
    if st.button("Clear Custom Rules", key="clear_button"):
        st.session_state.custom_patterns = []
        st.success("Cleared all custom rules.")

# =============================================================================
# Function: load_model
# -----------------------------------------------------------------------------
# This function loads and caches the spaCy model for efficiency. By caching,
# we avoid reloading the model on every script run, which speeds up the app.
# =============================================================================
@st.cache_resource
def load_model():
    """
    Load and return the English spaCy model.
    This function uses caching to avoid reloading the model on every run.
    """
    return spacy.load("en_core_web_sm")

# =============================================================================
# Function: add_entity_ruler
# -----------------------------------------------------------------------------
# This function adds an EntityRuler to the spaCy pipeline with the custom
# patterns provided by the user.
#
# It first removes any existing EntityRuler to prevent duplicate entries, then
# adds a new one before the built-in NER component.
# =============================================================================
def add_entity_ruler(nlp, patterns):
    """
    Add an EntityRuler to the spaCy pipeline with custom patterns.
    
    Parameters:
    - nlp: The spaCy language model.
    - patterns: A list of dictionaries, each with a "label" and "pattern".
    
    Returns:
    - The updated spaCy model with the new EntityRuler added.
    """
    if "entity_ruler" in nlp.pipe_names:
        nlp.remove_pipe("entity_ruler")
    ruler = nlp.add_pipe("entity_ruler", before="ner")
    ruler.add_patterns(patterns)
    return nlp

# =============================================================================
# Main Execution Block: Run NER
# -----------------------------------------------------------------------------
# When the "Run NER" button is clicked:
# 1. Verify that there is input text.
# 2. Load the spaCy model (using caching).
# 3. If there are any custom rules in session_state, add them via the
#    EntityRuler.
# 4. Process the input text.
# 5. Display the recognized entities and the highlighted text output.
# =============================================================================
if st.button("Run NER"):
    if not user_text.strip():
        st.warning("Please enter the text.")
    else:
        try:
            # Load spaCy model with caching.
            nlp = load_model()

            # If custom patterns exist in session_state, update the pipeline.
            if st.session_state.custom_patterns:
                nlp = add_entity_ruler(nlp, st.session_state.custom_patterns)
            
            # Process the input text with a spinner showing progress.
            with st.spinner("Processing text with spaCy..."):
                doc = nlp(user_text)
            
            # ---------------------------------------------------------------------
            # Output Section 1: Display Recognized Entities
            # ---------------------------------------------------------------------
            st.markdown("### 📍 Recognized Entities")
            if doc.ents:
                for ent in doc.ents:
                    st.write(f"**{ent.text}** — `{ent.label_}`")
            else:
                st.info("No entities recognized in the text.")
            
            # ---------------------------------------------------------------------
            # Output Section 2: Highlighted Text Using displaCy
            # ---------------------------------------------------------------------
            st.markdown("### 🎨 Highlighted Text")
            # Generate HTML with displaCy for visual highlighting of entities.
            html = spacy.displacy.render(doc, style="ent", jupyter=False)
            st.markdown(html, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"⚠️ Error: {e}")

# =============================================================================
# Sidebar: Example Custom Rule
# -----------------------------------------------------------------------------
# This sidebar snippet provides an example of a custom rule to guide the user.
# =============================================================================
st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Example Custom Rule")
st.sidebar.code('{"label": "PERSON", "pattern": "Barack Obama"}')
