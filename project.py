from tkinter import Tk, Label, Button, Entry, StringVar, PhotoImage,simpledialog
from PIL import Image, ImageEnhance, ImageFilter,ImageTk

class ImageUtil:
    def __init__(self, path):
        self.path = path
        self.image = Image.open(path)

    def open(self):
        self.image.show()

    def crop(self, x, y):

        try:
            val = (int(x), int(y))
            self.image.thumbnail(val)
            self.image.save(self.path)
            return True
        except ValueError:
            return False

    def rotate(self, angle):
        try:
            val = int(angle)
            self.image.rotate(val).save(self.path)
            return True
        except ValueError:
            return False

    def blur(self, radius):
        try:
            val = int(radius)
            self.image.filter(ImageFilter.GaussianBlur(radius=val)).save(self.path)
            return True
        except ValueError:
            return False

    def change_brightness(self, val):
        try:
            val = float(val)
            enhancer = ImageEnhance.Brightness(self.image)
            enhancer.enhance(val).save(self.path)
            return True
        except ValueError:
            return False

    def change_sharpness(self, val):
        try:
            val = float(val)
            enhancer = ImageEnhance.Sharpness(self.image)
            enhancer.enhance(val).save(self.path)
            return True
        except ValueError:
            return False

    def change_color(self, val):
        try:
            val = float(val)
            enhancer = ImageEnhance.Color(self.image)
            enhancer.enhance(val).save(self.path)
            return True
        except ValueError:
            return False

    def change_contrast(self, val):
        try:
            val = float(val)
            mod = ImageEnhance.Contrast(self.image)
            mod.enhance(val).save(self.path)
            return True
        except ValueError:
            return False

class ImageEditorApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Editor")

        
        try:
            # Load a background image
            background_image = Image.open("e:\\userdata\\Desktop\\background.jpg")  # Replace with your image file path
            background_photo = ImageTk.PhotoImage(background_image)
            background_label = Label(master, image=background_photo)
            background_label.image = background_photo  # to prevent image from being garbage collected
            background_label.place(relwidth=1, relheight=1)

        except Exception as e:
            print(f"Error loading image: {e}")

       







        self.label = Label(master, text="Image Editor",bg="grey",fg="white",width=40,height=2)
        self.label.pack(pady=10)


        self.path_entry = Entry(master,width=30)
        self.path_entry.pack(pady=10)

        self.open_button = Button(master, text="Open/Show", command=self.open_image,bg="#4CAF50",fg='white',width=15,height=2)
        self.open_button.pack(pady=10)

        self.crop_button = Button(master, text="Resize/Crop", command=self.crop_image,bg="#008CBA",fg='white',width=15,height=2)
        self.crop_button.pack(pady=10)

        self.rotate_button = Button(master, text="Adjust Rotation", command=self.rotate_image,bg="#FFC300",fg='white',width=15,height=2)
        self.rotate_button.pack(pady=10)

        self.blur_button = Button(master, text="Blur", command=self.blur_image,bg="#FF5733",fg='white',width=15,height=2)
        self.blur_button.pack(pady=10)

        self.brightness_button = Button(master, text="Adjust Brightness", command=self.adjust_brightness,bg="#900C3F",fg='white',width=15,height=2)
        self.brightness_button.pack(pady=10)

        self.sharpness_button = Button(master, text="Adjust Sharpness", command=self.adjust_sharpness,bg="#5E2D79",fg='white',width=15,height=2)
        self.sharpness_button.pack(pady=10)

        self.color_button = Button(master, text="Adjust Color", command=self.adjust_color,bg="#4CAF52",fg='white',width=15,height=2)
        self.color_button.pack(pady=10)

        self.contrast_button = Button(master, text="Adjust Contrast", command=self.adjust_contrast,bg="#4CAE30",fg='white',width=15,height=2)
        self.contrast_button.pack(pady=10)

    def open_image(self):
        path = self.path_entry.get()
        image = ImageUtil(path)
        image.open()
#crop-------------------------------------------------------
    def crop_image(self):
        path = self.path_entry.get()
        image = ImageUtil(path)
       
        try:
                input_str=simpledialog.askstring("Crop","(X,Y):")
                if input_str is not None:  # Check if the user canceled the input
                 coordinates = list(map(int, input_str.split(',')))
                
                # Check if there are enough values to unpack
                 if len(coordinates) == 2:
                    x, y = coordinates
                    image.crop(x, y)
                 else:
                    print("Invalid input: Please provide two values separated by a comma.")
                else:
                 print("Operation canceled.")
        except ValueError:
            print("Invalid input. Please enter integers for (X,Y).")
   #rotate ----------------------------------------    
    def rotate_image(self):
       path = self.path_entry.get()
       image = ImageUtil(path)

       try:
            # Use simpledialog.askstring to get input from the user
            angle_str = simpledialog.askstring("Rotate", "Angle:")
            
            if angle_str is not None:  # Check if the user canceled the input
                angle = int(angle_str)
                image.rotate(angle)
            else:
                print("Operation canceled.")
       except ValueError:
            print("Invalid input. Please enter an integer for the angle.")
# blur image--------------------------------
    def blur_image(self):
        path = self.path_entry.get()
        image = ImageUtil(path)

        try:
            # Use simpledialog.askstring to get input from the user
            radius_str = simpledialog.askstring("Blur", "Radius:")
            
            if radius_str is not None:  # Check if the user canceled the input
                radius = int(radius_str)
                image.blur(radius)
            else:
                print("Operation canceled.")
        except ValueError:
            print("Invalid input. Please enter an integer for the radius.")

#brightness --------------------------
    def adjust_brightness(self):
        path = self.path_entry.get()
        image = ImageUtil(path)

        try:
            # Use simpledialog.askfloat to get input from the user
            val = simpledialog.askfloat("Brightness", "Enter Brightness (between 0.0 and 2.0):", minvalue=0.0, maxvalue=5.0)
            
            if val is not None:  # Check if the user canceled the input
                image.change_brightness(val)
            else:
                print("Operation canceled.")
        except (ValueError, TypeError):
            print("Invalid input. Please enter a numeric value for brightness.")

#sharpness-------------------------
    def adjust_sharpness(self):
        path = self.path_entry.get()
        image = ImageUtil(path)

        try:
            # Use simpledialog.askfloat to get input from the user
            val = simpledialog.askfloat("Sharpness", "Enter Sharpness (between 0.0 and 2.0):", minvalue=0.0, maxvalue=5.0)
            
            if val is not None:  # Check if the user canceled the input
                image.change_sharpness(val)
            else:
                print("Operation canceled.")
        except (ValueError, TypeError):
            print("Invalid input. Please enter a numeric value for sharpness.")

            #color------------------------------
    def adjust_color(self):
       path = self.path_entry.get()
       image = ImageUtil(path)

       try:
            # Use simpledialog.askfloat to get input from the user
            val = simpledialog.askfloat("Color", "Enter Color (between 0.0 and 2.0):", minvalue=0.0, maxvalue=5.0)
            
            if val is not None:  # Check if the user canceled the input
                image.chage_color(val)  # Note: Fix the method name from chage_color to change_color
            else:
                print("Operation canceled.")
       except (ValueError, TypeError):
            print("Invalid input")

            #contrast--------------------------------------

    def adjust_contrast(self):
        path = self.path_entry.get()
        image = ImageUtil(path)

        try:
            # Use simpledialog.askfloat to get input from the user
            val = simpledialog.askfloat("Contrast", "Enter Contrast (between 0.0 and 2.0):", minvalue=0.0, maxvalue=5.0)
            
            if val is not None:  # Check if the user canceled the input
                image.change_contrast(val)
            else:
                print("Operation canceled.")
        except (ValueError, TypeError):
            print("Invalid input. Please enter a numeric value for contrast.")

root = Tk()
app = ImageEditorApp(root)
root.mainloop()