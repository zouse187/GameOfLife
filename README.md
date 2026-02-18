# 🧬 Game of Life – Python Implementation mit interaktivem UI

Dieses Projekt ist eine vollständig interaktive Umsetzung von **Conway’s Game of Life** in Python.  
Es kombiniert eine performante Simulation mit einer modular aufgebauten Benutzeroberfläche, die es ermöglicht, Parameter live oder nach einem Reset anzupassen.

---

## 🚀 Features

### 🟩 Simulation
- Klassische Regeln des Game of Life  
- Performante Grid‑Berechnung  
- Pause/Resume‑Funktion  
- Reset der Simulation mit neuen Parametern  
- Zufällige Startpopulation basierend auf Spawn‑Rate

### 🎛️ Interaktive UI
- **Slider** für:
  - Zellgröße (wirkt nach Reset)
  - Spawn‑Rate (wirkt nach Reset)
  - Simulationsgeschwindigkeit (wirkt sofort)
  - Zellfarbe (wirkt sofort)
- **Buttons** für:
  - Reset
  - Spiel schließen
  - Spiel nicht schließen
- Hover‑ und Click‑Effekte für Buttons

### 🧩 Architektur
- Modularer Aufbau:
  - Eigene Klassen für Buttons und Slider
  - Saubere Trennung von UI‑Logik und Simulationslogik
  - Wiederverwendbare Komponenten für zukünftige Projekte

---

## 📦 Installation

### Voraussetzungen
- Python 3.10+
- `pygame`

Installation der Abhängigkeiten:

```bash
pip install pygame
```

---

## ▶️ Starten der Anwendung

```bash
python main.py
```

---

## ⚙️ Bedienung

| Aktion | Beschreibung |
|----------|----------|
| Leertaste   | Simulation starten/pausieren   |
| Rechte Pfeiltaste   | Zur nächsten Generation springen (wenn pausiert ist)  |
| R   | Simulation zurücksetzen   |
| E   | Settings‑Overlay öffnen   |
| ESC   | Spiel schließen (mit Bestätigung)  |

---

## 📄 Lizenz

MIT License – frei nutzbar für eigene Projekte.