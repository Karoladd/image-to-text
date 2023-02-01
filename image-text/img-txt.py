import cv2
import pytesseract

#Imagem em Texto
img = cv2.imread("img1.jpg")
path = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = path + r"\tesseract.exe"
texto = pytesseract.image_to_string(img, lang="por")
print(texto)

#Texto em Notas
pathNotas = r"C:\Users\Karol\Desktop\python\image-text\note\note.txt"
#   w - novo    a - acrescentar
with open(pathNotas, 'a', encoding="utf=8") as f:
    # .lower() .upper() .title()
    f.write(texto + '\n')   