import customtkinter

class ResultsWindow:
    def __init__(self, root, main_window, unfound_paths, matched_paths):
        self.root = root
        self.main_window = main_window
        self.results_textbox = None
        self.unfound_paths = unfound_paths
        self.matched_paths = matched_paths

    def options_callback(self, option):
        self.results_textbox.configure(state="normal")
        self.results_textbox.delete("1.0", "end")
        if option == "Missing Paths":
            for path in self.unfound_paths:
                self.results_textbox.insert("end", f"{path}\n")
        elif option == "Matched Paths":
            for path in self.matched_paths:
                self.results_textbox.insert("end", f"{path}\n")
        self.results_textbox.configure(state="disabled")

    def create_results_window(self):
        # Result Window
        result_window = customtkinter.CTkToplevel(self.root)
        result_window.title("Results")
        self.main_window.center_window(result_window, 400, 450)
        # Ensures result_window begins on top of main window
        result_window.after(10, result_window.focus)
        # Frame
        frame = customtkinter.CTkFrame(master=result_window)
        frame.pack(pady=10, padx=10, fill="both", expand=True)
        # Options Combbox
        options_combobox = customtkinter.CTkComboBox(master=frame, values=["Missing Paths", "Matched Paths"], font=customtkinter.CTkFont("Inter", 12), command=self.options_callback)
        options_combobox.pack(pady=10, padx=10)
        options_combobox.configure(state="readonly")
        # Text
        self.results_textbox = customtkinter.CTkTextbox(master=frame, height=390, width=570, font=customtkinter.CTkFont("Inter", 12))
        self.results_textbox.pack(pady=5, padx=5, fill="both", expand=True)
        for path in self.unfound_paths:
            self.results_textbox.insert("end", f"{path}\n")
        self.results_textbox.configure(state="disabled")