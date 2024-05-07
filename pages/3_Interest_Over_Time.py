import streamlit as st
from pytrends.request import TrendReq

# Function to plot trends
def plot_trends(data, title):
    st.write(title)
    st.line_chart(data)

# Function for forecasting trends
def forecast_trends(pytrends, keyword, date_start, date_end, country):
    pytrends.build_payload([keyword], timeframe=f'{date_start} {date_end}', geo=country)
    data = pytrends.interest_over_time()
    plot_trends(data, f'Interest over Time for {keyword} between {date_start} and {date_end}')

# Streamlit app
def main():
    st.title("Google Trends Analysis")
    
    pytrends = TrendReq(hl='en-US', tz=360)
    
    # Get initial keyword
    keyword = st.text_input("Enter the keyword you want to search for:")
    
    if keyword:
        # Get the date to analyze
        date_start = st.text_input("Enter the starting date you want to analyze (YYYY):")
        
        if date_start:
            date_end = st.text_input("Enter the ending date you want to analyze (YYYY):")
            if date_end:
                # Get the country to analyze
                country = st.selectbox("Select the country to analyze", [
                    "US",  # United States
                    "CA",  # Canada
                    "AU",  # Australia
                    "GB",  # United Kingdom
                    "DE",  # Germany
                    "FR",  # France
                    "IT",  # Italy
                    "ES",  # Spain
                    "NL",  # Netherlands
                    "SE",  # Sweden
                    "CH",  # Switzerland
                    "NO",  # Norway
                    "DK",  # Denmark
                    "FI",  # Finland
                    "AT",  # Austria
                    "BE",  # Belgium
                    "IE",  # Ireland
                    "PT",  # Portugal
                    "GR",  # Greece
                    "PL",  # Poland
                ])  # Add more countries as needed

                if country:
                    # Execute analysis
                    forecast_trends(pytrends, keyword, date_start, date_end, country)

if __name__ == "__main__":
    main()
