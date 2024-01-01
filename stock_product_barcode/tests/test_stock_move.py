from odoo.tests import common


class TestStockMove(common.TransactionCase):
    def setUp(self):
        super(TestStockMove, self).setUp()
        self.StockMove = self.env['stock.move']
        self.product = self.env.ref('product.product_product_25')
        self.product.barcode = '123456789'
        self.stock_picking = self.env['stock.picking'].create({
            'picking_type_id': self.env.ref('stock.picking_type_in').id,
            'location_id': self.env.ref('stock.stock_location_stock').id,
            'location_dest_id': self.env.ref('stock.stock_location_suppliers').id,
        })

    def test_onchange_product_barcode(self):
        stock_move = self.StockMove.new({'product_barcode': '123456789'})
        stock_move._onchange_product_barcode()
        self.assertEqual(stock_move.product_id, self.product)

    def test_onchange_product_id(self):
        stock_move = self.StockMove.new({'product_id': self.product.id})
        stock_move._onchange_product_id()
        self.assertEqual(stock_move.product_barcode, self.product.barcode)

    def test_create_product_barcode(self):
        stock_move = self.StockMove.create({
            'name': 'Test Stock Move',
            'product_barcode': '123456789',
            'picking_id': self.stock_picking.id,
            'product_uom': self.product.uom_id.id,
            'location_id': self.stock_picking.location_id.id,
            'location_dest_id': self.stock_picking.location_dest_id.id,
        })
        self.assertEqual(stock_move.product_id, self.product)

    def test_create_product_id(self):
        stock_move = self.StockMove.create({
            'name': 'Test Stock Move',
            'product_id': self.product.id,
            'picking_id': self.stock_picking.id,
            'product_uom': self.product.uom_id.id,
            'location_id': self.stock_picking.location_id.id,
            'location_dest_id': self.stock_picking.location_dest_id.id,
        })
        self.assertEqual(stock_move.product_barcode, self.product.barcode)
