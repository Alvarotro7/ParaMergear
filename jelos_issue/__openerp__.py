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
    "name": "Jelos Issue",
    "version": "1.0",
    "author": "BisneSmart Team,"
              "BisneSmart",
    "contributors": [
        "Gonzalo Borras <gborras@bisnesmart.com>",
        "Alvaro Navarro <anavarro@bisnesmart.com>",
        "Departamento Odoo <odoo@bisnesmart.com>",
    ],
    "website": "http://www.bisnesmart.com",
    "depends": [
		'sales_team',
        'project',
        'jelos_other',
    ],
    "data": [
        "views/jelos_issue_view.xml",
    ],
    "installable": True,
    "application": True,

}
