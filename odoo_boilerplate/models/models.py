# -*- coding: utf-8 -*-
from odoo import fields, models, api, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    report_footer = fields.Char('Report Footer', config_parameter='product_resource.report_footer')


class ProductResource(models.Model):
    _name = 'product.resource'
    _description = 'Product Resources'

    name = fields.Char(string="Name", readonly=True, select=True, copy=False, default='New')
    url = fields.Char()
    description = fields.Text(string="Description")
    product_id = fields.Many2one('product.template', 'Product', auto_join=True, required=True,
                                 domain=[('type', '=', 'service')])
    views = fields.Integer(string="Views", default=0, readonly=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, copy=False, index=True, default='draft')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('product.resource') or 'New'
        result = super(ProductResource, self).create(vals)
        return result

    @api.multi
    def action_confirm(self):
        for re in self:
            re.state = 'confirm'


