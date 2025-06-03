# -*- coding: utf-8 -*-
import base64
import logging
from odoo import models
from odoo.tools.safe_eval import json

from ..utils.signer import SifenSigner

_logger = logging.getLogger(__name__)

class SifenAPI(models.AbstractModel):
    _name = 'sifen.api'
    _description = 'Comunicación con SIFEN Paraguay'

    def generar_xml_de(self, factura):
        # Generación de XML simulado
        xml_content = f"<DE><Id>{factura.id}</Id><Total>{factura.amount_total}</Total></DE>"
        return xml_content.encode('utf-8')

    def firmar_y_enviar(self, factura):
        params = self.env['ir.config_parameter'].sudo()
        cert_bin = params.get_param('l10n_py_sifen.cert_p12')
        cert_pass = params.get_param('l10n_py_sifen.cert_pass')

        if not cert_bin:
            raise ValueError("Certificado digital no configurado")

        cert_bytes = base64.b64decode(cert_bin)
        signer = SifenSigner(cert_bytes, cert_pass)

        xml_content = self.generar_xml_de(factura)
        signed_xml = signer.sign_xml(xml_content)

        factura.write({
            'sifen_xml_signed': base64.b64encode(signed_xml),
            'sifen_xml_signed_name': f"{factura.name or 'factura'}_firmado.xml",
            'sifen_estado': 'firmado',
        })

        # Simulación de envío
        _logger.info("Enviado a SIFEN (simulado)")
        factura.write({'sifen_estado': 'enviado'})
