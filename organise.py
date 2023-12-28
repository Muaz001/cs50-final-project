import face_recognition
import os
import shutil


def organise(source_images_folder, destination_images_folder):
    images = os.listdir(source_images_folder)                                      # This will return a list of names of the things in the directory

    # Load all the images in the program 1 by 1 and then storing them accordingly
    for each in images:
        image = face_recognition.load_image_file(f"{source_images_folder}/{each}")

        # Getting the number of faces in each pic
        faces = face_recognition.face_locations(image)
        no_of_faces = len(faces)

        # Making new folders to store the 2 types of images
        if not os.path.isdir(f"{destination_images_folder}/Organised pics"):
            os.mkdir(f"{destination_images_folder}/Organised Pics")

        face_folder = f"{destination_images_folder}/Organised Pics/Images with faces"
        other_folder = f"{destination_images_folder}/Organised Pics/Images without faces"
        if not os.path.isdir(face_folder):                                         # Checking if folder exists, if not then making a new folder
            os.mkdir(face_folder)
        if not os.path.isdir(other_folder):
            os.mkdir(other_folder)

        # Saving faced and non faced pics in the folders
        if no_of_faces > 0:
            shutil.copyfile(f"{source_images_folder}/{each}", f"{face_folder}/{each}")         # shutil.copyfile(source_path, destination_path)
        elif no_of_faces == 0:
            shutil.copyfile(f"{source_images_folder}/{each}", f"{other_folder}/{each}")
