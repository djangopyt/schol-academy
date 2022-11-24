# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class schol1courses(models.Model):
     _name = 'schol1.courses'
     _description = 'schol1.schol1'

     name = fields.Char(string="Title", required=True)
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text(string="desc")
     responsibl_id = fields.Many2one('res.users',ondelete='set null',string='responsibl',index=True)
     session_ids = fields.One2many('schol1.session','courses_id',string='sessions')

class Session(models.Model):
     _name = 'schol1.session'
     _description = 'description session'

     name = fields.Char(required=True)
     start_date = fields.Date(default=fields.Date.today)
     duration = fields.Float(digits=(6,2) ,help="duration in days")
     seats = fields.Integer(string="number the seats")
     instructor_id = fields.Many2one('res.partner',string='instructor')
     courses_id = fields.Many2one('schol1.courses',ondelete='CASCADE',string='course',required=True)
     attendee_ids = fields.Many2many('res.partner',string='attendee')
     active = fields.Boolean(default=True)
     token_seats = fields.Float(string="token seat", compute="_token_seats")


     @api.depends('seats','attendee_ids')
     def _token_seats(self):
          for r in self:
               if not r.seats:
                    r.token_seats = 0.0
               else:
                    r.token_seats = 100.0 * len(r.attendee_ids)/r.seats


     @api.onchange('seats','attendee_ids')
     def _verify_valid_seats(self):

          if self.seats < 0:

               return {
                    'warning': {
                                 'title': "incorrect 'seats' value",
                                 'message': "the number negative",
                                                                   },
                     }
          if self.seats < len(self.attendee_ids):
               return {
                    'warning': {
                                  'title': "too many attendees",
                                  'message': "increase seats or remove excess attendees",
                        },
                      }


     @api.constrains('instructor_id','attendee_ids')
     def _check_instructor_not_in_attendees(self):
          for r in self:
               if r.instructor_id and r.instructor_id in r.attendee_ids:
                    raise exceptions.ValidationError("a session instructor can t be attendee")
