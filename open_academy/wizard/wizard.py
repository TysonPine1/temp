from odoo import fields, models, api

class CreateAttendee(models.TransientModel):
    _name = "create.wizard"
    _description = "Create Attendee"
    
    session_id = fields.Many2one("openacademy.session", string="Session" )
    partner_id = fields.Many2many("res.partner", string="Attendees")
    course_id = fields.Many2one("openacademy.course",'Course')
    date = fields.Date(string='Date')
    
    def acton_wizport(self):
        
        data = {
            'model': 'create.wizard',
            'session_id': self.session_id.id,
            'partner_id': self.partner_id.ids,
            'date': self.date,
            'form': self.read()[0]
        }
        print(data)
        return self.env.ref('open_academy.action_report_wiz').with_context(landscape=True).report_action(self, data=data)