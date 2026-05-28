from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools import is_html_empty


class WebsiteFaqItem(models.Model):
    _name = 'website.faq.item'
    _description = 'FAQ Item'
    _order = 'sequence, id'

    question = fields.Char(string='Pertanyaan', required=True, translate=True)
    answer_html = fields.Html(string='Jawaban', translate=True, sanitize_attributes=False)
    category_id = fields.Many2one(
        comodel_name='website.faq.category',
        string='Kategori',
        ondelete='set null',
    )
    sequence = fields.Integer(string='Urutan', default=10)
    website_published = fields.Boolean(string='Dipublikasikan', default=False)
    active = fields.Boolean(default=True)

    @api.constrains('answer_html', 'website_published')
    def _check_answer_html(self):
        for item in self:
            if item.website_published and is_html_empty(item.answer_html):
                raise ValidationError(
                    self.env._('Jawaban wajib diisi untuk FAQ yang dipublikasikan.')
                )
