import streamlit as st
import time
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.sidebar.image('https://static.barclaycardus.com/servicing/cce519fe/img/base/header-logo.svg', width=200)

# Function to extract data from text
def extract_data(text):
    # Dummy data extraction logic (replace with your actual logic)
    data_dict = {'Category 1': 10, 'Category 2': 20, 'Category 3': 15}
    return data_dict

# Function to generate a bar chart
def generate_bar_chart(data_dict):
    labels = list(data_dict.keys())
    values = list(data_dict.values())
    plt.bar(labels, values)
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Bar Chart')
    st.pyplot()

# Function to generate a pie chart
def generate_pie_chart(data_dict):
    fig = px.pie(values=list(data_dict.values()), names=list(data_dict.keys()), title='Pie Chart')
    st.plotly_chart(fig)

def main():
    user_text = st.sidebar.text_input("Enter text:")
    chart_type = st.sidebar.selectbox("Select Chart Type", ["Bar Chart", "Pie Chart"])

    if st.sidebar.button("Generate Report"):
        if user_text:
            with st.spinner("Generating report..."):
                time.sleep(2)
                data_dict = extract_data(user_text)
                if chart_type == "Bar Chart":
                    generate_bar_chart(data_dict)
                elif chart_type == "Pie Chart":
                    generate_pie_chart(data_dict)
            
            st.sidebar.success("Report generated successfully!")

            # Detail view
            with st.expander("View Report Details"):
                st.write("Report Data:")
                df = pd.DataFrame.from_dict(data_dict, orient='index', columns=['Values'])
                st.dataframe(df.style.set_properties(**{'width': '100%'}))  # Set width to 100% using CSS
        else:
            st.sidebar.warning("Please enter some text.")

if __name__ == "__main__":
    main()
