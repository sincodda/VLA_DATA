import pandas as pd

def get_data_date():
    file1 = input("primer archivo: ")
    file2 = input("segundo archivo: ")
    df1 = pd.read_csv(f'./files/{file1}.csv')
    df2 = pd.read_csv(f'./files/{file2}.csv')
    df = pd.merge(df1, df2, on='Fecha', how='left').sort_values('Fecha')
    #para filtrar el archivo agrupado por tiempo y sumar los likes y comentarios
    #df = df.groupby('Forecast')[['like_count', 'comment_count']].sum().reset_index()
    
    df.to_csv(f'./files/goldens/g_{file1}_{file2}.csv', index=False)

def main():
    get_data_date()

if __name__ == "__main__":
    main()