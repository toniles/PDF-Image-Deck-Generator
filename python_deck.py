from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os
import random

# Pide al usuario la ruta de la carpeta con las imágenes
ruta_carpeta = input("Introduce la ruta de la carpeta con las imágenes: ")

# Lista para almacenar las imágenes
imagenes = []

# Recorre los archivos en la carpeta
for archivo in os.listdir(ruta_carpeta):
    if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
        img_path = os.path.join(ruta_carpeta, archivo)
        imagenes.append(img_path)

# Verifica si se han encontrado imágenes
if len(imagenes) == 0:
    print("No se han encontrado imágenes en la carpeta especificada.")
else:
    # Crea un PDF
    c = canvas.Canvas("mazo_de_cartas.pdf", pagesize=A4)
    width, height = A4

    x = 0
    y = height

    celda_size = 200  # Tamaño de cada celda en el PDF

    for i, img_path in enumerate(imagenes):
        if i % 6 == 0:  # Nueva página cada 6 imágenes
            if i != 0:
                c.showPage()
            x = 0
            y = height - celda_size

        img = Image.open(img_path).convert("RGBA")  # Convierte la imagen a RGBA
        img = img.resize((celda_size, celda_size), Image.LANCZOS)

        # Fondo blanco para imágenes con transparencia
        img_w, img_h = img.size
        fondo = Image.new("RGBA", (img_w, img_h), "white")
        img = Image.alpha_composite(fondo, img)
        img = img.convert("RGB")

        # Añade un borde negro a la imagen
        draw = ImageDraw.Draw(img)
        draw.rectangle([(0, 0), (celda_size, celda_size)], outline="black", width=2)

        # Añade un número aleatorio con fondo negro
        numero_aleatorio = f" {random.randint(1, 9)} "  # Espacios añadidos alrededor del número
        font = ImageFont.load_default()
        text_bbox = draw.textbbox((0, 0), numero_aleatorio, font=font)
        text_w = text_bbox[2] - text_bbox[0]
        text_h = text_bbox[3] - text_bbox[1]


        
        # Posiciones para centrar el texto
        rect_x1 = 95
        rect_y1 = 185
        rect_x2 = 105
        rect_y2 = 195
        text_x = rect_x1 + (rect_x2 - rect_x1 - text_w) // 2
        text_y = rect_y1 + (rect_y2 - rect_y1 - text_h) // 2

        draw.rectangle([(rect_x1, rect_y1), (rect_x2, rect_y2)], fill="black")
        draw.text((text_x, text_y), numero_aleatorio, font=font, fill="white")

        # Guarda la imagen temporalmente como JPEG
        temp_img_path = f"temp_{i}.jpg"
        img.save(temp_img_path, "JPEG")

        # Dibuja la imagen en el PDF
        c.drawImage(temp_img_path, x, y - celda_size, width=celda_size, height=celda_size)

        # Elimina la imagen temporal
        os.remove(temp_img_path)

        # Actualiza las coordenadas para la próxima imagen
        x += celda_size
        if x >= width:
            x = 0
            y -= celda_size

    c.save()
    print("PDF generado exitosamente.")
