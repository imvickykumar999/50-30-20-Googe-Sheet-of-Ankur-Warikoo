# `50:30:20 Rule` of Budgeting on Googe Sheet of [Ankur Warikoo](https://www.youtube.com/watch?v=5uaXq-xDp2g)

![image](https://user-images.githubusercontent.com/50515418/184974014-c10bfc59-160c-4178-acd2-4f288223eedd.png)

# `f(x)` : [excel formula tutorial](https://www.ablebits.com/office-addins-blog/google-sheets-formula-basics/)

> [![image](https://user-images.githubusercontent.com/50515418/184974202-bb39d497-c314-4c26-8b8b-77fe5fa836b9.png)](https://docs.google.com/spreadsheets/d/1tE4GtSjirvwpsrkREkCDKIK1Jhx1k2R7/edit?usp=sharing&ouid=117512306766539133793&rtpof=true&sd=true)

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
