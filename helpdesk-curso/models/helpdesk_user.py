from odoo import fields, models, api


class HelpDeskUser(models.Model):
    _inherit = "res.users"

    helpdesk_code = fields.Char(string="Helpdesk code",
                                required=False)


    """ticket_ids = fields.Many2many(
        comodel_name='helpdesk.ticket',
        relation="helpdesk_ticket_users_rel",
        column2="ticket_id", column1="user_id",
        string='Tickets',
    )"""

    """helpdeskteam_id = fields.Many2one(
        comodel_name='helpdesk.team',
        string='Helpdesk team',
        required=False)"""