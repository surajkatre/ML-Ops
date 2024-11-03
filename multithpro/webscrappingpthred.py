"""Real-World Example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping
Web scraping often involves making numerous network requests to
fetch web pages. These tasks are I/O-bound because they spend a lot of
time waiting for responses from servers. Multithreading can significantly
improve the performance by allowing multiple web pages to be fetched concurrently."""



url = "https://python.langchain.com/v0.2/docs/introduction/"
url2 = "https://python.langchain.com/v0.2/docs/concepts/"



import threading
import requests
import bs4


from bs4 import BeautifulSoup
urls = [
  "https://python.langchain.com/v0.2/docs/concepts/",
   "https://python.langchain.com/v0.2/docs/introduction/"

 ]

def fetchcontent(urls):
    res = requests.get(urls)
    # print(res.content)
    soup = BeautifulSoup(res.content, 'html.parser')
    print(f" length of text is {len(soup.text)}")
    # print(f" length of text is {(soup.text)}")


threads = []
for url in urls:
    thread = threading.Thread(target=fetchcontent, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads completed")