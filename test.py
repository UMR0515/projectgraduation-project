import openpyxl
wb = openpyxl.load_workbook("test.xlsx")
ws = wb.active
ws.delete_rows(1)
wb.save("test.xlsx")