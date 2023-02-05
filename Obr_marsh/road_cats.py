import openpyxl as xl


workbook = xl.load_workbook('Ведомость.xlsx', data_only=True)

sheet_names = workbook.sheetnames


reg_list = [x for x in sheet_names if workbook[x]['B2'].value == 'региональной']
fed_list = [x for x in sheet_names if workbook[x]['B2'].value == 'федеральной']
mest_list = [x for x in sheet_names if workbook[x]['B2'].value == 'местной']

print(reg_list)
print(fed_list)
print(mest_list)




