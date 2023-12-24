from odoo import api, models, fields


class SaleOrderLine(models.Model):
    _name = 'sale.order.line'
    _inherit = ['base.order.line', 'sale.order.line']
