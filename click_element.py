from playwright.async_api import async_playwright
import asyncio


async def click_links(url, browser, click_target):
    async with async_playwright() as ap:

        browser_instance = await ap[browser].launch()
        page = await browser_instance.new_page()
        await page.goto(url)

        try:
            links = await page.query_selector_all(click_target)
            if links:
                for link in links:
                    new_urls = []
                    print(f"The number of links is: {range(len(links))}")
                    await links.click()
                    new_url = await page.waitForURL('**/**')
                    new_urls.append(new_urls)
                    print(f"Clicked on links with selector: {click_target}. Navigated to {new_url}")
                    print(new_urls)
                else:
                    print(f"Links with selector {click_target} not found")
        except Exception as e:
            print(f"Error clicking links: {e}")
    

if __name__ == "__main__":
    url = 'https://www.healthyplanetcanada.com/catalogsearch/result/?q=vegan+probiotics&rows=160&page=1'
    browser = 'firefox'    
    click_target = 'strong.product.name.product-item-name a.product-item-link'

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(click_links(url, browser, click_target))
    finally:
        loop.close()
    