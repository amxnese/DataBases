import sqlite3

# connect to database
conn = sqlite3.connect('app.db')
cur = conn.cursor()

# create user table
cur.execute("""
  create table if not exists user(
  user_id integer primary key,
  name varchar(50),
  skill varchar(50)
  );
""")

cur.execute('''
  create table if not exists admin(
  admin_id integer primary key,
  name varchar(50)
  )
''')

admins = ["amine","samuel","mohamed","adam"]
for i in range(len(admins)):
  try:
    cur.execute('insert into admin (admin_id, name) values(?, ?)', (i+1, admins[i]))
  except sqlite3.IntegrityError as e:
    print(e)

# Commit the changes
conn.commit()

# Close the connection
conn.close()
