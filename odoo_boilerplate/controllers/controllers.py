# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import requests
from requests import Request, Session, exceptions


class ResouceController(http.Controller):
    @http.route('/resources', auth='public')
    def resource_detail(self):
        output = ''
        resources = request.env['product.resource'].search([])
        if resources:
            for re in resources:
                output += '<h3>{}</h3>'.format(re.name)
                output += '<b>{}</b>'.format(re.product_id.display_name)
                output += '<p>{}</p>'.format(re.description)
                output += '<a href="{}"><i>{}</i></a>'.format(re.url, 'Link')

        return output
