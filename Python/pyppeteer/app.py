import asyncio
from pyppeteer import launch

async def main():
    # launch chromium browser in the background
    browser = await launch()
    # open a new tab in the browser
    page = await browser.newPage()
    # add URL to a new page and then open it
    url1 = "https://www.python.org/"
    url2 = "https://vnexpress.net/ly-do-5-huyen-tp-hcm-muon-len-thanh-pho-4471954.html"
    await page.goto(url2)
    # Get a page's textContent
    # content = await page.evaluate('document.body.textContent', force_expr=True)
    # print(content)
    # Get an element's textContent
    element = await page.querySelector('h')
    print(element)
    title = await page.evaluate('(element) => element.textContent', element)
    # title = await page.xpath('/html/body/section[2]/section/div/div[2]/div/div[1]/div/div/ul[1]/li[2]/a')
    print(title)
    # create a screenshot of the page and save it
    # await page.screenshot({"path": "python.png"})
    # close the browser
    await browser.close()

print("Starting...")
asyncio.get_event_loop().run_until_complete(main())
# print("Screenshot has been taken")