import wikipedia

def search_bot():
    print("🔎 Welcome to Info Search Bot")
    query = input("Enter your search text: ")

    try:
        # Get summary of the search query
        result = wikipedia.summary(query, sentences=5)
        print("\n📘 Search Result:\n")
        print(result)

    except wikipedia.exceptions.DisambiguationError as e:
        print("\n⚠ Multiple results found. Showing some suggestions:")
        print(e.options[:5])

    except wikipedia.exceptions.PageError:
        print("\n❌ No information found for this search.")

    except Exception as e:
        print("\n⚠ Error:", e)

# Run the bot
search_bot()