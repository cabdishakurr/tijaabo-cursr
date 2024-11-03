from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    low_stock = fields.Boolean(
        string='Low Stock',
        compute='_compute_low_stock',
        store=True,
    )

    @api.depends('qty_available')
    def _compute_low_stock(self):
        for product in self:
            product.low_stock = product.qty_available < 10 