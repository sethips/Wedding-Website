from WeddingWebsite.secrets import DB_HOST_TEST

# Enable the TESTING flag to disable the error catching during request handling
# so that you get better error reports when performing test requests against the application.
TESTING = True

# Disable CSRF tokens in the Forms (only valid for testing purposes!)
WTF_CSRF_ENABLED = False

# Connect to the test DB
MONGO_URI = DB_HOST_TEST
