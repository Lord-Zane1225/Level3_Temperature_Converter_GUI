from tkinter import *
from functools import partial # To prevent unwanted windows


class Converter:
    """
    Temperature convertion tool (°C to °F or °F to °C)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """


        # frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_help_button = Button(self.temp_frame, text="Help / Info", bg="#CC6600", fg="#FFFFFF", font=("Arial", 12, "bold"), width=12,
                                     command=self.to_help)
        self.to_help_button.grid(row=1, padx=5, pady=5)


    def to_help(self):
        DisplayHelp(self)

class DisplayHelp:

    def __init__(self, partner):

        # setup dialogue box
        background = "#FFE6CC"
        self.help_box = Toplevel()

        # disable help button
        partner.to_help_button.config(state=DISABLED)

        # if users press the cross at the top, closes help and enables help button.
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # frame
        self.help_frame = Frame(self.help_box, width=300, height=200)
        self.help_frame.grid()

        # heading
        self.help_heading_label = Label(self.help_frame, text="Help / Info", font=("Arial", 14, "bold"))
        self.help_heading_label.grid(row=0)

        # help text
        help_text = ("To use the program, simply enter the temperature you wish to convert and then choose to convert to "
                     "either degrees Celsius (centigrade) or Fahrenheit. \n\n Note that -273 degrees C (or -459 F) is "
                     "absolute zero (the coldest possible temperature). If you try to convert to a temperature which is "
                     "less than -273 degrees C, you will get an error message. \n\nTo see your calculation history and "
                     "export it into a text file, please click the 'History / Export' button. ")

        self.help_text_label = Label(self.help_frame,
                                     text=help_text, wraplength=350, justify="left")
        self.help_text_label.grid(row=1, padx=10)

        # dismiss button
        self.dismiss_button = Button(self.help_frame, font=("Arial", 12, "bold"), text="Dismiss", bg="#CC6600", fg="#FFFFFF",
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, pady=10, padx=10)

        # list and loop to set background colour on everything except the buttons
        recolour_list = [self.help_frame, self.help_heading_label, self.help_text_label]

        for item in recolour_list:
            item.config(bg=background)

    def close_help(self, partner):

        """Closes help dialogue box and enables help button."""
        # make help button normal
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
