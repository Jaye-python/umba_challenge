import requests
import sqlite3
import argparse


# CREATE DATABASE
con = sqlite3.connect("user_database.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS github_users")
con.commit()

# CREATE TABLE
cur.execute("CREATE TABLE IF NOT EXISTS github_users (id INTEGER, username TEXT, avatar_url TEXT, type TEXT, url TEXT)")
con.commit()

# INITIATE THE '-t' and '--total' ARGUMENT
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--total", help = "Indicate total number of github users with which to seed the database")
args = parser.parse_args()

# CONNECT TO github API
url = "https://api.github.com/users"
response = requests.get(url)

# GRAB THE '-t' and '--total' ARGUMENT
if args.Output:
    payload = response.json()[:int(args.Output)]
else:
    payload = response.json()[:150]

# SEED THE DATABASE
for user in payload:
    cur.execute("INSERT INTO github_users VALUES (:id, :username, :avatar_url, :type, :url)", 
    {
        'id': user.get('id'),
        'username': user.get('login'),
        'avatar_url' : user.get('avatar_url'),
        'type' : user.get('type'),
        'url' : user.get('url'),
        
    })

    con.commit()

con.close()