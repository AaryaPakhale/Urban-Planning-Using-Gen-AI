from groq import Groq
from dotenv import load_dotenv
import os
import base64


def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def get_city_planning_suggestions(issue, pic):
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")

    client = Groq()
    Groq.api_key = api_key

    base64_image = encode_image(pic)

    completion = client.chat.completions.create(
        model="llama-3.2-11b-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "You are an expert city planner who is experienced in suggesting appropriate suggestions given the map of a region and the issues that are currently being faced in the region. You might also be provided with other information about the project, such as possible budget, economic, and ecological conditions of the area. Whenever you give a suggestion, you should make sure it doesn't create new problems and that the solution is equitable and good for all. After you have given the suggestions I would also like you to give an image prompt that I can pass to a diffusion model that will alter my original map to the map after these changes are made. So your final output should contain the following: 1. Issues identified, 2. Possible Fix, 3. Feasibility Analysis, 4. Image Prompt\n\nIssue:\n" + issue
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
        stop=None,
    )

    return completion.choices[0].message.content

# Example usage:
# issue = "The city is facing severe accommodation issues. The city planner aims to increase affordable housing units by 20%, enhancing social equity."
# pic = "https://upload.wikimedia.org/wikipedia/commons/1/1c/Map_of_LA_City_Council_Districts.png?20130207203753"
# print(get_city_planning_suggestions(issue, pic))
