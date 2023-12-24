from odoo.tests import common


class TestAccountMoveLine(common.TransactionCase):
    def setUp(self):
        super(TestAccountMoveLine, self).setUp()
        self.AccountMoveLine = self.env['account.move.line']
        self.product = self.env.ref('product.product_product_25')
        self.product.barcode = '123456789'
        self.account_move = self.env['account.move'].create({'move_type': 'out_invoice'}).with_context(check_move_validity=False)

    def test_onchange_product_barcode(self):
        account_move_line = self.AccountMoveLine.new({'product_barcode': '123456789'})
        account_move_line._onchange_product_barcode()
        self.assertEqual(account_move_line.product_id, self.product)
