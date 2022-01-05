from pathlib import Path

from .load_xlsx import load_xlsx_dict
from .export_to_dsl import export_to_dsl


def convert_xlsx_to_dsl(in_file, out_path=None, compress=True):
    in_file = Path(in_file)
    out_path = Path(out_path) if out_path else in_file.parent
    if not out_path.is_dir():
        out_path.mkdir(exist_ok=True)
    out_file = out_path / (in_file.stem + '.dsl')
    entries = load_xlsx_dict(in_file)
    export_to_dsl(entries, out_file, compress=compress)


def batch_conv_xlsx_to_dsl(in_path, out_path=None, compress=True):
    for f in Path(in_path).glob('*.xlsx'):
        convert_xlsx_to_dsl(f, out_path, compress)
