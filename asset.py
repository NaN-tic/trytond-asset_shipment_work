# This file is part asset_shipment_work module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta


class Asset:
    __name__ = 'asset'
    __metaclass__ = PoolMeta
    shipments = fields.One2Many('shipment.work', 'asset', 'Shipments Works')

