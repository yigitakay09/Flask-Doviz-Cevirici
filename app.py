from flask import Flask,render_template,request
import requests

api_key = "ee4c8bd85eb3236a5d94827b34e1cba8"
url = "http://data.fixer.io/api/latest?access_key=" + api_key

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        firstCurrency = request.form.get("firstCurrency")
        secondCurrency = request.form.get("secondCurrency")
        
        amount = request.form.get("amount")
        response = requests.get(url)
        app.logger.info(response)

        infos = response.json()

        firstValue = infos["rates"][firstCurrency]
        secondValue = infos["rates"][secondCurrency]

        result = (secondValue/firstValue) * float(amount)

        currencyInfo = dict()
        currencyInfo["firstCurrency"] = firstCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result

        return render_template("index.html",info = currencyInfo)
    else:
        return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)












