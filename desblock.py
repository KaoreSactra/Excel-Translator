import xlwings as xw

def remove_protection_clone(input_file, output_file):
    app = xw.App(visible=False)
    original = app.books.open(input_file)
    new = app.books.add()

    for sheet in original.sheets:
        copied = new.sheets.add(name=sheet.name)
        sheet.api.UsedRange.Copy(Destination=copied.range("A1").api)

    new.sheets[0].delete()
    new.save(output_file)
    original.close()
    new.close()
    app.quit()

if __name__ == "__main__":
    remove_protection_clone("input.xlsx", "clean_copy.xlsx")