from openai import AsyncOpenAI # dzieki temu możemy pracować asynchronicznie, czyli kilka zapytań jednocześnie
from dotenv import load_dotenv
import asyncio

load_dotenv()

client = AsyncOpenAI()


async def main():
    questions = [
        "How much is 2+2",
        "What is the difference between list and tuple",
        "What is the capital city od Poland"
    ]

    future_objects = []
    for q in questions:
        future_objects.append(
            client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": q
                    }
                ],
                model="gpt-3.5-turbo"
            )
        )
    return await asyncio.gather(*future_objects)

# awai musi byc zeby wiedzial, ze ma zaczekac na wszystkiego wyniki
# *rozpakowuje zbior


for response in asyncio.run(main()):
    print(response.choices[0].message.content)
    print('----------------------------')