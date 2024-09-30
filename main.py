import requests
from bs4 import BeautifulSoup


def save(filename, text):
    with open(filename, "w", encoding='utf-8') as f:
        f.write(text)


def fetch( url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get(url, headers=headers)
    return r.text

def extract_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for link in soup.find_all("a"):
        linkhref = link.get('href')
        if linkhref is not None:
            if "/dp/" in linkhref:
                links.append(link.get('href'))
    return links


if __name__ == '__main__':
    query = 'iphone'
    url = f'https://www.amazon.in/s?k={query}'
    text = fetch(url)
    save('index.html', text)
    links = extract_links(text)
    print(links)

    for link in links:
        print(link)
        content = fetch(f'https://amazon.in{link}')
        save('product.html', content)
