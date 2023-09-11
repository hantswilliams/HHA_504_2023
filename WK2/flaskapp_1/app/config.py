import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

"""

Environment Variables: The os.environ.get() method is used to fetch values from environment variables. This is a best practice as it helps to keep sensitive configuration values, like database connection strings or mail credentials, outside of your codebase. If an environment variable is not set, a default value is used.

Secret Key: This is a key used for securely signing the session cookie and for protecting against CSRF attacks. It's essential to keep it secret. In a real-world scenario, you'd likely have a unique key for every environment, and it would be sourced from an environment variable or secret management service.

Database Config: Shows how you might set up a default database connection string. In this case, it defaults to a SQLite database named site.db.

Mail Config: If your application involves sending emails (like for password resets), you'd have email configuration parameters.

"""


class Config:
    # Secret key for session management and CSRF protection
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_hard_to_guess_string'
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Mail server configuration (used for password resets and other notifications)
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.googlemail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    # Other configuration items can go here...

