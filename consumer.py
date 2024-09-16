from kafka import KafkaConsumer
import json
import mysql.connector

# Kafka broker and topic configuration
KAFKA_BROKER = 'localhost:9092'
TOPIC = 'weather-data'

# MySQL configuration
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'  # Update as necessary
MYSQL_PASSWORD = 'saransh'
MYSQL_DATABASE = 'weather_db'

# Set up Kafka consumer
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=[KAFKA_BROKER],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Set up MySQL connection
cnx = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)
cursor = cnx.cursor()

# Define the SQL query to insert data
insert_query = """
INSERT INTO weather_data (weather_main, weather_description, main_temp, main_feels_like, main_temp_min, main_temp_max, main_humidity)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

# Continuously process messages from Kafka
for message in consumer:
    data = message.value

    # Extract required fields from the data
    weather_main = data['weather'][0]['main']
    weather_description = data['weather'][0]['description']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    humidity = data['main']['humidity']

    # Prepare data for insertion
    values = (weather_main, weather_description, temp, feels_like, temp_min, temp_max, humidity)

    # Insert data into MySQL
    cursor.execute(insert_query, values)
    cnx.commit()

    print(f"Inserted data: {values}")

# Close the database connection (though this part will never be reached in this loop)
cursor.close()
cnx.close()
