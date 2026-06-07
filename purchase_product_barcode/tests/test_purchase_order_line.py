from odoo.tests import common, tagged


@tagged('post_install', '-at_install')
class TestPurchaseOrderLine(common.TransactionCase):
    def setUp(self):
        super().setUp()
        self.PurchaseOrderLine = self.env['purchase.order.line']
        self.product = self.env['product.product'].create({
            'name': 'Barcode Test Product',
            'barcode': '123456789',
        })
        self.partner = self.env['res.partner'].create({'name': 'Barcode Test Vendor'})
        self.purchase_order = self.env['purchase.order'].create({'partner_id': self.partner.id})

    def test_onchange_product_barcode(self):
        purchase_order_line = self.PurchaseOrderLine.new({'product_barcode': '123456789'})
        purchase_order_line._onchange_product_barcode()
        self.assertEqual(purchase_order_line.product_id, self.product)

    def test_onchange_product_id(self):
        purchase_order_line = self.PurchaseOrderLine.new({'product_id': self.product.id})
        purchase_order_line._onchange_product_id()
        self.assertEqual(purchase_order_line.product_barcode, self.product.barcode)

    def test_create_product_barcode(self):
        purchase_order_line = self.PurchaseOrderLine.create({
            'product_barcode': '123456789',
            'order_id': self.purchase_order.id,
        })
        self.assertEqual(purchase_order_line.product_id, self.product)

    def test_create_product_id(self):
        purchase_order_line = self.PurchaseOrderLine.create({
            'product_id': self.product.id,
            'order_id': self.purchase_order.id,
        })
        self.assertEqual(purchase_order_line.product_barcode, self.product.barcode)
