from odoo import fields, models


class WebsiteServiceCard(models.Model):
    _name = 'website.service.card'
    _description = 'Homepage Service Card'
    _order = 'audience, sequence, id'

    name = fields.Char(string='Judul', required=True, translate=True)
    audience = fields.Selection(
        selection=[
            ('commercial', 'Commercial'),
            ('residential', 'Residential'),
        ],
        string='Audience',
        required=True,
        default='commercial',
    )
    service_type = fields.Selection(
        selection=[
            ('solar', 'Solar Power'),
            ('electricity', 'Electricity'),
            ('ev_charging', 'EV Charging'),
        ],
        string='Kategori',
        required=True,
        default='solar',
    )
    image = fields.Image(string='Gambar', max_width=1200, max_height=800)
    link_url = fields.Char(string='URL', default='/solar-power')
    sequence = fields.Integer(string='Urutan', default=10)
    website_published = fields.Boolean(string='Dipublikasikan', default=True)
    active = fields.Boolean(default=True)
