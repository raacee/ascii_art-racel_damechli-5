# ascii_art-racel_damechli-5
# ASCII Art Console App using Python

This Python console application generates ASCII art from user-inputted text. It allows you to choose from various fonts and optionally apply colors to your ASCII art. Below are the instructions to set up and run the project.

## Setup

1. **Install Python:**
   - Make sure you have [Python](https://www.python.org/) installed on your machine.

2. **Install Required Package:**
   - Open your terminal or command prompt.
   - Run the following command to install the required 'art' package:
     ```bash
     pip install art
     ```

3. **Set Up Virtual Environment (Optional but Recommended):**
   - You can use a virtual environment to isolate project dependencies.
     - Using `venv`:
       ```bash
       python -m venv venv
       source venv/bin/activate
       ```
     - Using `poetry`:
       ```bash
       poetry install
       poetry shell
       ```

## Run the Application

After completing the setup, you can run the application by executing the following command in your terminal or command prompt:

```bash
python main.py

## How to Use

1. **Enter Text:**
   - Upon running the application, you will be prompted to enter a word or a sentence.

2. **Choose Font:**
   - You can choose a font for your ASCII art from options like "block," "banner," "standard," "avatar," and "3d_diagonal."

3. **Choose Color (Optional):**
   - You have the option to choose a color for your ASCII art. The available colors include "red," "green," "yellow," "blue," "magenta," "cyan," and "white."

4. **Review ASCII Art:**
   - The application will display the generated ASCII art based on your input, font choice, and color selection.

5. **Continue or Exit:**
   - After viewing the ASCII art, you can choose whether to continue using the application or exit.
     - To continue, type "yes."
     - To exit, type "no."

**Note:** Ensure that you enter a non-empty word or sentence when prompted. If the input is empty, the application will request valid input.

Feel free to experiment with different fonts and colors to create unique and visually appealing ASCII art!
