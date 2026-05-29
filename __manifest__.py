{
    'name': 'Website Landing Page & FAQ',
    'version': '19.0.1.3.0',
    'category': 'Website/Website',
    'summary': 'Halaman landing page dan FAQ yang dapat dikelola dari backend',
    'description': """
Website Landing Page & FAQ
==========================
Modul ini memungkinkan Anda membuat dan mengelola:

* **Landing Page** — section dinamis (hero, fitur, testimoni, CTA)
* **FAQ** — pertanyaan & jawaban dikelompokkan per kategori

Konten dikelola dari menu Website di backend Odoo.
Halaman publik: ``/`` (landing), ``/faq``, dan halaman menu via ``website.page``.
    """,
    'author': 'Aji',
    'website': 'https://www.example.com',
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/landing_section_views.xml',
        'views/service_card_views.xml',
        'views/services_section.xml',
        'views/faq_views.xml',
        'views/menu.xml',
        'views/footer.xml',
        'data/footer_config.xml',
        'views/templates.xml',
        'data/website_menu.xml',
        'data/website_pages.xml',
        'data/demo_data.xml',
        'data/services_content.xml',
        'data/hero_content.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'website_landing_faq/static/src/scss/website_landing_faq.scss',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
