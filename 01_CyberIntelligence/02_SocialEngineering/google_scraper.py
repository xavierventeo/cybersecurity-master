# Import the beautifulsoup and request libraries of python.
import requests
import bs4

# Make two strings with default google search URL
# 'https://google.com/search?q=' and
# our customized search keyword.
# Concatenate them
text= "Name Surname1 Surname2"
url = 'https://google.com/search?q=' + text
user_agent={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

response  = requests.get(url, headers = user_agent)

# Creating soup from the fetched request
soup = bs4.BeautifulSoup(response.text, "html.parser")
 
# Find all the search result divs
divs = soup.select("#search div.g")

for div in divs:
    # Search for a h3 tag
    results = div.select("h3")

    # Check if we have found a result
    if (len(results) >= 1):

        # Print the title
        h3 = results[0]
        print(h3.get_text())
        
# soup.find.all( h3 ) to grab 
# all major headings of our search result,
heading_object=soup.find_all( 'h3' )

# Iterate through the object 
# and print it as a string.
for info in heading_object:
    print(info.getText())
    print("------")


# soup.find.all( a ) to grab 
# all links of our search result,
links_object=soup.find_all( 'a' )
for link in links_object:
    print(link.get('href'))
