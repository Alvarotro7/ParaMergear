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
    _name = "hr.employee.formacion"

    name = fields.Many2one('hr.employee.cursos', 'name', required=True)

    employee_id = fields.Many2one('hr.employee', 'Employee', required=True)

    fecha_curso = fields.Date()

    fecha_validez_curso = fields.Date()

    observaciones = fields.Html()


class hr_employee_cursos(models.Model):
    _name = "hr.employee.cursos"

    name = fields.Char(
        string="Nombre Curso",
        required=True
    )
    observaciones = fields.Html()
