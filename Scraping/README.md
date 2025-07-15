# 🕷️ Real Estate Web Scraper

This module is responsible for extracting real estate listing data from three of the most popular Azerbaijani property websites:  
**[Bina.az](https://bina.az)**, **[Emlak.az](https://emlak.az)**, and **[Arenda.az](https://arenda.az)**.

The scraper is designed to run in an automated and parallelized fashion, handling dynamic web pages, anti-bot measures, and structured data extraction. Collected data is cleaned and pushed to a Microsoft SQL Server database for downstream use in analytics and machine learning.

---

## ⚙️ Technologies Used

- **Web Automation**: `Selenium`, `undetected-chromedriver`
- **Parsing**: `BeautifulSoup`
- **Threading & Parallelism**: `threading`, `ThreadPoolExecutor`, `queue`
- **Data Handling**: `pandas`, `numpy`, `re`, `json`
- **Storage**: `pyodbc`, `SQLAlchemy` (to MS SQL Server)
- **Utilities**: `os`, `time`, `random`, `warnings`, `requests`, `base64`

---

## 📦 Python Modules

```text
bs4
selenium
webdriver-manager
undetected-chromedriver
time
random
os
base64
pandas
numpy
re
json
requests
pyodbc
sqlalchemy
threading
queue
concurrent.futures
warnings
```

---

## 🧠 Features

- ✅ Anti-bot evasion via `undetected_chromedriver`
- ✅ Fully scrolls pages before collecting data
- ✅ Extracts listing URLs and scrapes each individually
- ✅ Cleans and transforms fields before storage
- ✅ Pushes clean data into normalized SQL Server tables
- ✅ Multithreaded scraping for speed and performance
- ✅ Handles timeouts, missing fields, duplicates

---

## 🗃️ Output Format

Scraped data is stored in a normalized **OLTP schema** in Microsoft SQL Server, with separate tables for:

- `EstateListing`  
- `Apartment`, `House`, `Office`, `CommercialProperty`, `Garage`, `Land`  
- `SellerInfo`, `URL`, `ListingImages`, `Description`, `Labels`

---

## ⚠️ Disclaimer

This web scraper is built and maintained **strictly for educational and research purposes**.  
All data has been collected from publicly available sources and is **not used for any commercial, resale, or competitive intent**.

If any content owner or website representative has concerns, they are encouraged to reach out, and the relevant data will be promptly removed.

> **This project is not affiliated with Bina.az, Emlak.az, or Arenda.az in any way.**

---

⭐ Feel free to fork, star, or contribute to this project if you're working on data engineering with real estate datasets.
