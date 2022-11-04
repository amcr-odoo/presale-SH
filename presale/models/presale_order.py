# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class PresaleOrder(models.Model):
    _name = "presale.order"
    _inherit = "mail.thread"
    _description = "Presale Order"
    _order = "id desc"

    name = fields.Char("Name", readonly=True, default="New")
    state = fields.Selection(
        string="Status",
        selection=[("draft", "Draft"), ("confirmed", "Confirmed")],
        required=True,
        copy=False,
        default="draft",
    )
    customer_id = fields.Many2one("res.partner", string="Customer", required=True)
    order_line_ids = fields.One2many("presale.order.line", "order_id", string="Lines")
    active = fields.Boolean("Active", default=True)

    def action_validate(self):
        for record in self:
            record.state = "confirmed"

        email_template_id = self.env.ref("presale.presale_order_mail_template").id
        self.env["mail.template"].browse(email_template_id).send_mail(record.id)
        return True

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code("presale.order") or "New"
        return super(PresaleOrder, self).create(vals)

    def _cron_archive_orders(self):
        presale_orders = self.env["presale.order"].search([("state", "=", "confirmed"), ("active", "=", True)])
        for order in presale_orders:
            order.active = False
