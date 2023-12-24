from odoo import api, models, fields


class BaseOrderLine(models.AbstractModel):
    _name = 'base.order.line'

    product_barcode = fields.Char(string='Barcode', help="Here you can provide the barcode for the product")

    @api.onchange('product_barcode')
    def _onchange_product_barcode(self):
        if self.product_barcode:
            product = self.env['product.product'].search([('barcode', '=', self.product_barcode)])
            self.product_id = product.id

    @api.model
    def create(self, vals):
        if vals.get('product_barcode') and not vals.get('product_id'):
            product = self.env['product.product'].search([('barcode', '=', vals.get('product_barcode'))])
            vals['product_id'] = product.id
        return super(BaseOrderLine, self).create(vals)
