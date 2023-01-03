DEPXCODEDICT = {
				'A': '``',
				'B': '••`',
				'C': '(',
				'D': '×)',
				'E': '|}',
				'F': '°°=',
				'G': '•••',
				'H': '|-|',
				'I': '•|•',
				'J': '°°==°°',
				'K': '|<=',
				'L': '--__--',
				'M': '|-|-|',
				'N': ':)',
				'O': '):(',
				'P': ';(',
				'Q': '0`',
				'R': '&<',
				'S': '°=°',
				'T': '_|',
				'U': '¥o',
				'V': '✓°',
				'W': '$•',
				'X': '×',
                'Y': '>]',
                'Z': ':(',
                'a': '``',
				'b': '••`',
				'c': '(',
				'd': '×)',
				'e': '|}',
				'f': '°°=',
				'g': '•••',
				'h': '|-|',
				'i': '•|•',
				'j': '°°==°°',
				'k': '|<=',
				'l': '--__--',
				'm': '|-|-|',
				'n': ':)',
				'o': '):(',
				'p': ';(',
				'q': '0`',
				'r': '&<',
				's': '°=°',
				't': '_|',
				'u': '¥o',
				'v': '✓°',
				'w': '$•',
				'x': '×',
                'y': '>]',
                'z': ':(',
                '0': '_',
                '1': '_-', 
                '2': '••-',
                '3': '•••_',
                '4': ')/',
                '5': '\°',
                '6': '--_&',
                '7': '\×/',
                '8': '€•',
                '9': '••°°'
	}

DEPX_TO_ENGLISH = {}
for key, value in DEPXCODEDICT.items():
    DEPX_TO_ENGLISH[value] = key

class DepxTranslator:
	def __init__(self, message):
		self.message = message
	def english_to_depx(self):
		depx = []
		for char in self.message:
			if char in DEPXCODEDICT:
				depx.append(DEPXCODEDICT[char])
		return " ".join(depx)
	def depx_to_english(self):
		self.message = self.message.split(" ")
		english = []
		for code in self.message:
			if code in DEPX_TO_ENGLISH:
				english.append(DEPX_TO_ENGLISH[code])
		return " ".join(english)


#depx2 = DepxTranslator("hello world").english_to_depx()
print(depx2)

#depx = DepxTranslator("|-| |} --__-- --__-- ):( $• ):( &< --__-- ×)").depx_to_english()
print(depx)