from flask import Flask
import pymysql
import os

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=os.getenv('MYSQL_HOST', 'db'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DB')
    )

@app.route('/')
def home():
    return "Flask + MySQL DevOps App 🚀"

@app.route('/data')
def data():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50))")
    cursor.execute("INSERT INTO users (name) VALUES ('Shrikant')")
    conn.commit()

    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return str(data)

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
