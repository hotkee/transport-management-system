# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2014 Argil Consulting - http://www.argil.mx
############################################################################
#    Coded by: Israel Cruz Argil (israel.cruz@argil.mx)
############################################################################
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


from osv import fields, osv


class tms_expense_line(osv.osv):
    _inherit = 'tms.expense.line'

    _columns = {
        'invoice_xml_file': fields.binary('Archivo XML', filters='*.xml', required=False, help='Aquí se debe subir el archivo XML de la Factura CFDI'),        
        'invoice_pdf_file': fields.binary('Archivo PDF', filters='*.pdf', required=False, help='Aquí se puede subir el archivo PDF de la Factura CFDI'),        
        
        }

 