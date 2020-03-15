# from odoo import exceptions

from odoo.tests import SavepointCase


class TestHelpdeskTicket(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.team_obj = cls.env["helpdesk.team"]
        cls.ticket_obj = cls.env["helpdesk.ticket"]
        cls.ticket_stage_obj = cls.env["helpdesk.ticket.stage"]
        cls.user_obj = cls.env["res.users"]

        cls.user_demo = cls.env.ref('base.user_demo')
        cls.user_admin = cls.env.ref('base.user_admin')

    def test_create_ticket_demo(self):
        date = 'no date'
        ticket_name = 'test ticket'
        ticket = self.ticket_obj.create({
            'name': ticket_name,
            'responsable_id': self.user_demo.id
        })
        self.assertEqual(ticket.description, 'test ticket - no date')



    def test_create_ticket_admin(self):
        ticket = self.ticket_obj.create({
            'responsable_id': self.user_admin.id
        })


'''
from odoo.test import SaveointCase

# XML_ID externo para hacer referencia al usuario
# primero -i para instalar el modulo, desp -u (dependencias)
# odoo.conf -d curso20201 -i helpdesk_curso stopafterinit test enable
# el nombre del fichero tiene que llevar test_ delante test_helpdesk_ticket

# transaction case == savepointcase


# para probar si funcionan los test condicion de error ->  self.assertEqual(1,False)
# defino los datos que recojo de env

class TestHelpdeskTicket(SavepointCase):
        @classmethod
        def setUpClass(cls):
            super().setUpClass()
            cls.team_obj = cls.env['helpdesk.team']
            cls.ticket_obj = cls.env['helpdesk.ticket']
            cls.ticket_stage_obj = cls.env['helpdesk.ticket.stage']
            cls.user_demo = cls.env.ref('base.user_demo')
            cls.user_admin = cls.env.ref('base.user_admin')

            # defino los test

            def test(self):
                date = 'no_date'
                ticket_name = 'test_ticket'
'''


