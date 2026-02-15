from tkinter import *
import all_constants as c
import conversion_rounding as cr
from functools import partial # To prevent unwanted windows


class Converter:
    """
    Temperature convertion tool (°C to °F or °F to °C)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        # history list
        self.all_calculations_list = []

        # frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        # Title - first row (row 0)
        self.temp_heading = Label(self.temp_frame, text="Temperature Converter", font=("Arial", 16, "bold"))
        self.temp_heading.grid(row=0)

        # Instructions - second row (row 1)
        instructions = ("Please enter a temperature below and then press one of the buttons "
                        "to convert it from centigrade to Fahrenheit.")
        self.temp_instructions = Label(self.temp_frame, text=instructions, wraplength=250, width=40, justify="left")
        self.temp_instructions.grid(row=1)

        # Entry - third row (row 2)
        self.temp_entry = Entry(self.temp_frame, font=("Arial", 14))
        self.temp_entry.grid(row=2, padx=10, pady=10)

        # Error / Answer - fourth row (row 3)
        error = "Please enter a number"
        self.answer_error = Label(self.temp_frame, text=error, font=("Arial", 14, "bold"), fg="#004C99")
        self.answer_error.grid(row=3)

        # Conversion, help and history / export buttons - fifth row (row 4)
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        # button list (button text | bg colour | command | row | column)
        button_details_list = [
            ["To Celsius", "#990099", lambda:self.check_temp(c.ABS_ZERO_CELSIUS), 0, 0],
            ["To Fahrenheit", "#009900", lambda:self.check_temp(c.ABS_ZERO_FAHRENHEIT), 0, 1],
            ["Help / Info", "#CC6600", self.to_help, 1, 0],
            ["History / Export", "#004C99", "", 1, 1]
        ]

        # List to hold buttons once they have been made
        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame, text=item[0], bg=item[1], fg="#FFFFFF",
                                      font=("Arial", 12, "bold"), width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)

        # retrieve to_help button
        self.to_help_button = self.button_ref_list[2]

        # retrieve 'history / export' button and disable it at the start
        self.to_history_button = self.button_ref_list[3]
        self.to_history_button.config(state=DISABLED)


    def check_temp(self,min_temp):
        """
        Checks temperature is valid and either calculates or shows error
        """

        # receive temperature to be converted
        to_convert = self.temp_entry.get()

        # reset label and entry box for post error
        self.answer_error.config(fg="#004C99", font=("Arial", 13, "bold"))
        self.temp_entry.config(bg="#FFFFFF")

        error = f"Enter a number more than / equal to {min_temp}"
        has_errors = "no"

        # error or invoke calculation
        try:
            to_convert = float(to_convert)
            if to_convert >= min_temp:
                self.convert(min_temp, to_convert)
            else:
                has_errors = "yes"
        except ValueError:
            has_errors = "yes"

        if has_errors != "no":
            self.answer_error.config(text=error, fg="#9C0000", font=("Arial", 10, "bold"))
            self.temp_entry.config(bg="#F4CCCC")
            self.temp_entry.delete(0, END)


    def convert(self, min_temp, to_convert):

        if min_temp == c.ABS_ZERO_CELSIUS:
            answer = cr.to_celsius(to_convert)
            answer_statement = f"{to_convert} °C is {answer} °F"
        else:
            answer = cr.to_fahrenheit(to_convert)
            answer_statement = f"{to_convert} °F is {answer} °C"

        self.answer_error.config(text=answer_statement)

        # enable history button
        self.to_history_button.config(state=NORMAL)

        # add answer to history list
        self.all_calculations_list.append(answer_statement)
        print(self.all_calculations_list)


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

