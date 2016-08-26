class log_parser():
    def __init__(self, filenames=[]):
        self.filenames = filenames

    def parse(self):
        for filename in self.filenames:
            file = open(filename, 'r', encoding='UTF-8')
            while True:
                line = file.readline()
                if not line:
                    break
            file.close()