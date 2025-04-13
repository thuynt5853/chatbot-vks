import requests
import logging
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

logger = logging.getLogger(__name__)


class ActionGetWeather(Action):
    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

      #  city = next(tracker.get_latest_entity_values("location"), None)
        city = "London"

        if not city:
            dispatcher.utter_message(text="Please tell me the location you want the weather for.")
            return []

        weather_data = self.get_weather(city)

        logger.info(f"City: {city}")
        logger.info(f"Weather Data: {weather_data}")

        if weather_data and 'main' in weather_data and 'weather' in weather_data:
            temp = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            response = f"The weather in {city} is {temp}°C with {description}."
        else:
            response = f"Sorry, I couldn't fetch the weather information for {city}."

        dispatcher.utter_message(text=response)
        return []

    @staticmethod
    def get_weather(city: str) -> Dict[Text, Any]:
        api_key = "9524bb51cf5f8675427d00260d806fbb"
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "units": "metric",
            "appid": api_key
        }

        try:
            logger.info(f"Requesting weather data for {city}")
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API Request Error: {e}")
            return None
