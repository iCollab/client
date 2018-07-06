import tkinter as tk
import numpy
import PIL
from PIL import Image, ImageTk, ImageEnhance


class Client(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.winfo_toplevel().title("iCollab")
        self.geometry("1280x900")

        self.sidebar()

        self.imgPath = ("./images/img.jpg")
        self.img_arr = numpy.asarray(PIL.Image.open(self.imgPath))
        self.img = Image.fromarray(self.img_arr, 'RGB')
        self.background_image = ImageTk.PhotoImage(self.img)
        self.background = tk.Label(self, image=self.background_image).grid(
            row=20, column=1, sticky="nesw")

    def sidebar(self):
        # Brightness
        self.brightnessLabel = tk.Label(
            self, text="Brightness").grid(row=1, sticky="nesw")

        self.brightness = tk.Scale(
            self, from_=0, to=100, orient=tk.HORIZONTAL, command=self.changeBrightness)
        self.brightness.set(100)
        self.brightness.grid(row=2, column=0, sticky="nesw")

        # Contrast
        self.contrastLabel = tk.Label(self, text="Contrast")
        self.contrastLabel.grid(row=3, column=0, sticky="nesw")

        self.contrast = tk.Scale(self, from_=0, to=100,
                                 orient=tk.HORIZONTAL, command=self.changeContrast)
        self.contrast.set(100)
        self.contrast.grid(row=4, column=0, sticky="nesw")

        # Hue
        self.hueLabel = tk.Label(self, text="Hue")
        self.hueLabel.grid(row=5, column=0)

        self.hue = tk.Scale(self, from_=0, to=100,
                            orient=tk.HORIZONTAL, command=self.printValue)
        self.hue.grid(row=6, column=0, sticky="nesw")

        # Saturation
        self.saturationLabel = tk.Label(self, text="Saturation")
        self.saturationLabel.grid(row=7, column=0, sticky="nesw")

        self.saturation = tk.Scale(
            self, from_=0, to=500, orient=tk.HORIZONTAL, command=self.changeSaturation)
        self.saturation.set(100)
        self.saturation.grid(row=8, column=0, sticky="nesw")

        # Exposure
        self.exposureLabel = tk.Label(self, text="Exposure")
        self.exposureLabel.grid(row=9, column=0, sticky="nesw")

        self.exposure = tk.Scale(self, from_=0, to=100,
                                 orient=tk.HORIZONTAL, command=self.printValue)
        self.exposure.grid(row=10, column=0, sticky="nesw")

        # Brilliance
        self.brillianceLabel = tk.Label(self, text="Brilliance")
        self.brillianceLabel.grid(row=11, column=0, sticky="nesw")

        self.brilliance = tk.Scale(
            self, from_=0, to=100, orient=tk.HORIZONTAL, command=self.printValue)
        self.brilliance.grid(row=12, column=0, sticky="nesw")

        # Sharpness
        self.sharpnessLabel = tk.Label(self, text="Sharpness")
        self.sharpnessLabel.grid(row=15, column=0, sticky="nesw")

        self.sharpness = tk.Scale(
            self, from_=0, to=200, orient=tk.HORIZONTAL, command=self.changeSharpness)
        self.sharpness.set(100)
        self.sharpness.grid(row=16, column=0, sticky="nesw")

    def printValue(self, val):
        print(val)

    def changeContrast(self, val):
        i = Image.open(self.imgPath)
        contrast = ImageEnhance.Contrast(i).enhance(float(val) / 100)
        self.img_arr = numpy.asarray(contrast)
        self.img = Image.fromarray(self.img_arr, 'RGB')
        self.background_image = ImageTk.PhotoImage(self.img)
        self.background = tk.Label(self, image=self.background_image).grid(
            row=20, column=1, sticky="E")

    def changeBrightness(self, val):
        i = Image.open(self.imgPath)
        brightness = ImageEnhance.Brightness(i).enhance(float(val) / 100)
        self.img_arr = numpy.asarray(brightness)
        self.img = Image.fromarray(self.img_arr, 'RGB')
        self.background_image = ImageTk.PhotoImage(self.img)
        self.background = tk.Label(self, image=self.background_image).grid(
            row=20, column=1, sticky="E")

    def changeSaturation(self, val):
        i = Image.open(self.imgPath)
        saturation = ImageEnhance.Color(i).enhance(float(val) / 100)
        self.img_arr = numpy.asarray(saturation)
        self.img = Image.fromarray(self.img_arr, 'RGB')
        self.background_image = ImageTk.PhotoImage(self.img)
        self.background = tk.Label(self, image=self.background_image).grid(
            row=20, column=1, sticky="E")

    def changeSharpness(self, val):
        i = Image.open(self.imgPath)
        sharpness = ImageEnhance.Sharpness(i).enhance(float(val) / 100)
        self.img_arr = numpy.asarray(sharpness)
        self.img = Image.fromarray(self.img_arr, 'RGB')
        self.background_image = ImageTk.PhotoImage(self.img)
        self.background = tk.Label(self, image=self.background_image).grid(
            row=20, column=1, sticky="E")


if __name__ == "__main__":
    app = Client(None)
    app.mainloop()
