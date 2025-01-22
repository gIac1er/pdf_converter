import sys
from PIL import Image

# higher quality pdf, uses dpi and quality value, tried to make output file size reasonable
def images_to_pdf(images, output_pdf="output.pdf"):
    dpi = 200
    quality = 50
    converted_images = []

    for image in images:
        ext = image.lower().split('.')[-1]

        if ext in ["jpg", "jpeg", "png"]:
            img = Image.open(image).convert("RGB")
            width, height = img.size
            new_width = int(width * (dpi / 72))
            new_height = int(height * (dpi / 72))
            img = img.resize((new_width, new_height), Image.LANCZOS)
            converted_images.append(img)

    converted_images[0].save(
        output_pdf, save_all=True, append_images=converted_images[1:],
        quality=quality, dpi=(dpi, dpi)
    )
    print(f"PDF saved as: {output_pdf}")
        
        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python images_to_pdf.py file_paths")
    else:
        images_to_pdf(sys.argv[1:])
