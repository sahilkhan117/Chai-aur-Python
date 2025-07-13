import requests

def fetch_random_username_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]

        username = user_data['login']['username']
        country = user_data['location']['country']
        return username, country
    
    else:
        raise Exception("Faild to fetch user data")


def main():
    try:
        username, country = fetch_random_username_freeapi()
        print(f"username: {username}\nCountry: {country}\n")

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()