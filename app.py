import sqlite3
# connecting to database
conn = sqlite3.connect('app.db')
cur = conn.cursor()

# fetching admins
admins = cur.execute('select admin_id from admin').fetchall()
# looping through each tuple in the list that fetchall() created
admins = [admin[0] for admin in admins]

# grabbing the user's name
user_id = int(input("please insert your id:  "))

# case where the given id is valid
if user_id in admins:
    # fetching admin's name
    name = cur.execute('select name from admin where admin_id = ?', (user_id,)).fetchone()[0]

    # fetching users
    cur.execute("select * from user").fetchall()

    print(f"hello {name} welcome to the database of yours")
    print(cur.fetchall())
# case where the given id is not valid
else:
    raise NameError("invalid id")

command_list = ["a","u","d","s","q"]
input_var ='''
what command do you want to apply
"a" ==> add user
"u" ==> update user
"d" ==> delete user
"s" ==> show users
"q" ==> quit database
Choose an option:
'''

def commit():
    conn.commit()
    conn.close()

user_input = input(f"{input_var} ==>  ")

def add_user():
    try:
        # getting new user information from the admin
        name = input(f"enter the new user's name:   ").lower().strip()
        skill = input("enter the new user's skill:   ").lower().strip()
        # inserting new user into database
        cur.execute(f"insert into user(name, skill) values(?, ?)", (name, skill))
        print("user added succesfully")
    # case where given id is not valid
    except Exception as e:
        print(f"an error has occured: {e}")  

def update_user():
    # getting the to be updated user's id from admin
    user_id = int(input("enter the id of the user you want to update:  "))
    # quering the given user id
    users = cur.execute('select user_id from user').fetchall()
    users = [user[0] for user in users]
    # case where user id exists
    if user_id in users:
        # getting the to be updated user's info from admin
        name = input("enter user's new name:  ")
        skill = input("enter user's new skill:  ")
        # updating user's info
        cur.execute('update user set name = ? , skill = ? where user_id = ?',(name, skill, user_id))
        print('user updated')
    else:
        print('user id not found')

def delete_user():
    user_id = int(input("enter the user's you want to delete id:   "))
    users = cur.execute('select user_id from user').fetchall()
    users = [user[0] for user in users]
    # case where user exists
    if user_id in users:
        cur.execute(f"delete from user where user_id = {user_id}")
        print("user deleted succesfully")
    # case where user doesn't exist
    else:
        print('invalid user id')

def show_user():
    # fetching info
    cur.execute("select * from user")
    users = cur.fetchall()
    # printing info
    print(f"there are {len(users)} users stored in the database")
    for i in users:
        print(f"id: {i[0]}, username is: {i[1]}, skill: {i[2]}")

if user_input in command_list:
    try:
        if user_input == "a":
            add_user()
        elif user_input == "u":
            update_user()
        elif user_input == "d":
            delete_user()
        elif user_input == "s":
            show_user()
        else:
            print("closed database")
    except Exception as e:
        print(e)
    finally:
        commit()
else:
    print(f"invalid command")
