from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)
api = Api(app)

def create_db_connection():
    try:
        connection = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="root",
            host="192.168.20.97",
            port="5432"
        )
        return connection
    except Exception as e:
        print("Error while connecting to the database:", e)
        return None

class VideoUpload(Resource):
    def post(self):
        try:
            conn = create_db_connection()

            if conn is None:
                return {'error': 'Database connection failed'}, 500

            cursor = conn.cursor()

            print("Form Data:", request.form)  # Print the entire form data for debugging

            file_name = request.form.get('file_name')
            title = request.form.get('title')

            cursor.execute("INSERT INTO videos (file_name, title) VALUES (%s, %s)", (file_name, title))
            conn.commit()

            cursor.close()
            conn.close()

            return {'message': 'Video uploaded successfully'}, 201
        except Exception as e:
            return {'error': str(e)}, 500




api.add_resource(VideoUpload, '/upload')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
