from ankiconnect import invoke
import config
D = f'deck:"{config.DECK_NAME}"'
for lbl, q in [
    ("v3_dagsbatch::*            ", f"{D} tag:v3_dagsbatch::*"),
    ("oberoende_verifierad::*    ", f"{D} tag:oberoende_verifierad::*"),
    ("sokverifierad::2026-08-08  ", f"{D} tag:flerbetydelse_sokverifierad::2026-08-08"),
    ("  ...av dem med v3-tagg    ", f"{D} tag:flerbetydelse_sokverifierad::2026-08-08 tag:v3_dagsbatch::*"),
    ("kort som klarar SLAPP-krav ", f"{D} tag:kortformat::v2 tag:flerbetydelse_granskad::* tag:flerbetydelse_sokverifierad::* tag:oberoende_verifierad::*"),
]:
    print(f"{lbl}: {len(invoke('findCards', query=q))}")
