# -*- coding: utf-8 -*-
from datetime import date
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HospitalPatient (models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Hospital Patient'

    name = fields.Char(string ="Name", tracking= True)
    date_of_birth = fields.Date(string="Date Of Birth")
    ref = fields.Char(string ="Reference")
    age = fields.Integer(string = "Age", compute='_compute_age', tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string="Gender")
    active = fields.Boolean(string="Active", default=True)
    tag_ids = fields.Many2many('price.tag', string="Tags")
    image = fields.Image(string="Image")
    appointment_count = fields.Integer(string='Appointment count', compute='_compute_appointment_count', store=True)
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string='Appointments')
    
    # compute the appointment count and store in db
    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])

    @api.constrains('date_of_birth')
    def check_date_of_birth(self):
        print("Today: ", fields.Date.today())
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.Date.today():
                 raise ValidationError(_("The entred date of birth is not aplicable !"))

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)
    
    def write(self, vals):
        if not self.ref and not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).write(vals)

    @api.depends('date_of_birth') #compute age in the real time when user change date of birth
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0

    def name_get(self):
	    return [(record.id, "[%s] %s"% (record.ref, record.name)) for record in self]