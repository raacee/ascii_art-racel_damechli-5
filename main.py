from art import tprint, ART_FONTS

def select_font():
    print("Choisissez une police pour votre art ASCII :")
    for i, font in enumerate(ART_FONTS, start=1):
        print(f"{i}. {font}")
    
    choice = input("Entrez le numéro de votre choix de police : ")
    return ART_FONTS[int(choice) - 1] if choice.isdigit() and 0 < int(choice) <= len(ART_FONTS) else ART_FONTS[0]

def main():
    s = input("Write something : ")
    font_choice = select_font()
    tprint(s, font=font_choice)

if __name__ == "__main__":
    main()
