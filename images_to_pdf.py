import os
import sys
import img2pdf
from PIL import Image

def images_to_pdf(images, output_pdf="output.pdf"):
    converted_images = []
    
    for image in images:
        ext = image.lower().split('.')[-1]

        if ext in ["jpg", "jpeg", "png"]:
            img = Image.open(image).convert("RGB")
            converted_images.append(img)

    if converted_images:
        converted_images[0].save(output_pdf, save_all=True, append_images=converted_images[1:])
        print(f"PDF saved as: {output_pdf}")
    else:
        print("No valid images found to convert.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_to_pdf.py image1.jpg image2.png ...")
    else:
        images_to_pdf(sys.argv[1:])
