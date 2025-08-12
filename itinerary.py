"""
Author: Roy Chen
Date: Nov 26, 2024
Description: This module defines the Itinerary class, which is responsible for generating a travel
itinerary based on user input. The class allows for setting the itinerary's name, destination, duration,
travel styles, and transport method. It reads data from files containing locations and activities,
processes this data, and creates an itinerary for the specified duration.
"""

import random

class Itinerary():
    """
    This class generates a travel itinerary based on user preferences, including destination, duration,
    styles, and transport.
    """

    def __init__(self):
        """
        Initializes the Itinerary object with default values for name, destination, duration, styles,
        and transport.
        """
        
        self.__name = ""
        self.__destination = ""
        self.__duration = ""
        self.__styles = []
        self.__transport = ""

    def open_data(self):
        """
        Opens the data files containing location and activity information. Takes no parameters. Returns
        nothing.
        """
        
        self.location_file = open("itinerary_data/locations.txt", "r")
        self.activity_file = open("itinerary_data/activities.txt", "r")

    def close_data(self):
        """
        Closes the data files containing location and activity information. Takes no parameters. Returns
        nothing.
        """
        
        self.location_file.close()
        self.activity_file.close()

    def create_itinerary(self):
        """
        Generates an itinerary based on the user's destination, travel styles, duration, and transport
        preferences. Reads the relevant location and activity data, selects random activities and locations,
        and assembles the itinerary for the specified duration. Takes no parameters. Returns the generated
        itinerary in text format.
        """
        
        self.location_file.seek(0)
        self.activity_file.seek(0)

        destination = self.get_destination()
        styles = self.get_styles()
        duration = self.get_duration()
        transport = self.get_transport()

        location_urban_list, location_natural_list = self.select_potential_locations(destination)
        
        activity_list = self.select_potential_activites(styles)
        
        itinerary = self.generate_activity(duration, location_urban_list, location_natural_list, \
                                            activity_list, transport, destination)

        return itinerary

    def select_potential_locations(self, destination):
        """
        Selects potential urban and natural locations based on the provided destination. Iterates through
        the location data and separates urban and natural attractions for the specified destination. The
        destination is passed as a string parameter. Returns two lists: a list of urban attractions and
        a list of natural attractions.
        """
        
        location_urban_list = []
        location_natural_list = []
        reached_relevant_block = False
        
        for line in self.location_file:
            
            if destination in line and "urban_attraction" in line:
                reached_relevant_block = True
                location_urban_list.append(line.replace(destination, "")\
                                           .replace("urban_attraction", "").strip())
                
            elif destination in line and "natural_attraction" in line:
                reached_relevant_block = True
                location_natural_list.append(line.replace(destination, "")\
                                             .replace("natural_attraction", "").strip())
                
            elif reached_relevant_block:
                break
                
        return location_urban_list, location_natural_list

    def select_potential_activites(self, styles):
        """
        Selects potential activities based on the specified styles. Iterates through the activity data
        and selects activities that match the specified travel styles pass as a list. Returns another list
        of activities that match the selected styles.
        """
        
        activity_list = []
        
        for line in self.activity_file:
            for style in styles:
                style_tag = "#%s" % style.lower()
                if style_tag in line:
                    activity_list.append(line.replace(style_tag, "").strip())
                    
        return activity_list

    def generate_activity(self, duration, location_urban_list, location_natural_list, activity_list, \
                           transport, destination):
        """
        Generates one itinerary activity by selecting random activities and locations and combining them to
        the existing itinerary. Gets the list of potential activities, list of potential locations, prefered
        transport method as a string, and the destination as a string as parameters. Returns the generated
        itinerary as a string, with the new activity.
        """
        
        itinerary = ""
        
        for day in range(1, int(duration) + 1):
            
            activity = self.select_random(activity_list)
            activity = activity.replace("urban_attraction", self.select_random(location_urban_list))\
                               .replace("natural_attraction", self.select_random(location_natural_list))\
                               .replace("method_of_access", transport.lower())\
                               .replace("location", destination)\
                               .replace("#", str(day))
            
            itinerary += activity + "\n"
        
        return itinerary

    def select_random(self, input_list):
        """
        Selects a random item from a list passed as a parameter. Returns the randomly selected item from
        the list.
        """
        
        item = random.choice(input_list)
        input_list.remove(item)
        return item

    def set_name(self, name):
        """
        Sets the name instance variable of the itinerary. The name is passed as a string parameter and
        stripped of leading/trailing whitespace and capitalized. Returns nothing.
        """
        
        self.__name = name.strip().title()

    def set_destination(self, destination):
        """
        Sets the destination instance variable of the itinerary. The destination is stored as a string
        parameter. Returns nothing.
        """
        
        self.__destination = destination

    def set_duration(self, duration):
        """
        Sets the duration instance variable of the itinerary (in days). The duration is passed as a string
        after stripping any surrounding whitespace. Returns nothing.
        """
        
        self.__duration = duration.strip()

    def set_styles(self, styles):
        """
        Sets the style instance variable of the itinerary. The styles variable is passed as
        a list parameter. Returns nothing.
        """
        
        self.__styles = styles

    def set_transport(self, transport):
        """
        Sets the transport instance variable of the itinerary. The transport variable is passed as
        a string parameter. Returns nothing.
        """
        
        self.__transport = transport

    def get_name(self):
        """
        Returns the current value of the name instance variable of the itinerary. Has no
        parameters.
        """
        
        return self.__name

    def get_destination(self):
        """
        Returns the current value of the destination instance variable of the itinerary. Has no
        parameters.
        """
        
        return self.__destination

    def get_duration(self):
        """
        Returns the current value of the duration instance variable of the itinerary. Has no
        parameters.
        """
        
        return self.__duration

    def get_styles(self):
        """
        Returns the current value of the styles instance variable of the itinerary. Has no
        parameters.
        """
        
        return self.__styles

    def get_transport(self):
        """
        Returns the current value of the transport instance variable of the itinerary. Has
        no parameters.
        """
        
        return self.__transport

    def validate_name(self, name):
        """
        Validates the name of the user. The name must be alphanumeric. The name is passed as a
        parameter Returns a bool; True if the name is valid, False otherwise.
        """
        
        name = name.replace(" ", "")
        return name.isalnum()

    def validate_styles(self, styles):
        """
        Validates the travel styles for the itinerary. Empty style list is invalid. The styles
        list is passed as a parameter. Returns a bool; True if the styles list is valid, False
        otherwise.
        """
        
        return len(styles) > 0

    def validate_duration(self, duration):
        """
        Validates the duration of the itinerary. The duration, passed as a parameter, must
        be a digit between 1 and 10 days. Returns a bool; True if the duration is valid, False
        otherwise.
        """
        duration = duration.strip()
        return duration.isdigit() and 0 < int(duration) < 11