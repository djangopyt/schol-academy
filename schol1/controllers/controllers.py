# -*- coding: utf-8 -*-
# from odoo import http


# class Schol1(http.Controller):
#     @http.route('/schol1/schol1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/schol1/schol1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('schol1.listing', {
#             'root': '/schol1/schol1',
#             'objects': http.request.env['schol1.schol1'].search([]),
#         })

#     @http.route('/schol1/schol1/objects/<model("schol1.schol1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('schol1.object', {
#             'object': obj
#         })
