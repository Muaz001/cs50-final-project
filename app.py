# Importing Tkinter modules
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
# Importing other .py files
from similar_faces import similar
from duplicate import duplicate
from organise import organise

face = ""
source = ""
destination = ""

def duplicate_func(source_folder, destination_folder, find_button):
    global source                                                                # global tells python to use the global variable of source not local
    global destination

    if source_folder == 1:
         source = filedialog.askdirectory()
    if destination_folder == 1:
         destination = filedialog.askdirectory()
    source_images_folder = source
    destination_images_folder = destination

    if find_button == 1:
        if source_images_folder and destination_images_folder:                                          # Checks if both folders provided, run the duplicate function
            duplicate(source_images_folder, destination_images_folder)


def organise_func(source_folder, destination_folder, organise_button):
    global source
    global destination

    if source_folder == 1:
        source = filedialog.askdirectory()
    if destination_folder == 1:
        destination = filedialog.askdirectory()
    source_images_folder = source
    destination_images_folder = destination

    if organise_button == 1:
        if source_images_folder and destination_images_folder:
            organise(source_images_folder, destination_images_folder)


def similar_func(face_file, source_folder, destination_folder, find_button):
    global face
    global source
    global destination

    if face_file == 1:
        face = filedialog.askopenfilename()
    if source_folder == 1:
        source = filedialog.askdirectory()
    if destination_folder == 1:
        destination = filedialog.askdirectory()
    face_image = face
    source_images_folder = source
    destination_images_folder = destination

    if find_button == 1:
        if face_image and source_images_folder and destination_images_folder:
            similar(face_image, source_images_folder, destination_images_folder)


def duplicate_window():
    # Making window for duplicate
    duplicate_window = Toplevel(root)
    duplicate_window.title("Find Duplicates")
    mainframe = ttk.Frame(duplicate_window, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, S, W, E))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    # Adding labels and other stuff
    ttk.Label(mainframe,
              text="By providing a folder containing images, this will find all the duplicate images and store them side by side in a seperate folder."
              ).grid(column=1, row=1, sticky=(W, E))

    ttk.Button(mainframe, text="Get the images folder", command=lambda: duplicate_func(1, 0, 0)).grid(column=1, row=2, sticky=(W, E))
    ttk.Button(mainframe, text="Select the destination folder (where images will be stored)", command=lambda: duplicate_func(0, 1, 0)).grid(column=1, row=3, sticky=(W, E))
    ttk.Button(mainframe, text="Start", command=lambda: duplicate_func(0, 0, 1)).grid(column=1, row=4, sticky=(W, E))

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)



def organise_window():
    # Making window for organise
    organise_window = Toplevel(root)
    organise_window.title("Organise Images")
    mainframe = ttk.Frame(organise_window, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, S, W, E))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    # Adding labels and other stuff
    ttk.Label(mainframe, text="By providing a folder containing images, this will automatically sort out images with faces from other images. Storing them in a seperate folder."
              ).grid(column=1, row=1, sticky=(W, E))
    ttk.Label(mainframe, text="(Note: The face recognition mechansims don't work very well with rotated images or images with filters. It's better to provide non-rotated and unfiltered images.)"
              ).grid(column=1, row=2, sticky=(W, E))

    ttk.Button(mainframe, text="Get the images folder", command=lambda: organise_func(1, 0, 0)).grid(column=1, row=3, sticky=(W ,E))
    ttk.Button(mainframe, text="Select the destination folder (where images will be stored)", command=lambda:organise_func(0, 1, 0)).grid(column=1, row=4, sticky=(W, E))
    ttk.Button(mainframe, text="Start", command=lambda: organise_func(0, 0, 1)).grid(column=1, row=5, sticky=(W ,E))

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)


def similar_window():
    # Making window for organise
    similar_window = Toplevel(root)
    similar_window.title("Find Same Faces")
    mainframe = ttk.Frame(similar_window, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, S, W, E))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    # Adding labels and oter stuff
    ttk.Label(mainframe, text="By providing an image with a face/faces, this will find all the pictures in a folder, which have that same face/faces, and automatically store them in a seperate folder."
              ).grid(column=1, row=1, sticky=(W, E))
    ttk.Label(mainframe, text="(Note: The face recognition mechanisms don't work very well with rotated images or images with filters. It's better to provide non-rotated and unfiltered images.)"
              ).grid(column=1, row=2, sticky=(W, E))
 
    ttk.Button(mainframe, text="Get the reference picture", command=lambda: similar_func(1, 0, 0, 0)).grid(column=1, row=3, sticky=(W, E))
    ttk.Button(mainframe, text="Get the folder of images to check", command=lambda: similar_func(0, 1, 0, 0)).grid(column=1, row=4, sticky=(W, E))
    ttk.Button(mainframe, text="Select the destination folder (where images will be stored)", command=lambda: similar_func(0, 0, 1, 0)).grid(column=1, row=5, sticky=(W, E))
    ttk.Button(mainframe, text="Start", command=lambda: similar_func(0, 0, 0, 1)).grid(column=1, row=6, sticky=(W, E))

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)


# Making the main application window
root = Tk()
root.title("Face Match")

# Making the main frame inside the main window
mainframe = ttk.Frame(root, padding="50 50 50 50 ")
mainframe.grid(column=0, row=0, sticky=(N, S, W, E))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Adding labels as headings, corresponding widgets and descriptions
ttk.Label(mainframe, text="   Find photos with look-alike faces!").grid(column=1, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Find similar faces", command=similar_window).grid(column=1, row=1, sticky=(W, E))

ttk.Label(mainframe, text="           Find duplicate photos").grid(column=1, row=4, sticky=(W, E))
ttk.Button(mainframe, text="Find duplicates", command=duplicate_window).grid(column=1, row=3, sticky=(W, E))

ttk.Label(mainframe, text="Organise your photos automatically!").grid(column=1, row=6, sticky=(W, E))
ttk.Button(mainframe, text="Organise", command=organise_window).grid(column=1, row=5, sticky=(E, W))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
