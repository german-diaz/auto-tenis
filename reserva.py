from playwright.sync_api import sync_playwright
import os

USUARIO = os.getenv("BIGUA_USER")
PASSWORD = os.getenv("BIGUA_PASS")

LOGIN_URL = "https://bigua.uy/com.biguasocios.ingresosocios"
RESERVA_URL = "https://bigua.uy/com.biguasocios.wpclases"
SELECTOR_TURNO = "#BTNRESERVARCLASE_0003"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
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

    # CLICK TURNO
    page.wait_for_selector(SELECTOR_TURNO, timeout=10000)
    page.click(SELECTOR_TURNO)
    page.wait_for_timeout(2000)

    print("🎾 Reserva enviada")
    browser.close()