#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2017
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
"""This module contains the classes that represent Telegram
InputVenueMessageContent"""

from telegram import InputMessageContent


class InputVenueMessageContent(InputMessageContent):
    """
    Represents the content of a venue message to be sent as the result of an inline query.

    Attributes:
        latitude (float): Latitude of the location in degrees.
        longitude (float): Longitude of the location in degrees.
        title (str); Name of the venue.
        address (str): Address of the venue.
        foursquare_id (str): Optional. Foursquare identifier of the venue, if known.

    Args:
        latitude (float): Latitude of the location in degrees.
        longitude (float): Longitude of the location in degrees.
        title (str); Name of the venue.
        address (str): Address of the venue.
        foursquare_id (Optional[str]): Foursquare identifier of the venue, if known.
        **kwargs (dict): Arbitrary keyword arguments.
    """

    def __init__(self, latitude, longitude, title, address, foursquare_id=None, **kwargs):
        # Required
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        # Optionals
        self.foursquare_id = foursquare_id

    @staticmethod
    def de_json(data, bot):
        return InputVenueMessageContent(**data)
