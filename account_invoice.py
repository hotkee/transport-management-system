# -*- encoding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
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




from osv import osv, fields
import time
from datetime import datetime, date
import decimal_precision as dp
import openerp

# Add special tax calculation for Mexico
class account_invoice(osv.osv):
    _inherit ='account.invoice'


    _columns = {
        'tms_type'      : openerp.osv.fields.selection([
                        ('none', 'N/A'),
                        ('waybill', 'Waybill'),
                        ('invoice', 'Invoice'),
                        ], 'TMS Type', help="Waybill -> This invoice results from one Waybill (Mexico - Carta Porte/Guia con valor fiscal)\nInvoice -> This Invoice results from several Waybills (México - Carta Porte/Guia sin valor Fiscal)", require=False),
        'waybill_ids': openerp.osv.fields.one2many('tms.waybill', 'invoice_id', 'Waybills', readonly=True, required=False),
        'departure_address_id': openerp.osv.fields.many2one('res.partner.address', 'Departure Address', readonly=True, required=False),
        'arrival_address_id': openerp.osv.fields.many2one('res.partner.address', 'Arrival Address', readonly=True, required=False),
    }
    
    _defaults = {
        'tms_type' : 'none',        
    }

    def unlink(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        invoices = self.read(cr, uid, ids, ['state','internal_number', 'origin'], context=context)
        for invoice in invoices:
            if invoice['state'] in ('draft', 'cancel') and invoice['internal_number'] != False and invoice['origin'] == 'TMS-Fuel Voucher':
                self.write(cr, uid, ids, {'internal_number':False})
                
        return super(account_invoice, self).unlink(cr, uid, ids, context=context)

account_invoice()



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: