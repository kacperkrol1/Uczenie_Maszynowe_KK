import requests


class Brewery:
    def __init__(self, name: str, brewery_type: str, city: str, state: str, phone: str, website_url: str):
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.state = state
        self.phone = phone
        self.website_url = website_url

    def __str__(self):
        return f"Nazwa: {self.name}\n Typ: {self.brewery_type}\n Miasto: {self.city}\n Stan: {self.state}\n Telefon: {self.phone}\n Strona internetowa: {self.website_url}\n"


def main():
    api_url = "https://api.openbrewerydb.org/breweries"
    params = {'per_page': 20}
    response = requests.get(api_url, params=params)
    breweries = response.json()

    brewery_objects = []
    for brewery in breweries:
        brewery_objects.append(
            Brewery(brewery['name'], brewery['brewery_type'], brewery['city'], brewery['state'], brewery['phone'],
                    brewery['website_url']))

    for brewery in brewery_objects:
        print(brewery)


if __name__ == '__main__':
    main()
