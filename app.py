import pandas as pd
from googletrans import Translator
import yaml

def read_yaml(file_path):
    """
    Reads a YAML file and returns the content.

    Args:
    - file_path (str): Path to the YAML file.

    Returns:
    - dict: Content of the YAML file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            content = yaml.safe_load(file)
            return content
        except yaml.YAMLError as e:
            print(f"Error reading YAML file: {e}")
            return None

def translate_excel(input_file, output_file, src_lang='en', dest_lang='vi'):
    """
    Translates the contents of an Excel file from the source language to the destination language.

    Args:
    - input_file (str): Path to the input Excel file.
    - output_file (str): Path to save the translated Excel file.
    - src_lang (str): Source language code (default is 'en' for English).
    - dest_lang (str): Destination language code (default is 'vi' for Vietnamese).
    """
    # Initialize the translator
    translator = Translator()

    # Load the workbook
    excel_file = pd.ExcelFile(input_file)

    # Function to translate text
    def translate_text(text, src=src_lang, dest=dest_lang):
        try:
            # Perform the translation
            translated = translator.translate(text, src=src, dest=dest)
            return translated.text
        except Exception as e:
            print(f"Error translating {text}: {e}")
            return text

    # Create a dictionary to hold translated dataframes
    translated_sheets = {}

    # Iterate over each sheet in the Excel file
    for sheet_name in excel_file.sheet_names:
        df = pd.read_excel(input_file, sheet_name=sheet_name)

        # Translate each cell in the DataFrame
        for column in df.columns:
            df[column] = df[column].apply(lambda x: translate_text(str(x)) if pd.notnull(x) else x)

        # Store the translated dataframe with the corresponding sheet name
        translated_sheets[sheet_name] = df

    # Write the translated dataframes to a new Excel file with the same sheet names
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        for sheet_name, translated_df in translated_sheets.items():
            translated_df.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"Translation complete. Translated file saved as {output_file}")


conf = read_yaml('config.yaml')
# Example usage
translate_excel(conf['excel_path'], output_file=f"Translation_output.xlsx", src_lang=conf['src_lang'], dest_lang=conf['dest_lang'])
