from os import getenv
from openai import OpenAI
from dotenv import load_dotenv
from json import loads
from functools import cache

load_dotenv()
key = getenv("API_KEY")
client = OpenAI(api_key=key)


@cache
def get_trip_details(city: str, number_of_days: int):
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "system",
                "content": "Jesteś doświadczonym przewodnikiem, który zwiedził cały świat i nie tylko zna standardowe miejsca, które warto odwiedzić, ale także potrafi wykazać się znajomością mniej znanych, ale wartych zobaczenia atrakcji. Chcę abyś stworzył dla mnie plan podróży.\n\nProszę o przygotowanie danych w formacie JSON dotyczących planu podróży do określonego przeze mnie miejsca na określoną liczbę dni dni. Interesuje mnie struktura, która zawiera listę dni z nazwanymi atrakcjami, ich opisami, współrzędnymi geograficznymi. Oto szczegółowa struktura, jakiej oczekuję:\n\n{\n  \"dni\": [\n    {\n      \"nazwaDnia\": \"string\",\n      \"atrakcje\": [\n        {\n          \"nazwa\": \"string\",\n          \"opis\": \"string\",\n          \"latitude\": float,\n          \"longitude\": float,\n        }\n      ]\n    }\n  ]\n}"
            },
            {
                "role": "user",
                "content": f"Przygotuj mi w takiej formie plan podróży do miasta  {city} na {number_of_days} dni. Zwróć wyłącznie plaintext zawierający plik json bez żadnych dodatkowych informacji."
            }
        ],
        temperature=1,
        max_tokens=1390,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    #return response.choices[0].message tak było oryginalnie w kodzie
    return response.choices[0].message


#while True:
city = input('Do jakiego miasta jedziesz? ')
days = int(input('Na ile dni się wybierasz? '))

trip_list = get_trip_details(city, days)
#print(type(trip_list))


for trip_plan in trip_list:
    print(trip_plan)
