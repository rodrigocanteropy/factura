# -*- coding: utf-8 -*-
from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sifen_ambiente = fields.Selection([
        ('1', 'Producción'),
        ('2', 'Pruebas')
    ], string="Ambiente SIFEN", default='2', config_parameter='l10n_py_sifen.ambiente')

    sifen_ruc_emisor = fields.Char("RUC Emisor", config_parameter='l10n_py_sifen.ruc_emisor')
    sifen_cert_p12 = fields.Binary("Certificado Digital (.p12)", config_parameter='l10n_py_sifen.cert_p12')
    sifen_cert_pass = fields.Char("Contraseña Certificado", config_parameter='l10n_py_sifen.cert_pass')
    sifen_url = fields.Char("URL WS SIFEN", config_parameter='l10n_py_sifen.url', default="https://ekuatia.set.gov.py/")

