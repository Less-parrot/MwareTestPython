import requests
import json
import pycountry

class IPinfo:
    def __init__(self, ip):
        self._IP  = ip
        self._API = f"http://ip-api.com/json/{self._IP}?fields=status,city,message,country,countryCode,lat,lon,isp"

    def obtener_emoji_de(self, country_code):
        try:
            return pycountry.countries.get(alpha_2=country_code).flag
        except:
            return False

    def start(self):
        response  = requests.get(self._API)
        json_data = response.json()

        if json_data["status"] == "success":
            json_objeto = json.loads(json.dumps(json_data))

            lat = json_objeto["lat"]
            lon = json_objeto["lon"]

            json_objeto["maps"] = f"{lat},{lon}"
            json_objeto["flag"] = self.obtener_emoji_de(json_objeto['countryCode'])

            for key in ['status', 'lat', 'lon', 'countryCode', 'message']:
                if key in json_objeto:
                    del json_objeto[key]

            return(json.dumps(json_objeto, indent=4, ensure_ascii=False))

        else:
            return(f"fail, message: {json_data['message']}")