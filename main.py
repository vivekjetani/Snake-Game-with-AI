import tkinter as tk
import random
from PIL import Image, ImageTk
import heapq

# Constants
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20
DARK_SNAKE_COLOR = '#FFFFFF'
LIGHT_SNAKE_COLOR = '#00FF00'
DARK_BG = '#2E2E2E'
LIGHT_BG = '#FFFFFF'
DARK_TEXT_COLOR = '#FFFFFF'
LIGHT_TEXT_COLOR = '#000000'

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.resizable(False, False)
        
        self.is_dark_mode = True
        self.is_ai_mode = False
        self.bg_color = DARK_BG
        self.text_color = DARK_TEXT_COLOR
        self.snake_color = DARK_SNAKE_COLOR

        self.create_ui()

        # Load the original apple image
        self.apple_image = Image.open(r"apple.png").convert("RGBA")
        self.apple_image = self.apple_image.resize((CELL_SIZE, CELL_SIZE), Image.LANCZOS)
        self.apple_photo = ImageTk.PhotoImage(self.apple_image)

        self.reset_game()

        self.root.bind("<KeyPress>", self.handle_keypress)
        self.update()

    def create_ui(self):
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, bg=self.bg_color, bd=0, highlightthickness=0)
        self.canvas.pack(pady=(20, 0))
        
        self.score = 0
        self.highest_score = 0

        self.score_frame = tk.Frame(self.root, bg=self.bg_color)
        self.score_frame.pack()

        self.score_label = tk.Label(self.score_frame, text=f"Score: {self.score}", fg=self.text_color, bg=self.bg_color, font=("Arial", 16, "bold"))
        self.score_label.pack(side="left", padx=(0, 20))

        self.highest_score_label = tk.Label(self.score_frame, text=f"Highest Score: {self.highest_score}", fg=self.text_color, bg=self.bg_color, font=("Arial", 16, "bold"))
        self.highest_score_label.pack(side="left")

        self.toggle_button = tk.Button(self.root, text="Toggle Dark/Light Mode", command=self.toggle_mode, bg=self.bg_color, fg=self.text_color, font=("Arial", 12, "bold"), bd=0, highlightthickness=0)
        self.toggle_button.pack(pady=(10, 10))

        self.ai_button = tk.Button(self.root, text="Toggle AI", command=self.toggle_ai_mode, bg=self.bg_color, fg=self.text_color, font=("Arial", 12, "bold"), bd=0, highlightthickness=0)
        self.ai_button.pack(pady=(10, 20))

    def reset_game(self):
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = 'Right'
        self.food = self.place_food()
        self.game_over = False
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")
        self.update_ui()

    def place_food(self):
        while True:
            x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in self.snake:
                return x, y

    def handle_keypress(self, event):
        if self.game_over:
            self.reset_game()
        else:
            self.change_direction(event)

    def change_direction(self, event):
        new_direction = event.keysym
        all_directions = {'Up': 'Down', 'Down': 'Up', 'Left': 'Right', 'Right': 'Left'}
        if new_direction in all_directions and new_direction != all_directions[self.direction]:
            self.direction = new_direction

    def move_snake(self):
        x, y = self.snake[0]
        if self.direction == 'Up':
            y -= CELL_SIZE
        elif self.direction == 'Down':
            y += CELL_SIZE
        elif self.direction == 'Left':
            x -= CELL_SIZE
        elif self.direction == 'Right':
            x += CELL_SIZE

        # Wrap around the screen
        x = x % WIDTH
        y = y % HEIGHT

        new_head = (x, y)

        if new_head in self.snake:
            self.game_over = True
            self.end_game()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 10
            if self.score > self.highest_score:
                self.highest_score = self.score
            self.score_label.config(text=f"Score: {self.score}")
            self.highest_score_label.config(text=f"Highest Score: {self.highest_score}")
            self.food = self.place_food()
        else:
            self.snake.pop()

    def update(self):
        if not self.game_over:
            if self.is_ai_mode:
                self.ai_move()
            self.canvas.delete(tk.ALL)
            self.draw_food()
            self.draw_snake()
            self.move_snake()
            self.root.after(100, self.update)

    def draw_snake(self):
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill=self.snake_color, outline=self.bg_color)

    def draw_food(self):
        x, y = self.food
        self.canvas.create_image(x, y, image=self.apple_photo, anchor='nw')

    def end_game(self):
        self.canvas.create_text(WIDTH / 2, HEIGHT / 2, text="Game Over", fill=self.text_color, font=("Arial", 24, "bold"))
        self.canvas.create_text(WIDTH / 2, HEIGHT / 2 + 30, text="Press any key to restart", fill=self.text_color, font=("Arial", 12, "bold"))

    def toggle_mode(self):
        self.is_dark_mode = not self.is_dark_mode
        self.bg_color = DARK_BG if self.is_dark_mode else LIGHT_BG
        self.text_color = DARK_TEXT_COLOR if self.is_dark_mode else LIGHT_TEXT_COLOR
        self.snake_color = DARK_SNAKE_COLOR if self.is_dark_mode else LIGHT_SNAKE_COLOR
        self.update_ui()

    def toggle_ai_mode(self):
        self.is_ai_mode = not self.is_ai_mode

    def update_ui(self):
        self.canvas.config(bg=self.bg_color)
        self.score_frame.config(bg=self.bg_color)
        self.score_label.config(bg=self.bg_color, fg=self.text_color)
        self.highest_score_label.config(bg=self.bg_color, fg=self.text_color)
        self.toggle_button.config(bg=self.bg_color, fg=self.text_color)
        self.ai_button.config(bg=self.bg_color, fg=self.text_color)

    def ai_move(self):
        head = self.snake[0]
        path = self.a_star_search(head, self.food)
        if path:
            next_move = path[1]
            dx, dy = next_move[0] - head[0], next_move[1] - head[1]
            if dx == CELL_SIZE:
                self.direction = 'Right'
            elif dx == -CELL_SIZE:
                self.direction = 'Left'
            elif dy == CELL_SIZE:
                self.direction = 'Down'
            elif dy == -CELL_SIZE:
                self.direction = 'Up'

    def a_star_search(self, start, goal):
        def heuristic(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        def get_neighbors(pos):
            neighbors = [
                (pos[0] + CELL_SIZE, pos[1]),
                (pos[0] - CELL_SIZE, pos[1]),
                (pos[0], pos[1] + CELL_SIZE),
                (pos[0], pos[1] - CELL_SIZE)
            ]
            valid_neighbors = []
            for n in neighbors:
                if 0 <= n[0] < WIDTH and 0 <= n[1] < HEIGHT and n not in self.snake:
                    valid_neighbors.append(n)
            return valid_neighbors

        frontier = []
        heapq.heappush(frontier, (0, start))
        came_from = {start: None}
        cost_so_far = {start: 0}

        while frontier:
            _, current = heapq.heappop(frontier)

            if current == goal:
                break

            for next in get_neighbors(current):
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + heuristic(goal, next)
                    heapq.heappush(frontier, (priority, next))
                    came_from[next] = current

        if goal not in came_from:
            return None

        path = []
        current = goal
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()
        return path

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
