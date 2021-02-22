const puppeteer = require("puppeteer");

(async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();
  await page.goto("https://www.cinepolis.com.sv/");
  await page.click(".btn.btnEnviar.btnVerCartelera");
  await page.screenshot({ path: "example.png" });

  await browser.close();
})();
