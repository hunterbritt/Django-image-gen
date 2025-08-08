import requests
import os
import json

from dotenv import load_dotenv

DEFAULT_PAYLOAD = {
        "prompt": "",
        "num_results": 1,
        "sync": True,
        "prompt_enhancement": "true",
        "enhance_image": "true",
        "negative_prompt": "",
        "seed": -1,
        # "aspect_ration": "",
        # "steps_num": "",
        # "text_guidance_scale": "",
        # "medium": "",
        # "prompt_content_moderation": "",
        # "content_moderation": "",
        # "ip_signal": ""
    }



load_dotenv()

def _hd_image_gen(api_key: str, prompt: str, *args, **kwargs):
    """
    This is a helper function responsible for generating HD images
    """

    model_version="3.2"
    URL = f"{os.getenv("BASE_IMAGE_GENERATIONS")}{model_version}"

    payload = DEFAULT_PAYLOAD
    payload['prompt'] = prompt
    payload['negative_prompt'] = "Logo,Watermark,Ugly,Morbid,Extra fingers,Poorly drawn hands,Mutation,Blurry,Extra limbs,Gross proportions,Missing arms,Mutated hands,Long neck,Duplicate,Mutilated,Mutilated hands,Poorly drawn face,Deformed,Bad anatomy,Malformed limbs,Missing legs,Too many fingers, deformity, missing body parts"


    headers = {
        "Content-Type": "application/json",
        "api_token": api_key
    }

    try:
        print("Generating...")
        response = requests.post(url=URL, json=payload, headers=headers)

        response.raise_for_status()

        response_data = response.json()

        return response_data
    except Exception as e:
        return e