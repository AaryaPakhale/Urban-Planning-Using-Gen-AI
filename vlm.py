from groq import Groq
from dotenv import load_dotenv
import os
import base64
import json


def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def get_city_planning_suggestions(issue, pic):
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")

    client = Groq()
    Groq.api_key = api_key

    base64_image = encode_image(pic)
    with open("prompt.txt", "r") as f:
        prompt = f.read()
    prompt = prompt + issue
    print(prompt)
    completion = client.chat.completions.create(
        model="llama-3.2-11b-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        }
                    }
                ]
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        # response_format={"type": "json_object"},
        stop=None,
    )
    
    # return completion.choices[0].message.content
    output = completion.choices[0].message.content
    text_output = output["solutions"]  # Exclude coordinates
    coordinates = output["coordinates"]  # Separate coordinates

    return text_output, coordinates
# Example usage:
# issue = "The city is facing severe accommodation issues. The city planner aims to increase affordable housing units by 20%, enhancing social equity."
# pic = "https://upload.wikimedia.org/wikipedia/commons/1/1c/Map_of_LA_City_Council_Districts.png?20130207203753"
# print(get_city_planning_suggestions(issue, pic))
