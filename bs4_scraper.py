1. Install Beautiful Soup: `pip install beautifulsoup4`

2. Import necessary libraries:
```python
import requests
from bs4 import BeautifulSoup
```

3. Use the `requests` library to get the HTML content of the website you want to scrape:
```python
response = requests.get("http://www.example.com")
```

4. Parse the HTML content using Beautiful Soup:
```python
soup = BeautifulSoup(response.content, 'html.parser')
```

5. Find the element(s) you want to scrape using one of Beautiful Soup's searching methods, such as `find_all`, `find`, `select`, etc.:
```python
elements = soup.find_all('div', class_='example')
```

6. Extract the text or attribute you want from the element:
```python
for element in elements:
    text = element.text
    attribute = element['href']
```
