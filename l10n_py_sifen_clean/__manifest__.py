# -*- coding: utf-8 -*-
{
    "name": "Paraguay - Facturación Electrónica (SIFEN)",
    "version": "18.0.1.0.0",
    "category": "Localization/Paraguay",
    "summary": "Emisión de Documentos Electrónicos conforme al SIFEN (SET - Paraguay)",
    "description": """
Este módulo permite emitir y gestionar Documentos Electrónicos (DE) conforme a los lineamientos de la Subsecretaría de Estado de Tributación (SET) de Paraguay y su sistema SIFEN.

Características:
- Generación de XML conforme a los esquemas de la SET
- Firma digital con certificado .p12
- Envío de facturas electrónicas al SIFEN
- Consulta de estado y CDC
- Generación del KuDE con código QR
- Compatible con facturación en modo contingencia
- Configuración sencilla desde Ajustes

Desarrollado para Odoo Community v18. Compatible con despliegues en Cloudpepper.
""",
    "author": "Desarrollo a medida",
    "website": "https://www.set.gov.py",
    "license": "LGPL-3",
    "depends": ["account"],
    "data": [
        "security/ir.model.access.csv",
        "data/sifen_document_types.xml",
        "views/invoice_views.xml",
        "views/settings_views.xml",
        "reports/kude_template.xml"
    ],
    "assets": {},
    "application": True,
    "installable": True,
    "auto_install": False,
    "icon": "static/description/icon.png"
}
