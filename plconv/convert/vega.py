from pathlib import Path
import pandas as pd


def vega(in_path: Path, out_path: Path):
    df = pd.read_excel(in_path)
    header_str = "Ценовая группа/ Номенклатура/ Характеристика номенклатуры"
    header_row = df.index.get_loc(df.index[df['Прайс-лист'] == header_str][0])
    df = pd.read_excel(in_path, header=header_row + 1)
    df = df[df['Цена'].notnull()]
    df = df.rename(columns={
        'Ценовая группа/ Номенклатура/ Характеристика номенклатуры': 'Наименование',
        'Номенклатура.Код': 'Код',
        'Номенклатура.Ставка НДС': 'НДС',
    })
    df = df[['Наименование', 'Производитель', 'Цена', 'НДС', 'Код']]
    out_file_name = in_path.stem + ".xls"
    df.to_excel(out_path / out_file_name, index=False)
