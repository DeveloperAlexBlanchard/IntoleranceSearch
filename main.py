import requests
import pandas as pd
from bs4 import BeautifulSoup
from lxml import etree

params = {
    'key': '9f36aeafbe60771e321a7cc95a78140772ab3e96',
    'tcins': '12945916,12944662,47968936,82553151,12945914,12944662,82553182,82553152,12945916,12945913,52503436,14871956,14871956,82553153,52805209,14899123,14871957,47968936,14871958,79605571,82553181,52233735,53329213,81783782',
    'required_store_id': '3264',
    'has_required_store_id': 'true',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

response = requests.get('https://redsky.target.com/redsky_aggregations/v1/web_platform/product_summary_with_fulfillment_v1', params=params)
results_json = response.json()

# Number of Results
num_results = int(len(results_json['data']['product_summaries']))


result_item = results_json['data']['product_summaries']

# # Product Name
# print(result_item['item']['product_description']['title'])

# # Product Price
# print(result_item['price']['current_retail'])

# # Product URL
# print(result_item['item']['enrichment']['buy_url'])

product_name = []
product_price = []
product_url = []

item_num = 0
search = True
while search == True:
    for name in result_item:
        if item_num != num_results:
            product_name.append(result_item[item_num]['item']['product_description']['title'])
            item_num += 1
        if item_num == num_results:
            print(product_name)
            item_num = 0
            for price in result_item:
                if item_num != num_results:
                    product_price.append(result_item[item_num]['price']['current_retail'])
                    item_num += 1
                if item_num == num_results:
                    print(product_price)
                    item_num = 0
                    for url in result_item:
                        if item_num != num_results:
                            product_url.append(result_item[item_num]['item']['enrichment']['buy_url'])
                            item_num += 1 
                        if item_num == num_results:
                            print(product_url)
                            search = False
