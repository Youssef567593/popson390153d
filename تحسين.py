from PIL import Image, ImageEnhance

def تحسين_الصورة(المسار, الناتج):
    صورة = Image.open(المسار)
    توضيح = ImageEnhance.Sharpness(صورة)
    محسنة = توضيح.enhance(2.0)
    محسنة.save(الناتج)
