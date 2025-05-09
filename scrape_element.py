from playwright.async_api import async_playwright
import asyncio

async def scrape_elements(page, target):
    results = await page.query_selector_all(target)
    for r in results:
        text = await r.text_content()
        print(f"Element text: {text}")
    return results