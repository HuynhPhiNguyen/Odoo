# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HospitalAppointment (models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Hospital Appointment'
    _rec_name ='patient_id'

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    gender = fields.Selection(related='patient_id.gender')
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now )
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    ref = fields.Char(string ="Reference", help="Testing help")
    doctor_id = fields.Many2one('res.users', string='Doctor')
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines','appointment_id', string='Pharmacy Lines' )
    # image = fields.Image(string="Image")

    # add a html field on oddo
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection([
            ('0','Normal'),
            ('1','Low'),
            ('2','High'),
            ('3','Very High') ], string="Priority")
    # status bar
    state = fields.Selection([
            ('draft','Draft'),
            ('in_consultation','In Consultation'),
            ('done','Done'),
            ('cancel','Cancel') ], default='draft', string="Status", required=True)





    
    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref
    # action button test
    def action_test(self):
        print("Action button!!!!!")  
        return {
            'effect':{
                'fadeout':'slow',
                'message': 'Click Successfull',
                'type':'rainbow_man',
            }
        }  

    def unlink(self):
        if self.state != 'draft':
            raise ValidationError(_("You can delete appointment only in draf status "))
        return super(HospitalAppointment, self).unlink()

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'
		
    def action_done(self):
        for rec in self:
            rec.state = 'done'
		
    def action_cancel(self):
        action = self.env.ref('om_hosptal.action_cancel_appointment').read()[0]
        return action
            
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    class AppointmentPharmacyLines(models.Model):
        _name = "appointment.pharmacy.lines"
        _description = "Appointment Pharmacy Lines"

        product_id = fields.Many2one('product.product', required=True)
        price_unit = fields.Float(string='Price')
        qty = fields.Integer(string='Quantity', default=1)
        appointment_id =fields.Many2one('hospital.appointment',string='Appointment')
