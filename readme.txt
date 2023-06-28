# IMDb Top Rated Movies Scraper

This Python script scrapes the IMDb Top Rated Movies list and filters the movies based on a user-defined rating threshold. It retrieves the movie titles and their corresponding ratings from the IMDb website and displays the movies that have a rating higher than the specified threshold.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- requests
- BeautifulSoup

You can install these dependencies using the following command:

```shell
pip install requests beautifulsoup4
```

## Usage

1. Import the necessary libraries:
   ```python
   import requests
   from bs4 import BeautifulSoup
   ```

2. Define the IMDb Top Rated Movies URL:
   ```python
   url = "https://www.imdb.com/chart/top/"
   ```

3. Send a GET request to the URL and retrieve the HTML content:
   ```python
   response = requests.get(url)
   html_content = response.content
   ```

4. Create a BeautifulSoup object to parse the HTML content:
   ```python
   soup = BeautifulSoup(html_content, "html.parser")
   ```

5. Prompt the user to enter a rating threshold:
   ```python
   user = float(input("Which rating movie would you like to reach?: "))
   ```

6. Find the movie titles and ratings in the HTML using appropriate selectors:
   ```python
   headers = soup.find_all("td", {"class": "titleColumn"})
   ratings = soup.find_all("td", {"class": "ratingColumn imdbRating"})
   ```

7. Iterate over the headers and ratings simultaneously and filter the movies based on the rating threshold:
   ```python
   for header, rating in zip(headers, ratings):
       header = header.text.strip().replace("\n", "")
       rating = rating.text.strip().replace("\n", "")
       
       if float(rating) > user:
           print("Movie name: {} Rating: {}".format(header, rating))
   ```

Make sure to enter a valid rating threshold when prompted.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgments

This script utilizes the requests and BeautifulSoup libraries for web scraping. Thanks to the developers of these libraries for their contributions to the field.




I wrote the code to download imdb 250 data from internet using Python and BeautifulSoup.
After downloading these movies, we can shoot movies above the desired rating with the inputs received from the user.



Step 1: Install Python
step 2: install from cmd command
                pip install requests
                pip install beatifulsoup4





You can use it for educational purposes as much as you want.

shorturl.at/buwF4
