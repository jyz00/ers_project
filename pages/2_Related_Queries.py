import streamlit as st
from pytrends.request import TrendReq

# Function for related queries analysis
def related_queries(pytrends, keyword, date_start, date_end, country):
    pytrends.build_payload([keyword], timeframe=f'{date_start} {date_end}', geo=country)
    related = pytrends.related_queries()
    top_queries = related[keyword]['top']
    rising_queries = related[keyword]['rising']
    st.write("Top related queries:")
    st.write(top_queries)
    st.write("\nRising related queries:")
    st.write(rising_queries)

# Streamlit app
def main():
    st.title("Google Trends Analysis")
    
    pytrends = TrendReq(hl='en-US', tz=360)
    
    # Get initial keyword
    keyword = st.text_input("Enter the keyword you want to search for:")
    
    if keyword:
        # Get the date to analyze
        date_start = st.text_input("Enter the starting date you want to analyze (YYYY-MM-DD):")
        
        if date_start:
            date_end = st.text_input("Enter the ending date you want to analyze (YYYY-MM-DD):")

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
                    related_queries(pytrends, keyword, date_start,date_end, country)

if __name__ == "__main__":
    main()
