# `50:30:20 Rule` of Budgeting on Googe Sheet of Ankur Warikoo

# `f(x)` : [excel formula tutorial](https://www.ablebits.com/office-addins-blog/google-sheets-formula-basics/)

[![image](https://user-images.githubusercontent.com/50515418/184592308-9d76c347-670d-4939-b52a-5bc86ac9ee3c.png)](https://docs.google.com/spreadsheets/d/1tE4GtSjirvwpsrkREkCDKIK1Jhx1k2R7/edit?usp=sharing&ouid=117512306766539133793&rtpof=true&sd=true)

-------------------------

# API Calls in [Google Sheets](https://docs.google.com/spreadsheets/d/1SYWpE0tS5F_g5dnhNRqqY0I20KsK8o3HA5EnV2VDEis/edit?usp=sharing)

    function callNumbers() {

      // Call the Numbers API for random math fact
      var response = UrlFetchApp.fetch("https://api.metalpriceapi.com/v1/latest?base=USD&currencies=XAU,XAG&api_key=Dxt3fx5NcET88EGsAtvrdJ");
      Logger.log(response.getContentText());

      var fact = response.getContentText();
      var sheet = SpreadsheetApp.getActiveSheet();
      sheet.getRange(sheet.getLastRow() + 1,1).setValue([fact]);

    }
