import pandas as pd
from decimal import Decimal
from plconv.models.supplier import ConvertParams


def avis_mmo(params: ConvertParams):
    in_path = params.in_params[0].filepath
    out_path = params.out_params.path
    df = pd.read_csv(in_path, encoding='cp1251', sep='\t', names=range(23))
    df_head = df[:3]
    df_body = df[3:]
    df_body[19] = df_body[19].apply(lambda x: float(Decimal(Decimal(x.replace(',', '.')) / Decimal(1.2)).quantize(Decimal('1.00'))))
    df_body[15] = df_body[15].apply(lambda x: int(float(x.replace(',', '.'))))
    df_body[20] = df_body[19] * df_body[15]
    df = df_head.append(df_body, ignore_index=True)
    out_file_name = in_path.stem + ".mmo"
    df.to_csv(out_path / out_file_name, encoding='cp1251', sep='\t', index=False, header=False)
