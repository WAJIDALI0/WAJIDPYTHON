# # # import sys
# # #
# # # import pygame
# # # from pygame.locals import *
# # #
# # # # Initialize Pygame
# # # pygame.init()
# # #
# # # # Screen Dimensions and Setup
# # # WIDTH, HEIGHT = 800, 600
# # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # pygame.display.set_caption("Welcome Wajid")
# # # # Colors
# # # BLACK = (0, 0, 0)
# # # WHITE = (255, 255, 255)
# # # RED = (255, 0, 0)
# # #
# # # # Fonts
# # # font_large = pygame.font.Font(None, 100)
# # # font_small = pygame.font.Font(None, 50)
# # #
# # # # Animation Parameters
# # # positions = {
# # #     "W": [-100, 50],
# # #     "A": [WIDTH + 100, 50],
# # #     "J": [-100, HEIGHT - 150],
# # #     "I": [WIDTH + 100, HEIGHT - 150],
# # #     "D": [WIDTH // 2, HEIGHT + 100],
# # # }
# # # final_positions = {
# # #     "W": (100, 150),
# # #     "A": (200, 150),
# # #     "J": (300, 150),
# # #     "I": (400, 150),
# # #     "D": (500, 150),
# # # }
# # # speed = 5
# # #
# # #
# # # def draw_heart(x, y):
# # #     pygame.draw.polygon(screen, RED, [
# # #         (x, y), (x - 10, y - 15), (x - 20, y), (x - 10, y + 10)
# # #     ])
# # #
# # #
# # # def animate_name(name, title):
# # #     clock = pygame.time.Clock()
# # #     text_positions = {char: list(positions[char]) for char in name}
# # #     hearts = []
# # #
# # #     running = True
# # #     while running:
# # #         screen.fill(BLACK)
# # #
# # #         # Render Title
# # #         title_surface = font_small.render(title, True, WHITE)
# # #         screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, 20))
# # #
# # #         # Update and Draw Characters
# # #         for char, pos in text_positions.items():
# # #             if pos[0] < final_positions[char][0]:
# # #                 pos[0] += speed
# # #             elif pos[0] > final_positions[char][0]:
# # #                 pos[0] -= speed
# # #
# # #             if pos[1] < final_positions[char][1]:
# # #                 pos[1] += speed
# # #             elif pos[1] > final_positions[char][1]:
# # #                 pos[1] -= speed
# # #
# # #             # Draw Character
# # #             char_surface = font_large.render(char, True, WHITE)
# # #             screen.blit(char_surface, pos)
# # #
# # #             # Add Hearts
# # #             if pos == list(final_positions[char]) and char not in hearts:
# # #                 hearts.append(char)
# # #                 draw_heart(pos[0] + 20, pos[1] - 20)
# # #
# # #         # Check if all letters reached final positions
# # #         if all(pos == list(final_positions[char]) for char, pos in text_positions.items()):
# # #             running = False
# # #
# # #         pygame.display.update()
# # #         clock.tick(30)
# # #
# # #
# # # def main():
# # #     animate_name("WAJID", "Welcome Wajid")
# # #     pygame.time.delay(2000)  # Pause before the next animation
# # #     animate_name("HAPPY SAJID", "Welcome Wajid")
# # #
# # #     # Final Display
# # #     screen.fill(BLACK)
# # #     final_surface1 = font_large.render("WAJID", True, WHITE)
# # #     final_surface2 = font_large.render("HAPPY SAJID", True, WHITE)
# # #
# # #     screen.blit(final_surface1, (WIDTH // 2 - final_surface1.get_width() // 2, HEIGHT // 2 - 50))
# # #     screen.blit(final_surface2, (WIDTH // 2 - final_surface2.get_width() // 2, HEIGHT // 2 + 50))
# # #     pygame.display.update()
# # #
# # #     pygame.time.delay(5000)  # Keep the screen for 5 seconds
# # #
# # #     pygame.quit()
# # #     sys.exit()
# # #
# # #
# # # if __name__ == "__main__":
# # #     main()
# # import random
# # import time
# # import tkinter as tk
# #
# # # Initialize the main window
# # root = tk.Tk()
# # root.title("Happy Birthday WAJID!")
# # root.geometry("800x600")
# # root.configure(bg="black")
# #
# # # Colors and Fonts
# # FONT_LARGE = ("Helvetica", 48, "bold")
# # FONT_MEDIUM = ("Helvetica", 36, "bold")
# # FONT_SMALL = ("Helvetica", 24, "italic")
# # TEXT_COLORS = ["red", "green", "blue", "pink", "purple", "yellow"]
# # BALLOON_COLORS = ["red", "blue", "yellow", "green", "purple", "orange"]
# #
# # # Create a canvas for animations
# # canvas = tk.Canvas(root, width=800, height=600, bg="black", highlightthickness=0)
# # canvas.pack()
# #
# #
# # def draw_balloon(x, y, color):
# #     """Draw a balloon at the specified position."""
# #     canvas.create_oval(x - 20, y - 30, x + 20, y + 30, fill=color, outline=color)
# #     canvas.create_line(x, y + 30, x, y + 50, fill="white")
# #
# #
# # def animate_balloons():
# #     """Animate balloons floating up the screen."""
# #     for _ in range(50):  # Number of frames
# #         canvas.delete("balloon")  # Clear old balloons
# #         for _ in range(5):  # Number of balloons
# #             x = random.randint(50, 750)
# #             y = random.randint(400, 600)
# #             color = random.choice(BALLOON_COLORS)
# #             draw_balloon(x, y, color)
# #         root.update()
# #         time.sleep(0.1)
# #
# #
# # def display_message():
# #     """Display the Happy Birthday message."""
# #     canvas.create_text(400, 150, text="Happy Birthday!", font=FONT_LARGE, fill=random.choice(TEXT_COLORS))
# #     canvas.create_text(400, 250, text="WAJID", font=FONT_LARGE, fill=random.choice(TEXT_COLORS))
# #     canvas.create_text(400, 350, text="Wishing you a wonderful day!", font=FONT_MEDIUM, fill=random.choice(TEXT_COLORS))
# #
# #
# # def background_animation():
# #     """Change the background colors dynamically."""
# #     for color in TEXT_COLORS:
# #         canvas.configure(bg=color)
# #         root.update()
# #         time.sleep(0.5)
# #
# #
# # def main_animation():
# #     """Main animation function."""
# #     # Animate balloons
# #     animate_balloons()
# #
# #     # Display the birthday message
# #     display_message()
# #
# #     # Background color animation
# #     background_animation()
# #
# #     # Keep the message on screen
# #     canvas.create_text(400, 450, text="Have a great year ahead!", font=FONT_SMALL, fill="white")
# #     root.update()
# #
# #
# # # Run the main animation
# # main_animation()
# #
# # # Keep the window open
# # root.mainloop()
# import random
# import time
# import tkinter as tk
#
# # Initialize the main window
# root = tk.Tk()
# root.title("Happy Birthday WAJID!")
# root.geometry("800x600")
# root.configure(bg="black")
#
# # Colors and Fonts
# FONT_LARGE = ("Helvetica", 48, "bold")
# FONT_MEDIUM = ("Helvetica", 36, "bold")
# FONT_SMALL = ("Helvetica", 24, "italic")
# TEXT_COLORS = ["red", "green", "blue", "pink", "purple", "yellow"]
# BALLOON_COLORS = ["red", "blue", "yellow", "green", "purple", "orange"]
#
# # Create a canvas for animations
# canvas = tk.Canvas(root, width=800, height=600, bg="black", highlightthickness=0)
# canvas.pack()
#
#
# def draw_balloon(x, y, color):
#     """Draw a balloon at the specified position."""
#     canvas.create_oval(x - 20, y - 30, x + 20, y + 30, fill=color, outline=color)
#     canvas.create_line(x, y + 30, x, y + 50, fill="white")
#
#
# def animate_balloons():
#     """Animate balloons floating up the screen."""
#     for _ in range(50):  # Number of frames
#         canvas.delete("balloon")  # Clear old balloons
#         for _ in range(5):  # Number of balloons
#             x = random.randint(50, 750)
#             y = random.randint(400, 600)
#             color = random.choice(BALLOON_COLORS)
#             draw_balloon(x, y, color)
#         root.update()
#         time.sleep(0.1)
#
#
# def display_message():
#     """Display the Happy Birthday message."""
#     canvas.create_text(400, 100, text="Happy Birthday!", font=FONT_LARGE, fill=random.choice(TEXT_COLORS))
#     canvas.create_text(400, 200, text="WAJID", font=FONT_LARGE, fill=random.choice(TEXT_COLORS))
#     canvas.create_text(400, 280, text="Born on: 01/01/2005", font=FONT_MEDIUM, fill=random.choice(TEXT_COLORS))
#     canvas.create_text(400, 350, text="Wishing You on: 01/01/2025", font=FONT_MEDIUM, fill=random.choice(TEXT_COLORS))
#     canvas.create_text(400, 420, text="Best Wishes From:", font=FONT_MEDIUM, fill=random.choice(TEXT_COLORS))
#     canvas.create_text(400, 480, text="Sajid, Farhan, and Abid", font=FONT_SMALL, fill=random.choice(TEXT_COLORS))
#
#
# def background_animation():
#     """Change the background colors dynamically."""
#     for color in TEXT_COLORS:
#         canvas.configure(bg=color)
#         root.update()
#         time.sleep(0.5)
#
#
# def main_animation():
#     """Main animation function."""
#     # Animate balloons
#     animate_balloons()
#
#     # Display the birthday message
#     display_message()
#
#     # Background color animation
#     background_animation()
#
#     # Keep the message on screen
#     canvas.create_text(400, 550, text="Enjoy Your Special Day!", font=FONT_SMALL, fill="white")
#     root.update()
#
#
# # Run the main animation
# main_animation()
#
# # Keep the window open
# root.mainloop()
import random
import time
import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Happy Birthday WAJID!")
root.geometry("800x600")
root.configure(bg="black")

# Colors and Fonts
FONT_LARGE = ("Helvetica", 48, "bold")
FONT_MEDIUM = ("Helvetica", 36, "bold")
FONT_SMALL = ("Helvetica", 24, "italic")
TEXT_COLORS = ["red", "green", "blue", "pink", "purple", "yellow"]
BALLOON_COLORS = ["red", "blue", "yellow", "green", "purple", "orange"]

# Create a canvas for animations
canvas = tk.Canvas(root, width=800, height=600, bg="black", highlightthickness=0)
canvas.pack()


class Balloon:
    """Class to represent a moving balloon."""

    def __init__(self, x, y, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.id = canvas.create_oval(x - 20, y - 30, x + 20, y + 30, fill=color, outline=color)
        self.string = canvas.create_line(x, y + 30, x, y + 50, fill="white")

    def move(self):
        """Move the balloon diagonally."""
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x < 0 or self.x > 800:  # Bounce horizontally
            self.speed_x = -self.speed_x
        if self.y < 0 or self.y > 600:  # Bounce vertically
            self.speed_y = -self.speed_y
        canvas.move(self.id, self.speed_x, self.speed_y)
        canvas.move(self.string, self.speed_x, self.speed_y)


def animate_balloons():
    """Animate balloons moving diagonally."""
    balloons = [
        Balloon(random.randint(50, 750), random.randint(400, 600),
                random.choice(BALLOON_COLORS),
                random.choice([-3, -2, 2, 3]),
                random.choice([-3, -2, 2, 3]))
        for _ in range(8)  # Number of balloons
    ]

    for _ in range(150):  # Number of frames
        for balloon in balloons:
            balloon.move()
        root.update()
        time.sleep(0.05)


def display_message():
    """Display the Happy Birthday message."""
    canvas.create_text(400, 100, text="Happy Birthday!", font=FONT_LARGE, fill=random.choice(TEXT_COLORS))
    canvas.create_text(400, 200, text="WAJID", font=FONT_LARGE, fill=random.choice(TEXT_COLORS))
    canvas.create_text(400, 280, text="Born on: 01/01/2005", font=FONT_MEDIUM, fill=random.choice(TEXT_COLORS))
    canvas.create_text(400, 350, text="Wishing You on: 01/01/2025", font=FONT_MEDIUM, fill=random.choice(TEXT_COLORS))
    canvas.create_text(400, 420, text="Best Wishes From:", font=FONT_MEDIUM, fill=random.choice(TEXT_COLORS))
    canvas.create_text(400, 480, text="Sajid, Farhan, and Abid", font=FONT_SMALL, fill=random.choice(TEXT_COLORS))


def background_animation():
    """Change the background colors dynamically."""
    for color in TEXT_COLORS:
        canvas.configure(bg=color)
        root.update()
        time.sleep(0.5)


def main_animation():
    """Main animation function."""
    # Animate balloons
    animate_balloons()

    # Display the birthday message
    display_message()

    # Background color animation
    background_animation()

    # Display final message
    canvas.create_text(400, 550, text="Enjoy Your Special Day!", font=FONT_SMALL, fill="gold")
    root.update()


# Run the main animation
main_animation()

# Keep the window open
root.mainloop()
