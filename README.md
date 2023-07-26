# Stock Data Retrieval Web Application

This is a simple web application that allows users to retrieve various stock-related data using the Yahoo Finance API. The application is built using Python and the Flask framework, making it easy to run and deploy on a local server.

## Features

- Users can input a stock ticker and select the type of data they want to retrieve (e.g., info, actions, dividends, splits, etc.).
- The application fetches the requested data from Yahoo Finance using the `yfinance` library.
- The data is then displayed to the user on the web interface.
- Users can also save the data as a CSV-like file for further analysis.

## How to Use

1. Clone this repository to your local machine.

2. Install the required dependencies by running the following command(with Python 3.x installed):

```
pip install flask yfinance pandas
```

3. Run the application using the following command:

```
python getmarketinfo.py
```

The application will be available at `http://127.0.0.1:5000/` in your web browser.

4. Enter a stock ticker and select the desired data view option from the dropdown list.

![image](https://github.com/CharlieCidral/marketinfo/assets/69029099/62e56adf-0ba8-475a-b08e-82d14f4d87bf)

5. Click the "Submit" button to retrieve the data and view it on the result page.

6. Optionally, you can click the "Save as CSV" button to save the data as a downloadable file with a `.csv` extension.

- have some format issues to fix as a date/time are not saving.

![image](https://github.com/CharlieCidral/marketinfo/assets/69029099/3d0bb3ef-8920-478d-a7e5-dd3c75ec9858)

## Folder Structure

- `getmarketinfo.py`: The main Python script containing the Flask application and data retrieval functions.
- `templates`: A directory containing the HTML templates used for the web interface.

## Notes

- Please make sure you have a stable internet connection to access the Yahoo Finance API and fetch the stock data.
- The application uses the Yahoo Finance API, and data availability is subject to Yahoo's terms and conditions.

Feel free to reach out if you have any questions or need further assistance!

---
Created by [Charlie CS]
