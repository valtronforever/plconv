from pathlib import Path
import pandas as pd


def pg(in_path: Path, out_path: Path):
    df = pd.read_excel(in_path)
    header_str = "Номер п/п"
    header_row = df.index.get_loc(df.index[df['Unnamed: 0'] == header_str][0])
    df = pd.read_excel(in_path, header=header_row + 1, converters={'Штрихкод': str})
    df = df[df['Штрихкод'].notnull()]
    df = df.rename(columns={df.columns[4]: 'Цена'})
    df.insert(loc=df.columns.get_loc("Цена") + 1, column='НДС', value=20)
    df.insert(loc=df.columns.get_loc("Наименование") + 1, column='Производитель', value='Procter & Gamble')
    df = df[(df['Штрихкод'].str.isnumeric()) & (df['Штрихкод'].str.len() == 13)]
    df = df[['Наименование', 'Производитель', 'Цена', 'НДС', 'ШТ/Кейс', 'Штрихкод']]
    out_file_name = in_path.stem + ".xls"
    df.to_excel(out_path / out_file_name, index=False)
