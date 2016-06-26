import os
from decouple import config

# Statement for enabling the development environment
DEBUG = config('DEBUG')

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', config('SQLALCHEMY_DATABASE_URI'))

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = config('THREADS_PER_PAGE')

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = config('CSRF_SESSION_KEY')

# Secret key for signing cookies
SECRET_KEY = config('SECRET_KEY')

SQLALCHEMY_TRACK_MODIFICATIONS = True
