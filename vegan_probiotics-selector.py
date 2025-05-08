from playwright.async_api import async_playwright
import asyncio
import pandas as pd

async def scrape_data(url,browser,target):
    async with async_playwright() as ap:

        browser_instance = await ap[browser].launch()
        page = await browser_instance.new_page()
        await page.goto(url)

        # Print the URL to verify the page is loaded
        print(f"Loaded URL: {url}")
        
        # Query all elements matching the target selector
        targets = await page.query_selector_all(target)
        
        # Print the number of elements found
        print(f"Found {len(targets)} elements matching the selector '{target}'")

        for t in targets:
            text = print(await t.text_content())
        await browser_instance.close()
        return text

if __name__ == "__main__":
    url = 'https://playwright.dev/'
    browser = 'firefox'    
    target = 'script'

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(scrape_data(url, browser, target))
    finally:
        loop.close()