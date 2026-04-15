import requests
import json

class SOCNotifier:
    def __init__(self):
        # Aquí pegarás la URL de tu Webhook de Discord o Slack después
        self.webhook_url = "TU_WEBHOOK_AQUI"

    def send_alert(self, ip, malicious_count, details):
        if self.webhook_url == "TU_WEBHOOK_AQUI":
            print("[!] Notificación omitida: Webhook no configurado.")
            return

        payload = {
            "content": "🚨 **ALERTA DE SEGURIDAD DETECTADA** 🚨",
            "embeds": [{
                "title": "Intento de Intrusión Identificado",
                "color": 15158528, # Rojo
                "fields": [
                    {"name": "IP Atacante", "value": ip, "inline": True},
                    {"name": "Reportes Maliciosos", "value": str(malicious_count), "inline": True},
                    {"name": "Estado", "value": "⚠️ Bloqueo Recomendado", "inline": False}
                ],
                "footer": {"text": "Sentinel SOC - Automatización de Ciberseguridad"}
            }]
        }
        
        try:
            requests.post(self.webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        except Exception as e:
            print(f"Error enviando notificación: {e}")
