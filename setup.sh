
import sqlite3

conn = sqlite3.connect('clear-read.db')
print("Opened database successfully")
conn.close()

export DATABASE_NAME=clear-read
export AUTH0_DOMAIN=clear-read.eu.auth0.com
export ALGORITHMS=['RS256']
export API_AUDIENCE=https://clear-read/
# export FLASK_APP=app.py
# export FLASK_ENV=development
