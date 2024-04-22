import pandas as pd

def get_data_date():
    file1 = input("primer archivo: ")
    file2 = input("segundo archivo: ")
    df1 = pd.read_csv(f'./files/{file1}.csv')
    df2 = pd.read_csv(f'./files/{file2}.csv')
    merge_column = input("Enter the name of the column to merge on: ")
    df = pd.merge(df1, df2, on=merge_column, how='inner').sort_values('Date')
    df.to_csv(f'./files/g/gdd_{file1}_{file2}.csv', index=False)

def get_likes_month():
    file1 = input("primer archivo: ")
    file2 = input("segundo archivo: ")
    df1 = pd.read_csv(f'./files/{file1}.csv')
    df2 = pd.read_csv(f'./files/{file2}.csv')
    df = pd.merge(df1, df2, on='Date')
    df['Date'] = pd.to_datetime(df['Date'])
    df['month'] = df['Date'].dt.month
    df = df.groupby('month')[['like_x', 'like_y']].sum().reset_index()
    df.to_csv(f'./files/g/gml-{file1}-{file2}.csv', index=False)

def main():
    choice = input("Enter your choice (1: Get data by date)\n"
                   "               (2: Get most likes): ")
    if choice == "1":
        get_data_date()
    elif choice == "2":
        get_likes_month()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()