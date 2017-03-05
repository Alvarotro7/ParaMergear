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

    formaciones_count = fields.Integer(compute='_formaciones_count', string='# formaciones')
    formacion_ids = fields.One2many('hr.employee.formacion', 'employee_id', 'Formaciones empleado')

    @api.one
    @api.depends('formacion_ids')
    def _formaciones_count(self):
        formaciones = self.env['hr.employee.formacion'].search([('employee_id', '=', self.id)])
        self.formaciones_count = len(formaciones)
