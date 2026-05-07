# 🎓 Dave's Coding-Stil für Schulungsabgaben

## Grundprinzip
**Locker, verständlich, authentisch** - nicht übertrieben formal!

---

## ✅ Kommentar-Stil

### Abkürzungen (erlaubt!)
- `f.` = für
- `m.` = mit
- `u.` = und
- `d.` = der/die/das
- `z.B.` = zum Beispiel
- `v.` = von
- `bzw.` = beziehungsweise

### Beispiele
```python
# Importe f. bessere Lesbarkeit
from fastapi import FastAPI

# Pydantic-Datenmodell f. Services
class Service(BaseModel):

# Abruf aller Services
@app.get("/services", ...)

# Check d. API-Funktionalität
@app.get("/health", ...)
```

### Sprache
- ✅ "zu checkenden Services" (locker)
- ✅ "Fake-Datenbank" (ehrlich & verständlich)
- ✅ "Abruf aller Services" (praktisch)
- ❌ "zu überwachenden Services" (zu förmlich)
- ❌ "im Speicher gespeichert" (zu technisch)

### Docstrings
- Kompakt aber vollständig
- Deutsche Begriffe bevorzugen
- Persönlicher Ton okay ("meiner API")

---

## ❌ Verbotene Elemente

### Kein CAPSLOCK
```python
# ❌ FALSCH
# IMPORTS
# HILFSFUNKTIONEN
# GET: ALLE SERVICES

# ✅ RICHTIG
# Imports
# Hilfsfunktionen
# Get: Alle Services
```

### Keine === Trennlinien
```python
# ❌ FALSCH
# ===== IMPORTS =====
# ===== DATENSPEICHER =====

# ✅ RICHTIG
# Imports
# oder einfach weglassen wenn klar
```

### Einfache Trennlinien erlaubt
```python
# ✅ OKAY (wenn überhaupt nötig)
# ---
# Oder einfach Leerzeilen
```

### Keine Emojis
# ❌ FALSCH
# 📝, ✅, ❌ etc. in er README okay, im Code aber nicht

---

## 📝 Wann dieser Stil?

### ✅ Verwenden bei:
- Schulungsabgaben
- Lern-Projekten
- Internen Skripten
- Übungen & Assignments

### ❌ NICHT verwenden bei:
- GitHub-Repos (dort professioneller!)
- Produktions-Code
- Team-Projekten
- Öffentlichen Libraries

---

## 💡 Wichtigste Regeln

1. **Verständlichkeit > Formalität**
   - Lieber "checken" als "überprüfen"
   - Lieber "Liste" als "Datenstruktur"

2. **Authentizität > Perfektion**
   - "Fake-DB" statt "temporärer Datenspeicher"
   - "zu checkenden" statt "zu validierenden"

3. **Praktisch > Akademisch**
   - Kurze, klare Kommentare
   - Keine wissenschaftliche Sprache
   - Alltagssprache bevorzugen

4. **Kein Overkill**
   - Keine übertriebenen Trennlinien
   - Kein CAPSLOCK-Geschrei
   - Leerzeilen reichen oft

---

## 🎯 Quick-Check

**Vor dem Abgeben fragen:**
1. Würde ich das so zu einem Kumpel sagen? ✅
2. Klingt es natürlich? ✅
3. Ist es trotzdem präzise? ✅
4. Habe ich CAPSLOCK/=== vermieden? ✅

---

**Zuletzt aktualisiert:** November 2025  
**Version:** 2.0  
**Für:** Schulungsabgaben IHK Cloud IT Administrator
