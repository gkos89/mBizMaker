import sqlite3
import urllib.request, urllib.parse, urllib.error
import ssl
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


conn = sqlite3.connect('wordbank.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Categories
    (cat_id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
     name       TEXT UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Types
    (type_id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
     name       TEXT UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Words
    (word_id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
     word       TEXT UNIQUE,
     type_id    INT,
     cat_id     INT)''')
