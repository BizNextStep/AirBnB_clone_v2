#!/usr/bin/python3


class AirbnbCloneProject:
    def __init__(self, partners: str) -> None:
        """Initialize AirbnbCloneProject object with partners."""
        self.partners = partners

    def get_partners(self) -> str:
        """Return the partners associated with this project."""
        return self.partners

    def set_partners(self, new_partners: str) -> None:
        """Set new partners for this project."""
        self.partners = new_partners
