import xlwings as xw
# pip install xlwings

# Cria um clone sem proteção da planilha
def remove_protection_clone(input_file, output_file):
    app = xw.App(visible=False)
    original = app.books.open(input_file)
    new = app.books.add()

    default_sheet = new.sheets[0]

    for sheet in original.sheets:
        # Desprotege a planilha
        if sheet.api.ProtectContents:
            sheet.api.Unprotect()

        sheet.api.Copy(Before=new.sheets[0].api)

    default_sheet.delete()

    new.save(output_file)
    original.close()
    new.close()
    app.quit()
    print(f"Desbloqueio Completo, Arquivo: {output_file}")

if __name__ == "__main__":
    # Coloque o nome dos arquivos, Default == | "input.xlsx", "copy.xlsx" |
    remove_protection_clone("././sheets/input.xlsx", "././sheets/copy.xlsx")
