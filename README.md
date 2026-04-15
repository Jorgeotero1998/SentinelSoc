# Sentinel by Jorge Otero

**Sentinel** es una herramienta de ciberseguridad avanzada diseñada para el monitoreo de integridad y detección de amenazas en tiempo real para entornos Windows.

## 🚀 Funcionalidades
- **Detección Heurística:** Identifica patrones de ataques masivos (Ransomware) analizando la frecuencia de eventos.
- **Auditoría Forense:** Registro persistente en formato JSON estructurado para análisis posterior.
- **Interfaz de Bajo Nivel:** Conexión directa con el kernel de Windows para la vigilancia de archivos.
- **Compatibilidad Inteligente:** Detección automática de rutas críticas mediante el Registro de Windows.

## 🛠️ Instalación
1. Clonar el repositorio: `git clone https://github.com/Jorgeotero1998/SentinelSoc`
2. Instalar dependencias: `pip install watchdog pywin32`
3. Ejecutar: `python src/monitor.py`
