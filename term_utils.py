import os


def center_input(prompt):
    # Get the user input
    user_input = input(center_text(prompt))
    return user_input


def input_number(prompt):
    try:
        return int(center_input(prompt))
    except ValueError:
        print("Invalid input. Please enter a number.")


def center_text(text):
    # Split the text into lines
    lines = text.split("\n")

    # Calculate the width of the terminal
    terminal_width = os.get_terminal_size().columns

    # Create a list to store centered lines
    centered_lines = []

    for line in lines:
        # Calculate the number of spaces needed to center each line
        padding = (terminal_width - len(line)) // 2
        centered_lines.append(" " * padding + line)

    # Return the joined centered lines
    return "\n".join(centered_lines)


def clear_screen():
    # Check if the operating system is Windows or not
    if os.name == "nt":
        os.system("cls")  # For Windows
    else:
        os.system("clear")  # For Linux/Mac
