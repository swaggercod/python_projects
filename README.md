# 🕸️ Simple Web Scraper (Python)

This project is a demonstration of fetching and processing data from the web using Python. It simulates extracting product information from an e-commerce platform.

## 🛠️ Key Skills Demonstrated (Relevant to Job Applications)

* **HTTP Requests:** Using the `requests` library to manage web communication.
* **Web Scraping/Parsing:** Utilizing `BeautifulSoup4` for efficient HTML parsing and data extraction.
* **Data Structuring:** Organizing the extracted raw data (Title, Price) into a usable Python dictionary format.
* **Dependency Management:** Defining project requirements in `requirements.txt`.

## ⚙️ How It Works (`scraper.py`)

The script targets a specific public demo website, sends an HTTP GET request, and parses the HTML content. It isolates product elements (book titles and prices) and prints the structured data to the console.

## 📝 Status

**Current Status:** Completed (Core data fetching and parsing logic working).

**Future Improvements (WIP):**
* Saving the final data to a structured format (CSV or JSON).
* Implementing pagination to scrape multiple pages automatically.
* Adding user-agent rotation to handle anti-scraping measures.
