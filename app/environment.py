from dotenv import load_dotenv
import os

load_dotenv()

auth_api_base_url = os.getenv('AUTH_API_BASE_URL')
auth_api_client_id = os.getenv('AUTH_API_CLIENT_ID')
auth_api_client_secret = os.getenv('AUTH_API_CLIENT_SECRET')
