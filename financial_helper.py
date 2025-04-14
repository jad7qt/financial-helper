import tkinter as tk
import pandas as pd
from tkinter import filedialog


class FinancialHelper():
    def __init__(self):
        # Set dataframe to None until CSV is imported
        self.df = None
        

    def upload_csv(self):
        file_path = filedialog.askopenfilename(
            title="Select a CSV file",
            filetypes=[("CSV files", "*.csv")]
        )

        if file_path:
            try:
                self.df = pd.read_csv(file_path)
            except Exception as e:
                # TODO: Display no CSV found on page
                print(f"Failed to load CSV: {e}")
        else:
            print("No file path found")
            # TODO: Display no CSV found on page
        return

if __name__ == "__main__":
    test = FinancialHelper()