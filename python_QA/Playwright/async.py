import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(haadless=False)
        page = await browser.new_page()
        await page.goto("https://www.businesspromanagement.co.za/")
        print(await page.title())
        browser.close()

asyncio.run(main())