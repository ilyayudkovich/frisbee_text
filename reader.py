from openpyxl import load_workbook
import datetime

currentDate = datetime.datetime.now()

wb = load_workbook('./docs/schedule.xlsx', read_only=True)
sheet = wb.get_sheet_by_name('Sheet1')
col = sheet['B1'].column

def max_row(ws):
    i = 0
    for row in ws.rows:
        i+=1
        for cell in row:
            continue
    return i

dates = [sheet.cell(row=i, column=2).value for i in range(2, max_row(sheet) + 1)]

def getDay():
    return currentDate.day

def getMonth():
    return currentDate.month

def getYear():
    return currentDate.year

def sameDay(date):
    return (getDay() == date.day and
           getMonth() == date.month and
           getYear() == date.year)

def practiceToday(dates):
    for d in dates:
        if sameDay(d):
            return True
    return False

print practiceToday(dates)


