import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from pytrends.request import TrendReq as UTrendReq
GET_METHOD='get'

import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'es-ES,es;q=0.5',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'SEARCH_SAMESITE=CgQIw5oB; HSID=Avi2x7iinsjCILQtI; SSID=AZiKdVi7VhF9hew52; APISID=K_m5ilPDQpLZvpli/APiI0ctpuIDU_JZIf; SAPISID=0YqWydt3DmLvdQa5/AcWRt6caniP3Jcx5P; __Secure-1PAPISID=0YqWydt3DmLvdQa5/AcWRt6caniP3Jcx5P; __Secure-3PAPISID=0YqWydt3DmLvdQa5/AcWRt6caniP3Jcx5P; SID=g.a000igjlBsoSDMIyoY3BlJRTfs_l311o-aWJoHdO-7g1gzNUXueh0vrvZZVOIQKoAcGDmgmr6AACgYKAQwSAQASFQHGX2Mig9woKs8LFRnUAwOVn7lxERoVAUF8yKo6ErxF19XNx5Sv62FlUFqO0076; __Secure-1PSID=g.a000igjlBsoSDMIyoY3BlJRTfs_l311o-aWJoHdO-7g1gzNUXuehugZ1Fbe3EpTX0uW7R9toqgACgYKAU4SAQASFQHGX2MiLId_2LkwfwL1SkXo3H7aDhoVAUF8yKr-T-dwi81pbzjkGUcFMp3J0076; __Secure-3PSID=g.a000igjlBsoSDMIyoY3BlJRTfs_l311o-aWJoHdO-7g1gzNUXuehCw4AX5K5yE44x6pg_ar1wQACgYKARcSAQASFQHGX2MiuqFl-FiRUYK7B4UyE0YvFxoVAUF8yKr9oGuCJbWVGLcAGk8yx_RE0076; __Secure-ENID=19.SE=MOECcSVhYNN3cNaMAoc2K8dadvmc5t1utQUh0KYa10aNDqhSMnoy6r8tlCNN-95AEmf0OP2oaviJZaHpqRCICoq2Tr5SVThkbOaTP38Fg743O0I5gqD_8rbC-_ti8oMVJTCuiyEOo1q-47WlwQtar9lfbqa-1l1EdmW2TzNL4BbZ6KdGDAGFaIdBYxdsOcO-zrQf5sb7w3WrDhE; OTZ=7548360_48_52_123900_48_436380; NID=514=HXWyLL7w1vMjEwTHnpeBk4T28WLsaKGyJBSir-rnZhbpxMnEZDwYDFGPlqLfelZ4xeIyyOPEIOb_yLvWOMp9zcMhkBQOgBkvSOjYI8unL3lXghmXBxvVGFAEE9M67QJU3Fu4Wz1LbN3nXKQPZNmBR3N4e4mRo71qd5rlDhudElXsjE9QZWzZDP5HmjqtrpcA4os0Iip73QLWor1_hMmwrodg-yXCS9TKtX240A',
    'origin': 'https://trends.google.es',
    'priority': 'u=1, i',
    'referer': 'https://trends.google.es/trends/explore?date=2019-01-01%202019-12-12&geo=US&q=loro&hl=es',
    'sec-ch-ua': '"Chromium";v="124", "Brave";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Nexus 5"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"6.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
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