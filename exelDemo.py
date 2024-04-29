import openpyxl
book=openpyxl.load_workbook("C:\\Users\\surya\\OneDrive\\Desktop\\PythonDemo.xlsx")
sheet=book.active
cell=sheet.cell(row=1, column=2)
print(cell.value)