from art import tprint

def select_font():
    fonts = ["block", "banner", "standard", "avatar", "3d_diagonal"]
    print("Choose a police for your art ASCII :")
    for i, font in enumerate(fonts, start=1):
        print(f"{i}. {font}")

    choice = input("Enter the number of your font choice : ")
    return fonts[int(choice) - 1] if choice.isdigit() and 0 < int(choice) <= len(fonts) else fonts[0]

def main():
    s = input("Write something : ")
    font_choice = select_font()
    tprint(s, font=font_choice)

if __name__ == "__main__":
    main()
