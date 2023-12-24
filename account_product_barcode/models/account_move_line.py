from odoo import api, models, fields


class AccountMoveLine(models.Model):
    _name = 'account.move.line'
    _inherit = ['base.order.line', 'account.move.line']
