# -*- coding: utf-8 -*-
from odoo import http

# class RidersMobileApi(http.Controller):
#     @http.route('/riders_mobile_api/riders_mobile_api/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/riders_mobile_api/riders_mobile_api/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('riders_mobile_api.listing', {
#             'root': '/riders_mobile_api/riders_mobile_api',
#             'objects': http.request.env['riders_mobile_api.riders_mobile_api'].search([]),
#         })

#     @http.route('/riders_mobile_api/riders_mobile_api/objects/<model("riders_mobile_api.riders_mobile_api"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('riders_mobile_api.object', {
#             'object': obj
#         })