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

    def detect_velocity(self):
        now = time.time()
        recent = [t for t in event_history if now - t < 1.0]
        return len(recent) > RANSOMWARE_THRESHOLD

    def on_any_event(self, event):
        if not event.is_directory:
            if any(x in event.src_path.lower() for x in [".tmp", ".ini", "desktop.ini"]):
                return
            current_time = datetime.now()
            event_history.append(current_time.timestamp())
            if len(event_history) > 100: event_history.pop(0)
            
            event_data = {
                "timestamp": current_time.strftime("%H:%M:%S"),
                "action": event.event_type.upper(),
                "file": os.path.basename(event.src_path),
                "status": "OK"
            }

            if self.detect_velocity():
                event_data["status"] = "CRITICAL"
                print(f"[{current_time.strftime('%H:%M:%S')}] 🚨 ALERTA: Actividad masiva detectada en {event_data['file']}")
            else:
                print(f"[{current_time.strftime('%H:%M:%S')}] [+] {event_data['action']}: {event_data['file']}")
            
            self.save_to_db(event_data)

if __name__ == "__main__":
    os.system('cls')
    print("-" * 50)
    print("             SENTINEL | BY JORGE OTERO")
    print("-" * 50)
    
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
        target_path, _ = winreg.QueryValueEx(key, "Desktop")
    except:
        target_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')

    print(f"[*] RUTA: {target_path}")
    print(f"[*] ESTADO: Vigilancia activa")
    print("[*] LOGS: logs/forensic_audit.json")
    print("-" * 50 + "\n")

    observer = Observer()
    observer.schedule(SentinelIntelligence(), target_path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
