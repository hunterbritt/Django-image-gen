import requests
import os
import json

from dotenv import load_dotenv



load_dotenv()

def _hd_image_gen(api_key: str, prompt: str, *args, **kwargs):
    """
    This is a helper function responsible for generating HD images
    """

    model_version="2.2"
    URL = f"{os.getenv("HD_IMAGE_GENERATIONS")}{model_version}"

    payload = {
        "prompt": prompt,
        "num_results": 2,
        "sync": True,
        "seed": "738027405"
    }


    headers = {
        "Content-Type": "application/json",
        "api_token": api_key
    }

    try:
        response = requests.post(url=URL, json=payload, headers=headers)

        response.raise_for_status()

        response_data = response.json()

        return response_data
    except Exception as e:
        return e