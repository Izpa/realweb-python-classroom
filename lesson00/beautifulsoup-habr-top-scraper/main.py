from bs4 import BeautifulSoup
import requests

url = 'https://habr.com/top/'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')

articles = soup.find(
    'ul', attrs={'class': 'content-list content-list_posts shortcuts_items'})

articles_data = list()
for article in articles.findAll('li', attrs={'class': 'content-list__item content-list__item_post shortcuts_item'}):
    article_data = dict()
    article_data['id'] = article.attrs.get('id')
    if article_data['id']:
        article_body = article.find('article')

        article_header = article.find('header')
        article_data['author_link'] = article_header.find('a').attrs['href']
        article_data['creation_time'] = article_header.find('span', attrs={'class': 'post__time'}).text

        article_footer = article.find('footer').find('ul')
        article_data['votings'] = int(article_footer.find('li', attrs={'class': 'post-stats__item post-stats__item_voting-wjt'}).text.strip())
        article_data['bookmarks'] = int(article_footer.find('li', attrs={'class': 'post-stats__item post-stats__item_bookmark'}).text.strip())
        article_data['views'] = article_footer.find('li', attrs={'class': 'post-stats__item post-stats__item_views'}).text.strip()
        article_data['comments'] = int(article_footer.find('li', attrs={'class': 'post-stats__item post-stats__item_comments'}).text.strip())

        articles_data.append(article_data)

print(articles_data)
