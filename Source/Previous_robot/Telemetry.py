from pybricks.tools import wait,StopWatch

# === telemetry.py ===
class Telemetry:
    ANSI_COLORS = {
        "BLACK": "30", "RED": "31", "GREEN": "32", "YELLOW": "33",
        "BLUE": "34", "MAGENTA": "35", "CYAN": "36", "WHITE": "37",
        "RESET": "0"
    }

    def __init__(self, refresh_time):
        print("\x1b[H\x1b[2J", end="")  # Очистить консоль при запуске
        self.static = []               # Статичные строки
        self.live = {}                 # Значения для обновления
        self.live_order = []           # Порядок отображения live
        self.timer=StopWatch()
        self.timer.reset()
        self.set_static("=== Telemetry Console ===")
        self.refresh_time = refresh_time

    def set_static(self, line: str):
        self.static.append(line)

    def set_live(self, key: str, value, color="RESET"):
        color_code = self.ANSI_COLORS.get(color, self.ANSI_COLORS["RESET"])
        if key not in self.live:
            self.live_order.append(key)
        self.live[key] = (value, color_code)

    def remove(self, key: str):
        if key in self.live:
            del self.live[key]
            self.live_order.remove(key)

    def clear(self):
        self.static.clear()
        self.live.clear()
        self.live_order.clear()

    def render(self):
        if self.timer.time() > self.refresh_time:

            print("\x1b[?25l", end="")      # Скрыть курсор
            print("\x1b[H", end="")         # В начало экрана

            # Печать статичных строк
            for line in self.static:
                print(line)

            # Печать live-значений с очисткой строки
            base_line = len(self.static) + 1
            for i, key in enumerate(self.live_order):
                value, color_code = self.live[key]
                row = base_line + i
                print(f"\x1b[{row};1H\x1b[{color_code}m{key}: {value}\x1b[0m\x1b[K", end="")

            print("\x1b[?25h", end="")      # Показать курсор
            self.timer.reset()
