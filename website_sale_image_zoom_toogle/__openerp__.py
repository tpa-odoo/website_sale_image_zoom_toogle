# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2015 Turkesh - https://turkeshpatel.odoo.com
#    All Rights Reserved.
#    Turkesh Patel (turkesh4friends@gmail.com)
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
    'name': 'Website Product Image Zoom toogle',
    'category': 'Website',
    'version': '1.0',
    'author': 'Turkesh Patel',
    'website': 'https://turkeshpatel.odoo.com',
    "description": """Using this module you can zoom image of product on click(toogle) for our website shop.""",
    "summary": "This module can be useful for adding image zoom functionality on mouse click(toogle) for your e-commerce website.",
    'depends': ['product', 'sale', 'website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/template.xml',
    ],
    'images': [
        'static/description/icon.png',
    ],
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
