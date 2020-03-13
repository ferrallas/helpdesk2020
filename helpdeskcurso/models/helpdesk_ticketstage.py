from odoo import fields, models, api


class HelpDeskTicketStage (models.Model):
    _name = 'helpdesk.ticket.stage'

    name = fields.Char(string="Stage", required=True)

