# -*- coding: utf-8 -*-
# from odoo import http


# class SmartMargin(http.Controller):
#     @http.route('/smart_margin/smart_margin', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/smart_margin/smart_margin/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('smart_margin.listing', {
#             'root': '/smart_margin/smart_margin',
#             'objects': http.request.env['smart_margin.smart_margin'].search([]),
#         })

#     @http.route('/smart_margin/smart_margin/objects/<model("smart_margin.smart_margin"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('smart_margin.object', {
#             'object': obj
#         })

