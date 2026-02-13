import re

class VATCleaner:
    def __init__(self):
        self.remove_extra_whitespace = re.compile(r'\s+')
        self.remove_special_chars = re.compile(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?~`]'")
        self.leading_whitespace = re.compile(r'^\s+')
        self.dashes = re.compile(r'-\s*')
        self.commas = re.compile(r',')


    def extra_whitespace(self, text):
        return self.remove_extra_whitespace.sub(' ', text)


    def special_chars(self, text):
        return self.remove_special_chars.sub('', text)


    def leading(self, text):
        return self.leading_whitespace.sub('', text)


    def dash(self, text):
        return self.dashes.sub('', text)


    def comma(self,text):
        return self.commas.sub('', text)