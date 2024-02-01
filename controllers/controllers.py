# -*- coding: utf-8 -*-
# from odoo import http


# class IntAccountLock(http.Controller):
#     @http.route('/int_account_lock/int_account_lock', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/int_account_lock/int_account_lock/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('int_account_lock.listing', {
#             'root': '/int_account_lock/int_account_lock',
#             'objects': http.request.env['int_account_lock.int_account_lock'].search([]),
#         })

#     @http.route('/int_account_lock/int_account_lock/objects/<model("int_account_lock.int_account_lock"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('int_account_lock.object', {
#             'object': obj
#         })
