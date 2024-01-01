from odoo.tests import common


class TestPurchaseOrderLine(common.TransactionCase):
    def setUp(self):
        super(TestPurchaseOrderLine, self).setUp()
        self.PurchaseOrderLine = self.env['purchase.order.line']
        self.product = self.env.ref('product.product_product_25')
        self.product.barcode = '123456789'
        self.purchase_order = self.env.ref('purchase.purchase_order_1')

    def test_onchange_product_barcode(self):
        purchase_order_line = self.PurchaseOrderLine.new({'product_barcode': '123456789'})
        purchase_order_line._onchange_product_barcode()
        self.assertEqual(purchase_order_line.product_id, self.product)

    def test_onchange_product_id(self):
        purchase_order_line = self.PurchaseOrderLine.new({'product_id': self.product.id})
        purchase_order_line._onchange_product_id()
        self.assertEqual(purchase_order_line.product_barcode, self.product.barcode)

    def test_create_product_barcode(self):
        purchase_order_line = self.PurchaseOrderLine.create({'product_barcode': '123456789', 'order_id': self.purchase_order.id})
        self.assertEqual(purchase_order_line.product_id, self.product)

    def test_create_product_id(self):
        purchase_order_line = self.PurchaseOrderLine.create({'product_id': self.product.id, 'order_id': self.purchase_order.id})
        self.assertEqual(purchase_order_line.product_barcode, self.product.barcode)

