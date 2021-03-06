# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Hiworth Chart of Accounts',
    'version': '1.0',
    'description': """
                    Tally default chart of accounts.""",
    'author': ['Hiworth'],
    'category': 'Account Charts',
    'depends': [
        'account',
        'account_chart'
    ],
    'demo': [],
    'data': [
#         'l10n_in_tax_code_template.xml',
        'l10n_in_schedule6_chart.xml',
        'l10n_in_schedule6_tax_template.xml',
        'l10n_in_wizard.xml',
    ],
    'auto_install': False,
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
