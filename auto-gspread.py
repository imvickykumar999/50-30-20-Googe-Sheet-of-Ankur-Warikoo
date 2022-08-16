
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


    def mark(self, attend, sheet_id,
                 top = ['Shipping Date', 'Location Reached', 'Delivery Charge']):
        
        import datetime
        dt = datetime.datetime.now()
        dt += datetime.timedelta(days = 0, hours = 5, minutes = 30)
        dt = str(dt).split()

        attend.insert(0, ' / '.join(dt)) # inserting at index 0, in list.
        print(attend)
        worksheet_up = self.sheet.get_worksheet_by_id(sheet_id)

        worksheet_up.update('A1', [top])
        worksheet_up.format("A1:C1", {
            "horizontalAlignment": "CENTER",
            "textFormat": {
            "foregroundColor": {
                "red": 1.0,
                "green": 0.0,
                "blue": 0.0
            },
            "fontSize": 10,
            "bold": True
            }
        })

        sz = len(worksheet_up.col_values(1))
        if sz == 1:
            sz=2

        worksheet_up.update(f'A{sz}', [attend])
        worksheet_up.format(f'A{sz}', {"textFormat": {"bold": False}}) 

        if top == ['Purchased Date', 'Objects', 'Cost']:
            worksheet_up.format(f'A{sz}', {"textFormat": {"bold": False}})
            
            worksheet_up.format(f'B{sz}', {"textFormat": {"bold": False}})
            worksheet_up.format(f'C{sz}', {"textFormat": {"bold": False}})

            worksheet_up.update(f'A{sz+1}', ' / '.join(dt))
            worksheet_up.format(f'A{sz+1}', {"textFormat": {"bold": True}}) 

            worksheet_up.update(f'B{sz+1}', 'Total Cost')
            worksheet_up.format(f'B{sz+1}', {"textFormat": {"bold": True}})

            worksheet_up.update(f'C{sz+1}', f"=SUM(C2:C{sz})", raw=False)
            worksheet_up.format(f'C{sz+1}', {"textFormat": {"bold": True}}) 
        else:
            worksheet_up.update(f'A{sz+1}', 'Customer Added')
            worksheet_up.format(f'A{sz+1}', {"textFormat": {"bold": True}}) 

        body = {
            "requests": [
                {
                    "autoResizeDimensions": {
                        "dimensions": {
                            "sheetId": sheet_id,
                            "dimension": "COLUMNS",
                            "startIndex": 0,  # Please set the column index.
                            "endIndex": 3  # Please set the column index.
                        }
                    }
                }
            ]
        }
        self.sheet.batch_update(body) 


    def add_cust(self, cust):
        try:
            worksheet = self.sheet.add_worksheet(title = cust, rows="100", cols="20")
            attend = [cust, worksheet.id]
            top = ['Shipping Date', 'Customer ID @ PINCODE', 'Worksheet ID']
            self.mark(attend, 0, top)
            return worksheet.id
        
        except Exception as e:
            return e


    def fetch(self, sheet_id):
        sheet_instance = self.sheet.get_worksheet_by_id(sheet_id)
        records_data = sheet_instance.get_all_records()

        import pandas as pd
        df = pd.DataFrame(records_data) 
        df.index += 1
        return df


# ------------------------------------------

obj = flask_sheet()
print(obj)

cust = input('Enter Your Name : ') 
sheet_id = obj.add_cust(cust) 
print(sheet_id)

saman = input('Enter Saman : ')
cost = float(input('Enter Cost : '))
attend = [saman, cost] 

# sheet_id = int(input('Enter sheet ID : '))
obj.mark(attend, sheet_id)

df = obj.fetch(sheet_id)
print(df)
