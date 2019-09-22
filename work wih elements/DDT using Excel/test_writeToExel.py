import openpyxl

def test_write_to_exel():
    fNAmeORPath = r"buddy.xlsx"
    workbook = openpyxl.load_workbook(fNAmeORPath)
    sheet=workbook.active

    for r in range(1,6):
        for c in range(1,4):
            sheet.cell(row=r,column=c).value = "test"

    workbook.save(fNAmeORPath)