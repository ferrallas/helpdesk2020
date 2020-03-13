from odoo import fields, models, api, _


class HelpdeskTicket (models.Model):
    _name = 'helpdesk.ticket'
    # heredo la funcionalidad de los mixin
    # da igual inherit que inherits en V13
    _inherit = ["mail.thread", "utm.mixin"]

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
    user_ids = fields.Many2many(
        comodel_name='res.users',
        relation="helpdesk_ticket_users_rel",
        column1="ticket_id", column2="user_id",
        string='Users',
    )
    responsable_id = fields.Many2one(
        comodel_name='res.user',
        string='Responsable')

    # onchange modifico un cliente, me actualiza la tarifa
    # modifico un producto, me actualiza el precio
    # cuando se modifique sel campo name o se modifique el campo date_deadline
    @api.onchange('name','date_deadline')
    def _onchange_description(self):
        # concatenacion absurda
        # name es required, deberi atener un valor siempre, pero puede que en el formulario no tenga ningun valor todavia si no lo he guardado
        # self.description = '%s - %s'%(self.name,self.date_deadline)
        if self.name and self.date_deadline:
            self.description = self.name + self.date_deadline

    # ejemplo apuntar cosas en el chatter
    # dentro del mail.sendmesagewithtemplate -> heredamoms el write -> y ponemos el onchange
    # code = fields.Char(string='Reference', index=True, tracking=True)

    # diferencia entre onchange y calculado
    # calculado en el momento de abrir
    # calculado y se almacene
    # si se modifica een esos otros modelos -> se recalcula en mi modelo (STORE)
    # ej mil leads tienen una funcion compleja, leerlo le va a costar mucho, se hace store y se irá recalculando
    # mejora la busqueda, si no tendria que redifinir una funcion search para el campo calculado

    # NUEVO CAMPO CALCULADO

    tickets_qty = fields.Integer(
        string='Tickets Qty',
        compute='_compute_tickets_qty'
    )

    # si se hace una actualiacion de un campo storage, se hace por base de datos, si no puede morir x timempo recargando
    # ej 200,000 facturas

    @api.depends('responsable_id')
    def _compute_tickets_qty(self):
        # self es un recordset, no un record, tengo que recorrer todos los tickets
        ticket_obj = self.env['helpdesk.ticket']
        # import pdb; pdb.set_trace()
        # web debugger wdb
        for ticket in self:
            tickets = ticket_obj.search(
                [('responsable_id', '=', 'ticket.responsable_id.id')]
            )
            ticket.tickets_qty = len(tickets)




    # boton para el formulario
    # self puedo tener uno, muchos o ninguno
    # solo se puede ejecutar si self es solo un ticket
    # quiero actualizar el valor del responsable
    # en self. tengo acceso al environment
    def selt_responsable(self):
        self.insure_one()

    # escrito a base de datos
    #  1) solo un acceso a la BBDD
        self.responsable_id = self.env.user

    # 2)
        self.write({
        'responsible_id':self.env.user.id
        })





    # """
    # @api.onchange('team_id')
    # def onchange_method(self):
    #     if self.team_id is not None and self.team_id is not False and self.team_id != [] and \
    #             self.team_id.user_ids is not None and self.team_id.user_ids is not False and self.team_id.user_ids != []:
    #         self.user_ids = [user for user in self.team_id.user_ids]
    # """
