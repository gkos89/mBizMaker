import sqlite3
import urllib.request, urllib.parse, urllib.error
import ssl
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup
from random import randint

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('wordbank.sqlite')
cur = conn.cursor()

# Get all the words currently in the database
cur.execute('''SELECT word FROM Words''')
words = list()
for row in cur:
    words.append(str(row[0]))


while True:
    userCatWords = list()
    # show categories & ask the user for a category number (1-5)
    print('''
    ==== WELCOME TO MILLENNIAL BUSINESS MAKER ====\n
    For millennials, only.\n
    What's in a name? Everything, that's what.
    We're here to help your pretentious,
    overpriced business go viral.\n
    Answer a few questions, and we'll create a
    business name so eye-popping, you'll need a
    new pair of horn-rimmed glasses.\n
    Hold onto your beanie.''')
    print('''
    ============ BUSINESS CATEGORIES =============\n
                 (1) animals
                 (2) food
                 (3) automotive
                 (4) finance
                 (5) art/design\n
    ==============================================
    ''')
    #ask the user for a biz category, or pick one at random
    userCat = input('''Which category best describes your business? Enter a category number (1-5), or just press enter to select at random:
''')
    if userCat == "" :
        userCat = str(randint(1,5))

    #ask the user to pick a word type for the first word, or pick one at random
    firstWordType = input('''\nShould the first word be a noun(1), an adjective(2), a verb(3), or random(enter)?
''')
    if firstWordType == "" :
        firstWordType = str(randint(1,3))

    # ask the user to pick a word type for the first word, or pick one at random
    if firstWordType == "2" :
        secondWordType = input('''\nShould the second word be an adjective(2), a verb(3), or random(enter)?
''')
    elif firstWordType == "3" :
        secondWordType = input('''\nShould the second word be a noun(1), an adjective(2), or random(enter)?
''')
    else :
        secondWordType = input('''\nShould the second word be a noun(1), an adjective(2), a verb(3), or random(enter)?
''')

    if secondWordType == "":
        if firstWordType == "2" :
            secondWordType = str(randint(2,3))
        elif firstWordType == "3" :
            secondWordType = str(randint(1,2))
        else :
            secondWordType = str(randint(1,3))

    # pull a random word from the database where cat_id = userCat
    cur.execute('SELECT * FROM Words WHERE cat_id = ? and type_id = ? ORDER BY RANDOM() LIMIT 1', (userCat,firstWordType))
    for row in cur :
        userCatWords.append(str(row[1]))

    # pull another random word from the database where cat_id = userCat
    cur.execute('SELECT * FROM Words WHERE cat_id = ? and type_id = ? and word != ? ORDER BY RANDOM() LIMIT 1', (userCat,secondWordType,userCatWords[0]))
    for row in cur :
        userCatWords.append(str(row[1]))

    # select a conjunction
    conjunctions = ["and","&","+","\'n\'"]
    rand_conj = conjunctions[randint(0,3)]


    #print(userCatWords[0],"&",userCatWords[1])
    print('''
    ==============================================\n
        Your new milliennial business name is:\n
              ****''',userCatWords[0].capitalize(),rand_conj,userCatWords[1].capitalize(),"****")
    print('''
    ==============================================\n
    ''')

    goAgain = input("Press [any key]+[enter] to create another, or just press [enter] to quit.")
    if not goAgain : break
    print(goAgain)

cur.close()
quit()
