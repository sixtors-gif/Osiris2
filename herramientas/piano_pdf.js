// Genera partituras/Cuaderno_de_partituras.pdf a partir de partituras/cuaderno.html
// Uso: node herramientas/piano_pdf.js cursos/Curso_Piano_Intermedio_Avanzado_SCORM
// Requiere Playwright (npm i playwright) y Chromium.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const dir = path.resolve(process.argv[2]);
  const exe = process.env.CHROMIUM || '/opt/pw-browsers/chromium';
  const browser = await chromium.launch(require('fs').existsSync(exe) ? { executablePath: exe } : {});
  const page = await browser.newPage();
  await page.goto('file://' + path.join(dir, 'partituras', 'cuaderno.html'));
  await page.waitForFunction(() => window.LISTO === true);
  await page.pdf({ path: path.join(dir, 'partituras', 'Cuaderno_de_partituras.pdf'), format: 'A4',
    margin: { top: '15mm', bottom: '15mm', left: '12mm', right: '12mm' }, printBackground: true });
  await browser.close();
  console.log('PDF generado');
})();
