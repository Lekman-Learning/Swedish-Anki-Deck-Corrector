@echo off
echo === Anki-Svenska Setup ===
echo.

echo [1/3] Installerar Python-paket...
pip install -r requirements.txt
if errorlevel 1 goto error

echo.
echo [2/3] Installerar Playwright Chromium-webbläsare...
playwright install chromium
if errorlevel 1 goto error

echo.
echo [3/3] Klart!
echo.
echo Nästa steg:
echo   1. Öppna Anki
echo   2. Installera AnkiConnect: Verktyg → Tillägg → Hämta tillägg → kod: 2055492159
echo   3. Starta om Anki
echo   4. Kör: python main.py --list-decks
echo.
goto end

:error
echo.
echo FEL: Något gick fel. Kontrollera att Python är installerat och i PATH.
exit /b 1

:end
pause
