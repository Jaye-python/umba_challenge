import requests
import sqlite3
import argparse
import pandas as pd
from pathlib import Path
import psycopg2

# INITIATE THE '-t' and '--total' ARGUMENT
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--total", help = "Indicate total number of github users with which to seed the database")
args = parser.parse_args()

# CONNECT TO github API
url = "https://api.github.com/users"
response = requests.get(url)

# GRAB THE '-t' and '--total' ARGUMENT
if args.total:
    payload = response.json()[:int(args.total)]
else:
    payload = response.json()[:150]


# CHECK IF DJANGO SETTINGS.PY (CONFIG FILE) EXISTS
file_path = "C:/Users/Jaye/Desktop/New Folder/scripts/umba/umbaproject/settings.py"
my_file = Path(file_path)

# CREATE POSTGRES CONNECTION
conn = psycopg2.connect(user='postgres', password = '', database='umba_db', host='localhost' )
cursor = conn.cursor()

for user in payload:
    if my_file.exists():  
        sql = "INSERT INTO github_githubusersdb (id, username, avatar_url, type, url) VALUES (%s, %s,%s, %s,%s)"
        val = (user.get('id'), user.get('login'), user.get('avatar_url'), user.get('type'), user.get('url') )
        cursor.execute(sql, val)
        conn.commit()
        
    else:
        con = sqlite3.connect("github_users.db")
        cur = con.cursor()

        # CREATE TABLE IF NOT AVAILABLE
        cur.execute("CREATE TABLE IF NOT EXISTS github_users (id INTEGER, username TEXT, avatar_url TEXT, type TEXT, url TEXT)")
        con.commit()

        # SEED THE DATABASE
        cur.execute("INSERT INTO github_users VALUES (:id, :username, :avatar_url, :type, :url)", 
        {
            'id': user.get('id'),
            'username': user.get('login'),
            'avatar_url' : user.get('avatar_url'),
            'type' : user.get('type'),
            'url' : user.get('url'),   
        })
        con.commit()



# OPTIONAL: PRINTS THE DATABASE OBJECTS AS PANDAS DATAFRAME FROM DB FOR CONFIRMATION AND DEBUGGING
if my_file.exists():
    cursor.execute("SELECT * FROM github_githubusersdb")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=[ 'id', 'username', 'avatar_url', 'type', 'url'])
    print (df)
    conn.close()

else:
    cur.execute("SELECT *, oid FROM github_users")
    rows = cur.fetchall()
    df = pd.DataFrame(rows, columns=[ 'id', 'username', 'avatar_url', 'type', 'url', 'oid'])
    print (df)
    con.close()