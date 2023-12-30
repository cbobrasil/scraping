import requests
from bs4 import BeautifulSoup
import psycopg2

url = "https://books.toscrape.com/"

response = requests.get(url) # Get the response from the URL
if response.status_code == 200: # Check if the request was successful
    print("Request successful")
else:
    print("Request failed")

# Create a soup object to parse the html content
soup = BeautifulSoup(response.text, "html.parser") # Parse the HTML
print(soup)


# find all 20 books on page 1
books = soup.find_all("article", class_="product_pod")

# Iterate through the books and extract the information for each book
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").get_text().strip()
    rating = book.p["class"][1]
    stock = book.find("p", class_="instock availability").get_text().strip()
    
    connection = psycopg2.connect(host='localhost', user='postgres', password='senha', dbname='postgres')
    cur = connection.cursor()

    cur.execute("""INSERT INTO books (title, price, rating) VALUES (%s, %s, %s)""", (
        title,
        price, 
        rating
    ))

    connection.commit()
    cur.close()
    connection.close()
    