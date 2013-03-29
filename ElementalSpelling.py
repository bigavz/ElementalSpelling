elements = {
    'Ac': 'Actinium',
    'Ag': 'Silver',
    'Al': 'Aluminum',
    'Am': 'Americium',
    'Ar': 'Argon',
    'As': 'Arsenic',
    'At': 'Astatine',
    'Au': 'Gold',
    'B': 'Boron',
    'Ba': 'Barium',
    'Be': 'Beryllium',
    'Bh': 'Bohrium',
    'Bi': 'Bismuth',
    'Bk': 'Berkelium',
    'Br': 'Bromine',
    'C': 'Carbon',
    'Ca': 'Calcium',
    'Cd': 'Cadmium',
    'Ce': 'Cerium',
    'Cf': 'Californium',
    'Cl': 'Chlorine',
    'Cm': 'Curium',
    'Cn': 'Copernicium',
    'Co': 'Cobalt',
    'Cr': 'Chromium',
    'Cs': 'Cesium',
    'Cu': 'Copper',
    'Db': 'Dubnium',
    'Ds': 'Darmstadtium',
    'Dy': 'Dysprosium',
    'Er': 'Erbium',
    'Es': 'Einsteinium',
    'Eu': 'Europium',
    'F': 'Fluorine',
    'Fe': 'Iron',
    'Fl': 'Flerovium',
    'Fm': 'Fermium',
    'Fr': 'Francium',
    'Ga': 'Gallium',
    'Gd': 'Gadolinium',
    'Ge': 'Germanium',
    'H': 'Hydrogen',
    'He': 'Helium',
    'Hf': 'Hafnium',
    'Hg': 'Mercury',
    'Ho': 'Holmium',
    'Hs': 'Hassium',
    'I': 'Iodine',
    'In': 'Indium',
    'Ir': 'Iridium',
    'K': 'Potassium',
    'Kr': 'Krypton',
    'La': 'Lanthanum',
    'Li': 'Lithium',
    'Lr': 'Lawrencium',
    'Lu': 'Lutetium',
    'Lv': 'Livermorium',
    'Md': 'Mendelevium',
    'Mg': 'Magnesium',
    'Mn': 'Manganese',
    'Mo': 'Molybdenum',
    'Mt': 'Meitnerium',
    'N': 'Nitrogen',
    'Na': 'Sodium',
    'Nb': 'Niobium',
    'Nd': 'Neodymium',
    'Ne': 'Neon',
    'Ni': 'Nickel',
    'No': 'Nobelium',
    'Np': 'Neptunium',
    'O': 'Oxygen',
    'Os': 'Osmium',
    'P': 'Phosphorus',
    'Pa': 'Protactinium',
    'Pb': 'Lead',
    'Pd': 'Palladium',
    'Pm': 'Promethium',
    'Po': 'Polonium',
    'Pr': 'Praseodymium',
    'Pt': 'Platinum',
    'Pu': 'Plutonium',
    'Ra': 'Radium',
    'Rb': 'Rubidium',
    'Re': 'Rhenium',
    'Rf': 'Rutherfordium',
    'Rg': 'Roentgenium',
    'Rh': 'Rhodium',
    'Rn': 'Radon',
    'Ru': 'Ruthenium',
    'S': 'Sulfur',
    'Sb': 'Antimony',
    'Sc': 'Scandium',
    'Se': 'Selenium',
    'Sg': 'Seaborgium',
    'Si': 'Silicon',
    'Sm': 'Samarium',
    'Sn': 'Tin',
    'Sr': 'Strontium',
    'Ta': 'Tantalum',
    'Tb': 'Terbium',
    'Tc': 'Technetium',
    'Te': 'Tellurium',
    'Th': 'Thorium',
    'Ti': 'Titanium',
    'Tl': 'Thallium',
    'Tm': 'Thulium',
    'U': 'Uranium',
    'V': 'Vanadium',
    'W': 'Tungsten',
    'Xe': 'Xenon',
    'Y': 'Yttrium',
    'Yb': 'Ytterbium',
    'Zn': 'Zinc',
    'Zr': 'Zirconium'
}


# kesti logic
# check first letter, then first two letters
def canSpell(word, spelling):
    if len(word) > 0:
        l = list(word)
        l[0] = l[0].upper()
        word = "".join(l)
        # base case
        if elements.get(word):
            spelling.append(word + ": " + elements[word])
            print('\n'.join(spelling))
        else:
            if elements.get(word[:2]):
                spelling.append(word[:2] + ": " + elements[word[:2]])
                canSpell(word[2:], spelling)
            elif elements.get(word[:1]):
                spelling.append(word[:1] + ": " + elements[word[:1]])
                canSpell(word[1:], spelling)
            else:
                print("can't spell this word using elements.")
    else:
        return


def main():
    # keep it compatible for python 2 and 3
    try:
        input = raw_input
    except NameError:
        pass

    print("Enter the word you would like to be spelled, or type 'q' to quit:")
    word = input(">>")

    while word != 'q':
        canSpell(word, [])
        print('------')
        aspell(word)
        word = input(">>")


def aspell(word):
    word = word[0].upper() + word[1:] #uppercase first character

    if len(word) == 1:
        if elements.get(word) == True:
            return elements[word]
        else:
            return False
    if len(word) == 0:
        return ''

    if elements.get(word[0:1]) == False: #compare first 2 chars to symbols
        if elements.get(word[0]) == False: #compare first char to symbols
            return False
        else: #if len1 matches
            print(elements[word[0]] + aspell(word[1:]))
    else: #if len2 matches
        print(elements[word[0:1]] + aspell(word[2:]))


#different permutations of len(1) and len(2) symbols

    #if elements[word[i:i+1]] == True: #if the first two lettes match a symbol
    #    guesses.append(word[i:i+1],elements[word[i:i+1]])
    #if elements[word[i]] == True: #if the first letter matches a symbol
    #    guesses.append([word[i],elements[word[i]]])

main()
