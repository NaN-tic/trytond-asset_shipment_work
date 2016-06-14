# This file is part asset_shipment_work module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .asset import *
from .shipment import *

def register():
    Pool.register(
        Asset,
        ShipmentWork,
        module='asset_shipment_work', type_='model')
