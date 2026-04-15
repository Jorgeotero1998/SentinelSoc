import json, os
from datetime import datetime

LOG_FILE = "src/logs/forensic_audit.json"

def generate_report():
    if not os.path.exists(LOG_FILE):
        print("[!] No hay base de datos para analizar.")
        return

    print("="*60)
    print(f"        REPORTE EJECUTIVO DE SEGURIDAD - SENTINEL SOC")
    print("="*60)
    
    total_events = 0
    critical_threats = 0
    actions = {}

    with open(LOG_FILE, "r") as f:
        for line in f:
            event = json.loads(line)
            total_events += 1
            if event.get("severity") == "CRITICAL":
                critical_threats += 1
            
            tipo = event.get("event_type")
            actions[tipo] = actions.get(tipo, 0) + 1

    print(f"[*] Total de eventos auditados: {total_events}")
    print(f"[*] Amenazas Críticas (Ransomware): {critical_threats}")
    print("[*] Desglose de actividades:")
    for act, cant in actions.items():
        print(f"    - {act}: {cant}")
    print("="*60)
    print(f"Reporte generado el: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    generate_report()
