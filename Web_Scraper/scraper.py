import requests
from bs4 import BeautifulSoup


URL = "http://books.toscrape.com/"

def fetch_book_data(url):
    """
    Belirtilen URL'den kitap verilerini çeker ve listeler.
    """
    try:
        
        response = requests.get(url)
        response.raise_for_status() 

        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        books = []
        
        articles = soup.find_all('article', class_='product_pod')

        for article in articles:
            title_tag = article.find('h3').find('a')
            price_tag = article.find('p', class_='price_color')
            
            book_info = {
                'title': title_tag['title'],
                'price': price_tag.text.strip(),
            }
            books.append(book_info)

        return books

    except requests.exceptions.RequestException as e:
        print(f"Hata: Web sitesine bağlanılamadı: {e}")
        return []

if __name__ == "__main__":
    book_list = fetch_book_data(URL)
    
    if book_list:
        print("\n--- Çekilen Kitap Listesi ---")
        for book in book_list:
            print(f"Başlık: {book['title']} | Fiyat: {book['price']}")
        print("------------------------------\n")
    else:
        print("Veri çekme işlemi başarısız oldu.")
