import requests

def get_random_quotes():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        quote = user_data["content"]
        author = user_data["authorSlug"]
        return quote , author
    else:
        raise Exception ("failed to fetch the data")

def main():
    try:
        quote,author = get_random_quotes()
        print(quote)
        print(f"By {author.upper()}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()