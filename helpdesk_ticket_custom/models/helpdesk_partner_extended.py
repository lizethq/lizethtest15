# -*- coding: utf-8 -*-
from odoo import models, fields, api

# heredamos del modelo usuarios
class helpdesk_partner_extended(models.Model):
    _inherit = 'res.partner'

    x_project = fields.Many2many(comodel_name='helpdesk_project',
                                 relation='x_helpdesk_project_res_partner_rel',
                                 column1='res_partner_id',
                                 column2='helpdesk_project_id',
                                 string='Proyecto',
                                 )

    @api.onchange('x_ticket_show', 'x_project')
    def _domain_depends_x_project(self):
        if self.is_company == False:
            return {'domain': {'x_project': [('partner_id', "in", self.parent_id.id)]}}







