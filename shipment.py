# This file is part asset_shipment_work module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Eval


class ShipmentWork:
    __name__ = 'shipment.work'
    __metaclass__ = PoolMeta
    asset = fields.Many2One('asset', 'Asset',
        states={
            'readonly': Eval('state') != 'draft',
            },
        depends=['state'])

    @classmethod
    def __setup__(cls):
        super(ShipmentWork, cls).__setup__()
        pool = Pool()
        Asset = pool.get('asset')
        if hasattr(Asset, 'owners'):
            cls.asset.domain = [
                ('owners.owner', '=', Eval('party')),
                ]
            cls.asset.depends.append('party')

    @fields.depends('asset', 'employees')
    def on_change_asset(self):
        if self.asset:
            if (hasattr(self.asset, 'zone') and self.asset.zone and
                    self.asset.zone.employee):
                self.employees = [self.asset.zone.employee.id]
            if self.asset.owner:
                self.party = self.asset.owner.id
