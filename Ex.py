import tkinter as tk
from tkinter import ttk


class BookPointsApp:
    def __init__(self, root):
        """
        Initializes the application, setting up the main window and GUI widgets.
        """
        self.root = root
        self.root.title("Serendipity Booksellers Points")
        self.root.geometry("350x220")  # Set a reasonable default size
        self.root.resizable(False, False)  # Disable resizing

        # Configure the root window's grid to expand
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        # --- Widget 1: Input Frame ---
        # This frame will contain the instructions, entry box, and calculate button
        input_frame = ttk.LabelFrame(self.root, text="Purchase Info", padding="10")
        input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        input_frame.columnconfigure(0, weight=1)  # Make entry widget expandable

        # Label widget: to display instruction to the user
        self.instruction_label = ttk.Label(
            input_frame,
            text="Enter the number of books purchased this month:"
        )
        self.instruction_label.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 5))

        # Entry widget user for user input
        self.books_entry = ttk.Entry(input_frame, width=30)
        self.books_entry.grid(row=1, column=0, sticky="ew", padx=(0, 5))

        # Button that computes and displays the points earned
        self.calculate_button = ttk.Button(
            input_frame,
            text="Calculate Points",
            command=self.calculate_and_display_points
        )
        self.calculate_button.grid(row=1, column=1, sticky="e", padx=(5, 0))

        # --- Widget 2: Output Frame ---
        # This frame will display the result.
        output_frame = ttk.LabelFrame(self.root, text="Points Awarded", padding="10")
        output_frame.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="ew")
        output_frame.columnconfigure(1, weight=1)  # Make points value align right

        # We use a StringVar to automatically update the result label
        self.points_var = tk.StringVar()
        self.points_var.set("0 points")  # Set an initial value

        self.result_title_label = ttk.Label(output_frame, text="You have earned:")
        self.result_title_label.grid(row=0, column=0, sticky="w")

        self.result_value_label = ttk.Label(
            output_frame,
            textvariable=self.points_var,
            font=("Helvetica", 16, "bold"),
            anchor="e"  # Anchor text to the right (east)
        )
        self.result_value_label.grid(row=0, column=1, sticky="ew", padx=(10, 0))

    def calculate_and_display_points(self):
        """
        This function is called when the 'Calculate Points' button is pressed.
        It gets the text from the entry, calculates the points, and updates the
        output widget.
        """
        try:
            # 1. Get the number of books from the entry widget
            books_purchased = int(self.books_entry.get())

            points = 0

            # 2. Check for invalid input (negative books)
            if books_purchased < 0:
                self.points_var.set("Invalid input")
                return

            # 3. Apply the points logic based *exactly* on the prompt's rules
            # We interpret the rules literally: only the exact numbers (0, 2, 4, 6)
            # and the range (8+) earn points. Other numbers (1, 3, 5, 7) earn 0.
            if books_purchased == 0:
                points = 0
            elif books_purchased == 2:
                points = 5
            elif books_purchased == 4:
                points = 15
            elif books_purchased == 6:
                points = 30
            elif books_purchased >= 8:
                points = 60
            else:
                # This will catch 1, 3, 5, 7, etc.
                points = 0

            # 4. Update the text variable, which updates the output label
            self.points_var.set(f"{points} points")

        except ValueError:
            # 5. Handle cases where the user did not enter a valid number
            self.points_var.set("Enter a number")


def main():
    """
    Main function to create the root window and start the app.
    """
    root = tk.Tk()
    app = BookPointsApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()