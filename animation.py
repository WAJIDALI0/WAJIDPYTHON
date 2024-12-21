# # # # import time
# # # # import tkinter as tk
# # # #
# # # # # Initialize the main window
# # # # root = tk.Tk()
# # # # root.title("Welcome Wajid")
# # # # root.geometry("800x600")
# # # # root.configure(bg="black")
# # # #
# # # # # Colors and Fonts
# # # # FONT_LARGE = ("Helvetica", 48, "bold")
# # # # FONT_SMALL = ("Helvetica", 24, "italic")
# # # # TEXT_COLOR = "white"
# # # # HEART_COLOR = "red"
# # # #
# # # # # Create a canvas for animations
# # # # canvas = tk.Canvas(root, width=800, height=600, bg="black", highlightthickness=0)
# # # # canvas.pack()
# # # #
# # # #
# # # # def create_heart(x, y):
# # # #     size = 20
# # # #     return canvas.create_polygon(
# # # #         x, y,
# # # #         x - size, y - size,
# # # #         x - size * 2, y,
# # # #         x - size, y + size,
# # # #         x, y,
# # # #         fill=HEART_COLOR, outline="")
# # # #
# # # #
# # # # def animate_word(word, initial_positions, final_positions, delay=50):
# # # #     letters = {}
# # # #     hearts = []
# # # #
# # # #     # Create text objects at initial positions
# # # #     for i, letter in enumerate(word):
# # # #         x, y = initial_positions[i]
# # # #         letters[letter] = canvas.create_text(x, y, text=letter, font=FONT_LARGE, fill=TEXT_COLOR)
# # # #
# # # #     # Animation loop
# # # #     while any(
# # # #             canvas.coords(letters[letter]) != list(final_positions[i]) for i, letter in enumerate(word)
# # # #     ):
# # # #         for i, letter in enumerate(word):
# # # #             x, y = canvas.coords(letters[letter])
# # # #             target_x, target_y = final_positions[i]
# # # #
# # # #             # Move the letter towards the final position
# # # #             dx = 1 if x < target_x else -1 if x > target_x else 0
# # # #             dy = 1 if y < target_y else -1 if y > target_y else 0
# # # #             canvas.move(letters[letter], dx, dy)
# # # #
# # # #             # Create a heart if it reaches the position
# # # #             if dx == 0 and dy == 0 and letter not in hearts:
# # # #                 hearts.append(letter)
# # # #                 create_heart(target_x + 30, target_y - 30)
# # # #
# # # #         root.update()
# # # #         time.sleep(delay / 1000)
# # # #
# # # #
# # # # def main_animation():
# # # #     # Clear the canvas for new animation
# # # #     canvas.delete("all")
# # # #
# # # #     # Welcome Wajid Animation
# # # #     word1 = "WAJID"
# # # #     initial_positions1 = [(-100, 50), (900, 50), (-100, 500), (900, 500), (400, 700)]
# # # #     final_positions1 = [(100, 150), (200, 150), (300, 150), (400, 150), (500, 150)]
# # # #
# # # #     animate_word(word1, initial_positions1, final_positions1)
# # # #
# # # #     # Pause before next animation
# # # #     time.sleep(2)
# # # #
# # # #     # Happy Sajid Animation
# # # #     word2 = "HAPPY SAJID"
# # # #     initial_positions2 = [(-100, 50), (900, 50), (-100, 500), (900, 500), (400, 700),
# # # #                           (-100, 150), (900, 150), (-100, 300), (900, 300), (400, 900)]
# # # #     final_positions2 = [(100, 250), (200, 250), (300, 250), (400, 250), (500, 250),
# # # #                         (150, 350), (250, 350), (350, 350), (450, 350), (550, 350)]
# # # #
# # # #     animate_word(word2, initial_positions2, final_positions2)
# # # #
# # # #     # Final Static Display
# # # #     canvas.create_text(400, 300, text="WAJID", font=FONT_LARGE, fill=TEXT_COLOR)
# # # #     canvas.create_text(400, 400, text="HAPPY SAJID", font=FONT_LARGE, fill=TEXT_COLOR)
# # # #
# # # #
# # # # # Run the main animation
# # # # main_animation()
# # # #
# # # # # Keep the window open
# # # # root.mainloop()
# # # # ....................#
# # # import time
# # # import tkinter as tk
# # #
# # # # Initialize the main window
# # # root = tk.Tk()
# # # root.title("Welcome Wajid")
# # # root.geometry("800x600")
# # # root.configure(bg="black")
# # #
# # # # Colors and Fonts
# # # FONT_LARGE = ("Helvetica", 48, "bold")
# # # FONT_SMALL = ("Helvetica", 24, "italic")
# # # TEXT_COLOR = "white"
# # # HEART_COLOR = "red"
# # #
# # # # Create a canvas for animations
# # # canvas = tk.Canvas(root, width=800, height=600, bg="black", highlightthickness=0)
# # # canvas.pack()
# # #
# # #
# # # def create_heart(x, y):
# # #     size = 20
# # #     return canvas.create_polygon(
# # #         x, y,
# # #         x - size, y - size,
# # #         x - size * 2, y,
# # #         x - size, y + size,
# # #         x, y,
# # #         fill=HEART_COLOR, outline="")
# # #
# # #
# # # def animate_word(word, initial_positions, final_positions, delay=50):
# # #     letters = {}
# # #     hearts = []
# # #
# # #     # Create text objects at initial positions
# # #     for i, letter in enumerate(word):
# # #         x, y = initial_positions[i]
# # #         letters[letter] = canvas.create_text(x, y, text=letter, font=FONT_LARGE, fill=TEXT_COLOR)
# # #
# # #     # Animation loop
# # #     while any(
# # #             canvas.coords(letters[letter]) != list(final_positions[i]) for i, letter in enumerate(word)
# # #     ):
# # #         for i, letter in enumerate(word):
# # #             x, y = canvas.coords(letters[letter])
# # #             target_x, target_y = final_positions[i]
# # #
# # #             # Move the letter towards the final position
# # #             dx = 1 if x < target_x else -1 if x > target_x else 0
# # #             dy = 1 if y < target_y else -1 if y > target_y else 0
# # #             canvas.move(letters[letter], dx, dy)
# # #
# # #             # Create a heart if it reaches the position
# # #             if dx == 0 and dy == 0 and letter not in hearts:
# # #                 hearts.append(letter)
# # #                 create_heart(target_x + 30, target_y - 30)
# # #
# # #         root.update()
# # #         time.sleep(delay / 1000)
# # #
# # #
# # # def main_animation():
# # #     # Clear the canvas for new animation
# # #     canvas.delete("all")
# # #
# # #     # Welcome Wajid Animation
# # #     word1 = "WAJID"
# # #     initial_positions1 = [(-100, 50), (900, 50), (-100, 500), (900, 500), (400, 700)]
# # #     final_positions1 = [(100, 150), (200, 150), (300, 150), (400, 150), (500, 150)]
# # #
# # #     animate_word(word1, initial_positions1, final_positions1)
# # #
# # #     # Pause before next animation
# # #     time.sleep(2)
# # #
# # #     # Happy Sajid Animation
# # #     word2 = "HAPPY SAJID"
# # #     initial_positions2 = [(-100, 50), (900, 50), (-100, 500), (900, 500), (400, 700),
# # #                           (-100, 150), (900, 150), (-100, 300), (900, 300), (400, 700)]
# # #     final_positions2 = [(50, 300), (150, 300), (250, 300), (350, 300), (450, 300),
# # #                         (100, 400), (200, 400), (300, 400), (400, 400), (500, 400)]
# # #
# # #     animate_word(word2, initial_positions2, final_positions2)
# # #
# # #     # Final Static Display
# # #     canvas.create_text(400, 300, text="WAJID", font=FONT_LARGE, fill=TEXT_COLOR)
# # #     canvas.create_text(400, 400, text="HAPPY SAJID", font=FONT_LARGE, fill=TEXT_COLOR)
# # #
# # #
# # # # Run the main animation
# # # main_animation()
# # #
# # # # Keep the window open
# # # root.mainloop()
# # import time
# # import tkinter as tk
# #
# # # Initialize the main window
# # root = tk.Tk()
# # root.title("Welcome Wajid")
# # root.geometry("800x600")
# # root.configure(bg="black")
# #
# # # Colors and Fonts
# # FONT_LARGE = ("Helvetica", 48, "bold")
# # TEXT_COLOR = "white"
# # HEART_COLOR = "red"
# #
# # # Create a canvas for animations
# # canvas = tk.Canvas(root, width=800, height=600, bg="black", highlightthickness=0)
# # canvas.pack()
# #
# #
# # def create_heart(x, y):
# #     size = 20
# #     return canvas.create_polygon(
# #         x, y,
# #         x - size, y - size,
# #         x - size * 2, y,
# #         x - size, y + size,
# #         x, y,
# #         fill=HEART_COLOR, outline="")
# #
# #
# # def animate_word(word, initial_positions, final_positions, delay=50):
# #     letters = {}
# #     hearts = []
# #
# #     # Create text objects at initial positions
# #     for i, letter in enumerate(word):
# #         x, y = initial_positions[i]
# #         letters[letter] = canvas.create_text(x, y, text=letter, font=FONT_LARGE, fill=TEXT_COLOR)
# #
# #     # Animation loop
# #     while any(
# #             canvas.coords(letters[letter]) != list(final_positions[i]) for i, letter in enumerate(word)
# #     ):
# #         for i, letter in enumerate(word):
# #             x, y = canvas.coords(letters[letter])
# #             target_x, target_y = final_positions[i]
# #
# #             # Move the letter towards the final position
# #             dx = 1 if x < target_x else -1 if x > target_x else 0
# #             dy = 1 if y < target_y else -1 if y > target_y else 0
# #             canvas.move(letters[letter], dx, dy)
# #
# #             # Create a heart if it reaches the position
# #             if dx == 0 and dy == 0 and letter not in hearts:
# #                 hearts.append(letter)
# #                 create_heart(target_x + 30, target_y - 30)
# #
# #         root.update()
# #         time.sleep(delay / 1000)
# #
# #
# # def main_animation():
# #     # Clear the canvas for new animation
# #     canvas.delete("all")
# #
# #     # Welcome Wajid Animation
# #     word1 = "WAJID"
# #     initial_positions1 = [(-100, 50), (900, 50), (-100, 500), (900, 500), (400, 700)]
# #     final_positions1 = [(100, 150), (200, 150), (300, 150), (400, 150), (500, 150)]
# #
# #     animate_word(word1, initial_positions1, final_positions1)
# #
# #     # Pause before next animation
# #     time.sleep(2)
# #
# #     # Happy Sajid Animation
# #     word2 = "HAPPY SAJID"
# #     initial_positions2 = [(-100, 50), (900, 50), (-100, 500), (900, 500), (400, 700),
# #                           (-100, 150), (900, 150), (-100, 300), (900, 300), (400, 700),
# #                           (800, 400)]
# #     final_positions2 = [(50, 300), (150, 300), (250, 300), (350, 300), (450, 300),
# #                         (100, 400), (200, 400), (300, 400), (400, 400), (500, 400),
# #                         (550, 400)]
# #
# #     animate_word(word2, initial_positions2, final_positions2)
# #
# #     # Final Static Display
# #     canvas.create_text(400, 300, text="WAJID", font=FONT_LARGE, fill=TEXT_COLOR)
# #     canvas.create_text(400, 400, text="HAPPY SAJID", font=FONT_LARGE, fill=TEXT_COLOR)
# #
# #
# # # Run the main animation
# # main_animation()
# #
# # # Keep the window open
# # root.mainloop()
# import itertools
# import time
# import tkinter as tk
#
# # Initialize the main window
# root = tk.Tk()
# root.title("Welcome Wajid")
# root.geometry("800x600")
#
# # Colors for background animation
# BACKGROUND_COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "white"]
# FONT_LARGE = ("Helvetica", 48, "bold")
# TEXT_COLORS = ["white", "cyan", "yellow", "lime", "orange", "pink"]
#
# # Load rose image
# ROSE_IMAGE_PATH = "path_to_rose_image.gif"  # Replace with your rose image path
# try:
#     rose_image = tk.PhotoImage(file=ROSE_IMAGE_PATH)
# except Exception as e:
#     print("Ensure the rose image is available and correctly referenced.")
#     rose_image = None  # Placeholder if no image is found
#
# canvas = tk.Canvas(root, width=800, height=600, highlightthickness=0)
# canvas.pack()
#
#
# def animate_background():
#     """Cycle through colors to animate the background."""
#     for color in itertools.cycle(BACKGROUND_COLORS):
#         canvas.configure(bg=color)
#         root.update()
#         time.sleep(0.5)
#
#
# def display_rose(x, y):
#     """Display a rose flower at the given position."""
#     if rose_image:
#         canvas.create_image(x, y, image=rose_image, anchor=tk.CENTER)
#
#
# def animate_word(word, initial_positions, final_positions, text_color, delay=50):
#     """Animate each letter of a word from initial to final positions."""
#     letters = {}
#
#     # Create text objects at initial positions
#     for i, letter in enumerate(word):
#         x, y = initial_positions[i]
#         letters[letter] = canvas.create_text(x, y, text=letter, font=FONT_LARGE, fill=text_color)
#
#     # Animate letters to their final positions
#     while any(
#             canvas.coords(letters[letter]) != list(final_positions[i]) for i, letter in enumerate(word)
#     ):
#         for i, letter in enumerate(word):
#             x, y = canvas.coords(letters[letter])
#             target_x, target_y = final_positions[i]
#
#             # Move letters closer to final position
#             dx = 1 if x < target_x else -1 if x > target_x else 0
#             dy = 1 if y < target_y else -1 if y > target_y else 0
#             canvas.move(letters[letter], dx, dy)
#
#             # Place a rose when a letter reaches its final position
#             if dx == 0 and dy == 0:
#                 display_rose(target_x, target_y + 50)
#
#         root.update()
#         time.sleep(delay / 1000)
#
#
# def main_animation():
#     """Run the main animation for both names."""
#     # Welcome Wajid Animation
#     word1 = "WAJID"
#     initial_positions1 = [(-100, 50), (900, 50), (-100, 500), (900, 500), (400, 700)]
#     final_positions1 = [(100, 150), (200, 150), (300, 150), (400, 150), (500, 150)]
#     animate_word(word1, initial_positions1, final_positions1, TEXT_COLORS[0])
#
#     # Pause before next animation
#     time.sleep(2)
#
#     # Happy Sajid Animation
#     word2 = "HAPPY SAJID"
#     initial_positions2 = [(-100, 50), (900, 50), (-100, 500), (900, 500), (400, 700),
#                           (-100, 150), (900, 150), (-100, 300), (900, 300), (400, 700),
#                           (800, 400)]
#     final_positions2 = [(50, 300), (150, 300), (250, 300), (350, 300), (450, 300),
#                         (100, 400), (200, 400), (300, 400), (400, 400), (500, 400),
#                         (550, 400)]
#     animate_word(word2, initial_positions2, final_positions2, TEXT_COLORS[1])
#
#     # Final Static Display
#     canvas.create_text(400, 300, text="WAJID", font=FONT_LARGE, fill=TEXT_COLORS[2])
#     canvas.create_text(400, 400, text="HAPPY SAJID", font=FONT_LARGE, fill=TEXT_COLORS[3])
#
#
# # Run the background animation in a separate thread
# import threading
#
# bg_thread = threading.Thread(target=animate_background, daemon=True)
# bg_thread.start()
#
# # Run the main animation
# main_animation()
#
# # Keep the window open
# root.mainloop()
import itertools
import time
import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Welcome Wajid")
root.geometry("800x600")

# Colors for animation
ANIMATION_COLORS = ["red", "green", "blue", "pink", "purple", "yellow"]
FONT_LARGE = ("Helvetica", 48, "bold")
FONT_SMALL = ("Helvetica", 24, "italic")
TEXT_COLOR = "white"

# Load flower image
FLOWER_IMAGE_PATH = "path_to_flower_image.gif"  # Replace with the actual path to your flower image
try:
    flower_image = tk.PhotoImage(file=FLOWER_IMAGE_PATH)
except Exception as e:
    print("Ensure the flower image is available and correctly referenced.")
    flower_image = None  # Placeholder if no image is found

canvas = tk.Canvas(root, width=800, height=600, bg="black", highlightthickness=0)
canvas.pack()


def create_flower(x, y):
    """Display a flower at the given position."""
    if flower_image:
        canvas.create_image(x, y, image=flower_image, anchor=tk.CENTER)


def animate_text_color(text_item):
    """Cycle through colors to animate the text."""
    for color in itertools.cycle(ANIMATION_COLORS):
        canvas.itemconfig(text_item, fill=color)
        root.update()
        time.sleep(0.2)


def animate_word(word, initial_positions, final_positions, delay=50):
    """Animate each letter of a word from initial to final positions."""
    letters = {}

    # Create text objects at initial positions
    for i, letter in enumerate(word):
        x, y = initial_positions[i]
        letters[letter] = canvas.create_text(x, y, text=letter, font=FONT_LARGE, fill=TEXT_COLOR)

    # Animate letters to their final positions
    while any(
            canvas.coords(letters[letter]) != list(final_positions[i]) for i, letter in enumerate(word)
    ):
        for i, letter in enumerate(word):
            x, y = canvas.coords(letters[letter])
            target_x, target_y = final_positions[i]

            # Move letters closer to final position
            dx = 1 if x < target_x else -1 if x > target_x else 0
            dy = 1 if y < target_y else -1 if y > target_y else 0
            canvas.move(letters[letter], dx, dy)

        root.update()
        time.sleep(delay / 1000)

    # Animate colors for each letter after reaching final position
    for letter in word:
        text_item = letters[letter]
        threading.Thread(target=animate_text_color, args=(text_item,), daemon=True).start()


def main_animation():
    """Run the main animation for both names."""
    # Add flowers at the edges of the canvas
    create_flower(400, 50)  # Top
    create_flower(400, 550)  # Bottom
    create_flower(50, 300)  # Left
    create_flower(750, 300)  # Right
    create_flower(400, 300)  # Center

    # Animate "WAJID"
    word1 = "WAJID"
    initial_positions1 = [(-100, 50), (900, 50), (-100, 500), (900, 500), (400, 700)]
    final_positions1 = [(100, 150), (200, 150), (300, 150), (400, 150), (500, 150)]
    animate_word(word1, initial_positions1, final_positions1)

    # Pause before next animation
    time.sleep(2)

    # Animate "HAPPY SAJID"
    word2 = "HAPPY SAJID"
    initial_positions2 = [(-100, 50), (900, 50), (-100, 500), (900, 500), (400, 700),
                          (-100, 150), (900, 150), (-100, 300), (900, 300), (400, 700),
                          (800, 400)]
    final_positions2 = [(50, 300), (150, 300), (250, 300), (350, 300), (450, 300),
                        (100, 400), (200, 400), (300, 400), (400, 400), (500, 400),
                        (550, 400)]
    animate_word(word2, initial_positions2, final_positions2)


# Run the main animation
import threading

bg_thread = threading.Thread(target=main_animation, daemon=True)
bg_thread.start()

# Keep the window open
root.mainloop()
