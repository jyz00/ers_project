import streamlit as st
from pytrends.request import TrendReq as UTrendReq
GET_METHOD='get'

import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'es-ES,es;q=0.7',
    # 'cookie': 'SEARCH_SAMESITE=CgQIw5oB; HSID=Avi2x7iinsjCILQtI; SSID=AZiKdVi7VhF9hew52; APISID=K_m5ilPDQpLZvpli/APiI0ctpuIDU_JZIf; SAPISID=0YqWydt3DmLvdQa5/AcWRt6caniP3Jcx5P; __Secure-1PAPISID=0YqWydt3DmLvdQa5/AcWRt6caniP3Jcx5P; __Secure-3PAPISID=0YqWydt3DmLvdQa5/AcWRt6caniP3Jcx5P; NID=514=VIwPMDaDOafbKNJoFlbAuVg7tilByKzkSvDcX2OJyDiTaRat9sYjRTPvTX5RozFRxZ9O1YCXVNzesOl8qzOokqLHRdpWnia5JI67z1y4ICdNnwEw6GZT4aCAlFzZA-1PDIkNJxbyhQwv5PG9UJH5RK-CN1Cy4oMMIlCjBahpXC8',
    'priority': 'u=1, i',
    'referer': 'https://trends.google.es/trends/explore?date=now%201-d&geo=ES&q=lunch&hl=es',
    'sec-ch-ua': '"Brave";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}


class TrendReq(UTrendReq):
    def _get_data(self, url, method=GET_METHOD, trim_chars=0, **kwargs):
        return super()._get_data(url, method=GET_METHOD, trim_chars=trim_chars, headers=headers, **kwargs)


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
    st.title("Interest Over Time")

    st.markdown("##### This page allows you to forecast the interest over time for a specific keyword.")
    
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
                    forecast_trends(pytrends, keyword, date_start, date_end, country)

if __name__ == "__main__":
    main()
