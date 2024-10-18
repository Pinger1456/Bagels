"""
Receiving data of digits and maximum guesses
"""
import os
from dotenv import load_dotenv


load_dotenv()

NUM_DIGITS = int(os.getenv('NUM_DIGITS'))
MAX_GUESSES = int(os.getenv('MAX_GUESSES'))


