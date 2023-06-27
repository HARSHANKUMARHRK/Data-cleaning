import feedparser
import tkinter as tk

def get_news():
    url = "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"

    # Parse the RSS feed
    feed = feedparser.parse(url)

    # Extract the news articles
    articles = feed.entries

    # Return the news articles
    return articles

def display_news_app():
    root = tk.Tk()
    root.title("News Application")

    # Create a text box to display the news articles
    news_text = tk.Text(root, height=30, width=80)
    news_text.pack()

    # Call the get_news function and insert the articles into the text box
    articles = get_news()
    if articles:
        for article in articles:
            news_text.insert(tk.END, f"Title: {article['title']}\n\n")
            news_text.insert(tk.END, f"Summary: {article['summary']}\n\n")
            news_text.insert(tk.END, f"Link: {article['link']}\n\n")
            news_text.insert(tk.END, "-" * 50 + "\n\n")
    else:
        news_text.insert(tk.END, "No articles found.")

    root.mainloop()

if __name__ == "__main__":
    display_news_app()
