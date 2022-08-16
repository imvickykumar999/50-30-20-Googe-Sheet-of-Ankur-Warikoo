
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
