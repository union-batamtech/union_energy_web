from odoo import api, models

# Odoo website footer templates that replace //div[@id='footer'] (must stay inactive).
WEBSITE_FOOTER_TEMPLATE_XMLIDS = (
    'website.footer_custom',
    'website.template_footer_descriptive',
    'website.template_footer_centered',
    'website.template_footer_links',
    'website.template_footer_minimalist',
    'website.template_footer_contact',
    'website.template_footer_call_to_action',
    'website.template_footer_headline',
    'website.template_footer_mega',
    'website.template_footer_mega_columns',
    'website.template_footer_mega_links',
    'website.template_footer_mega_cards',
    'website.template_footer_slideout',
)


class IrUiView(models.Model):
    _inherit = 'ir.ui.view'

    @api.model
    def _website_landing_faq_activate_union_footer(self):
        """Deactivate Odoo footer templates; keep Union footer active on every page."""
        union = self.env.ref('website_landing_faq.union_footer', raise_if_not_found=False)
        if not union:
            return

        for xmlid in WEBSITE_FOOTER_TEMPLATE_XMLIDS:
            view = self.env.ref(xmlid, raise_if_not_found=False)
            if view and view.id != union.id:
                view.active = False

        # Legacy template id from earlier module versions
        legacy = self.env.ref('website_landing_faq.footer', raise_if_not_found=False)
        if legacy and legacy.id != union.id:
            legacy.active = False

        layout = self.env.ref('website.layout')
        competing = self.search([
            ('inherit_id', '=', layout.id),
            ('active', '=', True),
            ('id', '!=', union.id),
            '|',
            ('key', '=like', 'website.template_footer%'),
            ('key', '=', 'website.footer_custom'),
        ])
        if competing:
            competing.write({'active': False})

        # Website editor may save a per-website copy of an old footer template.
        cow_footer_views = self.search([
            ('inherit_id', '=', layout.id),
            ('active', '=', True),
            ('website_id', '!=', False),
            ('id', '!=', union.id),
        ]).filtered(
            lambda v: 'id="footer"' in (v.arch_db or '') or "id='footer'" in (v.arch_db or '')
        )
        if cow_footer_views:
            cow_footer_views.write({'active': False})

        union.active = True
