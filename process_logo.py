from PIL import Image

def make_transparent(image_path, output_path):
    img = Image.open(image_path)
    img = img.convert("RGBA")
    
    datas = img.getdata()
    
    newData = []
    for item in datas:
        # Detectar preto ou quase preto (R, G, B < 30)
        if item[0] < 30 and item[1] < 30 and item[2] < 30:
            newData.append((255, 255, 255, 0)) # Tornar transparente
        else:
            newData.append(item)
            
    img.putdata(newData)
    img.save(output_path, "PNG")

if __name__ == "__main__":
    make_transparent("logo.png", "logo_transparent.png")
