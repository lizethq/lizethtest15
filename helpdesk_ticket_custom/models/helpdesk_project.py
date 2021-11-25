# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

# Se crea modelo proyecto
class helpdesk_project(models.Model):
    _name = 'helpdesk_project'
    _description = 'Proyecto en mesa de ayuda'

    name = fields.Char(string='Nombre', required="True")
    x_code = fields.Char(string='Codigo', required="True")
    # x_account_analytic = fields.Many2one(comodel_name='account.analytic.account', string='Cuenta analítica', required="True")
    # x_code_analytic = fields.Char(string='Cuenta Analitica', store=True, related="x_account_analytic.code")

    # Restricción a nivel de SQL
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'El proyecto ya existe'),
    ]

    # Permite concatenar el name y la cuenta an analitica
    def name_get(self):
        result = []
        for rec in self:
            name = rec.name + ' [ ' + rec.x_code + ' ]'
            result.append((rec.id, name))
        return result

    # # Permite concatenar el name y la cuenta an analitica
    # def name_get(self):
    #     result = []
    #     for rec in self:
    #         name = rec.name + ' [' + rec.x_code_analytic + ']'
    #         result.append((rec.id, name))
    #     return result