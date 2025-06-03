# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    sifen_cdc = fields.Char(string="Código de Control (CDC)", readonly=True)
    sifen_estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('firmado', 'Firmado'),
        ('enviado', 'Enviado'),
        ('aceptado', 'Aceptado'),
        ('rechazado', 'Rechazado'),
    ], string="Estado SIFEN", default='pendiente', readonly=True)
    sifen_xml_signed = fields.Binary(string="XML Firmado", readonly=True)
    sifen_xml_signed_name = fields.Char(string="Nombre XML", readonly=True)
    sifen_modo_emision = fields.Selection([
        ('normal', 'Normal'),
        ('contingencia', 'Contingencia')
    ], string="Modo de Emisión", default='normal')

    def action_generar_xml(self):
        self.ensure_one()
        self.message_post(body="XML generado (simulado).")

    def action_firmar_xml(self):
        self.ensure_one()
        self.write({
            'sifen_estado': 'firmado',
            'sifen_xml_signed_name': f"{self.name or 'factura'}_firmado.xml",
        })
        self.message_post(body="XML firmado (simulado).")

    def action_enviar_sifen(self):
        self.ensure_one()
        self.write({'sifen_estado': 'enviado'})
        self.message_post(body="Enviado al SIFEN (simulado).")

    def action_consultar_estado_sifen(self):
        self.ensure_one()
        self.write({'sifen_estado': 'aceptado'})
        self.message_post(body="Estado actualizado desde SIFEN (simulado).")
