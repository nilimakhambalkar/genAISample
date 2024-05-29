import streamlit as st
import pandas as pd
import spacy
from spacy import displacy
import matplotlib.pyplot as plt
import seaborn as sns

# Load the spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Title of the web app
st.title("NLP Data Visualization Tool")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV file
    data = pd.read_csv(uploaded_file)

    # Display the uploaded data
    st.write("Uploaded Data:")
    st.write(data)

    # Get user input for text analysis
    text_input = st.text_input("Enter text for NLP analysis:", "")

    if text_input:
        # Perform NLP analysis on the entered text
        doc = nlp(text_input)

        # Display the NLP analysis results using spaCy's visualization
        st.write("NLP Analysis Results:")
        displacy.render(doc, style="ent", jupyter=False)

    # Option to display specific columns from the CSV file
    st.subheader("Display Specific Columns from CSV:")
    selected_columns = st.multiselect("Select columns to display:", data.columns.tolist())

    if selected_columns:
        # Display the selected columns from the CSV file
        st.write("Selected Columns:")
        st.write(data[selected_columns])

        # Option to render different types of charts based on text instructions
        st.subheader("Render Chart Based on Text Instructions:")
        chart_instruction = st.text_input("Enter chart instruction (e.g., 'bar chart', 'scatter plot'):", "")

        if chart_instruction:
            # Check the chart instruction provided by the user and render the corresponding chart
            chart_instruction = chart_instruction.lower()

            if "bar" in chart_instruction:
                st.bar_chart(data[selected_columns])
            elif "line" in chart_instruction:
                st.line_chart(data[selected_columns])
            elif "scatter" in chart_instruction:
                st.scatter_chart(data, x=selected_columns[0], y=selected_columns[1])
            elif "heatmap" in chart_instruction:
                corr = data[selected_columns].corr()
                st.write("Correlation Heatmap:")
                st.write(sns.heatmap(corr, annot=True))
            else:
                st.write("Invalid chart instruction. Please try again.")
