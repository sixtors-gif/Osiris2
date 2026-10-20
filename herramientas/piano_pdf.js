// Genera partituras/Cuaderno_de_partituras.pdf (de partituras/cuaderno.html) y Planning_6_meses_piano.pdf (de planificacion.html)
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
  const plan = await browser.newPage();
  await plan.goto('file://' + path.join(dir, 'planificacion.html'));
  await plan.emulateMedia({ media: 'print' });
  await plan.pdf({ path: path.join(dir, 'Planning_6_meses_piano.pdf'), format: 'A4', landscape: true,
    margin: { top: '12mm', bottom: '12mm', left: '10mm', right: '10mm' }, printBackground: true });
  await browser.close();
  console.log('PDF generado (cuaderno y planning)');
})();
