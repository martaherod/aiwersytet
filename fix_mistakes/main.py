from dotenv import load_dotenv
import click
from openai import OpenAI
import os

load_dotenv()


class TextProcessor:
    def __init__(self, input_file, output_file, change_style=None, fix_punctuation_mistakes=False, fix_grammar_mistakes=False):
        # Przypisujemy wartości parametrów do właściwości instancji
        self.input_file = input_file
        self.output_file = output_file
        self.change_style = change_style
        self.fix_punctuation_mistakes = fix_punctuation_mistakes
        self.fix_grammar_mistakes = fix_grammar_mistakes
        self.client = OpenAI()

    def process_file(self):
        # Wyświetlamy wartości właściwości instancji
        print(f'Input file: {self.input_file}')
        print(f'Output file: {self.output_file}')
        print(f'Change style: {self.change_style if self.change_style else "None"}')
        print(f'Fix punctuation mistakes: {"Yes" if self.fix_punctuation_mistakes else "No"}')
        print(f'Fix grammar mistakes: {"Yes" if self.fix_grammar_mistakes else "No"}')

        with open(self.input_file, "r", encoding="utf8") as input_file, open(self.output_file, "w", encoding="utf8") as output_file:
            file_content = input_file.read()

            prompt = self._generate_prompt()
            prompt += "\n\n" + file_content

            processed_text = self._send_to_openai(prompt)

            output_file.write(processed_text)


    def _send_to_openai(self, prompt):
        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                    "role": "system",
                    "content": "You are responsible for repairing the text files. You will receive the content of the files in the prompt and the requirements for customizing these files. Please return only the content of the corrected file without any additional content. Result should be in the original language."
                },
                {"role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5,
            max_tokens=1002,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        click.echo(f'Tokens: {response.usage.total_tokens}')

        return response.choices[0].message.content


    def _generate_prompt(self):
        prompt = ["Please modify the text according to the following guidelines:"]

        if self.change_style:
            prompt.append(f'Change the writing style to {self.change_style}')

        if self.fix_punctuation_mistakes:
            prompt.append("Fix any punctuation mistakes")

        if self.fix_grammar_mistakes:
            prompt.append("Correct any grammar mistakes")

        return " ".join(prompt)


# Definiujemy funkcję, która będzie wywoływana po przekazaniu argumentów
@click.command()
@click.option('--input', 'input_file', required=True, type=click.Path(exists=True), help='Ścieżka do pliku wejściowego, który musi istnieć.')
@click.option('--output', 'output_file', required=True, help='Ścieżka do pliku wyjściowego, do którego zostaną zapisane wyniki.')
@click.option('--change-style', type=click.Choice(['formal', 'informal', 'friendly', 'aggresive'], case_sensitive=False), default=None, help='Opcjonalny styl zmiany tekstu.')
@click.option('--fix-punctuation-mistakes', is_flag=True, help='Opcjonalne flaga, która wskazuje czy poprawić błedy interpunkcyjne.')
@click.option('--fix-grammar-mistakes', is_flag=True, help='Opcjonalne flaga, która wskazuje czy poprawić błędy gramatyczne.')
def process_file(input_file, output_file, change_style, fix_punctuation_mistakes, fix_grammar_mistakes):
    click.echo (f'Input file: {input_file}')
    click.echo(f'Output file: {output_file}')
    click.echo(f'Change style: {change_style if change_style else "None"}')
    click.echo(f'Fix punctuation mistakes: {"Yes" if fix_punctuation_mistakes else "No"}')
    click.echo(f'Fix grammar mistakes: {"Yes" if fix_grammar_mistakes else "No"}')

    text_processor = TextProcessor(input_file, output_file, change_style, fix_punctuation_mistakes, fix_grammar_mistakes)
    text_processor.process_file()

if __name__ == '__main__':
    process_file()
