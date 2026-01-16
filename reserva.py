from playwright.sync_api import sync_playwright
import os
import time

USUARIO = os.getenv("BIGUA_USER")
PASSWORD = os.getenv("BIGUA_PASS")

LOGIN_URL = "https://bigua.uy/com.biguasocios.ingresosocios"
RESERVA_URL = "https://bigua.uy/com.biguasocios.wpclases"

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
    print("📄 Página de reservas cargada")

    # ESPERAR QUE APAREZCA ALGÚN BOTÓN DE RESERVA
    page.wait_for_selector("text=Reservar", timeout=20000)

    botones = page.locator("text=Reservar")
    count = botones.count()
    print(f"🎯 Botones encontrados: {count}")

    if count == 0:
        raise Exception("❌ No se encontró ningún botón de reserva")

    # Click al primer botón disponible
    botones.first.click()
    page.wait_for_timeout(2000)

    print("🎾 Reserva enviada")
    browser.close()
