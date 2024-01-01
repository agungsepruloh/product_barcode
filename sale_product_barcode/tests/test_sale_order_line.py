from odoo.tests import common


class TestSaleOrderLine(common.TransactionCase):
    def setUp(self):
        super(TestSaleOrderLine, self).setUp()
        self.SaleOrderLine = self.env['sale.order.line']
        self.product = self.env.ref('product.product_product_25')
        self.product.barcode = '123456789'
        self.sale_order = self.env.ref('sale.sale_order_1')

    def test_onchange_product_barcode(self):
        sale_order_line = self.SaleOrderLine.new({'product_barcode': '123456789'})
        sale_order_line._onchange_product_barcode()
        self.assertEqual(sale_order_line.product_id, self.product)

    def test_onchange_product_id(self):
        sale_order_line = self.SaleOrderLine.new({'product_id': self.product.id})
        sale_order_line._onchange_product_id()
        self.assertEqual(sale_order_line.product_barcode, self.product.barcode)

    def test_create_product_barcode(self):
        sale_order_line = self.SaleOrderLine.create({'product_barcode': '123456789', 'order_id': self.sale_order.id})
        self.assertEqual(sale_order_line.product_id, self.product)

    def test_create_product_id(self):
        sale_order_line = self.SaleOrderLine.create({'product_id': self.product.id, 'order_id': self.sale_order.id})
        self.assertEqual(sale_order_line.product_barcode, self.product.barcode)
