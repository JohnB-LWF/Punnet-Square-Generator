# Punnet Square Requirements


1. Inputs:
   
    A. Two Genotypes (ex. Hh, hh)
   
    B. Two Gene Types (Dominant, Recessive) of the two Parents
   
    C. Two Genotypes (ex. Hh, hh) and Two Phenotypes (ex. Hairy, Not Hairy)
   
3. Outputs:
   
    A. A completed Punnet Square showing the crossing of two Genotypes (in tabular form)
   
    B. The percentages of Phenotypes in the offspring (ex. 50% Hairy, 50% Not Hairy)
   

## Web Interface (Streamlit) - Recommended
The redesigned web interface provides a polished, user-friendly experience.

(Try it out now: https://punnett-square-generator.streamlit.app/)

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

3. Open your browser to the URL displayed (usually `http://localhost:8501`)

## Command Line Interface
The original command-line version is available in `punnetsquare.py`:

```bash
python punnetsquare.py
```

## Streamlit Features

- **Light Blue Background** with modern, clean design
- **Green Input Boxes** with rounded corners and hover effects
- **Interactive Results** displayed in an easy-to-read format
- **Punnett Square Visualization** with clear genetic cross representation
- **Phenotype Percentages** calculated and displayed prominently
