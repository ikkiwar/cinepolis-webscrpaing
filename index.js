const puppeteer = require("puppeteer");

(async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();
  await page.setViewport({ width: 1600, height: 900 });
  await page.goto("https://www.cinepolis.com.sv/");
  await page.click(".btn.btnEnviar.btnVerCartelera");
  await page.goto(
    "https://www.cinepolis.com.sv/cartelera/san-salvador-el-salvador",
    [60000, { waitUntil: "domcontentloaded" }]
  );
  let data = await page.evaluate(() => {
    const url = [...document.querySelectorAll(".btn.btnhorario.ng-scope")].map(
      (info) => info.innerHTML
    );

    return url;
  });
  /*  await page.screenshot({ path: "example.png" });  preloadCartelera*/
  console.log(data);
  await browser.close();
})();
