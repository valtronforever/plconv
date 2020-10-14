from pathlib import Path
import pandas as pd
import numpy as np
from typing import List
import xlrd


def sokul(in_path_list: List[Path], out_path: Path):
    result_df = None

    for in_path in in_path_list:
        try:
            xl = pd.ExcelFile(in_path)
        except UnicodeDecodeError:
            xlrd_book = xlrd.open_workbook(in_path, on_demand=True, encoding_override="cp1251")
            xl = pd.ExcelFile(xlrd_book)
        df = xl.parse()
        header_str = "Код"
        cols = list(df.columns)
        header_col = cols[1]
        header_row = df.index.get_loc(df.index[df[header_col] == header_str][0])
        df = xl.parse(header=header_row + 1)
        df = df.rename(columns={
            'Товар': 'Наименование',
            'Шт./упак': 'Упак.',
        })
        df.insert(loc=df.columns.get_loc("Наименование") + 1, column='Производитель', value=pd.Series(np.nan, dtype="string"))
        df.insert(loc=df.columns.get_loc("Цена с НДС") + 1, column='НДС', value=20)
        df['Цена с НДС'] = df['Цена с НДС'].apply(lambda x: x if isinstance(x, float) else np.nan)
        supplier = np.nan
        for index, row in df.iterrows():
            if pd.isna(row['Цена с НДС']) and pd.isna(row['Код УКТ']):
                supplier = row['Наименование']
            else:
                df.at[index, 'Производитель'] = supplier
        df = df[(df['Цена с НДС'].notnull())]
        df = df[['Код', 'Наименование', 'Производитель', 'Цена с НДС', 'НДС', 'Упак.']]
        if result_df is None:
            result_df = df
        else:
            result_df = result_df.append(df, ignore_index=True)

    if result_df is not None:
        out_file_name = "Сокульский.xls"
        result_df.to_excel(out_path / out_file_name, index=False)
