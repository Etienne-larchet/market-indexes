# SP500, DAX, and CAC40 Composition Retriever

This package provides an easy way to retrieve the current and past compositions of major stock indices, including the S&P 500. The package extracts data from publicly available sources such as Wikipedia to determine index constituents at a given date.

## Features
- Retrieve the current S&P 500 composition.
- Retrieve the historical composition of the S&P 500 based on a given date.
- Support for additional indices (DAX and CAC40, implementation pending).

## Installation
Ensure you have Python and the required dependencies installed:
```sh
pip install pandas[html]
```

## Usage
The main class `SP500` fetches the S&P 500 composition dynamically. The composition can be retrieved for today or for a past date.

### Example
```python
# Get today's S&P 500 composition
sp500_now = SP500()
print(sp500_now)

# Get S&P 500 composition as of January 1, 2022
sp500_2022 = SP500(lookup_date=date(2022, 1, 1))
print(sp500_2022)
```

## Classes
### `SP500`
Fetches the composition of the S&P 500 from Wikipedia.
- **Parameters:**
  - `lookup_date (date)`: The date for which the composition is requested. Defaults to today.
- **Returns:**
  - A Pandas Series with tickers as indices and company names as values.

### `DAX` and `CAC40`
Currently not implemented.

## License
MIT License.