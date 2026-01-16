from playwright.sync_api import sync_playwright
import os
import json

USUARIO = os.getenv("BIGUA_USER")
PASSWORD = os.getenv("BIGUA_PASS")

LOGIN_URL = "https://bigua.uy/com.biguasocios.ingresosocios"
RESERVA_URL = "https://bigua.uy/com.biguasocios.wpclases"
POST_URL = "https://bigua.uy/com.biguasocios.wpclases"

ROW = "0003"   # 👈 tu turno
GRID = 112

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    print("✅ Navegador Inicializado")

    # LOGIN
    page.goto(LOGIN_URL)
    page.wait_for_selector("input[type='text']")
    page.wait_for_selector("input[type='password']")
    page.locator("input[type='text']").first.fill(USUARIO)
    page.locator("input[type='password']").first.fill(PASSWORD)
    page.keyboard.press("Enter")
    page.wait_for_load_state("networkidle")
    print("✅ Login completado")

    # IR A RESERVAS
    page.goto(RESERVA_URL)
    page.wait_for_load_state("networkidle")
    print("📄 Página de reservas cargada")

    # DISPARAR EVENTO GENEXUS DIRECTO
    payload = {
        "MPage": False,
        "cmpCtx": "",
        "events": ["'DORESERVARCLASE'"],
        "grid": GRID,
        "grids": {"Grid": {"id": GRID, "lastRow": 1, "pRow": ""}},
        "hsh": [],
        "objClass": "wpclases",
        "pRow": "",
        "parms": [0, False, "0", True],
        "pkgName": "com.biguasocios",
        "row": ROW
    }

    response = context.request.post(
        POST_URL,
        data=json.dumps(payload),
        headers={"Content-Type": "application/json"}
    )

    print("📡 Status:", response.status)
    print("📨 Body:", response.text()[:300])

    browser.close()
