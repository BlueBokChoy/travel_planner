"""
Author: Roy Chen
Date: Nov 26, 2024
Description: This module defines the TravelPlanner class, which creates a GUI for users to plan a custom
travel itinerary. It allows users to input their name, destination, travel preferences, and duration.
"""

import tkinter as tk
from PIL import ImageTk, Image

class TravelPlanner(tk.Tk):
    """
    This class creates a GUI that the user can interact with to create a custom travel Itinerary.
    """

    def __init__(self, itinerary):
        """
        Initializes the TravelPlanner window and GUI components.
        """
        
        # Initializes the parent (tk.Tk) class.
        super().__init__()
        
        # Gets the window height and width.
        # Will be used as references for other GUI components.
        self.window_height = self.winfo_screenheight()
        self.window_width = self.winfo_screenwidth()
        
        # Configure the initial appearance and properties of the window.
        self.geometry("%ix%i" % (int(self.window_width*0.6), int(self.window_height*0.6)))
        self.resizable(False, False)
        self.title("CustomVacay Travel Assistant")
        
        # Assigns an instance variable to the itinerary object to be used.
        self.itinerary = itinerary
        
        # Instance variable that will be used to dynamically display GUI elements.
        self.name_display_var = tk.StringVar()
        self.destination_display_var = tk.StringVar()
        self.transport_display_var = tk.StringVar()
        self.selected_styles_display_var = tk.StringVar()
        self.duration_display_var = tk.StringVar()
        self.itinerary_display_var = tk.StringVar()
        self.error_type_display_var = tk.StringVar()
        
        # Initializes the GUI elements.
        self.init_frames()
        self.init_images()
        self.init_entry()
        self.init_checkboxes()
        self.init_radios()
        self.init_labels()
        self.init_buttons()
        
        # Tracks the current frame index
        # Defines the order of frames to cycle through in the program.
        self.current_frame = 0
        self.frame_cycle = [self.menu_frame,\
                            self.name_entry_frame,\
                            self.destination_frame_one,\
                            self.destination_frame_two,\
                            self.travel_preferences_frame,\
                            self.itinerary_frame]

    def init_frames(self):
        """
        Initializes frames used in the GUI.
        """
        
        # Creates the main frames.
        self.menu_frame = self.default_frame_template()
        self.name_entry_frame = self.default_frame_template()
        self.destination_frame_one = self.default_frame_template()
        self.destination_frame_two = self.default_frame_template()
        self.travel_preferences_frame = self.default_frame_template()
        self.itinerary_frame = self.default_frame_template()
        self.error_frame = self.default_frame_template()

        # Creates frames for the travel preference frame.
        self.left_preference_frame = tk.Frame(self.travel_preferences_frame,\
                                              height=int(self.window_height*0.4),\
                                              width=int(self.window_width*0.18),\
                                              bg="#E9ECF5")
        self.left_preference_frame.place(relx=0.28, rely=0.6, anchor="center")
        
        self.right_preference_frame = tk.Frame(self.travel_preferences_frame,\
                                               height=int(self.window_height*0.4),\
                                               width=int(self.window_width*0.28),\
                                               bg="#E9ECF5")
        self.right_preference_frame.place(relx=0.65, rely=0.6, anchor="center")

    def default_frame_template(self):
        """Returns a default frame template with specific height, width and color. A helper method
        of the init_frames method. Has no parameters and returns nothing."""
        
        return tk.Frame(self,\
                        height=int(self.window_height*0.6),\
                        width=int(self.window_width*0.6),\
                        bg="#E9ECF5")
    
    def init_images(self):
        """
        Initializes images used in the GUI.
        """
        
        self.tk_uk_img = self.config_img(Image.open("img/united_kingdom.jpg"))
        self.tk_fr_img = self.config_img(Image.open("img/france.jpg"))
        self.tk_ca_img = self.config_img(Image.open("img/canada.jpg"))
        self.tk_us_img = self.config_img(Image.open("img/united_states.jpg"))
        self.tk_it_img = self.config_img(Image.open("img/italy.jpg"))

    def config_img(self, img):
        """
        Returns an image applied with a specific cropping height, width, and resampling filter. A helper method
        of the init_images method. Takes an image as a parameter. Returns the image with the formatting applied.
        """
        
        return ImageTk.PhotoImage(img.resize((int(self.window_width*0.18),\
                                              int(self.window_height*0.6)),\
                                             Image.Resampling.LANCZOS))
    
    def init_entry(self):
        """
        Initializes entries used in the GUI.
        """
        
        self.name_entry = self.config_entry(tk.Entry(self.name_entry_frame, textvariable=self.name_display_var, width=20))
        self.duration_entry = self.config_entry(tk.Entry(self.right_preference_frame, textvariable=self.duration_display_var, width=4))
        self.duration_entry.place(relx=0.46, rely=0.6, anchor="w")
        self.name_entry.place(relx=0.6, rely=0.5, anchor="center")

    def config_entry(self, entry):
        """
        Returns an entry applied with a specific color, background color, font, and text size. A helper method
        of the init_entry method. Takes an entry as a parameter. Returns the entry with the formatting applied.
        """
        
        entry.config(fg="#000000",\
                     bg="#FFFFFF",\
                     relief="flat",\
                     font=('Segoe UI Semibold', 15))
        
        return entry
    
    def init_checkboxes(self):
        """
        Initializes checkboxes used in the GUI.
        """
        
        self.adventure_style = tk.BooleanVar()
        self.relaxation_style = tk.BooleanVar()
        self.cultural_style = tk.BooleanVar()
        self.luxury_style = tk.BooleanVar()
        self.family_style = tk.BooleanVar()

        self.config_checkboxes(tk.Checkbutton(self.left_preference_frame, text="Adventure",\
                                              variable=self.adventure_style)).place(relx=0.1, rely=0.25, anchor="w")
        self.config_checkboxes(tk.Checkbutton(self.left_preference_frame, text="Relaxation",\
                                              variable=self.relaxation_style)).place(relx=0.1, rely=0.4, anchor="w")
        self.config_checkboxes(tk.Checkbutton(self.left_preference_frame, text="Cultural",\
                                              variable=self.cultural_style)).place(relx=0.1, rely=0.55, anchor="w")
        self.config_checkboxes(tk.Checkbutton(self.left_preference_frame, text="Luxury",\
                                              variable=self.luxury_style)).place(relx=0.1, rely=0.7, anchor="w")
        self.config_checkboxes(tk.Checkbutton(self.left_preference_frame, text="Family",\
                                              variable=self.family_style)).place(relx=0.1, rely=0.85, anchor="w")

    def config_checkboxes(self, checkbox):
        """
        Returns a checkbox applied with a specific color, background color, font, and text size. A helper method
        of the init_checkboxes method. Takes a checkbox as a parameter. Returns the checkbox with the formatting
        applied.
        """
        
        checkbox.config(fg="#2D4654",\
                        bg="#E9ECF5",\
                        font=('Segoe UI Semibold', 15),\
                        activebackground="#E9ECF5")
        
        return checkbox
    
    def init_radios(self):
        """
        Intializes radio buttons used in the GUI.
        """
        
        self.transport_display_var.set("Car")
        self.config_radio(tk.Radiobutton(self.right_preference_frame, text="Car",\
                                         value="Car")).place(relx=0.1, rely=0.25, anchor="w")
        self.config_radio(tk.Radiobutton(self.right_preference_frame, text="Train",\
                                         value="Train")).place(relx=0.1, rely=0.4, anchor="w")
        self.config_radio(tk.Radiobutton(self.right_preference_frame, text="Boat",\
                                         value="Boat")).place(relx=0.5, rely=0.25, anchor="w")
        self.config_radio(tk.Radiobutton(self.right_preference_frame, text="Plane",\
                                         value="Plane")).place(relx=0.5, rely=0.4, anchor="w")

    def config_radio(self, radio):
        """
        Returns a radio button applied with a specific color, background color, font, text size, and active
        background color. A helper method of the init_radios method. Takes a radio button as a parameter. Returns
        the radio button with the formatting applied.
        """

        radio.config(fg="#2D4654",\
                     bg="#E9ECF5",\
                     font=('Segoe UI Semibold', 15),\
                     activebackground="#E9ECF5",\
                     variable=self.transport_display_var)
        
        return radio

    def init_labels(self):
        """
        Initializes labels used in the GUI.
        """
        
        # Creates the labels for the menu frame.
        tk.Label(self.menu_frame, fg="#2D4654", bg="#E9ECF5", text="Travel Assistant",\
                 font=('Segoe UI Semibold', 25, "italic")).place(relx=0.6, rely=0.5, anchor="center")
        tk.Label(self.menu_frame, fg="#87BCDE", bg="#E9ECF5", text="CustomVacay",\
                 font=('Segoe UI Semibold', 30)).place(relx=0.4, rely=0.405, anchor="center")
        
        # Creates the labels for the entry frame.
        self.config_label(tk.Label(self.name_entry_frame, text="Personal Information"), 20)\
                                                          .place(relx=0.3, rely=0.3, anchor="center")
        self.config_label(tk.Label(self.name_entry_frame, text="Name"), 18)\
                                                          .place(relx=0.25, rely=0.5, anchor="center")
        
        # Creates the labels for the destination frames.
        self.config_label(tk.Label(self.destination_frame_one, text="Destinations"), 20)\
                                                               .place(relx=0.88, rely=0.3, anchor="center")
        self.config_label(tk.Label(self.destination_frame_two, text="Destinations"), 20)\
                                                               .place(relx=0.88, rely=0.3, anchor="center")
        self.config_photo_label(tk.Label(self.destination_frame_one, image=self.tk_uk_img))\
                                                                     .place(relx=0.05, rely=0.5, anchor="w")
        self.config_photo_label(tk.Label(self.destination_frame_one, image=self.tk_fr_img))\
                                                                     .place(relx=0.3, rely=0.5, anchor="w")
        self.config_photo_label(tk.Label(self.destination_frame_one, image=self.tk_ca_img))\
                                                                     .place(relx=0.55, rely=0.5, anchor="w")
        self.config_photo_label(tk.Label(self.destination_frame_two, image=self.tk_us_img))\
                                                                     .place(relx=0.15, rely=0.5, anchor="w")
        self.config_photo_label(tk.Label(self.destination_frame_two, image=self.tk_it_img))\
                                                                     .place(relx=0.45, rely=0.5, anchor="w")
        
        # Creates the labels for the travel preferences frames.
        self.config_label(tk.Label(self.travel_preferences_frame, text="Travel Preferences"), 20)\
                                                                  .place(relx=0.25, rely=0.15, anchor="center")
        self.config_label(tk.Label(self.left_preference_frame, text="Travel Style"), 18)\
                                                               .place(relx=0.1, rely=0.1, anchor="w")
        self.config_label(tk.Label(self.right_preference_frame, text="Transportation"), 18)\
                                                                .place(relx=0.1, rely=0.1, anchor="w")
        self.config_label(tk.Label(self.right_preference_frame, text="Duration:"), 18)\
                                                                .place(relx=0.1, rely=0.6, anchor="w")
        self.config_label(tk.Label(self.right_preference_frame, text="Days"),18)\
                                                                .place(relx=0.65, rely=0.6, anchor="w")
        self.config_label(tk.Label(self.right_preference_frame, text="Maximum 10 Days*"), 10)\
                                                                .place(relx=0.1, rely=0.7, anchor="w")
        
        # Creates the labels for the itinerary frames.
        self.config_label(tk.Label(self.itinerary_frame, text="Itinerary for"), 20)\
                                                         .place(relx=0.05, rely=0.1, anchor="w")
        self.config_label(tk.Label(self.itinerary_frame, textvariable=self.name_display_var), 20)\
                                                         .place(relx=0.25, rely=0.1, anchor="w")
        self.config_label(tk.Label(self.itinerary_frame, text="Destination:"), 10)\
                                                         .place(relx=0.05, rely=0.22, anchor="w")
        self.config_label(tk.Label(self.itinerary_frame, textvariable=self.destination_display_var), 10)\
                                                         .place(relx=0.05, rely=0.26, anchor="w")
        self.config_label(tk.Label(self.itinerary_frame, text="Transportation:"), 10)\
                                                         .place(relx=0.05, rely=0.32, anchor="w")
        self.config_label(tk.Label(self.itinerary_frame, textvariable=self.transport_display_var), 10)\
                                                         .place(relx=0.05, rely=0.36, anchor="w")
        self.config_label(tk.Label(self.itinerary_frame, text="Preferences:"), 10)\
                                                         .place(relx=0.05, rely=0.42, anchor="w")
        self.config_label(tk.Label(self.itinerary_frame, textvariable=self.selected_styles_display_var, \
                                   wraplength=int(self.window_height*0.2), justify="left"), 10)\
                                                         .place(relx=0.05, rely=0.48, anchor="w")
        self.config_label(tk.Label(self.itinerary_frame, text="Duration (Days):"), 10)\
                                                         .place(relx=0.05, rely=0.56, anchor="w")
        self.config_label(tk.Label(self.itinerary_frame, textvariable=self.duration_display_var), 10)\
                                                         .place(relx=0.05, rely=0.6, anchor="w")
        
        # Creates the label for the custom itinerary on the intinerary frame.
        self.config_label(tk.Label(self.itinerary_frame, textvariable=self.itinerary_display_var, anchor="nw",\
                                   wraplength=int(self.window_height*0.78), justify="left"), 10)\
                                                         .place(relx=0.25, rely=0.18, anchor="nw")
        
        # Creates the label for the error frame.
        self.config_label(tk.Label(self.error_frame,textvariable=self.error_type_display_var), 20)\
                                                     .place(relx=0.5, rely=0.5, anchor="center")
        
    def config_label(self, label, size):
        """
        Returns a label applied with a specific color, background color, font, and text size. A helper method
        of the init_labels method. Gets the label and text size as an object and integer parameter respectively.
        Returns the label with the formatting applied.
        """
        
        label.config(fg="#2D4654",\
                     bg="#E9ECF5",\
                     font=('Segoe UI Semibold', size))
        
        return label
    
    def config_photo_label(self, label):
        """
        Returns a label applied with a specific height and width. A helper method of the init_labels method.
        Takes a label as a parameter. Returns the label with the formatting applied.
        """
        
        label.config(height=int(self.window_height*0.6),\
                     width=int(self.window_width*0.12))
        
        return label

    def init_buttons(self):
        """
        Initializes buttons used in the GUI.
        """
        
        # Creates the buttons for the menu frame.
        self.config_btn(tk.Button(self.menu_frame, width=15, text="Start Planning", command=self.display_next_frame))\
                                                   .place(relx=0.5, rely=0.65, anchor="center")
        self.config_btn(tk.Button(self.menu_frame, width=5, text="Quit", command=self.end_program))\
                                                   .place(relx=0.70, rely=0.65, anchor="center")
        
        # Creates the buttons for the name entry frame.
        self.config_btn(tk.Button(self.name_entry_frame, width=15, text=">>>Next>>>",\
                                  command=self.process_name_input)).place(relx=0.5, rely=0.65, anchor="center")
        self.config_btn(tk.Button(self.name_entry_frame, width=9, text="< Restart",\
                                  command=self.restart_program)).place(relx=0.88, rely=0.9, anchor="center")
        
        # Creates the buttons for the destination frame.
        # Creates the country selection buttons for the destination frame.
        self.config_btn(tk.Button(self.destination_frame_one, width=15, text="United Kingdom", \
                                  command=lambda: self.process_destination_input("United Kingdom")))\
                                  .place(relx=0.15, rely=0.8, anchor="center")
        self.config_btn(tk.Button(self.destination_frame_one, width=15, text="France",\
                                  command=lambda: self.process_destination_input("France")))\
                                  .place(relx=0.4, rely=0.8, anchor="center")
        self.config_btn(tk.Button(self.destination_frame_one, width=15, text="Canada",\
                                  command=lambda: self.process_destination_input("Canada")))\
                                  .place(relx=0.65, rely=0.8, anchor="center")
        self.config_btn(tk.Button(self.destination_frame_two, width=15, text="United States",\
                                  command=lambda: self.process_destination_input("United States")))\
                                  .place(relx=0.25, rely=0.8, anchor="center")
        self.config_btn(tk.Button(self.destination_frame_two, width=15, text="Italy",\
                                  command=lambda: self.process_destination_input("Italy")))\
                                  .place(relx=0.55, rely=0.8, anchor="center")
        # Creates the cycle frame buttons in the destination frames.
        self.config_btn(tk.Button(self.destination_frame_one, width=15, text=">>> >>>\nMore Locations\n>>> >>>",\
                                  command=self.display_next_frame)).place(relx=0.88, rely=0.5, anchor="center")
        self.config_btn(tk.Button(self.destination_frame_one, width=9, text="< Restart",\
                                  command=self.restart_program)).place(relx=0.88, rely=0.9, anchor="center")
        self.config_btn(tk.Button(self.destination_frame_two, width=15, text="<<< <<<\nReturn\n<<< <<<",\
                                  command=self.display_previous_frame)).place(relx=0.88, rely=0.5, anchor="center")
        
        # Creates the buttons for the travel preference frame.
        self.config_btn(tk.Button(self.right_preference_frame, width=15, text="Create Itinerary!",\
                                  command=self.process_preferences_input)).place(relx=0.25, rely=0.9, anchor="w")
        self.config_btn(tk.Button(self.travel_preferences_frame, width=9, text="< Restart",\
                                  command=self.restart_program)).place(relx=0.88, rely=0.9, anchor="center")
        
        # Creates the buttons for the itinerary frame.
        self.config_btn(tk.Button(self.itinerary_frame, width=9, text="< Restart",\
                                  command=self.restart_program)).place(relx=0.88, rely=0.9, anchor="center")
        
        # Creates the buttons for the error frame.
        self.config_btn(tk.Button(self.error_frame, width=15, text="< Back",\
                                  command=self.manage_error_frame)).place(relx=0.88, rely=0.9, anchor="center")
        
    def config_btn(self, btn):
        """
        Returns a button applied with a specific color, background color, border width, cursor style, hightlight color,
        active background color, and font. Also applies the button hover styles. A helper method of the init_buttons
        method. Takes a button as a parameter. Returns the button with the formatting applied.
        """
        
        # Applies the default styles.
        btn.config(fg="#096B72",\
                   bg="#E9ECF5",\
                   borderwidth=0,\
                   cursor="hand2",\
                   highlightcolor="#172A3A",\
                   activebackground="#E9ECF5",\
                   font=('Segoe UI Semibold', 15))
        
        # Applies the hover and unhover styles.
        btn.bind("<Enter>", btn.config(fg="#A5D8D3"))
        btn.bind("<Leave>", btn.config(fg="#096B72"))
        
        return btn
    
    def start_program(self):
        """
        Starts the program. Takes no parameters and returns nothing.
        """
        
        # Starts the frame cycle. 
        self.display_next_frame(0)
        
        # Opens the program data.
        self.itinerary.open_data()

    def end_program(self):
        """
        Ends the program. Takes no parameters and returns nothing.
        """
        
        # Closes the program data.
        self.itinerary.close_data()
        
        # Destroys the window.
        self.destroy()

    def restart_program(self):
        """
        Restarts the program. Takes no parameters and returns nothing.
        """
        
        # Resets to the first frame.
        self.frame_cycle[self.current_frame].place_forget()
        self.current_frame = 0
        self.display_next_frame(0)
        
        # Unlocks entry widgets.
        self.name_entry.config(state=tk.NORMAL)
        self.duration_entry.config(state=tk.NORMAL)

    def process_name_input(self):
        """
        Handles the name input and validates it.
        """
        
        if self.itinerary.validate_name(self.name_display_var.get()):
            
            # Sets the user name input into the itinerary object.
            self.itinerary.set_name(self.name_display_var.get())
            
            # Locks the name entry widget.
            self.name_entry.config(state=tk.DISABLED)
            
            # Assigns the name display in the GUI to the input name.
            self.name_display_var.set(self.itinerary.get_name())
            
            # Displays the next frame.
            self.display_next_frame()
        else:
            
            # Displays the error frame.
            self.manage_error_frame(True, "Name")

    def process_destination_input(self, destination):
        """Handles destination selection."""
        
        # Sets the user destination input into the itinerary object.
        self.itinerary.set_destination(destination)
        
        # Assigns the name display in the GUI to the input name.
        self.destination_display_var.set(destination)
        
        # Displays the next frame.
        if destination == "Italy" or destination == "United States":
            self.display_next_frame()
        else:
            self.display_next_frame(2)

    def process_preferences_input(self):
        """Handles the travel preferences input and validates them."""
        
        # Gets the user's preference styles as a list
        styles_list = []
        if self.adventure_style.get(): styles_list.append("Adventure")
        if self.relaxation_style.get(): styles_list.append("Relaxation")
        if self.cultural_style.get(): styles_list.append("Cultural")
        if self.luxury_style.get(): styles_list.append("Luxury")
        if self.family_style.get(): styles_list.append("Family")
        
        # Validates whether the necessary information has been given.
        if self.itinerary.validate_styles(styles_list) and self.itinerary.validate_duration(self.duration_display_var.get()):
            
            # Sets the user preferences input into the itinerary object.
            self.itinerary.set_styles(styles_list)
            self.itinerary.set_transport(self.transport_display_var.get()) 
            self.itinerary.set_duration(self.duration_display_var.get())
            
            # Locks the duration entry widget.
            self.duration_entry.config(state=tk.DISABLED)
            
            # Assigns the appropriate preference display in the GUI to the preferences input.
            self.duration_display_var.set(self.itinerary.get_duration())
            self.selected_styles_display_var.set(str(", ".join(styles_list)))
            
            # Creates the itinerary and assigns to the itineary display.
            self.itinerary_display_var.set(self.itinerary.create_itinerary())
            
            # Displays the next frame.
            self.display_next_frame()
        else:
            
            # Displays the error frame.
            self.manage_error_frame(True, "Preference(s)")
    
    def display_next_frame(self, increment=1):
        """
        Hides the current frame, increases the frame index, and displays the next frame at the center of the window.
        Gets the increment amount as a integer parameter that is default set to 1. Returns nothing.
        """
        
        self.frame_cycle[self.current_frame].place_forget()
        self.current_frame += increment
        self.frame_cycle[self.current_frame].place(relx=0.5, rely=0.5, anchor="center")
        
    def display_previous_frame(self, increment=1):
        """
        Hides the current frame, decreases the frame index, and displays the previous frame at the center of the window.
        Gets the increment amount as a integer parameter that is default set to 1. Returns nothing.
        """
        
        self.frame_cycle[self.current_frame].place_forget()
        self.current_frame -= increment
        self.frame_cycle[self.current_frame].place(relx=0.5, rely=0.5, anchor="center")
        
    def manage_error_frame(self, display=False, error="Input"):
        """
        Toggles between displaying the error frame with a custom error message and the current frame. The display parameter
        tracks whether to display or hide the error frame and is given as a bool parameter which is set to False by default and
        the error string parameter modifies the error frame with the type of error and is set to "Input" by default. Returns
        nothing.
        """
        
        if display:
            self.error_type_display_var.set("Invalid " + error)
            self.frame_cycle[self.current_frame].place_forget()
            self.error_frame.place(relx=0.5, rely=0.5, anchor="center")
        else:
            self.error_frame.place_forget()
            self.frame_cycle[self.current_frame].place(relx=0.5, rely=0.5, anchor="center")