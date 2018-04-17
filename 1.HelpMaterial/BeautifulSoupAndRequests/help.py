from bs4 import BeautifulSoup
import requests


with open('sample.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


# prints the whole html as string
print(soup.prettify())


# finds first title tag on html
match = soup.title.text
print(match)
# Test - A Sample Website

# finds first div tag
first_div = soup.div
print(first_div)

# finds div with class footer
footer_div = soup.find('div', class_='footer')
print(footer_div)
# <div class="footer">
# <p>Footer Information</p>
# </div>


# find div with class article
article_div = soup.find('div', class_='article')
# find text of href in article_div
headline = article_div.h2.a.text
print(headline)
# Article 1 Headline


for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()

    # Article 1 Headline
    # This is a summary of article 1

    # Article 2 Headline
    # This is a summary of article 2
