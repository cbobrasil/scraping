import requests
from bs4 import BeautifulSoup
import psycopg2

# Função para obter informações de uma página
def scrape_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Request successful for {url}")
        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")
        book_data = []
        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").get_text().strip()
            rating = book.p["class"][1]
            book_data.append((title, price, rating))
        return book_data
    return []

# Conectar ao banco de dados
connection = psycopg2.connect(host='localhost', user='postgres', password='senha', dbname='postgres')
cur = connection.cursor()

# Iterar sobre as páginas de 1 a 50
for page_num in range(1, 51):
    url = f'https://books.toscrape.com/catalogue/page-{page_num}.html'
    page_data = scrape_page(url)
    
    # Inserir informações no banco de dados
    for data in page_data:
        cur.execute("""INSERT INTO books (title, price, rating) VALUES (%s, %s, %s)""", data)
        connection.commit()

# Fechar a conexão
cur.close()
connection.close()
