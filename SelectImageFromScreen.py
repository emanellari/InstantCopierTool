import tkinter as tk
from tkinter import scrolledtext

import pyperclip
from PIL import ImageTk, ImageGrab
from plyer import notification

from EasyOcr import apply_ocr, from_easy_ocr
from necc_methods import Title_Case, Sentence_Case, UpperCase, Capitalized_Case, lower_case, AlternatingCase


def show_notification(message):
    try:
        root = tk.Tk()
        root.geometry("400x150")
        root.title("Text from OCR")
        root.configure(bg='#110c6e')
        root.resizable(width=False, height=False)

        formatted_text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=7)
        formatted_text_widget.insert(tk.END, message)
        formatted_text_widget.pack()

        def copy_text():
            pyperclip.copy(formatted_text_widget.get("1.0", "end-1c"))
            root.destroy()

        copy_button = tk.Button(root, text="Copy", command=copy_text)
        copy_button.pack(side=tk.LEFT, padx=10)
        root.mainloop()
    except tk.TclError:
        print("Error: Tkinter not supported on this system.")


class ScreenshotApp:
    def __init__(self, parent, key=None, option=None, txtbox=False, TEXT_CASE=None):
        self.txtbox = txtbox
        self.key = key
        self.option = option
        self.parent = parent
        self.TEXT_CASE = TEXT_CASE

        # Merr screenshot-in aktual të ekranit
        self.screenshot = ImageGrab.grab()
        self.photo = ImageTk.PhotoImage(self.screenshot)

        # Krijo një dritare të re për përzgjedhjen
        self.top_level = tk.Toplevel(self.parent)
        self.top_level.attributes('-fullscreen', True)
        self.top_level.config(cursor='crosshair')

        self.canvas = tk.Canvas(self.top_level, bg='white',
                                width=self.screenshot.width,
                                height=self.screenshot.height)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, anchor='nw', image=self.photo)

        # Variablat për përzgjedhjen
        self.selection_rect = None
        self.start_x = None
        self.start_y = None

        # Eventet për përzgjedhje
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def on_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)

        if self.selection_rect:
            self.canvas.delete(self.selection_rect)
        self.selection_rect = None

    def on_drag(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)

        if self.selection_rect:
            self.canvas.delete(self.selection_rect)

        self.selection_rect = self.canvas.create_rectangle(self.start_x, self.start_y, cur_x, cur_y, outline='red')

    def on_release(self, event):
        # Merr koordinatat e fundme të përzgjedhjes
        end_x = self.canvas.canvasx(event.x)
        end_y = self.canvas.canvasy(event.y)

        # Fshij kutinë e përzgjedhjes nëse ekziston
        if self.selection_rect:
            self.canvas.delete(self.selection_rect)

        # Përcakto kutinë e përzgjedhjes për t'u siguruar që janë përdorur koordinatat minimale dhe maksimale
        bbox = (min(self.start_x, end_x), min(self.start_y, end_y), max(self.start_x, end_x), max(self.start_y, end_y))

        # Merr screenshotin nga zona e përzgjedhur
        screenshot = ImageGrab.grab(bbox=bbox)

        # Ruaj screenshotin si një imazh
        screenshot.save("image2.png")

        # Mbyll dritaren e përzgjedhjes pas disa milisekondash
        self.top_level.after(400, self.top_level.destroy)

        # Procesoni tekstin nga OCR
        if self.option == "Better Accuracy(Requires Internet Conection)":
            text = apply_ocr()  # Përdor opsionin e saktë për OCR
        else:
            text = from_easy_ocr()  # Përdor versionin e lehtë të OCR

        # Zbato transformimin e tekstit sipas zgjedhjes së përdoruesit
        if self.TEXT_CASE == "Sentence case(The 1-st example.)":
            text = Sentence_Case(text)
        elif self.TEXT_CASE == "lower case(the 1-st example.)":
            text = lower_case(text)
        elif self.TEXT_CASE == "UPPER CASE(THE 1-ST EXAMPLE.)":
            text = UpperCase(text)
        elif self.TEXT_CASE == "Capitalized Case(The 1-st Example.)":
            text = Capitalized_Case(text)
        elif self.TEXT_CASE == "Title Case(The 1-St Example.)":
            text = Title_Case(text)
        elif self.TEXT_CASE == "aLtErNaTiNg cAsE(ThE 1-St ExAmPlE.)":
            text = AlternatingCase(text)

        # Shfaq ose kopjo tekstin e përpunuar
        if self.txtbox:
            show_notification(text)  # Shfaq tekstin në një dritare të re për përdoruesin
        else:
            pyperclip.copy(text)  # Kopjo tekstin në clipboard
            shfaq_toast_notification("Text copied to clipboard.")  # Shfaq njoftimin për kopjimin e tekstit

        # Printo tekstin për debug
        print(text)


def shfaq_toast_notification(message):
    notification.notify(
        title='Instant Copier',
        message=message,
        timeout=10,  # Koha në sekonda për të shfaqur njoftimin
    )
