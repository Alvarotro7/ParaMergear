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
    albaranes_count = fields.Integer(compute='_albaranes_count', string='# albaranes')
    albaran_ids = fields.One2many('stock.picking', 'partner_id', 'Albaranes empleado')
    partner_id = fields.Many2one(compute='_compute_partner')

    @api.one
    @api.depends('formacion_ids')
    def _formaciones_count(self):
        formaciones = self.env['hr.employee.formacion'].search([('employee_id', '=', self.id)])
        self.formaciones_count = len(formaciones)

    @api.one
    @api.depends('albaran_ids')
    def _albaranes_count(self):
        albaranes = self.env['stock.picking'].search([('partner_id', '=', self.user_id.partner_id.id)])
        self.albaranes_count = len(albaranes)

    @api.one
    def _compute_partner(self):
        partner = self.env['res.partner'].search([('id', '=', self.user_id.partner_id.id)])
        self.partner_id = partner.id
