from playwright.async_api import async_playwright
import asyncio

async def load_page(url, browser):
    async with async_playwright() as ap:

        # Launch the specified browser
        browser_instance = await ap[browser].launch()
        page = await browser_instance.new_page()
        website = await page.goto(url)

        # Print the URL to verify the page is loaded
        print(f"Loaded URL: {website}")

        return page, website