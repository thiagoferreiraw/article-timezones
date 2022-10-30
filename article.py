from dataclasses import dataclass
from datetime import timedelta, datetime, tzinfo
from pytz import UTC, timezone


@dataclass
class City:    
    name: str
    timezone: tzinfo

@dataclass
class Flight:
    origin: City
    destination: City
    flight_duration: timedelta
    departure_time: datetime

    @property
    def arrival_time(self) -> datetime:
        return self.departure_time + self.flight_duration
    
    @property
    def arrival_time_in_destination(self):
        return self.arrival_time.astimezone(self.destination.timezone)
    
    @property
    def arrival_time_in_origin(self):
        return self.arrival_time.astimezone(self.origin.timezone)
    
    @property
    def arrival_time_in_utc(self):
        return self.arrival_time.astimezone(UTC)

    def __str__(self) -> str:
        return (
            f"✈️  Flying from {self.origin.name} -> {self.destination.name}\n"
            f"- ⏱  Duration: {self.flight_duration}\n"
            f"- 🛫 Departure time: {self.departure_time}\n"
            f"- 🛬 Arrival time (in destination): {self.arrival_time_in_destination}\n"
            f"- 🛬 Arrival time (in origin): {self.arrival_time_in_origin}\n"
            f"- 🛬 Arrival time (in UTC): {self.arrival_time_in_utc}\n"
        )


if __name__ == "__main__":
    sao_paulo = City("São Paulo", timezone("America/Sao_Paulo"))
    manaus = City("Manaus", timezone("America/Manaus"))
    flight = Flight(
      origin=sao_paulo, 
      destination=manaus, 
      flight_duration=timedelta(hours=4, minutes=15),
      # https://groups.google.com/g/django-users/c/rXalwEztfr0/m/QAd5bIJubwAJ
      # Use sao_paulo.timezone.localize(datetime(2022, 10, 1, 16, 15))
      # instead of datetime(2022, 10, 1, 16, 15,tzinfo=sao_paulo.timezone)
      departure_time=sao_paulo.timezone.localize(datetime(2022, 10, 1, 16, 15))
    )
    print(flight)