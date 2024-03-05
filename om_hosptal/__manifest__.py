# -*- coding: utf-8 -*-
{
    'name': "Hospital Management Test",
    'version' : '1.0.0',
    'category' : 'Hospital',
    'author' : 'Phi Nguyen',
    'sequence' : -100,
    'summary' : 'Hospital mangement system testing',
    'description' : 'Hospital mangement system testing',
    'depends' : ['mail', 'product'],
    'data' : [
        'security/ir.model.access.csv',
        'data/patient_tag_data.xml',
        'data/price.tag.csv',
        'data/price.tag.csv',
        'data/sequence_data.xml',
        'wizard/cancel_appointment_view.xml',
        'views/menu.xml',
        'views/patients_view.xml',
        'views/patients_female_view.xml',
        'views/appointment_view.xml',
        'views/price_tag_view.xml',
    ],
    'demo' : [],
    'application' : True,
    'auto_install' : False,
    'license' : 'LGPL-3', 
    'icon': 'static/description/icons8-hospital-48.png',
}
