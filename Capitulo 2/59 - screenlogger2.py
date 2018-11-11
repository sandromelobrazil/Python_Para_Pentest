from PIL import ImageGrab
import io

screenshot = io.BytesIO() #1
ImageGrab.grab().save(screenshot, "JPEG") #2

with open("imagem.jpg", "wb") as imagem: #3
    imagem.write( screenshot.getvalue() ) #4
    screenshot.close() #5