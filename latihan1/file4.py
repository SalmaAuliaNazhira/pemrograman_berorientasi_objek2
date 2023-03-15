class Novel:
    def __init__(self, title, writer):
        self.title = title
        self.writer = writer
    def info(self):
        print(f"Title: {self.title}\nWriter: {self.writer}")
novelA = Novel("Earth", "Tere Liye")
novelA.info()