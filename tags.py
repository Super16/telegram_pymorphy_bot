"""Collections of tags from OpenCorpora 
(http://opencorpora.org/dict.php?act=gram) with normalized meaning to
reply"""

grammems = {"NOUN": "имя существительное",
            "ADJF": "полное имя прилагательное",
            "ADJS": "краткое имя прилагательное",
            "COMP": "компаратив",
            "VERB": "личная форма глагола",
            "INFN": "глагол (инфинитив)",
            "PRTF": "полное причастие",
            "PRTS": "краткое причастие",
            "GRND": "деепричастие",
            "NUMR": "числительное",
            "ADVB": "наречие",
            "NPRO": "местоимение-существительное",
            "PRED": "предикатив",
            "PREP": "предлог",
            "CONJ": "союз",
            "PRCL": "частица",
            "INTJ": "междометие",
            "nomn": "именительный падеж",
            "gent": "родительный падеж",
            "datv": "дательный падеж",
            "accs": "винительный падеж",
            "ablt": "творительный падеж",
            "loct": "предложный падеж",
            "voct": "звательный падеж",
            "gen2": "второй родительный (частичный) падеж",
            "acc2": "второй винительный падеж",
            "loc2": "второй предложный (местный) падеж",
            "sing": "единственное число",
            "plur": "множественное число",
            "masc": "мужской род",
            "femn": "женский род",
            "neut": "средний род",
            "Ms-f": "общий род",
            "Pltm": "парный род",
            "Sgtm": "только единственное число",
            "Fixd": "неизменяемое число",
            "Abbr": "аббревиатура",
            "Name": "имя",
            "Surn": "фамилия",
            "Patr": "отчество",
            "Geox": "топоним",
            "Supr": "превосходная степень",
            "Qual": "качественное",
            "Apro": "местоименное прилагательное",
            "Anum": "порядковое числительное",
            "Poss": "притяжательное",
            "perf": "совершенный вид",
            "impf": "несовершенный вид",
            "tran": "переходный",
            "intr": "непереходный",
            "Impe": "безличный",
            "Refl": "возвратный",
            "1per": "первое лицо",
            "2per": "второе лицо",
            "3per": "третье лицо",
            "pres": "настоящее время",
            "past": "прошедшее время",
            "futr": "будущее время",
            "indc": "изъявительное наклонение",
            "impr": "повелительное наклонение",
            "actv": "действительный залог",
            "pssv": "страдательный залог",
            "Infr": "разговорное",
            "Slng": "жаргонное",
            "Arch": "устаревшее",
            "Litr": "литературный вариант",
            "Erro": "опечатка",
            "Dist": "искажение",
            }

# Words with unacceptable tags are not analysed

unacceptable = ("LATN", "PNCT", "NUMB", "NUMB,intg", "NUMB,real", 
                "ROMN", "UNKN")

# Methods of analogy analysis

analogies = ("<KnownPrefixAnalyzer>", 
             "<KnownSuffixAnalyzer>", 
             "<FakeDictionary>", 
             "<UnknownPrefixAnalyzer>",
             "<HyphenAdverbAnalyzer>", 
             "<HyphenSeparatedParticleAnalyzer>", 
             "<HyphenatedWordsAnalyzer>")