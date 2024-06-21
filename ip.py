import urllib.request

# Define the URL to fetch data from
url = 'https://ipv4.icanhazip.com'

# Open the URL and fetch the response
with urllib.request.urlopen(url) as response:
    # Read the response content
    html = response.read()

# Decode the response content to a string
html_content = html.decode('utf-8')

# Print the fetched content
print(html_content)

