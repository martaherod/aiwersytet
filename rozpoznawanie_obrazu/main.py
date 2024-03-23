from dotenv import load_dotenv
from openai import OpenAI

def get_base64_from_image(src: str) -> str:
    with open(src, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")


load_dotenv()

client = OpenAI()

image_src = "hokej.jpg"
prompt = "Describe what you see in the picture"

response = client.chat.completions.create(
    model="gpt-4=vision-preview",
    messages=[
        {
            "role":"user",
            "content": [
                {
                    "type": "text",
                    "text": prompt
                }, {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{get_base64_from_image(image_src)}"
                }
            ]
        }
    ]
)