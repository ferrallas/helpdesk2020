from odoo import fields, models, api


class HelpDeskTeam (models.Model):
    _name = 'helpdesk.team'
    _description = 'Description'

    name = fields.Char(string="Name", required=True)

    ticket_ids = fields.One2many(
        comodel_name='helpdesk.ticket',
        inverse_name='team_id',
        string='Tickets',
        required=False)

