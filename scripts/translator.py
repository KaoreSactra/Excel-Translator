from google.cloud import translate_v2 as translate
import xlwings as xw
import time
import os
# pip install xlwings google-cloud-translate

# Crie uma chave de serviço com o google cloud API translator
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

def translate_sheet(input_file, output_file, src='en', dest='pt'): # Troque a linguagem como preferir, Default == | src='en', dest='pt' |
    translate_client = translate.Client()
    app = xw.App(visible=False)
    workbook = app.books.open(input_file)

    for sheet in workbook.sheets:
        used_range = sheet.used_range
        values = used_range.value

        if values is None:
            continue

        for i, row in enumerate(values):
            for j, cell in enumerate(row):
                if isinstance(cell, str) and cell.strip():
                    try:
                        translated = translate_client.translate(cell, source_language=src, target_language=dest)['translatedText']
                        values[i][j] = translated
                        time.sleep(0.1) # Evita sobrecarga na API
                    except Exception as e:
                        print(f"Erro na tradução: '{cell}': {e}")
                        continue

        used_range.value = values

    workbook.save(output_file)
    workbook.close()
    app.quit()
    print(f"Tradução Completa, Arquivo: {output_file}")

if __name__ == "__main__":
    # Coloque o nome dos arquivos, Default == | "copy.xlsx", "output.xlsx" |
    translate_sheet("sheets/copy.xlsx", "sheets/output.xlsx")
