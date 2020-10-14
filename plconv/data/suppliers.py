from widgets.layout_basic import LayoutBasic
from widgets.layout_multiple import LayoutMultiple
from widgets.layout_mmo import LayoutMmo
from convert.blade_n import blade_n
from convert.pg import pg
from convert.pg_mmo import pg_mmo
from convert.vega import vega
from convert.sokul import sokul

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
