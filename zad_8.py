import argparse
import requests


class Browar:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.brewery_type = kwargs.get('brewery_type')
        self.street = kwargs.get('street')
        self.city = kwargs.get('city')
        self.state = kwargs.get('state')
        self.postal_code = kwargs.get('postal_code')
        self.country = kwargs.get('country')
        self.longitude = kwargs.get('longitude')
        self.latitude = kwargs.get('latitude')
        self.phone = kwargs.get('phone')
        self.website_url = kwargs.get('website_url')
        self.updated_at = kwargs.get('updated_at')
        self.tag_list = kwargs.get('tag_list')

    def __str__(self):
        return f"Browar {self.name} z miasta {self.city}"


def pobierz_browary(city=None):
    url = "https://api.openbrewerydb.org/breweries"
    if city is not None:
        url += f"?by_city={city}"

    response = requests.get(url)
    browary_dane = response.json()

    browary = [Browar(**dane) for dane in browary_dane]
    return browary


def main(city):
    browary = pobierz_browary(city)

    for browar in browary:
        print(browar)


parser = argparse.ArgumentParser()
parser.add_argument("--city", help="Berlin")
args = parser.parse_args()
