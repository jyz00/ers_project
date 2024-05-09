import streamlit as st
from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=360, timeout=(10,25), proxies=['https://34.203.233.13:80'], retries=2, backoff_factor=0.1, requests_args={'verify':False})


# Function to plot trends
def plot_trends(data, title):
    st.write(title)
    st.line_chart(data)

# Function for regional interest analysis
def regional_interest(pytrends, keyword, date_start, date_end):
    pytrends.build_payload([keyword], timeframe=f'{date_start} {date_end}')
    by_region = pytrends.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False)
    top_regions = by_region[keyword].nlargest(10)
    st.write('Top countries with the most searches:')
    st.write(top_regions)
    st.write("Estimated search volume for the top regions:")
    st.bar_chart(top_regions * 1000)  # Multiplying by 1000 to scale to estimated search volume

# Streamlit app
def main():
    st.title("Regional Interest Analysis")

    st.markdown("##### This page allows you to analyze the regional interest for a specific keyword.")
    
    pytrends = TrendReq(hl='en-US', tz=360)
    
    # Get initial keyword
    keyword = st.text_input("Enter the keyword you want to search for:")
    
    if keyword:
        # Get the date to analyze
        date_start = st.text_input("Enter the starting date you want to analyze (YYYY-MM-DD):")
        
        if date_start:
            date_end = st.text_input("Enter the ending date you want to analyze (YYYY-MM-DD):")

            if date_end:
                regional_interest(pytrends, keyword, date_start, date_end)

if __name__ == "__main__":
    main()
