# Python-Assignment
To extract the popular (most frequent) queries done during a specific time range from a given log dataset.

This repository contains a Flask application that processes and filters queries from a TSV file based on a date prefix. The application exposes an API endpoint to count the number of unique queries for a given date prefix.

## Libraries and Techniques Used

Flask: A lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.
Pandas: A software library written for data manipulation and analysis in Python. In this application, it is used to read and manipulate the TSV file.
Datetime: A module in Python's standard library for manipulating dates and times. It is used here to convert the timestamp column in the DataFrame to datetime objects.

## Application Structure

The application is structured as follows:

parse_tsv_file: This function reads a TSV file using Pandas and converts the timestamp column to datetime objects.
filter_queries_by_date: Filters the DataFrame based on the date prefix and returns unique queries for that date.
get_query_count: An API endpoint that takes a date prefix as input, filters the queries by this date, and returns the count of unique queries.

## Running the Application

To run the application, ensure you have Python and the required libraries installed. Then, execute the following command in the terminal:

bash
python app.py


This will start the Flask development server, and you can access the application at http://127.0.0.1:5000/.

## API Endpoint

GET /1/queries/count/<date_prefix>: Returns the count of unique queries for the given date prefix.

## Example Usage

To get the count of unique queries for a specific date, make a GET request to the endpoint:

http
GET /1/queries/count/2015-08-03


This will return a JSON response with the count of unique queries for the date 2015-08-03

# Alternate Solution for Flask Application Using SQLAlchemy

This repository presents an alternate solution to the initial Flask application that processes and filters queries from a TSV file based on a date prefix. Instead of using Pandas for file reading and manipulation, this solution leverages Flask-SQLAlchemy for database operations, involving SQLite as the database engine.

## Key Features

- Flask-SQLAlchemy Integration: Utilizes Flask-SQLAlchemy to connect the Flask application to a SQLite database, enabling efficient data storage and retrieval.
- Database Model: Defines a Query model to represent the data structure in the SQLite database, facilitating the storage and manipulation of query data.
- API Endpoint: Provides an API endpoint that filters and counts unique queries based on a given date prefix, demonstrating how to query the database and process the results.









