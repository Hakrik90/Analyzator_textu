#Když se dvě a více slov skládájí ze stejných znaků, které mají ale různé pořadí, říkame jim anagramy. Anagram určitého slova nebo fráze může vytvořit jiné slovo nebo frázi. Takže například anglické slovo 'eat' má v angličtině následující anagramy:
#ate
#tea
#Cílem tohoto cvičení je vytvořit funkci, která příjímá list dvou nebo více stringů jako vstup a vrací boolean hodnotu, která nám říká, jestli všechny prvky uvnitř listu jsou anagramy, nebo ne.

#Pokud vložíme prázdný string, výstup by měl být False.
#Pokud vložíme list s jedním slovem, výstup by měl být True.

def all_anagrams(words):
    if words is False:
        return False
    sample = sorted(words.pop())
    for word in words:
        if word is False:
            return True
        elif sorted(word) == sample:
            return True
        else:
            return False

#Vzorové řešení
def all_anagrams2(words):
    if words:
        result = True
        seq= sorted(words.pop())
        for word in words:
            if sorted(word) != seq:
                result = False
            else:
                result = True
    else:
        result = False
    return result
# Slova
words = ['ship','hips','name']
# Volani fce
print(all_anagrams(words))

