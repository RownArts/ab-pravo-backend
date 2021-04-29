# from bs4 import BeautifulSoup
from urllib.parse import urljoin

FRONTEND_URL = 'https://telos-ci.weew.ru/'


def build_absolute_img_url(self, html_content):
    if html_content == None:
        return None
    else:
        request = self.context.get('request')
        host = 'https://' + request.get_host()

        # Replace SRC for images
        new = html_content.replace('src="/media/', 'src="'+host+'/media/')
        new = new.replace('src="/files/', 'src="'+host+'/media/files/')

        # Replace HREF for Links
        new = new.replace('href="/media/', 'href="'+host+'/media/')
        new = new.replace('href="/files/', 'href="'+host+'/media/files/')
        return new
    # return html_content

# #  # IT IS slower then uppper functon
# def build_absolute_img_url_with_soup(self, html_content):
#     if html_content == None:
#         return None
#     else:
#         request = self.context.get('request')
#         host = 'https://' + request.get_host()
#         soup = BeautifulSoup(str(html_content), 'html.parser')

#         # Replace SRC for images
#         for im in soup.find_all('img'):
#             im['src'] = urljoin(host, im['src'])

#         # # Replace HREF for Links
#         for l in soup.find_all('a'):
#             l['href'] = urljoin(host, l.get('href'))

#         return str(soup)


def build_frontend_url(self, slug, prefix=None):
    if slug == None:
        return None
    else:
        if prefix != None:
            link = FRONTEND_URL + prefix+'/' + slug
        else:
            link = FRONTEND_URL + slug
        return link


def unwrap_html(html):
    soup = BeautifulSoup(str(html), 'html.parser')
    divs = soup.find_all('div', recursive=False)
    # printy(str(len(divs)), 'yBU')
    if divs != None and len(divs) == 1:
        divs[0].unwrap()
        instanse_html = soup.prettify()
        return (soup.prettify())
    else:
        return(html)


def format_search_results(itemsArr, prefix='/services/'):
    result = []

    for items in itemsArr:
        for item in items:
            result.append(
                {
                    'link': prefix + item.slug,
                    'title': item.title,
                    'summary': item.description
                })

    return (result)
