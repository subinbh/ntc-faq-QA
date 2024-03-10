import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv() # Loading all the environment variable
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
