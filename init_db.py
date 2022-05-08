import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="chatbot_db",
        user=os.environ['emma'],
        password=os.environ['12345678'])
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS users;')
cur.execute('CREATE TABLE users (id serial PRIMARY KEY, email varchar(255) NOT NULL, password varchar(255) NOT NULL);')
cur.execute('INSERT INTO users (email, password) VALUES ("emma","12345678");')
cur.execute('DROP TABLE IF EXISTS chats;')
cur.execute('CREATE TABLE chats (id serial PRIMARY KEY, content TEXT NOT NULL, created_at timestamp DEFAULT CURRENT_TIMESTAMP, user_id integer NOT NULL, message_from_bot BOOLEAN NOT NULL);')
cur.execute('INSERT INTO chats ( content, user_id,message_from_bot) VALUES ("hi there",1,FALSE);')

conn.commit()
cur.close()
conn.close()