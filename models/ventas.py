# -*- coding: utf-8 -*-

from odoo import models, fields, api

class contabilidad(models.Model):
     _name = 'contabilidad.ventas'

     name = fields.Char(strin="name")
   
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100