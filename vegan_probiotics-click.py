from playwright.async_api import async_playwright
import asyncio
import pandas as pd

async def scrape_data(url,browser, click_target, click_selector_target):
    async with async_playwright() as ap:

        browser_instance = await ap[browser].launch()
        page = await browser_instance.new_page()
        await page.goto(url)

        print(f"Loaded URL: {url}")
        
        try:
            element = await page.query_selector_all(click_target)
            print(f"{len(elements)} elements contained: {click_target}")
            
            el = 0
            all_elements = []

            While len(elements) > el:
                if element:
                    await element.click()
                    print(f"Clicked on element with selector: {click_target}")
                else:
                    print(f"Element with selector {click_target} not found")
            except Exception as e:
                print(f"Error clicking element: {e}")

                #await page.wait_for_load_state('networkidle')

                #click_selector_result = await page.query_selector_all(click_selector_target)
                all_elements.append(click_selector_result)
                el =+ 1

            for r in all_elements:
            click_selector_text = print(await r.text_content())
        
        await browser_instance.close()
        return click_selector_text

if __name__ == "__main__":
    url = 'https://www.healthyplanetcanada.com/catalogsearch/result/?q=vegan+probiotics&rows=160&page=1'
    browser = 'firefox'    
    click_target = 'li.item.product.product-item.item-product'
    click_selector_target = 'div.product.info.main'

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(scrape_data(url, browser, click_target, click_selector_target))
    finally:
        loop.close()