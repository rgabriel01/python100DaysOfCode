import requests
import ipdb

class PokeApiScraper:
    URL = "http://pokeapi.co/api/v2/"

    def scrape(self):
        pokemons = self._process_request(self._type_url('2'))
        if (len(pokemons) > 0):
            print("looping pokemons!")
            for pokemon in pokemons['pokemon']:
                print(pokemon['pokemon']['name'])

        print("Done scraping!")

    def _type_url(self,type_id):
        return self.URL + "type/" + type_id

    def _process_request(self, url):
        response = requests.get(url)
        return '' if response.status_code != 200 else response.json()

PokeApiScraper().scrape()
