# -*- coding: utf-8 -*-
# © 2015 Oihane Crucelaegui - AvanzOSC
# © 2016 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3

from openerp.osv import osv, fields, expression
from openerp import api, fields, models, exceptions, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
import logging

_logger = logging.getLogger(__name__)


class he_employee(models.Model):
    _name = "hr.employee.tallas"

    name = fields.Char('Tallas')


    # contract_id = fields.One2many(
    #     comodel_name="hr.contract",
    #      inverse_name="employee_id",
    #      string="Assigned Machine",
    #      order='date_start desc',
    #      limit=1,)
    # horario = fields.Many2one(
    #     related='contract_id.working_hours',
    #     string='horario'
    # )
