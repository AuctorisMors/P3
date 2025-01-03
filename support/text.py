from collections import namedtuple

class Text:
    lang = None
    def set_lang(self, lang):
        self.lang = lang
    def get_lang(self):
        return self.lang
    Paragraph = namedtuple("Paragraph", ["Style", "Width", "Type"])

    def print(n, char, width, bType=None):
        boxType = bType if bType else "box"
        n = str(n)
        paragraphs = n.split(" ")
        line = [""]
        lineCount = charCount = 0

        print('\n\033[31m' + char * width + '\033[0m')
        if boxType in ["box", "3col"]:
            colCount = 0
            for word in paragraphs:
                if charCount + len(word) < width - 3 and (boxType == "box" or colCount < 3):
                    charCount += len(word) + 1
                    line[lineCount] += word + " "
                    colCount += 1 if boxType == "3col" else 0
                else:
                    colCount = 1 if boxType == "3col" else 0
                    lineCount += 1
                    charCount = len(word) + 1
                    line.append(word + " ")
        else:
            print("Error: Invalid box type")
            return

        for l in line:
            print(char + " " + l.center(width - 3) + char)
        print('\033[31m' + char * width + '\033[0m')

    def prompt():
        lang = Text.get_lang(Text)
        while True:
            try:
                _ans = input(lang['yon']).strip().lower()
                if _ans in ["y", "yes"]:
                    return True
                elif _ans in ["n", "no"]:
                    return False
                else:
                    print(lang['not-valid'])
            except:
                print(lang['not-valid'])

    def request(choices):
        lang = Text.get_lang(Text)
        choices = [choice.lower() for choice in choices]
        while True:
            try:
                _ans = input('$> ').strip().lower()
                if _ans in choices:
                    return _ans
                else:
                    print(lang['request'] + str(choices))
            except:
                print(lang['request'] + str(choices))
