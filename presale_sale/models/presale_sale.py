# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import Command, fields, models


class PresaleSale(models.Model):
    _inherit = "presale.order"

    def action_validate(self):
        for record in self:
            sale_order_lines = []
            for order_line in record.order_line_ids:
                line = Command.create({
                    'product_id': order_line.product_id.id,
                    'price_unit': order_line.price,
                    'product_uom_qty': order_line.qty
                })
                sale_order_lines.append(line)

            sale_order = self.env['sale.order'].create({
                'name': record.name,
                'user_id': self.env.user.id,
                'partner_id': record.customer_id.id,
                'order_line': sale_order_lines,
                'presale_order_id': record.id
            })
            sale_order.action_confirm()

            return super().action_validate()
