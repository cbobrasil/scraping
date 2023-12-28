postgres 

 CREATE TABLE IF NOT EXISTS books(
            id serial PRIMARY KEY, 
            title text,
            price text,
            rating text
);
