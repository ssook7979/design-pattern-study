class Bitmap:
    def __init__(self, filename) -> None:
        self.filename = filename
        print(f'Loading image from {self.filename}') #some code for loading image

    def draw(self):
        print(f'Drawing image {self.filename}')

# lazily load image
class LazyBitmap:
    def __init__(self, filename) -> None:
        self.filename = filename
        self._bitmap = None
    
    def draw(self):
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()

def draw_image(image):
    print('About to draw image')
    image.draw()
    print('Done drawing image')

if __name__ == '__main__':
    # bmp = Bitmap('example.jgp')
    # will draw after some work done. no need to loading early for economical memory usage
    # Say, editting Bitmap class is too expensive 
    # then a proxy class(LazyBitmap) that implements Bitmap interface would be useful..
    bmp = LazyBitmap('example.jgp')