import customtkinter
from main_window import MainWindow

if __name__ == "__main__":
    root = customtkinter.CTk()
    main_window = MainWindow(root)
    root.mainloop()