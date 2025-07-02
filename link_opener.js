const puppeteer = require('puppeteer');
const fs = require('fs');

async function openAllTabsAtOnce(urls) {
  const browser = await puppeteer.launch({
    headless: false,
    defaultViewport: null,
    args: ['--start-maximized']
  });

  const context = browser; // Not using incognito

  // Launch all tabs in parallel
  const openPromises = urls.map(async (url) => {
    try {
      const page = await context.newPage();
      console.log(`Opening: ${url}`);
      await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 10000 });
    } catch (err) {
      console.error(`Failed to open ${url}: ${err.message}`);
    }
  });

  // Wait for all tabs to be initiated
  await Promise.all(openPromises);

  console.log("✅ All tabs launched.");
}

const urls = fs.readFileSync('links.txt', 'utf8')
  .split('\n')
  .map(url => url.trim())
  .filter(url => url.startsWith('http'));

if (!urls.length) {
  console.log("No valid URLs found in links.txt");
  process.exit(1);
}

openAllTabsAtOnce(urls).catch(console.error);
