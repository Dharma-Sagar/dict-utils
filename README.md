# dict-utils
create, process, maintain dictionaries and glossaries

## Usage

See [usage](usage.py)

### functions

```python
from dict_utils import convert_xlsx_to_dsl, batch_conv_xlsx_to_dsl

convert_xlsx_to_dsl(in_file, out_path=None, compress=True)
# if out_path is not provided, the dsl file will be written in the same folder
# if out_path doesn't exist, it is created

batch_conv_xlsx_to_dsl(in_path, out_path=None, compress=True)
# converts all .xlsx files found in in_path
```

### input format

- 1st row is legend
- A column contains lemma
- rows with empty A column are meanings of the last row that have a lemma in column A
- other columns are optional definition fields

### output format

DSL dictionary files, compressed or not (see arguments of the functions)

DSL format definition:
http://lingvo.helpmax.net/en/troubleshooting/dsl-compiler/dsl-dictionary-structure/
