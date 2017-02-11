# -*- encoding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": "Informes Valia",
    "version": "1.0",
    "author": "BisneSmart Team,"
              "BisneSmart",
    "contributors": [
        "Gonzalo Borras <gborras@bisnesmart.com>",
        "Ruben Cabrera <rcabrera@bisnesmart.com>",
        "Departamento Odoo <odoo@bisnesmart.com>",
    ],
    "website": "http://www.bisnesmart.com",
    "depends": [
        "stock",
        "account",
        # "product_manufacturer",
        "product",
        "base",
        "sale",
        "stock_picking_taxes",
        "stock_valued_picking_report",
        "sale_validity",
        "account_invoice_production_lot",
        "sale_order_taxes",
        "account_invoice_shipping_address",
    ],
    "data": [
        "views/stock/power_stock_picking.xml",
        "views/stock/prima_almacen.xml",
        #"views/stock/power_del_shipping.xml",
        #"views/stock/power_stock_picking_not_valued.xml",
        #"views/stock/stock_report_picking_in_out.xml",
        "views/sale/report_saleorder_ledyspa.xml",
        "views/sale/report_saleorder_ledyspa_document.xml",
        "views/external_layout/external_layout_header_power.xml",
        "views/external_layout/external_layout_footer_power.xml",
        "views/purchases/report_purchaseorder_power.xml",
        "views/purchases/report_purchaseorder_power_document.xml",
        "views/account/report_invoice_powerworks.xml",
        "views/account/report_invoice_powerworks_document.xml",




        # "views/product_view.xml",

    ],
    "installable": True,
    "application": True,
    #"active": True,
}
