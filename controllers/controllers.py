# -*- coding: utf-8 -*-
from odoo import http

# class ProyectoL(http.Controller):
#     @http.route('/proyecto_l/proyecto_l/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyecto_l/proyecto_l/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyecto_l.listing', {
#             'root': '/proyecto_l/proyecto_l',
#             'objects': http.request.env['proyecto_l.proyecto_l'].search([]),
#         })

#     @http.route('/proyecto_l/proyecto_l/objects/<model("proyecto_l.proyecto_l"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyecto_l.object', {
#             'object': obj
#         })