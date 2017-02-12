# -*- coding: utf-8 -*-
# © 2016 Gonzalo Borras- bisnemsart
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3

from openerp.osv import osv, fields, expression
from openerp import api, fields, models, exceptions, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
import logging

_logger = logging.getLogger(__name__)


class he_employee(models.Model):
    _inherit = "hr.employee"

    medical_count = fields.Integer(compute='_medical_count', string='# revisiones')
    medical_ids = fields.One2many('hr.employee.medical', 'employee_id', 'Revisiones médicas')

    @api.one
    @api.depends('medical_ids')
    def _medical_count(self):
        medicals = self.env['hr.employee.medical'].search([('employee_id', '=', self.id)])
        self.medical_count = len(medicals)
