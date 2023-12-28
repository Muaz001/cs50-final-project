from PIL import Image
import imagehash
import os
import shutil


def duplicate(source_images_folder, destination_images_folder):

    # list of images to confirm the already identified images
    images_already_identified = []

    images = os.listdir(source_images_folder)                                                  # This will return a list of names of the things in the directory

    # loading in all images 1 by 1 as main images to check for matching images
    i = 1
    for each_main in images:
        if each_main in images_already_identified:
            continue                                                                           # Skips the current iteration

        main_image = Image.open(f"{source_images_folder}/{each_main}")
        # Generating hash for the main image
        main_hash = imagehash.phash(main_image)

        # Loading in all the images 1 by 1 to check against
        stored = False
        for each_other in images:
            if each_other != each_main:                                                        # j!=1 skips the main image so that we dont check against it
                other_image = Image.open(f"{source_images_folder}/{each_other}")
                # Generating hash for the other image
                other_hash = imagehash.phash(other_image)

                # Making a folder to store images
                if not os.path.isdir(f"{destination_images_folder}/Duplicates"):
                    os.mkdir(f"{destination_images_folder}/Duplicates")

                # Now comparing hashes and storing images
                number = 1
                if main_hash == other_hash:
                    shutil.copyfile(f"{source_images_folder}/{each_other}", f"{destination_images_folder}/Duplicates/pic{i}and_its{number}.jpg")
                    #other_image.save(f"{destination_images_folder}/pic{i}and_its{number}.jpg") # Stores all the identical images wihtin the j loop
                    stored = True
                    number += 1                                                                # Used {number} because main pic stored will be named pic{i}.jpg
                    images_already_identified.append(each_other)

        # Storing the single image of i loop with all the images in the j loop, if stored the identical image of j loop
        if stored == True:
            shutil.copyfile(f"{source_images_folder}/{each_main}", f"{destination_images_folder}/Duplicates/pic{i}.jpg")
            i += 1
