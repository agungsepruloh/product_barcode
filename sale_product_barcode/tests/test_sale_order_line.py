from odoo.tests import common, tagged


@tagged('post_install', '-at_install')
class TestSaleOrderLine(common.TransactionCase):
    def setUp(self):
        super().setUp()
        self.SaleOrderLine = self.env['sale.order.line']
        self.product = self.env['product.product'].create({
            'name': 'Barcode Test Product',
            'barcode': '123456789',
        })
        self.partner = self.env['res.partner'].create({'name': 'Barcode Test Customer'})
        self.sale_order = self.env['sale.order'].create({'partner_id': self.partner.id})

    def test_onchange_product_barcode(self):
        sale_order_line = self.SaleOrderLine.new({'product_barcode': '123456789'})
        sale_order_line._onchange_product_barcode()
        self.assertEqual(sale_order_line.product_id, self.product)

    def test_onchange_product_id(self):
        sale_order_line = self.SaleOrderLine.new({'product_id': self.product.id})
        sale_order_line._onchange_product_id()
        self.assertEqual(sale_order_line.product_barcode, self.product.barcode)

    def test_create_product_barcode(self):
        sale_order_line = self.SaleOrderLine.create({
            'product_barcode': '123456789',
            'order_id': self.sale_order.id,
        })
        self.assertEqual(sale_order_line.product_id, self.product)

    def test_create_product_id(self):
        sale_order_line = self.SaleOrderLine.create({
            'product_id': self.product.id,
            'order_id': self.sale_order.id,
        })
        self.assertEqual(sale_order_line.product_barcode, self.product.barcode)
