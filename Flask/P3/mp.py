from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL connection settings
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = ''  # Replac with your MySQL password
app.config['MYSQL_DB'] = 'raj'  # Replace with your MySQL database name

mysql = MySQL(app)

@app.route('/')
def index():
    # Example: Fetch data from a MySQL table
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM c2c')  # Replace with your actual table name
    data = cur.fetchall()
    cur.close()

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
