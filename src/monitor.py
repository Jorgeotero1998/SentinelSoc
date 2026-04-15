import time, os, sys, json, winreg
from datetime import datetime
try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError:
    os.system("pip install watchdog pywin32")
    import time

LOG_FILE = "logs/forensic_audit.json"
RANSOMWARE_THRESHOLD = 4
event_history = []

class SentinelIntelligence(FileSystemEventHandler):
    def save_to_db(self, data):
        try:
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(json.dumps(data) + "\n")
        except:
            pass

    def detect_ransomware(self):
        now = time.time()
        recent_events = [t for t in event_history if now - t < 1.0]
        return len(recent_events) > RANSOMWARE_THRESHOLD

    def on_any_event(self, event):
        if not event.is_directory:
            if any(x in event.src_path.lower() for x in [".tmp", ".ini", "desktop.ini"]):
                return
            current_time = datetime.now()
            event_history.append(current_time.timestamp())
            if len(event_history) > 100: event_history.pop(0)
            event_data = {
                "timestamp": current_time.strftime("%Y-%m-%d %H:%M:%S"),
                "event_type": event.event_type.upper(),
                "file": os.path.basename(event.src_path),
                "severity": "LOW"
            }
            if self.detect_ransomware():
                event_data["severity"] = "CRITICAL"
                print(f"\n[🚨] ALERTA: ACTIVIDAD SOSPECHOSA EN {event_data['file']}")
            else:
                print(f"[+] Monitor: {event_data['event_type']} -> {event_data['file']}")
            self.save_to_db(event_data)

if __name__ == "__main__":
    os.system('cls')
    print("="*60 + "\n                SENTINEL BY JORGE OTERO\n" + "="*60)
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
        target_path, _ = winreg.QueryValueEx(key, "Desktop")
    except:
        target_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    print(f"[*] Escaneando: {target_path}")
    print("[*] Proteccion Heuristica: ACTIVA")
    print("[!] Sistema Operativo y Protegiendo...\n")
    observer = Observer()
    observer.schedule(SentinelIntelligence(), target_path, recursive=False)
    observer.start()
    try:
        while True: time.sleep(0.1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
