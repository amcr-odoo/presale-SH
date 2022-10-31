# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    presale_order_id = fields.Many2one('presale.order', string="Presale Order", readonly=True, copy=False)
