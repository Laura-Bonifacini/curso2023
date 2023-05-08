from odoo import models, fields, api

class HelpdeskTicketTag(models.Model):
    _name = 'helpdesk.ticket.tag'
    _description = "Helpdesk Ticket Tag"

    name = fields.Char(required=True)

    ticket_ids = fields.Many2many(
        comodel_name='helpdesk.ticket',
        relation='helpdesk_ticekt_tag_rel',
        column1='tag_id',
        column2='ticket_id',
        string='Tickets'
    )

    @api.model
    def _clean_tags(self):
        self.search([('ticket_ids', '=', False)]).unlink()

    
     