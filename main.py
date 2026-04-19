import tkinter as tk
import ctypes
from ctypes import wintypes
from brain import process_command
from actions import execute_action, speak
from voice import listen
from memory import Memory

# --- настройки ---
WIDTH, HEIGHT = 500, 400
BG_COLOR = "#0d0d0d"
EYE_COLOR = "#2a2a2a"
ANIMATION_DURATION = 800  # общая длительность анимации (мс)
STEP = 30  # шаг анимации (мс)

# --- координаты для полукругов (точки отрисовки полигона) ---
left_half_circle = [140, 150, 150, 150, 160, 152, 170, 155, 180, 160, 190, 165,
                    200, 170, 205, 175, 210, 180, 210, 185, 205, 190, 200, 195,
                    190, 200, 180, 205, 170, 208, 160, 210, 150, 210, 140, 210]
right_half_circle = [290, 150, 300, 150, 310, 152, 320, 155, 330, 160, 340, 165,
                     350, 170, 355, 175, 360, 180, 360, 185, 355, 190, 350, 195,
                     340, 200, 330, 205, 320, 208, 310, 210, 300, 210, 290, 210]

# форма стрелочки ^ (точки отрисовки полигона)
left_arrow = [140, 180, 175, 120, 210, 180, 175, 150]
right_arrow = [290, 180, 325, 120, 360, 180, 325, 150]


class FramelessWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pollux")
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.wm_attributes('-topmost', True)
        # Убираем рамки
        self.root.overrideredirect(True)

        # Делаем окно круглым
        self.make_round(radius=150)  # радиус скругления

        # --- создание окна и self.canvas ---

        self.canvas = tk.Canvas(self.root, bg=BG_COLOR, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_oval(10, 400, 490, 30, fill="#80CBC4", outline="#004D40")
        # постоянные полигоны
        self.eye1 = self.canvas.create_polygon(left_arrow, fill=EYE_COLOR, outline="", smooth=True)
        self.eye2 = self.canvas.create_polygon(right_arrow, fill=EYE_COLOR, outline="", smooth=True)

        # --- переменные состояния ---

        self.blink_timer = None
        self.idle_timer = None
        self.idle_animation_active = False  # идет ли анимация стрелок
        self.transition_animation_active = False  # идет ли анимация перехода
        self.current_state = "normal"  # "normal" или "arrow"

        # Привязываем события для перемещения
        self.root.bind("<Button-1>", self.start_move)
        self.root.bind("<B1-Motion>", self.on_move)
        self.root.bind(self.make_round())
        # --- привязка событий мыши ---
        # Кнопка закрытия
        close_btn = tk.Button(self.root, text="X", command=self.root.quit)
        close_btn.pack(pady=10)

        #label = tk.Label(self.root, text="Это круглое окно без рамок")
        #label.pack(expand=True)

        self.root.mainloop()

    def make_round(self, radius=None):
        """Делает окно круглым (эллиптическим).
        Если radius не указан, используется половина минимальной стороны."""
        # Получаем дескриптор окна
        hwnd = ctypes.windll.user32.GetParent(self.root.winfo_id())

        # Получаем размеры окна
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        if width == 1 or height == 1:  # если окно ещё не отображено
            self.root.update_idletasks()
            width = self.root.winfo_width()
            height = self.root.winfo_height()

        if radius is None:
            radius = min(width, height) // 2

        # Создаём эллиптический регион
        # CreateRoundRectRgn(x1, y1, x2, y2, width_ellipse, height_ellipse)
        rgn = ctypes.windll.gdi32.CreateRoundRectRgn(0, 0, width, height, radius * 2, radius * 2)
        # Применяем регион к окну
        ctypes.windll.user32.SetWindowRgn(hwnd, rgn, True)
    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def on_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")




    # --- запуск ---

app = FramelessWindow()







