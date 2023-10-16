import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from faker import Faker

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

def insert_fake_data(engine, num_records=100):
    # Start a connection
    with engine.connect() as connection:
        # Insert fake data into patients
        for _ in range(num_records):
            MRN = fake.unique.random_number(digits=10)
            connection.execute(f"INSERT INTO patients (MRN) VALUES ('{MRN}')")
        
        # Fetch all patient IDs
        patient_ids = [row[0] for row in connection.execute("SELECT patient_id FROM patients").fetchall()] # Noqa: E501
        
        # Insert fake data into demographics
        for patient_id in patient_ids:
            first_name = fake.first_name()
            last_name = fake.last_name()
            date_of_birth = fake.date_of_birth(minimum_age=10, maximum_age=90)
            address = fake.address().replace('\n', ', ')
            phone_number = fake.phone_number()
            email = fake.email()
            connection.execute(f"""
                INSERT INTO demographics (patient_id, first_name, last_name,
                                date_of_birth, address, phone_number, email)
                VALUES ({patient_id}, '{first_name}', '{last_name}', '{date_of_birth}', 
                '{address}', '{phone_number}', '{email}') 
            """)

if __name__ == "__main__":
    insert_fake_data(db_engine)
    print("Fake data insertion complete!")
