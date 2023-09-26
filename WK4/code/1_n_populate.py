import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from faker import Faker
import random

# Load environment variables
load_dotenv()

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

# Create a database engine
db_engine = create_engine(conn_string, echo=False)
fake = Faker()

specializations = ['Cardiology', 'Neurology', 'Pediatrics', 
                   'Orthopedics', 'Radiology', 'General Practice']

def insert_fake_data(engine, num_doctors=50, num_patients=100):
    # Start a connection
    with engine.connect() as connection:
        # Insert fake data into doctors
        for _ in range(num_doctors):
            first_name = fake.first_name()
            last_name = fake.last_name()
            specialization = random.choice(specializations)
            connection.execute(f"INSERT INTO doctors (first_name, last_name, specialization) VALUES ('{first_name}', '{last_name}', '{specialization}')") # Noqa: E501
        
        # Fetch all doctor IDs
        doctor_ids = [row[0] for row in connection.execute("SELECT doctor_id FROM doctors").fetchall()] # Noqa: E501
        
        # Insert fake data into patients
        for _ in range(num_patients):
            first_name = fake.first_name()
            last_name = fake.last_name()
            date_of_birth = fake.date_of_birth(minimum_age=10, maximum_age=90)
            primary_doctor_id = random.choice(doctor_ids)
            connection.execute(f"""INSERT INTO patients (first_name, last_name, date_of_birth, primary_doctor_id) VALUES ('{first_name}', '{last_name}', '{date_of_birth}', {primary_doctor_id})""") # Noqa: E501

if __name__ == "__main__":
    insert_fake_data(db_engine)
    print("Fake data insertion complete!")
