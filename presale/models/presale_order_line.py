# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class PresaleOrderLine(models.Model):
    _name = "presale.order.line"
    _description = "Presale Order Line"
    _order = "id desc"

    product_id = fields.Many2one("product.product", string="Product", required=True)
    qty = fields.Float("Quantity", required=True)
    price = fields.Float("Price", required=True)
    order_id = fields.Many2one("presale.order", string="Order")
