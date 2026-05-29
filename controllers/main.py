from odoo import http
from odoo.addons.website.controllers.main import Website
from odoo.http import request


class WebsiteLandingFaq(Website):
    """Landing page on ``/`` and FAQ on ``/faq`` / ``/electricity/faqs``."""

    def _get_service_cards(self):
        cards = request.env['website.service.card'].sudo().search([
            ('active', '=', True),
            ('website_published', '=', True),
        ])
        return {
            'commercial_cards': cards.filtered(lambda c: c.audience == 'commercial'),
            'residential_cards': cards.filtered(lambda c: c.audience == 'residential'),
        }

    @http.route('/', auth='public', website=True, sitemap=True)
    def index(self, **kwargs):
        sections = request.env['website.landing.section'].sudo().search([
            ('active', '=', True),
            ('website_published', '=', True),
        ])
        return request.render('website_landing_faq.landing_page', {
            'sections': sections,
            **self._get_service_cards(),
        })

    @http.route(['/landing', '/landing-page'], auth='public', website=True, sitemap=True)
    def landing_page(self, **kwargs):
        return self.index(**kwargs)

    @http.route(['/faq', '/electricity/faqs'], auth='public', website=True, sitemap=True)
    def faq_page(self, **kwargs):
        env = request.env
        return request.render('website_landing_faq.faq_page', {
            'categories': env['website.faq.category'].sudo().search([]),
            'faq_items': env['website.faq.item'].sudo().search([
                ('active', '=', True),
                ('website_published', '=', True),
            ]),
        })
