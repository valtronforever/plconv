from plconv.widgets.layout_basic import LayoutBasic
from plconv.widgets.layout_multiple import LayoutMultiple
from plconv.widgets.layout_mmo import LayoutMmo
from plconv.widgets.layout_box import LayoutBox
from plconv.convert.blade_n import blade_n
from plconv.convert.pg import pg
from plconv.convert.pg_mmo import pg_mmo
from plconv.convert.vega import vega
from plconv.convert.sokul import sokul
from plconv.convert.avis import avis
from plconv.convert.avis_mmo import avis_mmo

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
    {
        'id': 'avis',
        'name': "Авис",
        'widget': LayoutBox,
        'convert': avis,
        'params': {
            'in_params': [{
                'label': 'Прайс-лист Дана',
                'data': {'supplier': 'Дана'},
            }, {
                'label': 'Прайс-лист Курносики',
                'data': {'supplier': 'Линдо'},
            }, {
                'label': 'Прайс-лист Хорол',
                'data': {'supplier': 'Хорол'},
            }, {
                'label': 'Прайс-лист Хумана',
                'data': {'supplier': 'Humana'},
            }, {
                'label': 'Прайс-лист Чудо-чадо',
                'data': {'supplier': 'Вітмарк-Україна'},
            }],
            'out_params': {
                'name': 'авис'
            },
        }
    },
    {
        'id': 'avis_mmo',
        'name': "Авис (Накладные)",
        'widget': LayoutBox,
        'convert': avis_mmo,
        'params': {
            'in_params': [{
                'label': 'Накладная mmo',
            }],
            'out_params': {
                'name': 'авис'
            },
        }
    }
]
