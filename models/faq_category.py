from odoo import fields, models


class WebsiteFaqCategory(models.Model):
    _name = 'website.faq.category'
    _description = 'FAQ Category'
    _order = 'sequence, name'

    name = fields.Char(string='Kategori', required=True, translate=True)
    sequence = fields.Integer(string='Urutan', default=10)
    item_ids = fields.One2many(
        comodel_name='website.faq.item',
        inverse_name='category_id',
        string='Pertanyaan',
    )
    item_count = fields.Integer(compute='_compute_item_count')

    def _compute_item_count(self):
        for category in self:
            category.item_count = len(category.item_ids)
