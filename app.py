from flask import Flask, render_template, request,jsonify,redirect,url_for,json,session
import sqlite3
mydict={
    "tech":["ecell","kp","stac","kbg","saic","nirman","yantrik"],
    "lit":["qurosity","uhlekh","tsod"],
    "cult":["designauts","artgeeks","dance","drama","music","pmc","spicmacy"]
}
app = Flask(__name__, static_url_path='/static')
app.secret_key = 'your_secret_key'

@app.route('/')
def index():

    return render_template('home_final.html')

@app.route('/login', methods=['GET','POST'])
def login():
    # Replace 'your_database_name.db' with the actual name of your SQLite database file
    db_file = 'login.db'

    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    if request.method == 'POST':
        user_id = request.form.get('idinput')
        password = request.form.get('password')
        session['user_id'] = user_id 
    # Example query: select all rows from a table named 'user_credentials'
        query = f"SELECT * FROM user_credentials WHERE userid = ? AND password = ?"
        cursor.execute(query, (user_id, password))

    # Fetch the result
        result = cursor.fetchone()

    # Close the cursor and connection
        cursor.close()
        conn.close()
        # Get user input from the HTML form
    

        if result:
            # User is authenticated, handle redirection or other actions
            if user_id.startswith("club_member@") :
                return redirect(url_for('club_member_home'))
            elif user_id.startswith("club_fa@"):
                return redirect(url_for('club_fa_home'))
            elif user_id.startswith("club_cordy@s"):
                return redirect(url_for('club_member_home'))
            elif user_id.startswith("society_fa@"):
                return redirect(url_for('society_fa_home'))
            elif user_id.startswith("admin@"):
                return redirect(url_for('admin_home'))
            else:
                return "You are not an authorized user."
        else:
            return "Invalid credentials."
    
    return render_template('login.html')

@app.route('/admin_home')
def admin_home():
    return render_template('admin_home.html')
@app.route('/club_member_home')
def club_member_home():
    return render_template('club_member_home.html')
@app.route('/society_fa_home')
def society_fa_home():
    return render_template('society_fa_home.html')
@app.route('/submit_form', methods=['POST'])
def submit_form():
    try:
        # Assuming you have a SQLite connection and cursor
        # Replace 'your_database_name.db' with your actual database name
        conn = sqlite3.connect('login.db')
        cursor = conn.cursor()

        # Extract data from the JSON request
        club_name = request.form['clubName']
        monetary_fund = request.form['monetaryFund']
        appeal_text = request.form['appealText']
        

        # Insert data into the database
        cursor.execute('''
        INSERT INTO maindb(user_id, club_name, appeal_text, attachment_path, total_monetary_fund)
        VALUES (?, ?, ?, ?, ?)
        ''', (session.get('user_id', None), club_name, appeal_text, 'none', monetary_fund))


        # Commit the changes
        conn.commit()

        # Close the connection
        conn.close()

        return redirect(url_for('club_member_home'))
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})




@app.route('/get_message')
def get_message():
    conn = sqlite3.connect('login.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM acceptdb;')
    rows = cursor.fetchall()
    conn.close()

    data = []
    for row in rows:
        message = {
            'user': row[1],
            'club': row[2],
            'money': row[5],
            'appeal': row[3]
        }
        data.append(message)

    return jsonify(data)


@app.route('/add_data', methods=['POST'])
def add_data():
    try:
        data = request.get_json()

        # Extract values
        user = str(data.get('value1', ''))
        club = str(data.get('value2', ''))
        msgs = str(data.get('value3', ''))
        money = str(data.get('value4', ''))

        # Connect to the database
        conn = sqlite3.connect('login.db')
        cursor = conn.cursor()

        # Insert data into the acceptdb table
        cursor.execute('''
            INSERT INTO acceptdb (user_id, club_name, appeal_text, attachment_path, total_monetary_fund)
            VALUES (?, ?, ?, ?, ?)
            ''', (user, club, msgs, 'none', money))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        # Return a success r esponse
        return jsonify({'success': True, 'message': 'Data added successfully'})

    except Exception as e:
        # Log the error for debugging
        print(f"Error: {str(e)}")

        # Return an error response
        return jsonify({'success': False, 'error': str(e)})



@app.route('/club_fa_home')
def club_fa_home():
    return render_template('club_fa_home.html')
""" @app.route('/logout', methods=['POST'])
def logout():
    # Clear the user session
    session.pop('user_id', None)

    # Redirect to the login page or any other desired page after logout
    return render_template('login.html') """

@app.route('/get_messages')
def get_messages():
    
    conn = sqlite3.connect('login.db')
    cursor = conn.cursor()

    # Example query
    cursor.execute('SELECT * FROM maindb;')

    # Fetch all rows
    rows = cursor.fetchall()

    data = []
    for row in rows:
        message = {
            'user': row[1],
            'club': row[2],
            'requestedfund': row[5],
            'message': row[3],
        }
        if str(message['club']) in str(session.get('user_id', None)):
         data.append(message)

    conn.close()

    # Using jsonify directly within the route
    return jsonify(data)


# ... (your existing routes)
@app.route('/get_messages2')
def get_messages2():
    
    conn = sqlite3.connect('login.db')
    cursor = conn.cursor()

    # Example query
    cursor.execute('SELECT * FROM maindb;')

    # Fetch all rows
    rows = cursor.fetchall()
    societyname= str(session.get('user_id',None))[11:]

    data = []
    for row in rows:
        message = {
            'user': row[1],
            'club': row[2],
            'requestedfund': row[5],
            'message': row[3],
        }
        if str(message['club']) in mydict[societyname]:
         data.append(message)

    conn.close()

    # Using jsonify directly within the route
    return jsonify(data)
# New route for deleting a row
@app.route('/delete_row', methods=['POST'])
def delete_row():
    try:
        # Assuming you have a SQLite connection and cursor
        # Replace 'your_database_name.db' with your actual database name
        conn = sqlite3.connect('login.db')
        cursor = conn.cursor()

        # Extract data from the JSON request
        data = request.get_json()

        # Delete the row from the database
        cursor.execute('''
        DELETE FROM maindb
        WHERE appeal_text = ?
        ''', (data['message'],))


        # Commit the changes
        conn.commit()

        # Close the connection
        conn.close()

        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@app.route('/delete_1', methods=['POST'])
def delete_row_1():
    try:
        # Assuming you have a SQLite connection and cursor
        # Replace 'your_database_name.db' with your actual database name
        conn = sqlite3.connect('login.db')
        cursor = conn.cursor()

        # Extract data from the JSON request
        data = request.get_json()

        # Delete the row from the database
        cursor.execute('''
        DELETE FROM maindb
        WHERE appeal_text = ?
        ''', (data['user'],))


        # Commit the changes
        conn.commit()

        # Close the connection
        conn.close()

        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/logout', methods=['GET','POST'])
def logout():
    previous_route = request.referrer
    return render_template('logout_sure.html',previous_route=previous_route)


if __name__ == '__main__':
    app.run(debug=True)
