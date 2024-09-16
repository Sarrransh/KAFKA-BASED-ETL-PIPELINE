
# Kafka-Based Weather Data Pipeline

This project demonstrates a data pipeline that fetches weather data from the OpenWeatherMap API, sends it to Kafka, and then processes the data to store it in a MySQL database. The pipeline components are managed using Docker.

## Project Structure

- `producer.py`: A Kafka producer that fetches weather data from the OpenWeatherMap API and sends it to Kafka.
- `consumer.py`: A Kafka consumer that retrieves data from Kafka and inserts it into a MySQL database.
- `docker-compose.yml`: Docker Compose configuration file for setting up Zookeeper, Kafka, and MySQL.
- `sql_commands.sql`: SQL commands to set up the MySQL database and table (for reference only).

## Prerequisites

1. **Docker**: Ensure Docker and Docker Compose are installed on your machine.

2. **API Key**: Obtain an API key from OpenWeatherMap and save it in a file named `api_key.py` with the following content:
    ```python
    API_KEY = 'your_openweather_api_key_here'
    ```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Sarrransh/KAFKA-BASED-ETL-PIPELINE.git
cd KAFKA-BASED-ETL-PIPELINE
```

### 2. Start Services with Docker Compose

In the root directory of the project, run the following command to start Zookeeper, Kafka, and MySQL using Docker Compose:

```bash
docker-compose up
```

This command will download the necessary Docker images and start the containers as defined in `docker-compose.yml`.

### 3. Create the Database and Table

Access the MySQL container:

```bash
docker exec -it <mysql_container_id> mysql -u root -p
```

Enter the MySQL root password (`saransh`) and execute the commands from `sql_commands.sql`:

```sql
-- Create the database
CREATE DATABASE IF NOT EXISTS weather_db;

-- Use the database
USE weather_db;

-- Create the table
CREATE TABLE IF NOT EXISTS weather_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    weather_main VARCHAR(255),
    weather_description VARCHAR(255),
    main_temp DECIMAL(5,2),
    main_feels_like DECIMAL(5,2),
    main_temp_min DECIMAL(5,2),
    main_temp_max DECIMAL(5,2),
    main_humidity INT
);
```

### 4. Start the Producer

In a new terminal, navigate to the project directory and run:

```bash
python producer.py
```

The producer will start fetching weather data from OpenWeatherMap and sending it to the Kafka topic `weather-data`.

### 5. Start the Consumer

In another terminal, navigate to the project directory and run:

```bash
python consumer.py
```

The consumer will start retrieving data from the Kafka topic `weather-data` and inserting it into the MySQL database.

## Notes

- **Kafka Topics**: The Kafka topic used in this project is `weather-data`. Ensure that this topic is created before running the producer and consumer. If needed, you can create topics using Kafka command-line tools.
- **Data Interval**: The producer fetches data every 10 seconds. Adjust this interval as necessary by modifying the `time.sleep(10)` line in `producer.py`.

## Troubleshooting

- **Connection Issues**: Ensure that Docker containers are running and properly configured. Use `docker-compose ps` to check the status of the containers.
- **Logs**: Check logs of the containers using `docker logs <container_id>` if you encounter issues.

