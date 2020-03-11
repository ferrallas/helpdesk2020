from odoo import fields, models, api, _


class HelpdeskTicket (models.Model):
    _name = 'helpdesk.ticket'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    date_deadline = fields.Datetime(string='Date limit')
