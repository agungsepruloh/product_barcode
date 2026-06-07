from odoo.tests import common, tagged


@tagged('post_install', '-at_install')
class TestAccountMoveLine(common.TransactionCase):
    def setUp(self):
        super().setUp()
        self.AccountMoveLine = self.env['account.move.line']
        self.product = self.env['product.product'].create({
            'name': 'Barcode Test Product',
            'barcode': '123456789',
        })

    def test_onchange_product_barcode(self):
        account_move_line = self.AccountMoveLine.new({'product_barcode': '123456789'})
        account_move_line._onchange_product_barcode()
        self.assertEqual(account_move_line.product_id, self.product)

    def test_onchange_product_id(self):
        account_move_line = self.AccountMoveLine.new({'product_id': self.product.id})
        account_move_line._onchange_product_id()
        self.assertEqual(account_move_line.product_barcode, self.product.barcode)
