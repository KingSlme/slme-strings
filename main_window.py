import customtkinter
from results_window import ResultsWindow
from file_scanner import FileScanner

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.textbox_strings = None
        self.textbox_paths = None
        self.create_main_window()

    @staticmethod
    def center_window(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")

    def scan_callback(self):
            strings = FileScanner.get_strings(self.textbox_strings)
            paths = FileScanner.get_paths(self.textbox_paths)
            unfound_paths, found_paths = FileScanner.filter_paths(paths)
            matched_paths = FileScanner.match_strings(strings, found_paths)
            results_window = ResultsWindow(self.root, self, unfound_paths, matched_paths)
            results_window.create_results_window()

    def create_main_window(self):
        # Main Window
        self.root.title("SlmeStrings")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        MainWindow.center_window(self.root, 640, 480)
        # Frame
        frame = customtkinter.CTkFrame(master=self.root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        # Strings Label and Textbox
        strings_label = customtkinter.CTkLabel(master=frame, text="Strings", font=customtkinter.CTkFont("Inter", 25))
        strings_label.pack(pady=(10, 0))
        self.textbox_strings = customtkinter.CTkTextbox(master=frame, height=60, width=580, font=customtkinter.CTkFont("Inter", 12))
        self.textbox_strings.pack(pady=10, padx=10, fill="both", expand=True)
        # File Paths Label and Textbox
        file_paths_label = customtkinter.CTkLabel(master=frame, text="File Paths", font=customtkinter.CTkFont("Inter", 25))
        file_paths_label.pack()
        self.textbox_paths = customtkinter.CTkTextbox(master=frame, height=200, width=580, font=customtkinter.CTkFont("Inter", 12))
        self.textbox_paths.pack(pady=10, padx=10, fill="both", expand=True)
        # Scan Button
        scan_button = customtkinter.CTkButton(
            width=250,
            height=100,
            master=frame,
            text="Scan",
            font=customtkinter.CTkFont("Inter", 25, weight="bold"),
            command=self.scan_callback
        )
        scan_button.pack(pady=(5, 15), padx=175, fill="both", expand=True)