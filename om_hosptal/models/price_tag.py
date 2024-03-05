# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
class PriceTag (models.Model):
    _name = 'price.tag'
    _description = 'Price Tag'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Actice', default=True, copy=False)
    color = fields.Integer(string = 'Color' )
    color_2 = fields.Char(string="Color 2")
    sequence = fields.Integer(string="Sequence")

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        
        if not default.get('name'):
            default['name'] = _("(copy of) %s", self.name)
        default['sequence'] = 10
        return super(PriceTag, self).copy(default)


    _sql_constraints = [
        ('unique_tag_name', 'unique (name,active)', 'Name must be unique.'),
        ('check_sequence', 'check (sequence > 0)', 'Sequence must be > 0.')
    ]
   