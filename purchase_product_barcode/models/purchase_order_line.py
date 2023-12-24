from odoo import api, models, fields


class PurchaseOrderLine(models.Model):
    _name = 'purchase.order.line'
    _inherit = ['base.order.line', 'purchase.order.line']
