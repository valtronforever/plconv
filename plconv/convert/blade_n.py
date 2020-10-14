from pathlib import Path
import pandas as pd


def blade_n(in_path: Path, out_path: Path):
    xl = pd.ExcelFile(in_path)
    result_df = None
    for sheet in xl.sheet_names:
        df = xl.parse(sheet, converters={'Штрихкод': str})
        df = df.rename(columns={df.columns[4]: 'Цена'})
        try:
            df = df[df['Штрихкод'].notnull()]
        except KeyError:
            continue
        df.insert(loc=df.columns.get_loc("Цена") + 1, column='НДС', value=20)
        df.insert(loc=df.columns.get_loc("Наименование") + 1, column='Производитель', value=sheet)
        df = df[['Наименование', 'Производитель', 'Цена', 'НДС', 'Упак.', 'Штрихкод']]
        df = df[(df['Штрихкод'].str.len() == 13) & (df['Штрихкод'].str.isnumeric())]
        if result_df is None:
            result_df = df
        else:
            result_df = result_df.append(df, ignore_index=True)
    out_file_name = in_path.stem + ".xls"
    result_df.to_excel(out_path / out_file_name, index=False)
