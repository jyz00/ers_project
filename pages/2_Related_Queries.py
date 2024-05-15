import streamlit as st
from pytrends.request import TrendReq as UTrendReq
GET_METHOD='get'

import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'es-ES,es;q=0.9',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'SEARCH_SAMESITE=CgQIw5oB; HSID=Avi2x7iinsjCILQtI; SSID=AZiKdVi7VhF9hew52; APISID=K_m5ilPDQpLZvpli/APiI0ctpuIDU_JZIf; SAPISID=0YqWydt3DmLvdQa5/AcWRt6caniP3Jcx5P; __Secure-1PAPISID=0YqWydt3DmLvdQa5/AcWRt6caniP3Jcx5P; __Secure-3PAPISID=0YqWydt3DmLvdQa5/AcWRt6caniP3Jcx5P; __Secure-ENID=19.SE=MOECcSVhYNN3cNaMAoc2K8dadvmc5t1utQUh0KYa10aNDqhSMnoy6r8tlCNN-95AEmf0OP2oaviJZaHpqRCICoq2Tr5SVThkbOaTP38Fg743O0I5gqD_8rbC-_ti8oMVJTCuiyEOo1q-47WlwQtar9lfbqa-1l1EdmW2TzNL4BbZ6KdGDAGFaIdBYxdsOcO-zrQf5sb7w3WrDhE; OTZ=7548360_48_52_123900_48_436380; SID=g.a000jQjlBn3JLt3R7teaobacpU4cZU5_O0vS53W7y8VPGd7AjBw6yN3-xOS1o-XsbRnwlLk0iwACgYKAa8SAQASFQHGX2MiwaK3kHpwVpJSHCrUMe0qaRoVAUF8yKpp9F07Xxrx83rcbYd3-plZ0076; __Secure-1PSID=g.a000jQjlBn3JLt3R7teaobacpU4cZU5_O0vS53W7y8VPGd7AjBw68y8zlsPZSUwK9ixRcOdmmgACgYKARASAQASFQHGX2Mi-6Iw-2eOI2SU6BjIpT0zVxoVAUF8yKq58OuGIx5erEtsFuAVIXi00076; __Secure-3PSID=g.a000jQjlBn3JLt3R7teaobacpU4cZU5_O0vS53W7y8VPGd7AjBw6qYj3DAisIF7h0irwzwRxbAACgYKAe4SAQASFQHGX2MiqFCfKw1xMMvUvAuKW7OlARoVAUF8yKpdgodFrH-SOhdAw4mjnGR20076; NID=514=eJRcRAS-l4YOxiZ4dXYUB4FXbcpM7_H1fGoercKRuAQejhvlWGtBLswj9h1YU-o38OeoxRn1DnzChepuibSnxllCMWHI8msuHKzPDWPD-nb_7VuZMSMTdaz9PIoryBnIHI3kG8bG_odZ10wD06oZ7poUbkZIFLbOarRQZIowcjkJACXHgpKiBfyy9CurjuoSZJCFYvAuZIug8wlRTAv-gS-maj5cNzueCyjLf1zB2_fc6BwjFMk0DqPMJUSL9R1SPTG6ucJdFPHEuqevcbrY7LJEJn3G7eIFFip1',
    'origin': 'https://trends.google.es',
    'priority': 'u=1, i',
    'referer': 'https://trends.google.es/trends/explore?date=now%201-d&geo=ES-CE&q=Real&hl=es',
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
    st.title("Related Queries Analysis")

    st.markdown("##### This page allows you to analyze the related queries for a specific keyword.")
    
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
