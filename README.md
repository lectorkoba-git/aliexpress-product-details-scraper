# 🛒 AliExpress Product Details Scraper

[![AliExpress Product Details Scraper](https://apify.com/actor-badge?actor=magic-scraper/aliexpress-product-details-scraper)](https://apify.com/magic-scraper/aliexpress-product-details-scraper)
![Free Tier](https://img.shields.io/badge/Apify%20Free%20Tier-$5%20Monthly%20Credit-blue?style=flat-square)
![Pay-Per-Result](https://img.shields.io/badge/Pricing-$4.00%20%2F%201K%20products-blue?style=flat-square)
![No Login](https://img.shields.io/badge/Login-Not%20Required-success?style=flat-square)
![Export](https://img.shields.io/badge/Export-JSON%20|%20CSV%20|%20Excel-orange?style=flat-square)

Python examples and API reference for the **[AliExpress Product Details Scraper](https://apify.com/magic-scraper/aliexpress-product-details-scraper)** on Apify: full product records from URLs, IDs or search keywords — **every variant with its price and stock, shipping options with delivery days, ratings, units sold, specifications, seller documents and store stats** — for the ship-to country and currency you choose.

> ⚡ **No code needed:** 👉 **[Run it in your browser on Apify (free $5 monthly credit)](https://apify.com/magic-scraper/aliexpress-product-details-scraper)**

---

## 🎯 Who is this for?

- **Dropshippers** — check variant stock, warehouse location and delivery days before listing a product.
- **Price monitoring tools** — schedule daily runs and track price and stock per SKU.
- **Product researchers** — collect sales, ratings and store reputation for any keyword.

---

## 📌 Key Facts

| | |
| :--- | :--- |
| **Pricing** | $4.00 per 1,000 products + $0.00005 start fee per GB of run memory; skipped or failed products are not charged |
| **Run time (measured)** | ~10 s for 100 products (2026-10-30) |
| **Countries** | Prices, stock and shipping for your ship-to country (US, DE, GB, FR, PL, BR, ...) in any currency |
| **Unknown values** | `null` — nothing is guessed or filled with placeholders |
| **Login / cookies** | Not required |

### ⚠️ Limitations

- Individual review texts and the full HTML description are not included (you get rating, review count, `descriptionUrl`, specifications and documents).
- Titles are in English for every country.
- US-only listings (IDs starting with `3256`) are usually not sold to other countries and are skipped there.

---

## 🚀 Quickstart (Python)

```bash
pip install apify-client
export APIFY_TOKEN=your_token   # https://console.apify.com/settings/integrations
python example.py
```

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("magic-scraper/aliexpress-product-details-scraper").call(run_input={
    "productIds": ["1005006639944031"],
    "shipTo": "DE",
    "currency": "EUR",
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["title"][:60], item["price"], item["currency"], "stock:", item["totalStock"])
```

---

## 📥 Input

| Parameter | Type | Default | Description |
| :--- | :--- | :---: | :--- |
| `productUrls` | `array` | — | Product pages on any AliExpress domain, app share links, affiliate links |
| `productIds` | `array[string]` | — | Bare product IDs |
| `searchKeywords` | `array[string]` | — | Find products by keyword and scrape their details |
| `maxProductsPerKeyword` | `integer` | `20` | Search results per keyword |
| `maxItems` | `integer` | `50` | Max products saved per run |
| `shipTo` | `string` | `"US"` | Country for prices, stock and shipping |
| `currency` | `string` | `"USD"` | Currency for all prices |
| `maxConcurrency` | `integer` | `25` | Parallel IP sessions |
| `proxyConfiguration` | `object` | Apify Proxy | Residential IPs are used automatically |

---

## 📤 Output Fields

| Field | Type | Description |
| :--- | :--- | :--- |
| `productId` / `url` | `string` | Product ID and URL |
| `title` | `string` | Product title |
| `price` / `priceMax` | `number` | Lowest and highest variant price |
| `originalPrice` / `originalPriceMax` | `number \| null` | Price before discount |
| `discountPercent` | `integer \| null` | Discount in percent |
| `currency` / `shipTo` | `string` | Currency and ship-to country of the record |
| `rating` / `reviewCount` | `number \| null` / `integer` | Star rating and number of reviews |
| `soldCount` / `soldText` | `integer \| null` / `string \| null` | Units sold |
| `totalStock` | `integer \| null` | Stock across all variants |
| `images` / `video` | `array` / `string \| null` | Gallery and product video |
| `categoryId` / `categoryPath` | `string` | AliExpress category |
| `attributes` | `array` | Specifications (`name`, `value`) |
| `skuProperties` | `array` | Variant options (color, size, ships from, ...) |
| `skus` | `array` | Every variant: `skuId`, `attributes`, `price`, `originalPrice`, `stock`, `maxBuyCount`, `available` |
| `shipping` | `array` | `method`, `code`, `fee`, `freeShipping`, `shipFrom`, `shipTo`, `deliveryDaysMin/Max`, `estimatedDelivery`, `tracking` |
| `store` | `object` | `id`, `name`, `url`, `sellerId`, `positiveRate`, `rating`, `soldLast180Days`, `country`, `openedAt`, `topRatedSeller` |
| `descriptionUrl` | `string \| null` | AliExpress description page |
| `documents` | `array` | Seller documents such as PDF manuals |
| `searchKeyword` | `string \| null` | Keyword the product was found with |
| `scrapedAt` | `string` | ISO 8601 timestamp |

A full real sample record is in the [Actor README on Apify](https://apify.com/magic-scraper/aliexpress-product-details-scraper).

---

## 🔗 Related Scrapers

- [Temu Trending Products Scraper](https://apify.com/magic-scraper/temu-trending-products-scraper)
- [Etsy Bestsellers & Tags Scraper](https://apify.com/magic-scraper/etsy-bestsellers-tags-scraper)
- [eBay Seller Contact Scraper](https://apify.com/magic-scraper/ebay-seller-contact-scraper)

---

## 📄 License

MIT — see [LICENSE](LICENSE). This repository contains usage examples; the scraper itself runs on [Apify](https://apify.com/magic-scraper/aliexpress-product-details-scraper).
