import requests

# Define your API key
key = "your api key"

# Construct the API address
api_address = f"https://newsapi.org/v2/everything?q=Apple&sortBy=popularity&apiKey={key}"

# Fetch JSON data from the API
response = requests.get(api_address)
json_data = response.json()

# Print the entire JSON response for debugging (optional)
print(json_data)

# Initialize an array to store news headlines
ar = []

def news():
    """Fetch the top 3 news articles and format them."""
    # Check if articles exist in the response
    if "articles" in json_data and len(json_data["articles"]) > 0:
        count = 0  # Counter for valid articles
        for i in range(len(json_data["articles"])):  # Loop through all articles
            title = json_data["articles"][i]["title"]  # Access the title correctly
            
            # Check if the title is not marked as removed or empty
            if title and "[Removed]" not in title:
                ar.append(f"Article {count + 1}: {title}.")  # Format the output with article number
                count += 1
            
            # Stop after collecting 3 valid articles
            if count >= 3:
                break
        
        if count == 0:  # If no valid articles were found
            ar.append("No valid articles found.")
    else:
        ar.append("No articles found.")
    return ar

# Call the news function and store the results
arr = news()

# Print the formatted news articles with titles and numbers
print("Search results:")
if arr:
    for article in arr:
        print(article)
else:
    print("No articles found.")

# Additional Information for Search Results
print("Attached URL:", api_address)
print("File name:", api_address.split("?")[1])  # Extracting query parameters for file name
