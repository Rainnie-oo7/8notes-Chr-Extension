import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import ImageGrab
import pyautogui
################## Schiebe\Scrolle bis 1mm über dem Musikstück ############### Zoome Webseit4 auf 110 % an ###############
class SnippingTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Snipping Tool")
        self.rect_width = 730
        self.rect_height = 1107

        # Create a title bar frame
        self.title_bar = tk.Frame(root, bg="gray", height=200)
        self.title_bar.pack(fill=tk.X, side=tk.TOP)

        # Create a button on the title bar to start the snipping process
        self.snip_button = tk.Button(self.title_bar, text="Snip", command=self.create_overlay)
        self.snip_button.pack(pady=20)

        # Set minimum size for the root window
        self.root.minsize(300, 200)

    def create_overlay(self):
        self.root.withdraw()
        self.overlay = tk.Toplevel(self.root)
        self.overlay.attributes("-fullscreen", True)
        self.overlay.attributes("-alpha", 0.3)  # Make the overlay semi-transparent
        self.overlay.attributes("-topmost", True)

        # Bind the escape key to close the overlay
        self.overlay.bind("<Escape>", self.close_overlay)
        self.overlay.bind("<Button-1>", self.start_snip)

    def start_snip(self, event):
        self.overlay.withdraw()
        self.take_screenshot()

    def close_overlay(self, event=None):
        self.overlay.destroy()
        self.root.deiconify()

    def take_screenshot(self):
        # Ask for the screenshot name
        screenshot_name = simpledialog.askstring("Save Screenshot", "Enter the name for the screenshot:")

        if screenshot_name:
            # Take the screenshot after a short delay
            self.root.after(500, lambda: self.save_screenshot(screenshot_name))
        else:
            messagebox.showinfo("Screenshot", "Screenshot not saved. No name provided.")
            self.close_overlay()

    def save_screenshot(self, screenshot_name):
        screen_width, screen_height = pyautogui.size()
        xzero = ((screen_width - self.rect_width) // 2) - 14
        yzero = ((screen_height - self.rect_height) // 2) - 7
        x1 = xzero + self.rect_width
        y1 = yzero + self.rect_height

        screenshot = ImageGrab.grab(bbox=(xzero, yzero, x1, y1))
        screenshot.save(f"{screenshot_name}.png")

        self.close_overlay()
        # messagebox.showinfo("Screenshot", f"Screenshot saved as {screenshot_name}.png")

if __name__ == "__main__":
    root = tk.Tk()
    app = SnippingTool(root)
    root.mainloop()
