from datetime import date
from jugaad_data.nse import bhavcopy_save, full_bhavcopy_save, bhavcopy_fo_save, bhavcopy_index_save,stock_csv,stock_df
import pandas as pd

def DownloadData(symbol):
    csv_name="./" + symbol+".csv"
     #Download data and save to a csv file
    stock_csv(symbol=symbol, from_date=date(1999,1,1),
            to_date=date.today(), series="EQ", output=csv_name)
    df = pd.read_csv(csv_name)
    sorted_df = df.sort_values(by=["DATE"],ascending=True)
    sorted_df.to_csv("./"+symbol+"-data.csv",index=False)

def main():
    count = 0
    print("reading file...")
    symbol_file = open('symbols.txt', 'r')
    
    for symbol in symbol_file:
        count += 1
        print("Line{}: {}".format(count, symbol.strip()))
        DownloadData(symbol.strip())
    # Closing files
    symbol_file.close()
    
if __name__ == "__main__":
    main()
