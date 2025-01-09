from dotenv import load_dotenv
import os

load_dotenv()

# Configuration for the Anthropics API
API_KEY = os.getenv("ANTHROPIC_API_KEY")
MODEL = "claude-3-5-sonnet-20241022"
MAX_TOKENS = 1024
