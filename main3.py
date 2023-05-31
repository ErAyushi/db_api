import psycopg2
from flask import Flask, jsonify
import os

def create_connection():
    connection = psycopg2.connect(
        host='192.168.20.97',
        port='5435',
        dbname='postgres',
        user='postgres',
        password='1234'
    )
    return connection

app = Flask(__name__)

@app.route('/query1', methods=['GET'])
def execute_query1():
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT "Restaurants" FROM public.restaurants')
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(result)
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/query2', methods=['GET'])
def execute_query2():
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM public.restaurants')
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(result)
    except Exception as e:
        return jsonify(error=str(e)), 500

# Add more routes and corresponding query functions as needed

if __name__ == '__main__':
    app.run(port=5003)

