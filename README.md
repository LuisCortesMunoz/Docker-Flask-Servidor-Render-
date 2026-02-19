# Docker-Flask-Servidor-Render-
# LED Control: GitHub Pages -> Render Flask -> ESP32 WS2812

## Flujo
1) Frontend (GitHub Pages) manda ON/OFF + color (hex) a Render (Flask).
2) Flask guarda el "estado deseado".
3) ESP32 hace polling a /api/state y aplica el color/estado en WS2812.

## Endpoints
- GET  /api/state
- POST /api/set   body: {"on": true, "hex":"#00ff88", "brightness":120}
- POST /api/off

## Seguridad (opcional)
Configura API_KEY en Render y usa:
- /api/state?key=TUKEY
- /api/set?key=TUKEY
