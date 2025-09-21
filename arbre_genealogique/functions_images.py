import base64

def charger_image_base64(fichier_image):
    image_base64 = base64.b64encode(fichier_image.read()).decode('utf-8')
    return image_base64