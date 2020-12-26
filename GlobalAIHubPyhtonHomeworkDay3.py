import random
import time

def take_word():
    words = random.choice(["big", "data", "artificial", "intelligence",
                            "fantastic", "top","python","code"])
    words = words.upper()
    return words

def play(words):
    yerTutucu = "-" * len(words)
    tahmin = False
    tahminHarf = []
    tahminKelime = []
    deneme = 6
    print(durum(deneme))
    print("#"*(len(words)+4))
    print(f"# {yerTutucu} #")
    print("#"*(len(words)+4))
    print("\n")
    while not tahmin and deneme > 0:
        kullaniciTahmin = input("Guess a letter or write the word if you found it:").upper()
        if len(kullaniciTahmin) == 1 and kullaniciTahmin.isalpha():
            if kullaniciTahmin in tahminHarf:
                print("You already guessed this letter", kullaniciTahmin)
            elif kullaniciTahmin not in words:
                print(kullaniciTahmin, "no letter")
                deneme -= 1
                tahminHarf.append(kullaniciTahmin)
            else:
                print("Congratulations!", kullaniciTahmin, "has letter.")
                tahminHarf.append(kullaniciTahmin)
                kelimeSoruListele = list(yerTutucu)
                endeksler = [i for i, harf in enumerate(words) if harf == kullaniciTahmin]
                for akif in endeksler:
                    kelimeSoruListele[akif] = kullaniciTahmin
                yerTutucu = "".join(kelimeSoruListele)
                if "-" not in yerTutucu:
                    tahmin = True
        elif len(kullaniciTahmin) == len(words) and kullaniciTahmin.isalpha():
            if kullaniciTahmin in tahminKelime:
                print(kullaniciTahmin, "you guessed the word", )
            elif kullaniciTahmin != words:
                print(kullaniciTahmin, "not the word")
                deneme -= 1
                tahminKelime.append(kullaniciTahmin)
            else:
                tahmin = True
                yerTutucu = words
        else:
            print("not a valid guess!")
        print(durum(deneme))
        print("#"*(len(words)+4))
        print(f"# {yerTutucu} #")
        print("#"*(len(words)+4))
        print("\n")
    if tahmin:
        print("CONGRATULATIONS! You found the word.")
    else:
        print(f"Sorry :( Your rights ran out and you couldn't find the word. The word would be {words}.")

def durum(deneme):
    sahne = ["""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
--------""","""

   +---+
   |   |
   O   |
  /|   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
   |   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
       |
       |
       |
--------""","""
   +---+
   |   |
       |
       |
       |
       |
--------"""]
    return sahne[deneme]

def main():
    print("Welcome to Hangman Game. \nEnter Your Name: ")
    kullanici=input("")
    print(f"WELCOME {kullanici}")
    words = take_word()
    play(words)

if __name__ == "__main__":
    main()
    exit()
