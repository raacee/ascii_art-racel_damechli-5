from art import text2art
import colorama

def select_font():
    fonts = ["block", "banner", "standard", "avatar", "3d_diagonal"]
    print("Choose a police for your art ASCII :")
    for i, font in enumerate(fonts, start=1):
        print(f"{i}. {font}")

    choice = input("Enter the number of your font choice : ")
    return fonts[int(choice) - 1] if choice.isdigit() and 0 < int(choice) <= len(fonts) else fonts[0]

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def select_color():
    colors = {
        "red": "31",
        "green": "32",
        "yellow": "33",
        "blue": "34",
        "magenta": "35",
        "cyan": "36",
        "white": "37"
    }
    
    print("Choose a color :")
    for color in colors:
        print(color)
    
    color_choice = input("Enter the name of the choosen color (let empty for no specific color) : ").lower()
    return colors.get(color_choice, "")


def main():
    colorama.init()

    while True:
        s = input("Write something : ")
        font_choice = select_font()
        color_code = select_color()
        ascii_art = text2art(s, font=font_choice)
        colored_ascii_art = color_text(ascii_art, color_code) if color_code else ascii_art
        print(colored_ascii_art)

        continue_choice = input("Do you want to continue? (yes/no) : ").lower()
        if continue_choice != "yes":
            break

if __name__ == "__main__":
    main()
