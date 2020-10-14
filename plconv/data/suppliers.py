from plconv.widgets.layout_basic import LayoutBasic
from plconv.widgets.layout_multiple import LayoutMultiple
from plconv.widgets.layout_mmo import LayoutMmo
from plconv.convert.blade_n import blade_n
from plconv.convert.pg import pg
from plconv.convert.pg_mmo import pg_mmo
from plconv.convert.vega import vega
from plconv.convert.sokul import sokul

suppliers = [
    {
        'id': 'blade_n',
        'name': "Блейд Н",
        'widget': LayoutBasic,
        'convert': blade_n,
    },
    {
        'id': 'pg',
        'name': "СТВ Груп",
        'widget': LayoutBasic,
        'convert': pg,
    },
    {
        'id': 'pg_mmo',
        'name': "СТВ Груп (накладные)",
        'widget': LayoutMmo,
        'convert': pg_mmo,
    },
    {
        'id': 'vega',
        'name': "Медтехніка Південь",
        'widget': LayoutBasic,
        'convert': vega,
    },
    {
        'id': 'sokul',
        'name': "Сокульский",
        'widget': LayoutMultiple,
        'convert': sokul,
    },
]
