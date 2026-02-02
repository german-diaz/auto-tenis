from playwright.sync_api import sync_playwright
import os

USUARIO = "47727916"
PASSWORD = "123456"

LOGIN_URL = "https://bigua.uy/com.biguasocios.ingresosocios"
RESERVA_URL = "https://bigua.uy/com.biguasocios.wpclases"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=100)
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



    # Click en la clase específica
    page.click("BTNRESERVARCLASE_0001")      # Ajustar al botón real
    print()
    page.wait_for_timeout(2000)  # espera 2s a que se procese
    print("🎾 Reserva enviada")

    browser.close()

if __name__ == "__main__":
    main()
