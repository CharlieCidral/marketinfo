import csv
import io
from flask import Flask, render_template, request, Response
import yfinance as yf
import pandas as pd

app = Flask(__name__)

def get_stock_data(ticker, view_option):
    if view_option == "info":
        return yf.Ticker(ticker).info
    elif view_option == "actions":
        return yf.Ticker(ticker).actions
    elif view_option == "dividends":
        return yf.Ticker(ticker).dividends
    elif view_option == "splits":
        return yf.Ticker(ticker).splits
    elif view_option == "capital_gains":
        return yf.Ticker(ticker).capital_gains
    elif view_option == "shares":
        return yf.Ticker(ticker).get_shares_full(start="2022-01-01", end=None)
    elif view_option == "income_stmt":
        return yf.Ticker(ticker).income_stmt
    elif view_option == "balance_sheet":
        return yf.Ticker(ticker).balance_sheet
    elif view_option == "cashflow":
        return yf.Ticker(ticker).cashflow
    elif view_option == "holders":
        return yf.Ticker(ticker).major_holders
    elif view_option == "earnings_dates":
        return yf.Ticker(ticker).earnings_dates
    elif view_option == "isin":
        return yf.Ticker(ticker).isin
    elif view_option == "options":
        return yf.Ticker(ticker).options
    elif view_option == "news":
        return yf.Ticker(ticker).news
    else:
        return "Invalid view option."
    # Add other options here...

@app.route("/save_csv", methods=["POST"])    
def save_csv():
    ticker = request.form["ticker"]
    view_option = request.form["view_option"]
    stock_data = get_stock_data(ticker, view_option)
    
    print(stock_data)

    # Prepare the CSV data
    csv_data = []
    if isinstance(stock_data, dict):
        for key, value in stock_data.items():
            if isinstance(value, pd.Timestamp):  # Convert pandas timestamp to string
                value = value.strftime("%Y-%m-%d %H:%M:%S")
            csv_data.append([key, value])
    else:
        if isinstance(stock_data[0], pd.Timestamp):  # Convert pandas timestamps to strings
            stock_data = [item.strftime("%Y-%m-%d %H:%M:%S") for item in stock_data]
        csv_data.append(["Data"])
        csv_data.extend([[item] for item in stock_data])

    # Set up the HTTP response to download the CSV file
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerows(csv_data)
    response = Response(output.getvalue(), content_type="text/csv")
    response.headers["Content-Disposition"] = f"attachment; filename={ticker}_{view_option}.csv"
    
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ticker = request.form["ticker"]
        view_option = request.form["view_option"]
        stock_data = get_stock_data(ticker, view_option)
        return render_template("result.html", ticker=ticker, view_option=view_option, stock_data=stock_data)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
