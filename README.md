# `50:30:20 Rule` of [Budgeting](https://github.com/imvickykumar999/50-30-20-Googe-Sheet-of-Ankur-Warikoo/blob/08d3dc734eccfb4d84cabe1f3ce21c8d09cdfa55/auto-gspread.py#L67) on Google Sheet of [Ankur Warikoo](https://www.youtube.com/watch?v=5uaXq-xDp2g)

![image](https://user-images.githubusercontent.com/50515418/184974014-c10bfc59-160c-4178-acd2-4f288223eedd.png)

------------------------

# `f(x)` : [excel formula tutorial](https://www.ablebits.com/office-addins-blog/google-sheets-formula-basics/)

        for i in range(3, 12):
            var = [f'=(A{i-1}+1)', f'=(D{i-1})', f'=(10%*B{i})',
                   f'=(B{i}+C{i})', f'=(E{i-1}+C{i}*$J$2/12)',
                   f'=(F{i-1}+C{i}*$I$2/12)',
                   f'=(G{i-1}+C{i}*$H$2/12)', f'=(E{i}*12/$D{i})',
                   f'=(F{i}*12/$D{i})', f'=(G{i}*12/$D{i})']

            obj.mark(sheet_id, f'A{i}', [var])
    
---------------------------------

> [![image](https://user-images.githubusercontent.com/50515418/185191663-5fe3bb82-d255-469a-99a2-5d8ba2169959.png)](https://docs.google.com/spreadsheets/d/14XZFGM8UN8DDga7dH30t8ycYjHeGG-w9gDk_5hI8rns/edit?usp=sharing)

-------------------------

# API Calls in [Google Sheets](https://docs.google.com/spreadsheets/d/1SYWpE0tS5F_g5dnhNRqqY0I20KsK8o3HA5EnV2VDEis/edit?usp=sharing)

        function callNumbers() {
          let url = "https://api.metalpriceapi.com/v1/latest?base=USD&currencies=XAU,XAG&api_key=Dxt3fx5NcET88EGsAtvrdJ";
          let fact = UrlFetchApp.fetch(url);

          let apiResponse = JSON.parse(fact.getContentText());
          Logger.log(apiResponse);

          const date = new Date(apiResponse.timestamp*1000);
          let unixdate = date.toLocaleDateString("en-IN");
          let unixtime = date.toLocaleTimeString("en-IN");

          let price = apiResponse.rates.XAU*100000000;
          console.log(unixdate, unixtime, price);

          let sheet = SpreadsheetApp.getActiveSheet();
          sheet.getRange(1,1).setValue("Unix Timestamp");
          sheet.getRange(1,2).setValue("Rate of Gold");

          sheet.getRange(sheet.getLastRow() + 1,1).setValue(unixdate + ' ' + unixtime);
          sheet.getRange(sheet.getLastRow() + 0,2).setValue(price);
        }

--------------------------------

# Auto Function Trigger : [StackOverflow](https://stackoverflow.com/a/9129775/11493297)

[![image](https://user-images.githubusercontent.com/50515418/184603569-3159874f-3939-43a5-91bd-ae71f1fe9cfd.png)](https://script.google.com/home/projects/18aYVuDMURltcEGcgES_MY2JpLVcMsPcPSmRFxPPZ_Xz9Aug5EcD1MOze/edit)
