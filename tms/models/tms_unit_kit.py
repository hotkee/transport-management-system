# -*- coding: utf-8 -*-
# © <2012> <Israel Cruz Argil, Argil Consulting>
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

# import time

from openerp import fields, models
# from openerp.tools.translate import _


# Units Kits
class TmsUnitKit(models.Model):
    _name = "tms.unit.kit"
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _description = "Units Kits"

    name = fields.Char('Name', size=64, required=True)
    unit_id = fields.Many2one('fleet.vehicle', 'Unit', required=True)
    # unit_type = fields.Many2one(
    #     'tms.unit.category',
    #     related='unit_id.unit_type_id',
    #     string='Unit Type', store=True, readonly=True)
    # trailer1_id = fields.Many2one('fleet.vehicle', 'Trailer 1',required=True)
    # trailer1_type = fields.Many2one(
    #     'tms.unit.category',
    #     related='trailer1_id.unit_type_id',
    #     string='Trailer 1 Type', store=True, readonly=True)
    # dolly_id = fields.Many2one('fleet.vehicle', 'Dolly')
    # dolly_type = fields.Many2one(
    #     'tms.unit.category',
    #     related='dolly_id.unit_type_id',
    #     string='Dolly Type', store=True, readonly=True)
    # trailer2_id = fields.Many2one('fleet.vehicle', 'Trailer 2')
    # trailer2_type = fields.Many2one(
    #     'tms.unit.category',
    #     related='trailer2_id.unit_type_id',
    #     string='Trailer 2 Type', store=True, readonly=True)
    employee_id = fields.Many2one(
        'hr.employee', 'Driver', domain=[('tms_category', '=', 'driver')])
    date_start = fields.Datetime('Date start', required=True)
    date_end = fields.Datetime('Date end', required=True)
    notes = fields.Text('Notes')
    active = fields.Boolean('Active', default=(lambda *a: True))

    # def _check_expiration(self):
    #     for record in self.browse(self):
    #         date_start = record.date_start
    #         date_end = record.date_end

    #         sql = (
    #             'select name from tms_unit_kit where id <> ' +
    #             str(record.id) + ' and unit_id = ' + str(record.unit_id.id) +
    #        ' and (date_start between ' + date_start + ' and ' + date_end +
    #             ' or date_end between ' + date_start + ' and ' + date_end +
    #             ');')

    #         self.execute(sql)
    #         data = filter(None, map(lambda x: x[0], self.fetchall()))
    #         if len(data):
    #             raise Warning(
    #                 _('Validity Error !'),
    #                 _('You cannot have overlaping expiration dates for \
    #                     unit %s !\n This unit is overlaping Kit << %s >>\
    #                     ') % (record.unit_id.name, data[0]))
    #         if record.dolly_id.id:
    #             sql = (
    #                 'select name from tms_unit_kit where id <> ' +
    #                 str(record.id) + ' and dolly_id = ' +
    #                 str(record.dolly_id.id) + ' and (date_start between ' +
    #                 date_start + ' and \'' + date_end +
    #                 ' or date_end between ' + date_start + ' and ' +
    #                 date_end + '\');')

    #             self.execute(sql)
    #             data = filter(None, map(lambda x: x[0], self.fetchall()))
    #             if len(data):
    #                 raise Warning(
    #                     _('Validity Error !'),
    #                     _('You cannot have overlaping expiration dates for \
    #                     dolly %s !\n This dolly is overlaping Kit << %s >>\
    #                     ') % (record.dolly_id.name, data[0]))
    #         sql = ('select name from tms_unit_kit where id <> ' +
    #                str(record.id) + ' and (trailer1_id = ' +
    #                str(record.trailer1_id.id) + 'or trailer2_id = ' +
    #                str(record.trailer1_id.id) + ')' +
    #                ' and (date_start between \'' + date_start + '\' and \'' +
    #                date_end + '\'' + ' or date_end between \'' + date_start +
    #                '\' and \'' + date_end + '\');')
    #         self.execute(sql)
    #         data = filter(None, map(lambda x: x[0], self.fetchall()))
    #         if len(data):
    #             raise Warning(
    #                 _('Validity Error !'),
    #                 _('You cannot have overlaping expiration dates for \
    #                 trailer %s !\n This trailer is overlaping Kit << %s >>\
    #                 ') % (record.trailer1_id.name, data[0]))
    #         if record.trailer2_id.id:
    #             sql = (
    #                 'select name from tms_unit_kit where id <> ' +
    #                 str(record.id) + ' and (trailer1_id = ' +
    #                 str(record.trailer2_id.id) + 'or trailer2_id = ' +
    #                 str(record.trailer2_id.id) + ')' +
    #         ' and (date_start between \'' + date_start + '\' and \'' +
    #                 date_end + '\'' + ' or date_end between \'' +
    #                 date_start + '\' and \'' + date_end + '\');')
    #             self.execute(sql)
    #             data = filter(None, map(lambda x: x[0], self.fetchall()))
    #             if len(data):
    #                 raise Warning(
    #                     _('Validity Error !'),
    #                     _('You cannot have overlaping expiration dates \
    #                     for trailer %s !\n This trailer is overlaping \
    #                     Kit << %s >>') % (record.trailer2_id.name, data[0]))
    #         return True

    # _constraints = [
    #     (_check_expiration,
    #         'The expiration is overlaping an existing Kit for this unit!',
    #         ['date_start'])
    # ]

    # _sql_constraints = [
    #     ('name_uniq', 'unique(unit_id,name)',
    #      'Kit name number must be unique for each unit !'),
    # ]
    # _order = "name desc, date_start desc"

    # def on_change_tms_unit_id(self, tms_unit_id):
    #     res = {'value': {'date_start': time.strftime('%Y-%m-%d %H:%M')}}
    #     if not (tms_unit_id):
    #         return res
    #   self.execute("select date_end from tms_unit_kit where id=%s order by  \
    #       date_end desc limit 1", tms_unit_id)
    #     date_start = self.fetchall()
    #     if not date_start:
    #         return res
    #     else:
    #         return {'value': {'date_start': date_start[0]}}

    # def on_change_active(self, active):
    #     if active:
    #         return {}
    #     return {'value': {'date_end': time.strftime('%d/%m/%Y %H:%M:%S')}}
