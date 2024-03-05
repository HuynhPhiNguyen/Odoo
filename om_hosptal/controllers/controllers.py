# -*- coding: utf-8 -*-
# from odoo import http


# class OmHosptal(http.Controller):
#     @http.route('/om_hosptal/om_hosptal', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_hosptal/om_hosptal/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_hosptal.listing', {
#             'root': '/om_hosptal/om_hosptal',
#             'objects': http.request.env['om_hosptal.om_hosptal'].search([]),
#         })

#     @http.route('/om_hosptal/om_hosptal/objects/<model("om_hosptal.om_hosptal"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_hosptal.object', {
#             'object': obj
#         })
