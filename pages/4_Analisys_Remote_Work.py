import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

# Create pytrends object
pytrends = TrendReq(hl='en-US', tz=360)
keyword = "remote work"

# Function to plot trends
def plot_trends(data, title):
    st.write(title)
    st.line_chart(data)

# Function to fetch top trending searches
def fetch_top_trending(year, country):
    pytrends.build_payload({}, cat=0, timeframe=f'{year}-01-01 {year}-12-31', geo=country)
    top_trending = pytrends.trending_searches(pn='united_states')
    return top_trending

# 1. 地域分析
def regional_interest():
    pytrends.build_payload([keyword], timeframe='today 5-y')
    by_region = pytrends.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False)
    top_regions = by_region.sort_values(by=keyword, ascending=False).head(10)
    st.write("Top 10 Regions for Remote Work Interest:")
    st.bar_chart(top_regions)

# 2. 相关查询和主题分析
def related_queries():
    pytrends.build_payload([keyword], timeframe='today 5-y')
    related = pytrends.related_queries()
    top_queries = related[keyword]['top']
    rising_queries = related[keyword]['rising']
    st.write("Top related queries:")
    st.write(top_queries)
    st.write("Rising related queries:")
    st.write(rising_queries)

# 3. 时间序列预测 (使用简单的滚动平均作为示例)
def forecast_trends():
    pytrends.build_payload([keyword], timeframe='today 5-y')
    data = pytrends.interest_over_time()
    data['MA'] = data[keyword].rolling(window=12).mean()
    plot_trends(data[['MA']], 'Forecasting with Moving Average')

# Streamlit app
def main():
    st.title("Remote Work Trends Analysis")

    analysis_option = st.sidebar.selectbox(
        "Select analysis option:",
        ("Regional Interest", "Related Queries", "Forecast Trends")
    )

    if analysis_option == "Regional Interest":
        regional_interest()
    elif analysis_option == "Related Queries":
        related_queries()
    elif analysis_option == "Forecast Trends":
        forecast_trends()

    st.sidebar.title("Top Trending Searches Analysis")

    # Get user inputs
    year = st.sidebar.number_input("Enter the year you want to analyze:", min_value=2004, max_value=2023, step=1)
    country = st.sidebar.selectbox("Select the country to analyze", [
        "US", "CA", "AU", "GB", "DE", "FR", "IT", "ES", "NL", "SE", 
        "CH", "NO", "DK", "FI", "AT", "BE", "IE", "PT", "GR", "PL"
    ])

    if st.sidebar.button("Fetch Top Trending Searches"):
        # Fetch top trending searches
        top_trending = fetch_top_trending(year, country)
        st.sidebar.write(f"Top Trending Searches in {country} for {year}:")
        st.sidebar.write(top_trending)

if __name__ == "__main__":
    main()