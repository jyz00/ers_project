import streamlit as st
from pytrends.request import TrendReq as UTrendReq
GET_METHOD='get'

import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'es-ES,es;q=0.9',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'SEARCH_SAMESITE=CgQIw5oB; HSID=Avi2x7iinsjCILQtI; SSID=AZiKdVi7VhF9hew52; APISID=K_m5ilPDQpLZvpli/APiI0ctpuIDU_JZIf; SAPISID=0YqWydt3DmLvdQa5/AcWRt6caniP3Jcx5P; __Secure-1PAPISID=0YqWydt3DmLvdQa5/AcWRt6caniP3Jcx5P; __Secure-3PAPISID=0YqWydt3DmLvdQa5/AcWRt6caniP3Jcx5P; __Secure-ENID=19.SE=MOECcSVhYNN3cNaMAoc2K8dadvmc5t1utQUh0KYa10aNDqhSMnoy6r8tlCNN-95AEmf0OP2oaviJZaHpqRCICoq2Tr5SVThkbOaTP38Fg743O0I5gqD_8rbC-_ti8oMVJTCuiyEOo1q-47WlwQtar9lfbqa-1l1EdmW2TzNL4BbZ6KdGDAGFaIdBYxdsOcO-zrQf5sb7w3WrDhE; OTZ=7548360_48_52_123900_48_436380; NID=514=HXWyLL7w1vMjEwTHnpeBk4T28WLsaKGyJBSir-rnZhbpxMnEZDwYDFGPlqLfelZ4xeIyyOPEIOb_yLvWOMp9zcMhkBQOgBkvSOjYI8unL3lXghmXBxvVGFAEE9M67QJU3Fu4Wz1LbN3nXKQPZNmBR3N4e4mRo71qd5rlDhudElXsjE9QZWzZDP5HmjqtrpcA4os0Iip73QLWor1_hMmwrodg-yXCS9TKtX240A; SID=g.a000jwjlBv2G4-rxwt7ygeoXwzI9bdKxCQntGvhLNzHAiCZmXhgbhRAqqeKWLNFYIs6gDbvlvAACgYKARcSAQASFQHGX2MiRWxD7DyXUP7hlBY-rCE8uBoVAUF8yKrerG6VIO3dKHwsbwnvJ9_y0076; __Secure-1PSID=g.a000jwjlBv2G4-rxwt7ygeoXwzI9bdKxCQntGvhLNzHAiCZmXhgb45gnnFNI48_qLA8iKXmhoQACgYKASYSAQASFQHGX2Mi3eVOGR6PQUoa0hhVR1nW4hoVAUF8yKqWp43QMBLvZvicJUhTPEBa0076; __Secure-3PSID=g.a000jwjlBv2G4-rxwt7ygeoXwzI9bdKxCQntGvhLNzHAiCZmXhgbBL5YTKbmSr5uiWKUu9Y_uwACgYKAQwSAQASFQHGX2MiM2amD-hHnVPCH7PyiE1qRhoVAUF8yKpdZ4fKZGiL8ua4pZ0PZO0p0076',
    'origin': 'https://trends.google.es',
    'priority': 'u=1, i',
    'referer': 'https://trends.google.es/trends/explore?date=now%201-d&geo=ES&q=loki&hl=es',
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
