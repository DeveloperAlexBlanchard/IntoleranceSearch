import requests

cookies = {
    'TealeafAkaSid': 'YPqfltM_IzuYPA1bw-lnkdD0UhnvPrl1',
    'visitorId': '018005E0CDB10201AEBAFF00C9B0FB29',
    'sapphire': '1',
    'fiatsCookie': 'DSI_3264|DSN_San%20Francisco%20Stonestown|DSZ_94132',
    '__gads': 'ID=daababf455e53154:T=1649366062:S=ALNI_MYT986BZe3qXxq2r9ZhVBtJjoV-yA',
    'ci_pixmgr': 'other',
    '_gcl_au': '1.1.1995797880.1649366063',
    '_ga': 'GA1.2.670127125.1650492953',
    'crl8.fpcuid': '44acb762-56e4-4c58-a684-f9c17f35c340',
    'UserLocation': '95124|37.25577163696289|-121.92688751220703|CA|US',
    '__gpi': 'UID=000004a29c8dca2e:T=1650556610:RT=1651686824:S=ALNI_MbPtY2un6p9R6S47Kjr8VHmVG1Meg',
    'accessToken': 'eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI1MmVhZGJkYi01MjNjLTRhZmYtYjY0ZC1jNjQ5ODczYTg2OTciLCJpc3MiOiJNSTYiLCJleHAiOjE2NTE3ODAxNjYsImlhdCI6MTY1MTY5Mzc2NiwianRpIjoiVEdULmY5NzNiYTRhZDEwZDQxYzlhZWFlOTJkNjRlMjViM2MzLWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6ImNkY2ZkNThlMzg1ZDYxMmY3YWI1OTdiOTJjN2QyNDNmMjZlYzEyZGJhZjhlODY4ZjIxNmRlNzgyOTgxZWYyOTkiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.r6H8k2hZnf_QK_hEEKhkp8A-mAYHtCnyO_DbDCD7g9viFbBiMZalTDjsylI56J_jyTgaCrnTkUdmU7ivpFz_Q2y5aBHiWt3WZA_-pSDzhgoP8iuYBZFIq386L_dXaX1MYxagidue3yGzqJU_agK32nVcZZnD495c2uKgD0pcORHq0x9mQpPEcMnHqFLyDQ5j7bAzabag2NAbuQwvjRCLyMEkf4fElXN8p7vuHysXIob1std9KNPNOwY7eK7_lrOi2zMu5tYj28O_SVD7pM9w9rEVGS6_AquoWCzQCAQ0GelgoBxDqqHJ9jVJeUSAefYskC4ea-cSPcIH9zKEC9zWog',
    'idToken': 'eyJhbGciOiJub25lIn0.eyJzdWIiOiI1MmVhZGJkYi01MjNjLTRhZmYtYjY0ZC1jNjQ5ODczYTg2OTciLCJpc3MiOiJNSTYiLCJleHAiOjE2NTE3ODAxNjYsImlhdCI6MTY1MTY5Mzc2NiwiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlfX0.',
    'refreshToken': '5pQeoXZ4OdoNoqVvAmen0khOD7ja2Yk78Hzhv2q0XMJdU8ubKrS1ggbRfCTKZKJCc7axUOtluiVMJcDHHDOTAA',
    '_mitata': 'OTRkYmI4MzM1MDBiZDg2YjgwOWZkNWYyYWZjMTYyMzkxODZkMjdmY2ExNTdlMDdhOTBmYTQ1ZTY1ZWRmMmM4Mg==_/@#/1651706491_/@#/cI3YSuVB7nCwVB6i_/@#/NDNiZjc0YzJjODI3ODJiZDE5ZmVlZDcwNGFhNTQxNDIwNmMxZGE0YWM2MjRjNzdmMDFjM2Y0ZTU3MGI3ODg1YQ==_/@#/000',
    'ffsession': '{%22sessionHash%22:%222b983bfa676421649366061487%22%2C%22prevPageName%22:%22grocery:%20meat%20&%20seafood:%20bacon%22%2C%22prevPageType%22:%22level%203%22%2C%22prevPageUrl%22:%22https://www.target.com/c/bacon-meat-seafood-grocery/-/N-4tgi9%22%2C%22sessionHit%22:51%2C%22prevSearchTerm%22:%22non-search%22}',
    '_uetsid': 'c35b5130cb1811ec9adae9002e3ffbc0',
    '_uetvid': '33ebb610077411ec9972477f4f8bc97d',
}

headers = {
    'authority': 'redsky.target.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'TealeafAkaSid=YPqfltM_IzuYPA1bw-lnkdD0UhnvPrl1; visitorId=018005E0CDB10201AEBAFF00C9B0FB29; sapphire=1; fiatsCookie=DSI_3264|DSN_San%20Francisco%20Stonestown|DSZ_94132; __gads=ID=daababf455e53154:T=1649366062:S=ALNI_MYT986BZe3qXxq2r9ZhVBtJjoV-yA; ci_pixmgr=other; _gcl_au=1.1.1995797880.1649366063; _ga=GA1.2.670127125.1650492953; crl8.fpcuid=44acb762-56e4-4c58-a684-f9c17f35c340; UserLocation=95124|37.25577163696289|-121.92688751220703|CA|US; __gpi=UID=000004a29c8dca2e:T=1650556610:RT=1651686824:S=ALNI_MbPtY2un6p9R6S47Kjr8VHmVG1Meg; accessToken=eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI1MmVhZGJkYi01MjNjLTRhZmYtYjY0ZC1jNjQ5ODczYTg2OTciLCJpc3MiOiJNSTYiLCJleHAiOjE2NTE3ODAxNjYsImlhdCI6MTY1MTY5Mzc2NiwianRpIjoiVEdULmY5NzNiYTRhZDEwZDQxYzlhZWFlOTJkNjRlMjViM2MzLWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6ImNkY2ZkNThlMzg1ZDYxMmY3YWI1OTdiOTJjN2QyNDNmMjZlYzEyZGJhZjhlODY4ZjIxNmRlNzgyOTgxZWYyOTkiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.r6H8k2hZnf_QK_hEEKhkp8A-mAYHtCnyO_DbDCD7g9viFbBiMZalTDjsylI56J_jyTgaCrnTkUdmU7ivpFz_Q2y5aBHiWt3WZA_-pSDzhgoP8iuYBZFIq386L_dXaX1MYxagidue3yGzqJU_agK32nVcZZnD495c2uKgD0pcORHq0x9mQpPEcMnHqFLyDQ5j7bAzabag2NAbuQwvjRCLyMEkf4fElXN8p7vuHysXIob1std9KNPNOwY7eK7_lrOi2zMu5tYj28O_SVD7pM9w9rEVGS6_AquoWCzQCAQ0GelgoBxDqqHJ9jVJeUSAefYskC4ea-cSPcIH9zKEC9zWog; idToken=eyJhbGciOiJub25lIn0.eyJzdWIiOiI1MmVhZGJkYi01MjNjLTRhZmYtYjY0ZC1jNjQ5ODczYTg2OTciLCJpc3MiOiJNSTYiLCJleHAiOjE2NTE3ODAxNjYsImlhdCI6MTY1MTY5Mzc2NiwiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlfX0.; refreshToken=5pQeoXZ4OdoNoqVvAmen0khOD7ja2Yk78Hzhv2q0XMJdU8ubKrS1ggbRfCTKZKJCc7axUOtluiVMJcDHHDOTAA; _mitata=OTRkYmI4MzM1MDBiZDg2YjgwOWZkNWYyYWZjMTYyMzkxODZkMjdmY2ExNTdlMDdhOTBmYTQ1ZTY1ZWRmMmM4Mg==_/@#/1651706491_/@#/cI3YSuVB7nCwVB6i_/@#/NDNiZjc0YzJjODI3ODJiZDE5ZmVlZDcwNGFhNTQxNDIwNmMxZGE0YWM2MjRjNzdmMDFjM2Y0ZTU3MGI3ODg1YQ==_/@#/000; ffsession={%22sessionHash%22:%222b983bfa676421649366061487%22%2C%22prevPageName%22:%22grocery:%20meat%20&%20seafood:%20bacon%22%2C%22prevPageType%22:%22level%203%22%2C%22prevPageUrl%22:%22https://www.target.com/c/bacon-meat-seafood-grocery/-/N-4tgi9%22%2C%22sessionHit%22:51%2C%22prevSearchTerm%22:%22non-search%22}; _uetsid=c35b5130cb1811ec9adae9002e3ffbc0; _uetvid=33ebb610077411ec9972477f4f8bc97d',
    'origin': 'https://www.target.com',
    'referer': 'https://www.target.com/c/bacon-meat-seafood-grocery/-/N-4tgi9',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
}

params = {
    'key': '9f36aeafbe60771e321a7cc95a78140772ab3e96',
    'category': '4tgi9',
    'channel': 'WEB',
    'count': '24',
    'default_purchasability_filter': 'true',
    'include_sponsored': 'true',
    'offset': '0',
    'page': '/c/4tgi9',
    'platform': 'desktop',
    'pricing_store_id': '3264',
    'scheduled_delivery_store_id': '324',
    'store_ids': '3264,3353,320,1407,2768',
    'useragent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'visitor_id': '018005E0CDB10201AEBAFF00C9B0FB29',
}

target_bacon = requests.get('https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v1', params=params, cookies=cookies, headers=headers)

target_bacon_data = target_bacon.json()
target_result_items = target_bacon_data['data']['search']['products']
# print(target_data['data']['search']['products'][0]['item']['product_description']['title'])

product_url = []
product_name = []
product_price = []

for result in target_result_items:
    # Product URL
    product_url.append(result['item']['enrichment']['buy_url'])

    # Product Name
    product_name.append(result['item']['product_description']['title'])

    # Product Price
    product_price.append(result['price']['formatted_current_price'])

print(product_name)
