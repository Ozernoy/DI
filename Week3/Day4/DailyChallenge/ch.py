from psycopg2 import sql
import requests
import random
import sys
import os


# Go up one level from the current directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the specific folder in the parent directory to the system path
specific_folder = os.path.join(parent_dir, 'ExerciseXP')
sys.path.append(specific_folder)
# Now you can import the module from the specific folder
from utils import Utils


new_db_name = "countries_db"

try:
    Utils.db_high_level(new_db_name, 'create')

    conn = Utils.get_connection(new_db_name)
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute(sql.SQL("""
        CREATE TABLE IF NOT EXISTS Countries (
            id SERIAL PRIMARY KEY, 
            name VARCHAR(100) NOT NULL, 
            capital VARCHAR(100), 
            flag TEXT, 
            subregion VARCHAR(100), 
            population BIGINT
        )
    """))


    response = requests.get("https://restcountries.com/v3.1/all")
    if response.status_code == 200:
        countries_data = response.json()
    else:
        raise Exception("Failed to fetch data from the REST Countries API")

    random_countries = random.sample(countries_data, 10)


    for country in random_countries:
        name = country.get("name", {}).get("common", "Unknown")
        capital = country.get("capital", ["Unknown"])[0] if country.get("capital") else "Unknown"
        flag = country.get("flags", {}).get("png", "")
        subregion = country.get("subregion", "Unknown")
        population = country.get("population", 0)

        cursor.execute(sql.SQL("""
            INSERT INTO Countries (name, capital, flag, subregion, population)
            VALUES (%s, %s, %s, %s, %s)
        """), (name, capital, flag, subregion, population))

    cursor.execute(sql.SQL("SELECT * FROM Countries"))
    countries = cursor.fetchall()
    print("Countries added to the database:")
    for country in countries:
        print(country)

    # Close cursor and connection
    cursor.close()
    conn.close()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Ensure all connections to the database are closed before attempting to drop it
    Utils.terminate_connections(new_db_name)
    
    # Ensure the database is deleted
    Utils.db_high_level(new_db_name, 'delete')
    print(f"Database {new_db_name} has been deleted.")
