class GameStats:
    """Відстежувати статистики гри"""

    def __init__(self, ai_game):
        """Ініціалізація статистики."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Розпочати гру в неактивному стані.
        self.game_active = False

    def reset_stats(self):
        """Ініціалізація статистики, що може змінюватися впродовж гри."""
        self.ships_left = self.settings.ship_limit
