from bs4 import BeautifulSoup
import requests

def scrape_timesjobs(query) :
    titles_timesjobs = []
    links_timesjobs = []

    html_text = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={query}&txtLocation=').text
    soup = BeautifulSoup(html_text , 'lxml')
    jobs_timesjobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for job in jobs_timesjobs :
        titles_timesjobs.append(job.a.text.replace('\n',''))
        links_timesjobs.append(job.a['href'])
    items_timesjobs = list(zip(titles_timesjobs, links_timesjobs))
    return items_timesjobs


# # Example usage

# results = scrape_timesjobs("computer+science")    
# for title, link in results:
#     print(f"Title: {title}, Link: {link}")
#     print(len(results))