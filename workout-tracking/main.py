import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv("../.env")

NUTRITION_API_ID = os.environ.get("NUTRITION_API_ID")
NUTRITION_API_KEY = os.environ.get("NUTRITION_API_KEY")

# TODO: 1. Using the Nutritionix "Natural Language for Exercise" API Documentation, figure out how to print the exercise stats for plain text input.

