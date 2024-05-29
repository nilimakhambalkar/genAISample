import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the sidebar
st.sidebar.image('https://static.barclaycardus.com/servicing/cce519fe/img/base/header-logo.svg', width=200)#
# st.sidebar.header("Upload and Filter Data")

# Upload CSV file
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV file
    data = pd.read_csv(uploaded_file)

    # Sidebar options to filter data and select columns
    st.sidebar.header("Filter and Select Columns")
    text_input = st.sidebar.text_input("Enter text to filter columns and data:")
    selected_columns = st.sidebar.multiselect("Select columns to display:", data.columns.tolist())

    # Main page title and uploaded data display
    st.title("NLP Data Visualization Tool")
    st.header("Uploaded Data")
    st.write(data)

    if text_input:
        # Filter columns based on the entered text
        filtered_columns = [col for col in data.columns if text_input.lower() in col.lower()]

        # Check for matches in the data itself
        for col in data.columns:
            if any(data[col].astype(str).str.contains(text_input, case=False, na=False)):
                if col not in filtered_columns:
                    filtered_columns.append(col)

        if filtered_columns:
            selected_columns = filtered_columns

    if selected_columns:
        # Display the selected columns from the CSV file
        st.header("Selected Columns")
        st.dataframe(data[selected_columns], width=2000)

        # Option to render different types of charts based on text instructions
        st.header("Render Chart Based on Text Instructions")
        chart_instruction = st.text_input("Enter chart instruction (e.g., 'bar chart', 'scatter plot', 'pie chart'):", "")

        if chart_instruction:
            # Check the chart instruction provided by the user and render the corresponding chart
            chart_instruction = chart_instruction.lower()

            if "bar" in chart_instruction:
                st.bar_chart(data[selected_columns])
            elif "line" in chart_instruction:
                st.line_chart(data[selected_columns])
            elif "scatter" in chart_instruction:
                if len(selected_columns) >= 2:
                    fig, ax = plt.subplots(figsize=(20, 10))
                    sns.scatterplot(x=selected_columns[0], y=selected_columns[1], data=data, ax=ax)
                    st.pyplot(fig)
                else:
                    st.write("Please select at least two columns for a scatter plot.")
            elif "heatmap" in chart_instruction:
                if len(selected_columns) > 1:
                    corr = data[selected_columns].corr()
                    fig, ax = plt.subplots(figsize=(20, 10))
                    sns.heatmap(corr, annot=True, ax=ax)
                    st.pyplot(fig)
                else:
                    st.write("Please select at least two columns for a heatmap.")
            elif "pie" in chart_instruction:
                if len(selected_columns) == 1:
                    fig, ax = plt.subplots(figsize=(20, 10))
                    data[selected_columns[0]].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
                    st.pyplot(fig)
                else:
                    st.write("Please select exactly one column for a pie chart.")
            else:
                st.write("Invalid chart instruction. Please try again.")
