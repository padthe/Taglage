from dotenv import load_dotenv
import os

# Ladda .env-filen
load_dotenv()

# Hämta API-nyckeln
api_key = os.getenv('API_KEY')
