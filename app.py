import openpyxl
from googletrans import Translator
# pip install openpyxl googletrans==4.0.0-rc1

def translate_sheet(input_file, output_file, src='pt', dest='en'): # Troque a linguagem como preferir, Default == | src='pt', dest='en' |
    workbook = openpyxl.load_workbook(input_file)
    translator = Translator()

    for sheet in workbook.worksheets:
        for row in sheet.iter_rows():
            for cell in row:
                if isinstance(cell.value, str):
                    try:
                        translated = translator.translate(cell.value, src=src, dest=dest).text
                        cell.value = translated
                    except Exception as e:
                        print(f"Erro na tradução: '{cell.value}': {e}")
                        continue

    workbook.save(output_file)
    print(f"Tradução Completa, Arquivo: {output_file}")

if __name__ == "__main__":
    translate_sheet("input.xlsx", "translated_output.xlsx") # Coloque o nome dos arquivos, Default == | "input.xlsx", "translated_output.xlsx" |