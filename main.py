import requests
import streamlit as sl
import os


@sl.fragment(run_every="24h")
def fetch_random_image():
	url = os.getenv("API_URL")
	request = requests.get(url)
	data = request.json()

	image = requests.get(data["urls"]["full"])

	with open("image.png", "wb") as file:
		file.write(image.content)

	sl.image("image.png")


sl.set_page_config(layout="wide")
fetch_random_image()