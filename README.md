# SentinelSoc 🛡️
> Lightweight Windows EDR Engine for Behavioral Threat Detection & Forensic Telemetry Logging.

Sentinel is an Endpoint Detection and Response (EDR) engine focused on early behavior-based threat detection and real-time file integrity monitoring within Windows environments, designed for SOC analysts and SecOps teams.

---

## 🚀 Architecture & Technical Capabilities

The core system combines low-level Windows API access with local heuristic analysis to process events efficiently without compromising system performance.

*   **Heuristic Ransomware Detection:** An algorithm that analyzes the frequency rate of Input/Output (I/O) events. If massive modifications are detected within a critical time threshold, it mitigates the impact and identifies the attack pattern.
*   **Low-Level Kernel Interface:** Direct connection via Windows API calls for file system event capture, ensuring real-time telemetry.
*   **Intelligent Path Discovery:** Automatic inspection of the Windows Registry to dynamically map critical operating system paths and monitor sensitive user directories.
*   **Structured Forensic Auditing:** Generation of persistent logs in structured JSON format, ready for direct ingestion into SIEM solutions (Splunk, Elastic, Azure Sentinel).

---

## 📁 Project Structure

```text
SentinelSoc/
├── src/
│   ├── monitor.py       # Core EDR engine and event capture loop
│   ├── notifier.py      # Alerting module, telemetry dispatch, and response logic
│   └── utils.py         # Windows API abstractions and Registry queries
├── logs/                # Local storage for forensic audit logs (JSON)
├── Iniciar_Sentinel.bat # Automated quick-deployment script
└── requirements.txt     # Environment execution dependencies


## Screenshots
<img width="1270" height="682" alt="Captura de pantalla 2026-04-15 174835" src="https://github.com/user-attachments/assets/6194977e-791d-4277-8c7f-af80863d55d7" />
<img width="1273" height="680" alt="Captura de pantalla 2026-04-15 174902" src="https://github.com/user-attachments/assets/39a7d664-5756-4093-a138-dc504c2a5482" />
<img width="1257" height="612" alt="Captura de pantalla 2026-04-15 174928" src="https://github.com/user-attachments/assets/f3159ee6-5699-4090-b791-55b0e452886a" />


🛠️ Installation
Clone the repository: `git clone https://github.com/Jorgeotero1998/SentinelSoc`
Installation dependencies: `pip install watchdog pywin32`
Run: `python src/monitor.py`
