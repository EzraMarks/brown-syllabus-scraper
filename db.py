import sqlite3

# Create connection to database
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Delete tables if they exist
c.execute('DROP TABLE IF EXISTS "syllabi";')

# DONE: Create tables in the database and add data to it. REMEMBER TO COMMIT
c.execute('''
    CREATE TABLE syllabi (
        symbol VARCHAR(255) NOT NULL PRIMARY KEY,
        link VARCHAR(255)
    );
''')
conn.commit()

links = ["link1", "link2", "link3"]

for link in links:
    c.execute('INSERT INTO syllabi VALUES (?, ?)',
        (link, "link"))
    conn.commit()