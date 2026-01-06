import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# Get credential values
client_id = os.environ.get("e246c06be2ef4d96b0a7c89b9e2a8189")
client_secret = os.environ.get("90d70000d68e41188c47a17af29e703e")