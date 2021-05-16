import sqlite3
PlayerName = ""


def insert_signupvalues_database(name, password):
    global PlayerName
    conn = sqlite3.connect('database\SevenStones.db')
    cursor = conn.cursor()
    PlayerName = name
    cursor.execute('''INSERT INTO login(
       Name, Password) VALUES 
       (?, ?)''', (name, password))
    conn.commit()
    conn.close()


def checkforlogin(name, password):
    global PlayerName
    PlayerName = name
    conn = sqlite3.connect('database\SevenStones.db')
    cursor = conn.cursor()
    temp = cursor.execute('''SELECT Name, Password from login WHERE Name=(?)''', (name,))
    conn.commit()
    passw = ''
    for i in temp:
        n, passw = i
    conn.close()
    return password == passw


def gethighscore():
    sql = "SELECT Score FROM login WHERE Name = ?;"
    conn = sqlite3.connect('database\SevenStones.db')
    cursor = conn.cursor()
    scores = cursor.execute(sql, (PlayerName,))
    conn.commit()
    score = ""
    print(scores)

    for i in scores:
        score = i[0]
        print(i)
    conn.close()

    return int(score) if score else 0


def getcoins():
    sql = "SELECT Coins FROM login WHERE Name = ?;"
    conn = sqlite3.connect('database\SevenStones.db')
    cursor = conn.cursor()
    coins = cursor.execute(sql, (PlayerName,))
    conn.commit()
    coin =  ""
    for i in coins:
        coin = i[0]
    conn.close()
    return int(coin) if coin else 0

def updatecoins(coins):
    sql = "UPDATE login SET Coins = ? WHERE Name = ?;"
    conn = sqlite3.connect('database\SevenStones.db')
    cursor = conn.cursor()
    cursor.execute(sql, (coins, PlayerName))
    conn.commit()
    conn.close()


def updatehighscore(score):
    sql = "UPDATE login SET Score = ? WHERE Name = ?;"
    conn = sqlite3.connect('database\SevenStones.db')
    cursor = conn.cursor()
    cursor.execute(sql, (score, PlayerName))
    conn.commit()
    conn.close()


def updatedefaultball(ball):
    sql = "UPDATE login SET Ball = ? WHERE Name = ?;"
    conn = sqlite3.connect('database\SevenStones.db')
    cursor = conn.cursor()
    cursor.execute(sql, (ball, PlayerName))
    conn.commit()
    conn.close()


def updatepurchase(ball):
    sql = "UPDATE login SET Purchased = ? WHERE Name = ?;"
    conn = sqlite3.connect('database\SevenStones.db')
    cursor = conn.cursor()
    cursor.execute(sql, (ball, PlayerName))
    conn.commit()
    conn.close()


def getpurchased():
    sql = "SELECT Purchased FROM login WHERE Name = ?;"
    conn = sqlite3.connect('database\SevenStones.db')
    cursor = conn.cursor()
    purchases = cursor.execute(sql, (PlayerName,))
    conn.commit()
    purchase = ""
    for i in purchases:
        purchase = i[0]
    conn.close()
    return purchase


def getdefaultball():
    sql = "SELECT Ball FROM login WHERE Name = ?;"
    conn = sqlite3.connect('database\SevenStones.db')
    cursor = conn.cursor()
    balls = cursor.execute(sql, (PlayerName,))
    conn.commit()
    ball = ""
    for i in balls:
        ball = i[0]
    conn.close()
    return ball

updatepurchase('red')