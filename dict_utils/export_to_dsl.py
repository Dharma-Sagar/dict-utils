import io

import idzip
from io import BytesIO


def format_to_dsl(entries, dict_name, add_legend=True):
    out = [f'#NAME "{dict_name}"',
           '#INDEX_LANGUAGE ""',
           '#CONTENTS_LANGUAGE ""']

    for lemma, acceptions in entries.items():
        lines = [lemma]
        for n, acc in enumerate(acceptions):
            if len(acceptions) > 1:
                fields = [f'      [b]{n+1}.[/b]']
            else:
                fields = []
            if add_legend:
                for legend, field in acc.items():
                    fields.append(f'      [m1][*]{legend}[/*]–{field}[/m]')
            else:
                fields.append(', '.join(acc.values()))

            lines.extend(fields)

        out.extend(lines)
    return '\n'.join(out)


def export_to_dsl(entries, out_file, compress=True):
    dsl = format_to_dsl(entries, out_file.stem)
    if not compress:
        out_file.write_text(dsl, encoding='utf-16')
    else:
        out_file = out_file.parent / (out_file.stem + '.dsl.dz')
        with BytesIO() as buffer:
            sb = io.TextIOWrapper(buffer, 'utf-16', newline='')
            sb.write(dsl)
            sb.flush()
            buffer.seek(0)
            with idzip.IdzipFile(str(out_file), 'wb', sync_size=1048576*100) as writer:
                while True:
                    data = buffer.read(1048576+1)
                    if not data:
                        break
                    writer.write(data)
