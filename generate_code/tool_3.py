import ast
import asyncio
from json import loads

from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AsyncOpenAI()

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def get_code_from_openai(function_name: str, pydoc: str):
    return client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "system",
          "content": "I will give you the name of the function and its documentation. Your task will be to write code of this function in the following format.  I would like it to be a JSON object in which the name of the function will be the key, while its value will be the code of this function.\n\nReturn only the json without any extra text like ```json. "
        },
        {
          "role": "user",
          "content": f"Function name:  {function_name}\n\nPydoc of the function: {pydoc}"
        },
      ],
      temperature=1,
      max_tokens=750,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )


def get_functions_from_file(filename):
    with open(filename, 'r') as file:
        tree = ast.parse(file.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                yield node


async def generate_code_for_files(filename):
    future_objects = []
    for function in get_functions_from_file(filename):
        future_objects.append(get_code_from_openai(function.name, ast.get_docstring(function)))

    return await asyncio.gather(*future_objects)


file_to_generate = 'code/ex_2.py'
# asyncio.run(generate_code_for_files(file_to_generate))
# to tworzy listę jsonów, wiec trzeba ja najpierw jakby rozpakowac do listy

with open('result.py', 'w') as output_file:
    for response in asyncio.run(generate_code_for_files(file_to_generate)):
        for function_name, function_code in loads(response.choices[0].message.content).items():
            output_file.write(function_code)

        output_file.write('\n\n')



