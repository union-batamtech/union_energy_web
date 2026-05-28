from odoo import fields, models


class WebsiteLandingSection(models.Model):
    _name = 'website.landing.section'
    _description = 'Landing Page Section'
    _order = 'sequence, id'

    name = fields.Char(string='Nama Internal', required=True, translate=True)
    section_type = fields.Selection(
        selection=[
            ('hero', 'Hero'),
            ('features', 'Fitur'),
            ('testimonial', 'Testimoni'),
            ('cta', 'Call to Action'),
            ('custom', 'Kustom'),
        ],
        string='Tipe Section',
        required=True,
        default='hero',
    )
    title = fields.Char(string='Judul', translate=True)
    subtitle = fields.Char(string='Subjudul', translate=True)
    body_html = fields.Html(string='Konten', translate=True, sanitize_attributes=False)
    image = fields.Image(string='Gambar', max_width=1920, max_height=1080)
    button_text = fields.Char(string='Teks Tombol', translate=True)
    button_url = fields.Char(string='URL Tombol', default='/contactus')
    sequence = fields.Integer(string='Urutan', default=10)
    website_published = fields.Boolean(string='Dipublikasikan', default=True)
    active = fields.Boolean(default=True)
