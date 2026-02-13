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
        self.pattern_H = re.compile(r"[ḢḤḦḨĤȞƕhḣḥḧḩĥȟɦħ]")
        self.pattern_I = re.compile(r"[ÌÍÎÏĨĪĬĮİǏƗỊỈȈȊiìíîïĩīĭįıǐịỉȉȋɨ]")
        self.pattern_k = re.compile(r"[ḰḲḴƘǨkḱḳḵƙǩ]")
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


        def a(self, text):
            return self.pattern_A.sub('a',text)

        def b(self, text):
            return self.pattern_A.sub('b', text)

        def c(self, text):
            return self.pattern_A.sub('c', text)

        def d(self, text):
            return self.pattern_A.sub('d', text)

        def e(self, text):
            return self.pattern_A.sub('e', text)

        def f(self, text):
            return self.pattern_A.sub('f', text)

        def g(self, text):
            return self.pattern_A.sub('g', text)

        def h(self, text):
            return self.pattern_A.sub('h', text)

        def i(self, text):
            return self.pattern_A.sub('i', text)

        def j(self, text):
            return self.pattern_A.sub('j', text)

        def k(self, text):
            return self.pattern_A.sub('k', text)

        def l(self, text):
            return self.pattern_A.sub('l', text)

        def m(self, text):
            return self.pattern_A.sub('m', text)

        def n(self, text):
            return self.pattern_A.sub('n', text)

        def o(self, text):
            return self.pattern_A.sub('o', text)

        def p(self, text):
            return self.pattern_A.sub('p', text)

        def q(self, text):
            return self.pattern_A.sub('q', text)

        def r(self, text):
            return self.pattern_A.sub('r', text)

        def s(self, text):
            return self.pattern_A.sub('s', text)

        def t(self, text):
            return self.pattern_A.sub('t', text)

        def u(self, text):
            return self.pattern_A.sub('u',text)

        def v(self, text):
            return self.pattern_A.sub('v',text)

        def w(self, text):
            return self.pattern_A.sub('w',text)

        def x(self, text):
            return self.pattern_A.sub('x',text)

        def y(self, text):
            return self.pattern_A.sub('y',text)

        def z(self, text):
            return self.pattern_A.sub('z',text)


        def special(self, text):
            return self.special_char.sub('',text)











