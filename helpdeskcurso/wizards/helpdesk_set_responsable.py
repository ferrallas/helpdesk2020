from odoo import models, api, fields, _


class HelpdeskSetResponsable(models.TransientModel):
    _name = 'helpdesk.set.responsable'

    tickets_qty = fields.Integer(
        string='Tickets Qty')

    @api.model
    def default_get(self, fields):
        res = super(HelpdeskSetResponsable, self).default_get(fields)
        user_id = self.env.user.id
        tickets = self.env['helpdesk.ticket'].search(
            [('responsable_id', '=', user_id)])
        res['tickets_qty'] = len(tickets)
        return res


    def set_responsable(self):
        self.ensure_one()
        # context = {
        #     'active_id': 3,
        #     'active_model': 'helpdesk.ticket'
        # }
        # context.get('active_ids') = False
        active_id = self.env.context.get('active_id')
        active_model = self.env.context.get('active_model')
        if active_id and active_model and active_model == 'helpdesk.ticket':
            ticket = self.env['helpdesk.ticket'].browse(active_id)
            ticket.responsable_id = self.env.user




'''
from odoo import models, api, fields, _


class HelpdeskSetResponsable(models.TransientModel):
    _name = 'helpdesk.set.responsable'


    tickets_qty = fields.Integer(
    string=
    )

# se va a ejecutar antes del dato, no tengo un objeto creado
# no voy a poder llamar a los campos de mi modelo porque no se han creado
# lo tengo que definit como api.model
    # hay una funcion default_get

    @api.model
    def default_get(self, fields):
        res = super(HelpdeskSetResponsable, self).default_get(fields)
        # quiero saber el numero de tickets que hay asignados a mi usuario
        # mi usuario sabemos que es seld env user_id o self .env.user_id
        user_id = self.env.user_id
        tickets = self.env['helpdesk.ticket']. # quiero buscar todos los tickets que estan asignados a un usuario => search (le tengo que pasar un domino, condiciones para cumplir)
        # campo sobre el que quiero buscar (responsable)
        self.env['helpdesk.ticket'].search([('responsable_id','=','user_id'])
        # tickets va a ser un recordset que cumple la condiciones
        # hago un count sobre un recordset

        res['tickets_qty'] = len(tickets) # numero de tickets que tengo asignados
        return res




    def set_responsable(self):
        self.ensure_one()
        ticket = False

        # ticket.responsable_id = self.env.user
        # resultado =
        # return res[0]


        # ejemplo diccionario en python, context

         # context =
         # {
         # 'active_id': 3,
         # 'active_model': 'helpdesk.ticket'
         # }
         # context.get('active_ids') = False
        # cuando yo lo lanzo, active_id = 3
        # si alguien llama al wizard desde un formulario diferente o directamente, no tendra el active_id

        if active_id:
        # ticket recoge un record, como es unico recibe 1
            ticket = self.env['helpdesk_ticket'].browse(active_id)
            ticket.responsable_id = self.env.user
'''