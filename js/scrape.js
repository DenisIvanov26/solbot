const puppeteer = require('puppeteer');
const cheerio = require('cheerio');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://rugcheck.xyz/tokens/D53gNPqwkqvuME2G5QQVXqmcjzERvfzjrceNxkwMhH2R', {waitUntil: 'networkidle2'}); // Adjust the URL accordingly

  // Get the HTML content of the page
  const html = await page.content();

  // Now you can close the browser
  await browser.close();
  console.log(html)

  // Parse the HTML with Cheerio
  const $ = cheerio.load(html);

  // Example of extracting data: Get the text of a specific element
  const specificElementText = $('selector').text(); // Replace 'selector' with the actual CSS selector
  console.log(specificElementText);

  // You can use Cheerio to extract other data as needed
})();