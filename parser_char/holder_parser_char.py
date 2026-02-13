import re

class HolderNameCleaner:
    def __init__(self):
        self.pattern_A = re.compile(
                r"[ÀÁÂÃÄÅĀĂĄǍȀȂȦẠẢẤẦẨẪẬẮẰẲẴẶaàáâãäåāăąǎȁȃȧạảấầẩẫậắằẳẵặ]")
        self.pattern_B = re.compile(
                r"[BḂḄḆƁƂƄbḃḅḇƀƃ]")
        self.pattern_C = re.compile(r"[ĆĈĊČÇƇƆcćĉċčçƈɕ]")
        self.pattern_D = re.compile(r"[ḊḌḎĐƊƋdḋḍḏđɗɖ]")
        self.pattern_E = re.compile(r"[ÈÉÊËĒĔĖĘĚƎƐẸẺẼẾỀỂỄỆeèéêëēĕėęěəɛẹẻẽếềểễệ]")
        self.pattern_F = re.compile(r"[ḞƑfḟƒ]")
        self.pattern_G = re.compile(r"[ǴĞĠĢƓɠgǵğġģɠɡ]")
        self.pattern_J = re.compile(r"[ĴJjĵɉʝ]")
        self.pattern_H = re.compile(r"[ḢḤḦḨĤȞƕhḣḥḧḩĥȟɦħ]")
        self.pattern_I = re.compile(r"[ÌÍÎÏĨĪĬĮİǏƗỊỈȈȊiìíîïĩīĭįıǐịỉȉȋɨ]")
        self.pattern_K = re.compile(r"[ḰḲḴƘǨkḱḳḵƙǩ]")
        self.pattern_L = re.compile(r"[ĹĻĽĿŁƚlĺļľŀłɫɬ]")
        self.pattern_M = re.compile( r"[ḾṀṂmḿṁṃɱ]")
        self.pattern_N = re.compile(r"[ŃŅŇÑṄṆṈṊƝƞnńņňñṅṇṉṋɲ]")
        self.pattern_O = re.compile(r"[ÒÓÔÕÖŌŎŐƠǑǪǬƆỌỎỐỒỔỖỘỚỜỞỠỢoòóôõöōŏőơǒǫǭɔọỏốồổỗộớờởỡợ]")
        self.pattern_P = re.compile(r"[ṔṖƤpṕṗƥ]")
        self.pattern_Q = re.compile(r"[Ɋɋq]")
        self.pattern_R = re.compile(r"[ŔŖŘṘṚṜṞƦɌɍrŕŗřṙṛṝṟɽ]")
        self.pattern_S = re.compile(r"[ŚŜŞŠȘṠṢṤṦṨƧſsśŝşšșṡṣṥṧṩ]")
        self.pattern_T = re.compile(r"[ŢŤŦȚṪṬṮṰƬƮtţťŧțṫṭṯṱƭ]")
        self.pattern_U = re.compile(r"[ÙÚÛÜŨŪŬŮŰŲƯǓǕǗǙǛƱỤỦỨỪỬỮỰuùúûüũūŭůűųưǔǖǘǚǜƲụủứừửữự]")
        self.pattern_V = re.compile(r"[ṼṾƲvṽṿʋ]")
        self.pattern_W = re.compile(r"[ŴẀẂẄẆẈwŵẁẃẅẇẉ]")
        self.pattern_X = re.compile(r"[ẊẌxẋẍ]")
        self.pattern_Y = re.compile(r"[ÝŶŸƳỲỴỶỸyýÿŷƴỳỵỷỹ]")
        self.pattern_Z = re.compile(r"[ŹŻŽƵẐẒẔzźżžƶẑẓẕ]")
        self.special_char = re.compile(r"[!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~]")

        self.patterns = {
            'a': self.pattern_A, 'b': self.pattern_B, 'c': self.pattern_C,
            'd': self.pattern_D, 'e': self.pattern_E, 'f': self.pattern_F,
            'g': self.pattern_G, 'h': self.pattern_H, 'i': self.pattern_I,
            'j': self.pattern_J, 'k': self.pattern_K, 'l': self.pattern_L,
            'm': self.pattern_M, 'n': self.pattern_N, 'o': self.pattern_O,
            'p': self.pattern_P, 'q': self.pattern_Q, 'r': self.pattern_R,
            's': self.pattern_S, 't': self.pattern_T, 'u': self.pattern_U,
            'v': self.pattern_V, 'w': self.pattern_W, 'x': self.pattern_X,
            'y': self.pattern_Y, 'z': self.pattern_Z,
        }


    def clean_all(self, text):
        for replacement, pattern in self.patterns.items():
            text = pattern.sub(replacement, text)
        text = self.special_char.sub('', text)
        return text











