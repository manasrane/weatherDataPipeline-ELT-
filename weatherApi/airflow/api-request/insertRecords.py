import psycopg2
from requestApi import sampleRequestResponse
from datetime import datetime

def connect_to_db():
    print("Connecting to the postgreSQL database....")
    try:
        con = psycopg2.connect(
            host = "db",
            port = 5432,
            dbname = "db",
            user = "db_user",
            password = "db_password")
        return con
    except psycopg2.Error as e:
        print(f"ERROR TO CONNECT DB:{e}")
        raise

def create_table(conn):
    print("creating table")
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE SCHEMA IF NOT EXISTS dev;
        CREATE TABLE IF NOT EXISTS dev.raw_weather_data(
            id SERIAL PRIMARY KEY,
                       city TEXT,
                       temperature FLOAT,
                       weather_description TEXT,
                       wind_speed FLOAT,
                       time TIMESTAMP,
                       inserted_at TIMESTAMP DEFAULT NOW(),
                       utc_offset TEXT                          
                       );                 
                       """)
        conn.commit()
        print("TABLE was created.")

    except psycopg2.Error as e:
        print(f"FAILED TO CREATE TABLE:{e}")
        raise

def insert_records(con,data):
    print("Inserting weather data into db...")
    try:
        print(data['current'])
        weather = data['current']
        location = data['location']
        cursor= con.cursor()
        cursor.execute("""
                       INSERT INTO dev.raw_weather_data
                       (city,
                       temperature,
                       weather_description,
                       wind_speed,
                       time,
                       inserted_at,
                       utc_offset
                       ) VALUES (%s,%s,%s,%s,%s,NOW(),%s)
                       """,(location['name'],
                            weather['temperature'],
                            weather['weather_descriptions'][0],
                            weather['wind_speed'],
                            location['localtime'],
#                            datetime.now(),
                            location['utc_offset']))
        con.commit()
        print("Succesfully INSERTED")
    except psycopg2.Error as e:
        print(f"ERROR TO INSERT RECORD INTO DB:{e}")
        raise
def main():
    try:
        conn = connect_to_db()
        create_table(conn)
        data = sampleRequestResponse()
        insert_records(conn,data)
    except Exception as e:
        print(f"Exception : {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            print("Database Connection Closed")
main()