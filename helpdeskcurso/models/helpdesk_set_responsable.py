from odoo import models, api, fields, _

#transitmodel porque es un wizzard

class HelpdeskSetResponsable(models.TransitModel):
_name = 'helpdesk.set.responsable'



def set_responsable(self):
    self.ensure_one()
    ticket.responsable_id = self.env.user
