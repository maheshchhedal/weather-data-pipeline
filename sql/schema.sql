CREATE DATABASE IF NOT EXISTS weather_pipeline;

USE weather_pipeline;

CREATE TABLE IF NOT EXISTS dim_city (
    city_id INT AUTO_INCREMENT PRIMARY KEY,
    city_name VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL
);

CREATE TABLE IF NOT EXISTS fact_weather_readings (
    reading_id INT AUTO_INCREMENT PRIMARY KEY,
    city_id INT,
    temperature FLOAT NOT NULL,
    min_temp FLOAT NOT NULL,
    max_temp FLOAT NOT NULL,
    humidity FLOAT NOT NULL,
    weather VARCHAR(100) NOT NULL,
    wind_speed FLOAT NOT NULL,
    visibility FLOAT NOT NULL,
    timestamp DATETIME NOT NULL,
    FOREIGN KEY (city_id) REFERENCES dim_city(city_id)
);