"""
Author: Roy Chen
Date: Nov 26, 2024
Description: This program is a travel planning app that guides users through creating a personalized
itinerary. Using input for personal details, destination, preferences, and duration, this program
generates a custom travel itinerary for the user with activites and locations.
"""

import travel_planner
import itinerary

def main():
    """The Mainline Logic."""
    
    current_itinerary = itinerary.Itinerary()
    
    travelplanner = travel_planner.TravelPlanner(current_itinerary)

    travelplanner.start_program()
    
    travelplanner.mainloop()
    
# Calls the main function.
main()    