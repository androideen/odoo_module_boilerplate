# -*- coding: utf-8 -*-
from odoo import fields, models, api, _

class DraftProductResource(models.TransientModel):
    _name = 'wizard.draft.product.resource'
    _description = 'Set Resource to Draft'

    def _default_orders(self):
        return self.env['sale.order'].browse(self._context.get('active_ids'))

    resource_ids = fields.Many2many('product.resource', string='Resources', default=_default_orders,
                                 auto_join=True, required=True, readonly=True)

    @api.multi
    def action_draft(self):
        for re in self.resource_ids:
            re.state = 'draft'