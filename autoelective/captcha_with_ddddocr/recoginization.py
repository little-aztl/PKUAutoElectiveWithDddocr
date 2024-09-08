import ddddocr

class Recognizer():
    def __init__(self):
        self.ocr = ddddocr.DdddOcr()

    def recognize(self, image):
        assert isinstance(image, bytes)
        return self.ocr.classification(image)
    
if __name__ == "__main__":
    recognizer = Recognizer()
    with open("test_ddddocr/DrawServlet.jpeg", "rb") as f:
        image = f.read() 
    print(recognizer.recognize(image))