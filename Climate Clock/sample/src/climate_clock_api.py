import json
import requests

def climateclock():
    climate_clock_api_endpoint = "https://api.climateclock.world/v1/clock"
    climate_clock_data = requests.get(climate_clock_api_endpoint)
    climate_clock_text_data = climate_clock_data.text
    climate_clock_json_data = json.loads(climate_clock_text_data)
    nh2 = climate_clock_json_data["data"]["modules"]["newsfeed_1"]["newsfeed"][3]["headline"]
    r1 = climate_clock_json_data["data"]["modules"]["renewables_1"]
    nh1 = climate_clock_json_data["data"]["modules"]["newsfeed_1"]["newsfeed"][0]["headline"]
    cd1 = climate_clock_json_data["data"]["modules"]["carbon_deadline_1"]
    return [cd1,r1,nh1,nh2]