import pandas as pd
import xlrd
from plconv.models.supplier import ConvertParams


def avis(params: ConvertParams):
    result_df = None

    for param in params.in_params:
        in_path = param.filepath
        supplier = param.data.get('supplier', '-')
        try:
            xl = pd.ExcelFile(in_path)
        except UnicodeDecodeError:
            xlrd_book = xlrd.open_workbook(in_path, on_demand=True, encoding_override="cp1251")
            xl = pd.ExcelFile(xlrd_book)
        df = xl.parse(header=8)
        df = df.iloc[:, [1, 2, 3, 4]]
        df.columns = ['Наименование', 'Код', 'Цена с НДС', 'Упак.']
        df = df[pd.to_numeric(df['Цена с НДС'], errors='coerce').notnull()]
        df['Код'] = df['Код'].astype(int).astype(str)
        df.insert(loc=df.columns.get_loc("Наименование") + 1, column='Производитель', value=supplier)
        df.insert(loc=df.columns.get_loc("Цена с НДС") + 1, column='НДС', value=20)
        df = df[['Наименование', 'Производитель', 'Цена с НДС', 'НДС', 'Упак.', 'Код']]

        if result_df is None:
            result_df = df
        else:
            result_df = result_df.append(df, ignore_index=True)

    if result_df is not None:
        out_file_name = params.out_params.name + ".xls"
        result_df.to_excel(params.out_params.path / out_file_name, index=False)
