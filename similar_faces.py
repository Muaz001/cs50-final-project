import face_recognition
import os
import shutil
import numpy

def similar(face_image, source_images_folder, destination_images_folder):

    # Loading the reference picture to match with and getting its face encoding
    known_pic = face_recognition.load_image_file(face_image)
    # Getting the face encoding of the reference image
    no_of_people = len(face_recognition.face_locations(known_pic))
    if no_of_people == 1:
        known_encodings = face_recognition.face_encodings(known_pic)[0].reshape(1, -1) # Added .reshape to make it into a 2d numpy array because it was a 1d numpy array
    elif no_of_people > 1:
        known_encodings = face_recognition.face_encodings(known_pic)


    # Load the images 1 by 1 to check from, and cheking with them 1 by 1 (to save ram memory)
    images = os.listdir(source_images_folder)                                                  # This will return a list of names of the things in the directory
    for each in images:
        image = face_recognition.load_image_file(f"{source_images_folder}/{each}")

        # Getting the face encoding of each image
        no_of_faces = len(face_recognition.face_locations(image))
        if no_of_faces == 1:
            unknown_encodings = face_recognition.face_encodings(image)[0].reshape(1, -1) # Added .reshape to make it into a 2d numpy array because it was a 1d numpy array
        elif no_of_faces > 1:
            unknown_encodings = face_recognition.face_encodings(image)
        elif no_of_faces == 0:                                          # As in the case of an image of text and such
            continue                                                    # By using continue, the loop skips the current iteration

        # Making new folder to store images
        if not os.path.isdir(f"{destination_images_folder}/Images with same faces"):
            os.mkdir(f"{destination_images_folder}/Images with same faces")

        # Now checking and storing images
        results = face_recognition.compare_faces(known_encodings, unknown_encodings, tolerance=0.6)

        if True in results:
            shutil.copyfile(f"{source_images_folder}/{each}", f"{destination_images_folder}/Images with same faces/{each}")



