"""
Example: full AliExpress product details (variants, stock, shipping, store) via the Apify Python client.
Requires: pip install apify-client   and   APIFY_TOKEN in the environment.
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "productUrls": [{"url": "https://www.aliexpress.com/item/1005006639944031.html"}],
    "searchKeywords": ["desk lamp"],
    "maxProductsPerKeyword": 10,
    "shipTo": "US",
    "currency": "USD",
    "maxItems": 20,
}

print("Running magic-scraper/aliexpress-product-details-scraper on Apify...")
run = client.actor("magic-scraper/aliexpress-product-details-scraper").call(run_input=run_input)
print(f"Run finished: {run['status']}\n")

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    ship = item["shipping"][0] if item["shipping"] else {}
    print(item["title"][:80])
    print(f"  Price: {item['price']}-{item['priceMax']} {item['currency']} | discount: {item.get('discountPercent')}%")
    print(f"  Rating: {item.get('rating')} ({item['reviewCount']} reviews) | {item.get('soldText')} | stock: {item.get('totalStock')}")
    print(f"  Variants: {len(item['skus'])} | ships from {ship.get('shipFrom')} in {ship.get('deliveryDaysMin')}-{ship.get('deliveryDaysMax')} days")
    print(f"  Store: {item['store']['name']} ({item['store'].get('positiveRate')}% positive)")
    print(f"  URL:   {item['url']}\n")
