# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import models, fields, api

class Cargo(models.Model):
    _name = 'contabilidad.cargo'
    name = fields.Char(string="Nombre  ", required=True)
class Libros(models.Model):
    _name = 'contabilidad.libros'
    name = fields.Char(string="Nombre del operario ", required=True)
    
    date_contract1 = fields.Date(string="Fecha ", required=True)
    saldo_inicial = fields.Integer(string="Saldo inicial caja", required=True)
    #cost = fields.Float(string="prima")
    #date_contract =fields.Date("Fecha de término", required=True)
    cargo_id = fields.Many2one('contabilidad.cargo', string="cargo")