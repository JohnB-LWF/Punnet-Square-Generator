"""Streamlit-based Punnett Square Generator with polished UI.
Maintains functionality from punnetsquare.py with modern web interface.
"""

import streamlit as st
from streamlit_utils import (
    normalize_genotype,
    calculate_punnett_square,
    calculate_phenotype_percentages,
)

# Configure Streamlit page
st.set_page_config(
    page_title="Punnett Square Generator",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for styling - Modern Science-Inspired Light Theme
st.markdown(
    """
    <style>
    /* Main background - clean off-white */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #f5f8fb 0%, #f0f4f8 100%);
    }
    
    [data-testid="stHeader"] {
        background: linear-gradient(135deg, #f5f8fb 0%, #f0f4f8 100%);
    }
    
    /* Input boxes - white with teal border */
    [data-testid="stTextInput"] > div > div > input {
        background-color: #ffffff !important;
        color: #2c3e50 !important;
        
        padding: 12px !important;
        font-size: 16px !important;
        box-shadow: none !important;
        outline: none !important;
    }
    
    [data-testid="stTextInput"] > div > div > input:focus {
        border: 2px solid #d4e8e4 !important;
        box-shadow: none !important;
        outline: none !important;
    }
    
    [data-testid="stTextInput"] > div > div > input:hover {
        border: 2px solid #d4e8e4 !important;
        box-shadow: none !important;
    }
    
    /* Labels - science-inspired teal text */
    [data-testid="stTextInput"] > label {
        background-color: transparent !important;
        color: #2e9d7a !important;
        padding: 0px !important;
        border-radius: 0px !important;
        margin-bottom: 8px !important;
        display: block !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        letter-spacing: 0.3px !important;
    }
    
    /* Column containers for input boxes */
    [data-testid="column"] {
        background-color: transparent !important;
        border-radius: 0 !important;
        padding: 0 !important;
        box-shadow: none !important;
        transition: none;
    }
    
    [data-testid="column"]:hover {
        box-shadow: none !important;
    }
    
    /* Title styling - modern gradient */
    h1 {
        background: linear-gradient(135deg, #2e9d7a 0%, #48b596 100%) !important;
        color: #ffffff !important;
        text-align: center !important;
        margin-bottom: 30px !important;
        padding: 25px !important;
        border-radius: 15px !important;
        box-shadow: 0 6px 20px rgba(46, 157, 122, 0.2) !important;
        letter-spacing: 0.5px !important;
    }
    
    h2 {
        background: transparent !important;
        color: #2e9d7a !important;
        margin-top: 30px !important;
        margin-bottom: 15px !important;
        padding: 10px 0px !important;
        border-bottom: 3px solid #d4e8e4 !important;
        border-radius: 0px !important;
        font-weight: 700 !important;
        letter-spacing: 0.3px !important;
    }
    
    /* Result boxes */
    [data-testid="stContainer"] {
        background-color: rgba(46, 157, 122, 0.08);
        border-left: 5px solid #2e9d7a;
        padding: 20px !important;
        border-radius: 12px !important;
        box-shadow: 0 2px 8px rgba(46, 157, 122, 0.1) !important;
    }
    
    /* Button styling - teal modern button */
    button {
        background: linear-gradient(135deg, #2e9d7a 0%, #48b596 100%) !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 14px 30px !important;
        font-weight: 600 !important;
        border: none !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(46, 157, 122, 0.25) !important;
        letter-spacing: 0.5px !important;
        text-transform: uppercase !important;
        font-size: 14px !important;
    }
    
    button:hover {
        background: linear-gradient(135deg, #257560 0%, #348a73 100%) !important;
        box-shadow: 0 6px 18px rgba(46, 157, 122, 0.35) !important;
        transform: translateY(-2px) !important;
    }
    
    button:active {
        transform: translateY(0px) !important;
    }
    
    /* Punnett Square display - elegant white card */
    .punnett-square {
        background-color: #ffffff !important;
        color: #2c3e50 !important;
        padding: 30px !important;
        border-radius: 15px !important;
        font-family: monospace;
        font-size: 20px;
        line-height: 2;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 6px 20px rgba(46, 157, 122, 0.12) !important;
        border: 2px solid #d4e8e4 !important;
    }
    
    /* Phenotype results - clean card styling */
    .phenotype-results {
        background-color: #ffffff !important;
        color: #2c3e50 !important;
        padding: 25px !important;
        border-radius: 15px !important;
        font-size: 18px;
        line-height: 2.5;
        margin-top: 20px;
        box-shadow: 0 6px 20px rgba(46, 157, 122, 0.12) !important;
        border: 2px solid #d4e8e4 !important;
    }
    
    /* Error messages - modern styling */
    .stAlert {
        background-color: #fff5f5 !important;
        border: 2px solid #f8a5a5 !important;
        border-radius: 12px !important;
        color: #d32f2f !important;
    }
    
    /* Text styling improvements */
    body {
        color: #2c3e50 !important;
    }
    
    /* Smooth transitions throughout */
    * {
        transition: all 0.3s ease !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown("# 🧬 Punnett Square Generator")

# Initialize session state for inputs
if "generate_clicked" not in st.session_state:
    st.session_state.generate_clicked = False

# Input section
st.markdown("## Input Your Genetic Data")

# Create columns for better layout
col1, col2 = st.columns(2)

with col1:
    dominant_allele = st.text_input(
        "🔤 Dominant Allele Symbol",
        value="H",
        max_chars=1,
    )
with col2:
    recessive_allele = st.text_input(
        "🔤 Recessive Allele Symbol",
        value="h",
        max_chars=1,
    )
col1, col2 = st.columns(2)

with col1:
    parent1 = st.text_input(
        "👨 Parent 1 Genotype",
        value="Hh",
        max_chars=2,
    )
with col2:
    parent2 = st.text_input(
        "👩 Parent 2 Genotype",
        value="hh",
        max_chars=2,
    )
col1, col2 = st.columns(2)

with col1:
    dominant_phenotype = st.text_input(
        "✨ Dominant Phenotype",
        value="Hairy",
    )
with col2:
    recessive_phenotype = st.text_input(
        "✨ Recessive Phenotype",
        value="Not Hairy",
    )
# Validation and processing
def validate_inputs():
    """Validate all user inputs."""
    errors = []
    
    if not dominant_allele or not recessive_allele:
        errors.append("Both allele symbols are required.")
    elif dominant_allele == recessive_allele:
        errors.append("Dominant and recessive alleles must be different.")
    
    if len(parent1) != 2:
        errors.append("Parent 1 genotype must be exactly 2 characters.")
    elif not all(a in {dominant_allele, recessive_allele} for a in parent1):
        errors.append(
            f"Parent 1 can only contain '{dominant_allele}' or '{recessive_allele}'."
        )
    
    if len(parent2) != 2:
        errors.append("Parent 2 genotype must be exactly 2 characters.")
    elif not all(a in {dominant_allele, recessive_allele} for a in parent2):
        errors.append(
            f"Parent 2 can only contain '{dominant_allele}' or '{recessive_allele}'."
        )
    
    return errors


# Generate button
if st.button("🧬 Generate Punnett Square", use_container_width=True):
    st.session_state.generate_clicked = True

# Display results if generate was clicked
if st.session_state.generate_clicked:
    errors = validate_inputs()
    
    if errors:
        for error in errors:
            st.error(f"❌ {error}")
    else:
        # Calculate offspring
        offspring = calculate_punnett_square(
            parent1, parent2, dominant_allele, recessive_allele
        )
        
        # Display Punnett Square
        st.markdown("## 📊 Punnett Square")
        
        # Create formatted Punnett square display
        p1_gametes = [parent1[0], parent1[1]]
        p2_gametes = [parent2[0], parent2[1]]
        
        square_html = f"""
        <div class="punnett-square">
            <div style="margin-bottom: 20px;">
                <strong>Parent 1: {parent1} (Gametes: {p1_gametes[0]}, {p1_gametes[1]})</strong><br>
                <strong>Parent 2: {parent2} (Gametes: {p2_gametes[0]}, {p2_gametes[1]})</strong>
            </div>
            <div style="font-size: 18px; font-family: courier;">
                <table style="width: 100%; margin: 20px 0; border-collapse: collapse; color: #2c3e50;">
                    <tr style="border-bottom: 2px solid rgba(46, 157, 122, 0.3);">
                        <td style="padding: 10px; text-align: center;"></td>
                        <td style="padding: 10px; text-align: center; border-left: 2px solid rgba(46, 157, 122, 0.3);"><strong>{p2_gametes[0]}</strong></td>
                        <td style="padding: 10px; text-align: center; border-left: 2px solid rgba(46, 157, 122, 0.3);"><strong>{p2_gametes[1]}</strong></td>
                    </tr>
                    <tr style="border-bottom: 2px solid rgba(46, 157, 122, 0.3);">
                        <td style="padding: 10px; text-align: center; border-right: 2px solid rgba(46, 157, 122, 0.3);"><strong>{p1_gametes[0]}</strong></td>
                        <td style="padding: 10px; text-align: center; border-left: 2px solid rgba(46, 157, 122, 0.3);">{offspring[0]}</td>
                        <td style="padding: 10px; text-align: center; border-left: 2px solid rgba(46, 157, 122, 0.3);">{offspring[1]}</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px; text-align: center; border-right: 2px solid rgba(46, 157, 122, 0.3);"><strong>{p1_gametes[1]}</strong></td>
                        <td style="padding: 10px; text-align: center; border-left: 2px solid rgba(46, 157, 122, 0.3);">{offspring[2]}</td>
                        <td style="padding: 10px; text-align: center; border-left: 2px solid rgba(46, 157, 122, 0.3);">{offspring[3]}</td>
                    </tr>
                </table>
            </div>
        </div>
        """
        st.markdown(square_html, unsafe_allow_html=True)
        
        # Calculate and display phenotype percentages
        phenotype_info = calculate_phenotype_percentages(
            offspring,
            dominant_allele,
            recessive_allele,
            dominant_phenotype,
            recessive_phenotype,
        )
        
        st.markdown("## 📈 Phenotype Results")
        results_html = f"""
        <div class="phenotype-results">
            <div style="margin: 15px 0;"><strong>{phenotype_info['dominant_percent']:.0f}%</strong> {dominant_phenotype}</div>
            <div style="margin: 15px 0;"><strong>{phenotype_info['recessive_percent']:.0f}%</strong> {recessive_phenotype}</div>
            <div style="margin: 15px 0; font-size: 16px; opacity: 0.9;">
                <strong>{phenotype_info['hetero_percent']:.0f}%</strong> may be heterozygous ({dominant_allele}{recessive_allele})
            </div>
        </div>
        """
        st.markdown(results_html, unsafe_allow_html=True)
