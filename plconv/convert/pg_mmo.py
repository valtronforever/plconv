from pathlib import Path
import pandas as pd


def pg_mmo(in_path: Path, out_path: Path):
    df = pd.read_csv(in_path, encoding='cp1251', sep='\t', names=range(23))
    df_head = df[:3]
    df_body = df[3:]
    df_body[0] = df_body[4]
    df = df_head.append(df_body, ignore_index=True)
    out_file_name = in_path.stem + ".mmo"
    df.to_csv(out_path / out_file_name, encoding='cp1251', sep='\t', index=False, header=False)
