# This file is part asset_shipment_work module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval, If, Bool


class ShipmentWork:
    __name__ = 'shipment.work'
    __metaclass__ = PoolMeta
    asset = fields.Many2One('asset', 'Asset',
            domain=[
                If(Bool(Eval('party')),
                    [('owner', '=', Eval('party'))],
                    []),
                ],
            depends=['party'])

    @fields.depends('asset', 'employees')
    def on_change_asset(self):
        if self.asset:
            if (hasattr(self.asset, 'zone') and self.asset.zone and
                    self.asset.zone.employee):
                self.employees = [self.asset.zone.employee.id]
            if self.asset.owner:
                self.party = self.asset.owner.id
