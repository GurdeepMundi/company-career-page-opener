import webbrowser

def searchjobs(website):
    # Construct the search URL
    search_url = f"{website}"

    # Open the search URL in a new tab
    webbrowser.open_new_tab(search_url)

# Open each career website in a new tab
with open('career_websites_list.txt') as websites:
    for website in websites:
        searchjobs(website.rstrip('\n'))