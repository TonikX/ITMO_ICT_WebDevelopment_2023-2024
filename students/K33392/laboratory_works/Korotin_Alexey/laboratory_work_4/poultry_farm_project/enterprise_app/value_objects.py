from dataclasses import dataclass
from .exceptions import LocationException

from math import pi, atan2, cos, sin, sqrt


@dataclass(frozen=True)
class Location:
    """
        Value object that encapsulates location in geographic coordinate system
    """

    longitude: float

    latitude: float

    @property
    def longitude_rad(self) -> float:
        """ Radian value of longitude """
        return self.longitude * pi / 180

    @property
    def latitude_rad(self) -> float:
        """ Radian latitude value """
        return self.longitude * pi / 180

    def __post_init__(self):
        if not -180 < self.longitude < 180:
            raise LocationException("Longitude value should be in range [-180, 180]")

        if not -90 < self.latitude < 90:
            raise LocationException("Latitude value should be in range [-90, 90]")

    def distance_to(self, other: "Location") -> float:
        """ Calculates distance between two locations in meters, using Haversine formula """

        r = 6_371_000  # Earth radius in meters

        # Haversine formula implementation
        phi_1 = self.latitude_rad
        phi_2 = other.latitude_rad

        delta_phi = (other.latitude - self.latitude) * pi / 180
        delta_lambda = (other.longitude - self.latitude) * pi / 180

        a = sin(delta_phi / 2) ** 2 + cos(phi_1) * cos(phi_2) * sin(delta_lambda / 2) ** 2

        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        return r * c

    def __str__(self):
        return f"(longitude: {self.longitude}, latitude: {self.latitude})"
