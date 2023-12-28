# Face Match
## Video Demo: https://youtu.be/a9JhqO9b8y4

### What Face Match does:
Face Match, as the name suggests, works with images (with faces) to automate certain day-to-day frustrating tasks. As of now, it has three main functions:

### Find similar faces:
By showing an image with a face, it will find all the images in a folder with the same face.

### Find duplicates:
By providing a folder of images, it will find all the duplicate images within that folder. (It works with images with faces, and other types of images too!)

### Organise your images:
By providing a folder of images, it will organise all the images inside that folder by separating images with a face/faces from other types of images. (Currently, it organises images only using this technique, but more advanced techniques will be added soon.)

#### (Note: The face_locations library doesn't work very well with rotated images or images with filters.It's better to provide non-rotated and unfiltered images.)

### Find Similar Faces:
By showing an image with a face and providing a folder (with images) to check from, it will look for all the images inside that folder, which have that same face. It then stores all the images in a folder named "Images with same faces" in the directory specified by you.

#### (Note: The face_locations library doesn't work very well with rotated images or images with filters.It's better to provide non-rotated and unfiltered images.)

When you open the app for the first time, it will show you three options: 1) Find similar faces, 2) Find duplicates, 3) Organise. Upon clicking the similar faces button, it will open another window showing the following options:

1) Get the reference picture
2) Get the folder of images to check
3) Select the destination folder (where images will be stored)
4) Start

By clicking on the first option, you can choose any image that contains a face. By clicking on the second option, you have to provide the application with a folder containing images. This is the folder that gets checked for finding any images with the same face. By clicking on the third option, you have to provide the application with a destination folder where all the images (with a matching face/faces) will be stored. By clicking on the fourth option, the application runs and starts storing images.

### Find Duplicates:
By providing a folder containing images, it will look for all the duplicates and stores them in a folder named "Duplicates" in the directory specified by you. This function works with all types of images, be it with faces or not. Upon clicking the Find duplicates button, it will open another window showing the following options:

1) Get the images folder
2) Select the destination folder (where images will be stored)
3) Start

By clicking on the first option, you have to provide the application with a folder containing images. This is the folder that gets checked for any duplicates. By clicking on the second option, you have to provide the application with a destination folder where all the duplicate images will be stored. The duplicate image will be stored as follows: pic1, pic1_and_its1, pic1_and_its2 pic1_and_its3. By clicking on the third option, the application runs and starts storing images

### Organise Your Images:
By providing a folder containing all sorts of images, it will look for images that contain a face/faces and separate them from other types of images. (Make sure the images you provide are not rotated) It then stores the images with a face/faces in a folder named "Images with faces" and other images in a folder named "Images without faces" in the directory specified by you. Upon clicking the organise button, it will open another window showing the following options:

1) Get the images folder
2) Select the destination folder (where images will be stored)
3) Start

By clicking on the first option, you have to provide the application with a folder containing images. This is the folder that gets checked for any images with a face/faces to separate them. By clicking on the second option, you have to provide the application with a destination folder where the two folders "Images with faces" and "Images without faces" are made, and the respective images are stored within each folder. By clicking on the third option, the application runs and starts organising images.

### How Face Match works:
The whole application is based upon 4 .py files namely: app.py, similar_face.py, duplicate.py, and organise.py.

The app.py file is the main file that makes everything run. It uses the Tkinter library for making the application GUI and also calls the other three .py files whenever a button is clicked to perform a certain function. It uses Tkinter buttons to call certain functions, which then call their respective .py files to run a certain task like: "Organise photos."

The similar_faces.py file contains all the code which runs the application's Find similar faces functionality. It uses the latest face_recognition library for detecting face locations in an image to count the number of faces, getting face encodings for each face found and then comparing each face encoding with all the images in a folder. It also uses the os library for making new folders and performing other such tasks and shutil library for copying images to a new folder.

The duplicate.py file contains all the code which runs the application's Find Duplicate functionality. It uses the imagehash library for getting image hashes for each image, and then compares it against hashes of all the images in a folder. It also uses the os library, shutil library, and the PIL library for making new folders, copying images, and opening images inside the code for hashing.

The organise.py file contains all the code which runs the application's Organise images functionality. Like similar_faces.py, it also uses the latest face_recognition library for detecting face locations in an image to count the number of faces, and then storing images accordingly. This file also uses the os and shutil library for making new folders and copying images.

### About the design:
Currently, the GUI and overall application design are intentionally kept as simple as possible. The primary goal was to ensure the application is bug-free and functions seamlessly based on its fundamental cool concept.
