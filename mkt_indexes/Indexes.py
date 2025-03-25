from datetime import date
import pandas as pd



class SP500:
    url: str = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    tickers_alias: dict[str,str] = {'CDAY':'DAY'} # for some tickers with that changes names
    
    def __new__(cls, lookup_date: date = date.today()) -> pd.Series: 
        actual, history = pd.read_html(cls.url)
        actual.set_index('Symbol', inplace=True)
        compo = actual.loc[:, 'Security']

        date_index = pd.to_datetime(history.iloc[:,0], format='%B %d, %Y').dt.date
        history = history.set_index(date_index).sort_index(ascending=False)
        history = history[history.index >= lookup_date]
        for _, serie in history.iterrows():
            if isinstance(ticker := serie[('Added', 'Ticker')], str):
                try:
                    compo.drop(ticker, inplace=True)
                except KeyError:
                    compo.drop(cls.tickers_alias[ticker], inplace=True)
            if isinstance(ticker := serie[('Removed', 'Ticker')], str):
                compo.loc[ticker] = serie[('Removed', 'Security')]
        return compo


    

class DAX:
    ...

class CAC40:
    ...


def main():
    sp500_now = SP500()
    sp500_2022 = SP500(lookup_date=date(2022,1,1))

if __name__ == '__main__':
    main()
