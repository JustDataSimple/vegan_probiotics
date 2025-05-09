from playwright.async_api import async_playwright
import asyncio


async def click_links(url, browser, link_element, click_target):
    async with async_playwright() as ap:

        try:
            
            browser_instance = await ap[browser].launch()
            page = await browser_instance.new_page()
            response = await page.goto(url)
            print(f"Response status: {response.status if response else 'No response'}")
            
            if response == 200:
                link_elements = await page.query_selector_all(link_element)
                print(f"Number of elements found: {len(link_elements)}")
                    for element in link_elements:
                        link_target = await page.query_selector(click_target)
                        print(f'found link at: {click_target}')
                    break

            
            else:
                print(f'Could not obtain link using: {link_elements}')

            for element in link_element:

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
    link_element = 'li.product'
    click_target = 'li.product > div > a'

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(click_links(url, browser, click_target))
    finally:
        loop.close()
    