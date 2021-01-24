import gspread

gc = gspread.service_account('credentials.json')

# Open a sheet from a spreadsheet in one go
wks = gc.open("john-mcclane-bot").sheet1

# Update a range of cells using the top left corner address
wks.update('A1', [[1, 2], [3, 4]])
