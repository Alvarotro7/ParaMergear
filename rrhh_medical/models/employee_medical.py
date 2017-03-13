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
    _name = "hr.employee.medical"

    name = fields.Char(
        string="Referencia",
        required=True
    )
    employee_id = fields.Many2one('hr.employee', 'Employee', required=True)

    fichero = fields.Binary()

    fecha_revision = fields.Date()

    fecha_validez = fields.Date()

    observaciones = fields.Html()
