import psycopg2
from flask import Flask, jsonify
import os

def create_connection():
    connection = psycopg2.connect(
        host='192.168.20.97',
        port='5432',
        dbname='postgres',
        user='postgres1',
        password='1234'
    )
    return connection

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_users():
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM public."Amc_Road" LIMIT 10')  # Specify the schema name
        users = cursor.fetchall()
        for row in users:
            print(row)

        cursor.close()
        connection.close()
        # Return the users as JSON response
        return jsonify(users)
    except Exception as e:
        print("An error occurred:", str(e))
        return jsonify(error=str(e)), 500  # Return the error message as a JSON response with status code 500

 
if __name__ == '__main__':
    app.run()
