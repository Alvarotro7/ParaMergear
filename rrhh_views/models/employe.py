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
    _inherit = "hr.employee"

    street = fields.Char(
        #related="address_home_id.name",
        string="Domicilio",
        store=True
    )

    street2 = fields.Char(
        #related="address_home_id.street",
        string="Domicilio2",
        store=True
    )

    cp_empleado = fields.Char(
        #related="address_home_id.zip",
        string="C.P:",
        store=True
    )



    poblacion = fields.Char(
        #related="address_home_id.city",
        string="Población",
        store=True
    )

    provincia = fields.Many2one(
        #related="address_home_id.state_id",
        'res.country.state',
        string="Provincia",
        store=True
    )
    telefono_fijo = fields.Char(
        #related="address_home_id.phone",
        string="Telf Fijo",
        store=True
    )
    movil = fields.Char(
        #related="address_home_id.mobile",
        string="Telf movil",
        store=True
    )
    email_empleado = fields.Char(
        #related="address_home_id.email",
        string="Email",
        store=True
    )

    calzado = fields.Many2one('hr.employee.tallas', 'name')
    pantalon = fields.Many2one('hr.employee.tallas', 'name')
    camiseta = fields.Many2one('hr.employee.tallas', 'name')
    chaqueta = fields.Many2one('hr.employee.tallas', 'name')
    bata = fields.Many2one('hr.employee.tallas', 'name')


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
