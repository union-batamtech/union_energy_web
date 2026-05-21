from odoo import api, fields, models


class Faq(models.Model):
    _name = 'union_energy.faq'
    _description = 'FAQ'
    _order = 'sequence asc'

    sequence = fields.Integer(string='Sequence', default=10, tracking=True)
    question = fields.Char(string='Question', tracking=True, required=True)
    answer = fields.Text(string='Answer', tracking=True, required=True)
    active = fields.Boolean(string='Active', default=False, tracking=True)

    def name_get(self):
        return [(faq.id, faq.question) for faq in self]
