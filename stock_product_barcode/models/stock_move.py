from odoo import api, models, fields


class StockMove(models.Model):
    _name = 'stock.move'
    _inherit = ['base.order.line', 'stock.move']
