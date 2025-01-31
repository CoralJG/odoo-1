# -*- coding: utf-8 -*-
# from odoo import http


# class Miprimermodulo(http.Controller):
#     @http.route('/miprimermodulo/miprimermodulo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/miprimermodulo/miprimermodulo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('miprimermodulo.listing', {
#             'root': '/miprimermodulo/miprimermodulo',
#             'objects': http.request.env['miprimermodulo.miprimermodulo'].search([]),
#         })

#     @http.route('/miprimermodulo/miprimermodulo/objects/<model("miprimermodulo.miprimermodulo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('miprimermodulo.object', {
#             'object': obj
#         })

