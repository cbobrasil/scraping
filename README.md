This Project uses BeautifulSoup to extract data from the scraping website https://books.toscrape.com/

It saves the data on a local postgres database. The table that the data will e inserted was created manually using this SQL code : 

 CREATE TABLE IF NOT EXISTS books(
            id serial PRIMARY KEY, 
            title text,
            price text,
            rating text
);
