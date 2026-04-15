import time, os, sys, json, winreg
from datetime import datetime
try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError:
    os.system("pip install watchdog pywin32")
    import time

LOG_FILE = "logs/forensic_audit.json"
LIMIT = 4
history = []

class Sentinel(FileSystemEventHandler):
    def save(self, data):
        try:
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(json.dumps(data) + "\n")
        except: pass

    def on_any_event(self, event):
        if not event.is_directory:
            if any(x in event.src_path.lower() for x in [".tmp", ".ini", "desktop.ini"]): return
            
            now = datetime.now()
            history.append(now.timestamp())
            if len(history) > 50: history.pop(0)
            
            # Cálculo de ráfaga
            recent = [t for t in history if now.timestamp() - t < 1.0]
            
            entry = {
                "t": now.strftime("%H:%M:%S"),
                "ev": event.event_type.upper(),
                "file": os.path.basename(event.src_path)
            }

            if len(recent) > LIMIT:
                print(f"[{entry['t']}] 🚨 ALERTA: Rafaga detectada -> {entry['file']}")
            else:
                print(f"[{entry['t']}] [+] {entry['ev']}: {entry['file']}")
            
            self.save(entry)

if __name__ == "__main__":
    os.system('cls')
    print("-" * 50)
    print("             SENTINEL | BY JORGE OTERO")
    print("-" * 50)
    
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
        path, _ = winreg.QueryValueEx(key, "Desktop")
    except:
        path = os.path.join(os.environ['USERPROFILE'], 'Desktop')

    print(f"[*] RUTA: {path}")
    print(f"[*] STATUS: Activo")
    print("-" * 50 + "\n")

    obs = Observer()
    obs.schedule(Sentinel(), path, recursive=False)
    obs.start()
    try:
        while True: time.sleep(0.1)
    except:
        obs.stop()
    obs.join()
