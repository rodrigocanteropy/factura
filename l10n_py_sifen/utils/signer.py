# -*- coding: utf-8 -*-
import logging

_logger = logging.getLogger(__name__)

class SifenSigner:
    def __init__(self, p12_file, password):
        self.p12_file = p12_file
        self.password = password

    def sign_xml(self, xml_content):
        # Firma simulada sin caracteres especiales
        signed_xml = xml_content + b"<!-- Simulacion firma -->"
        _logger.info("XML firmado (simulado)")
        return signed_xml
