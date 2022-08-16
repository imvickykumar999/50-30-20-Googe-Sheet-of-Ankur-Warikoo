
class flask_sheet:
    def __init__(self, 
            url = 'https://docs.google.com/spreadsheets/d/14XZFGM8UN8DDga7dH30t8ycYjHeGG-w9gDk_5hI8rns/edit?usp=sharing',
            jfile = 'cred.json',
        ):

        from oauth2client.service_account import ServiceAccountCredentials as sac
        import gspread, os

        scope = ['https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive']

        self.jfile = os.path.join('./cred', jfile)
        creds = sac.from_json_keyfile_name(self.jfile, scope)
        client = gspread.authorize(creds)

        self.url = url        
        self.sheet = client.open_by_url(self.url)


    def mark(self, sheet_id, row, fill):
        worksheet_up = self.sheet.get_worksheet_by_id(sheet_id)
        worksheet_up.update(row, fill, raw=False)

        # worksheet_up.update(f'A{row+1}', f"=A2+{row})", raw=False)
        # worksheet_up.update(f'C{sz+1}', f"=SUM(C2:C{sz})", raw=False)


    def fetch(self, sheet_id):
        sheet_instance = self.sheet.get_worksheet_by_id(sheet_id)
        records_data = sheet_instance.get_all_records()

        import pandas as pd
        df = pd.DataFrame(records_data) 
        df.index += 1
        return df


# ------------------------------------------


obj = flask_sheet()
# sheet_id = int(input('Enter sheet ID : '))

sheet_id = 0
your_salary = 400000
year = 2021

head = ['Year', 'Starting Salary',
        'Increment', 'Ending Salary', 
        'Needs', 'Wants', 'Investments', 
        'Needs %', 'Wants %', 'Investments %']

body = [year, 0 , 0, 
        your_salary, '=D2*H2/12',
        '=I2*D2/12', '=J2*D2/12',
        '=50%', '=30%', '=20%']


obj.mark(sheet_id, 'A1', [head])
obj.mark(sheet_id, 'A2', [body])

for i in range(3, 12):
    var = [f'=A{i-1}+1', f'=D{i-1}', f'=10%*B{i}',
           f'=B{i}+C{i}', f'=E{i-1}+C{i}*$J${i-1}/12',
           f'=F{i-1}+C{i}*$I${i-1}/12',
           f'=G{i-1}+C{i}*$H${i-1}/12', f'=E{i}*12/$D{i}',
           f'=F{i}*12/$D{i}', f'=G{i}*12/$D{i}']

    obj.mark(sheet_id, f'A{i}', [var])


df = obj.fetch(sheet_id)
print(df)
