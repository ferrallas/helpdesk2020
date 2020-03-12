from odoo import fields, models, api, _


class HelpdeskTicket (models.Model):
    _name = 'helpdesk.ticket'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    date_deadline = fields.Datetime(string='Date limit')

    stage_id = fields.Many2one(
        comodel_name='helpdesk.ticket.stage',
        string='Stage',
        required=True)
    team_id = fields.Many2one(
        comodel_name='helpdesk.team',
        string='Team',
        required=True)