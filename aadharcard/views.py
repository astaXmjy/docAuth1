from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
import base64
import numpy as np
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Path to tesseract.exe
)
# Create your views here.


def extract(request):
    if request.method == "POST":
        try:
            image = request.FILES["imagefile"]
            # encode image to base64 string
            image_base64 = base64.b64encode(image.read()).decode("utf-8")
        except:
            messages.add_message(
                request, messages.ERROR, "No image selected or uploaded"
            )
            return render(request, "form.html")
        lang = request.POST["language"]
        img = np.array(Image.open(image))
        text = pytesseract.image_to_string(img, lang=lang)
        # return text to html
        return render(request, "form.html", {"ocr": text, "image": image_base64})

    return render(request, "form.html")
