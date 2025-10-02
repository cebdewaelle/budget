from nicegui import ui
import os
import requests

API_URL = os.getenv("API_URL", "http://fastapi:8000")


@ui.page("/")
def index():
    ui.label("Hello from NiceGUI!")

    def call_api():
        r = requests.get(f"{API_URL}/")
        ui.label(f"API response: {r.json()}")

    ui.button("Call FastAPI", on_click=call_api)


ui.run(host="0.0.0.0", port=8080)
