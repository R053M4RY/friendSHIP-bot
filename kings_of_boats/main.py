from PIL import Image
import pytesseract

# Read the image

#    Preprocessing of the Image
#    Text Localization
#    Character Segmentation
#    Character Recognition
#    Post Processing


# Parse the data - OSEF for now

def whoami():
    iam = "I Am Blue Ajah"
    return iam

if __name__ == "__main__":
    print("Hello World")
    print(whoami())
    image = "/home/smourre/Documents/Work/Projects/kings_of_boats/kings_of_boats/kc_test.jpg"
    print(pytesseract.image_to_string(Image.open(image)))
