import pygame
import sys

try:
    from snake_game.settings import (
        SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE, GRID_WIDTH, GRID_HEIGHT,
        COLORS, DIFFICULTY, HIGHSCORE_FILE
    )
    from snake_game.snake import Snake
    from snake_game.food import Food
    from snake_game.score_manager import ScoreManager
except ModuleNotFoundError:
    from settings import (
        SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE, GRID_WIDTH, GRID_HEIGHT,
        COLORS, DIFFICULTY, HIGHSCORE_FILE
    )
    from snake import Snake
    from food import Food
    from score_manager import ScoreManager


class Game:
    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake Game')
        self._clock = pygame.time.Clock()
        
        pygame.font.init()
        self._font_large = pygame.font.Font(None, 64)
        self._font_medium = pygame.font.Font(None, 36)
        self._font_small = pygame.font.Font(None, 24)
        
        self._snake = Snake(GRID_WIDTH, GRID_HEIGHT)
        self._food = Food(GRID_WIDTH, GRID_HEIGHT)
        self._scores = ScoreManager(HIGHSCORE_FILE)
        
        self._food.spawn(self._snake.occupied())
        self._difficulty = 'Medium'
        self._speed = DIFFICULTY[self._difficulty]
        self._state = 'playing'

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if self._state == 'playing':
                    if event.key == pygame.K_UP:
                        self._snake.set_direction((0, -1))
                    elif event.key == pygame.K_DOWN:
                        self._snake.set_direction((0, 1))
                    elif event.key == pygame.K_LEFT:
                        self._snake.set_direction((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        self._snake.set_direction((1, 0))
                    elif event.key == pygame.K_1:
                        self._difficulty = 'Easy'
                        self._speed = DIFFICULTY['Easy']
                    elif event.key == pygame.K_2:
                        self._difficulty = 'Medium'
                        self._speed = DIFFICULTY['Medium']
                    elif event.key == pygame.K_3:
                        self._difficulty = 'Hard'
                        self._speed = DIFFICULTY['Hard']
                elif self._state == 'gameover':
                    if event.key == pygame.K_r:
                        self._restart()
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

    def _restart(self):
        self._snake.reset()
        self._scores.reset()
        self._food.spawn(self._snake.occupied())
        self._state = 'playing'

    def _update(self):
        if self._state != 'playing':
            return
        
        self._snake.update()
        
        if self._snake.head == (self._food.x, self._food.y):
            self._snake.grow()
            self._scores.add(10)
            self._food.spawn(self._snake.occupied())
        
        if self._snake.hit_wall() or self._snake.hit_self():
            self._state = 'gameover'

    def _draw(self):
        self._screen.fill(COLORS['background'])
        
        fx = self._food.x * GRID_SIZE
        fy = self._food.y * GRID_SIZE
        pygame.draw.rect(self._screen, COLORS['food'], (fx + 2, fy + 2, GRID_SIZE - 4, GRID_SIZE - 4))
        
        for i, (x, y) in enumerate(self._snake.body):
            px = x * GRID_SIZE
            py = y * GRID_SIZE
            color = COLORS['snake_head'] if i == 0 else COLORS['snake_body']
            pygame.draw.rect(self._screen, color, (px + 1, py + 1, GRID_SIZE - 2, GRID_SIZE - 2))
        
        score_surf = self._font_small.render(f'Score: {self._scores.score}', True, COLORS['text'])
        highscore_surf = self._font_small.render(f'High Score: {self._scores.highscore}', True, COLORS['text_dim'])
        diff_surf = self._font_small.render(f'Difficulty: {self._difficulty}', True, COLORS['text_dim'])
        
        self._screen.blit(score_surf, (15, 15))
        self._screen.blit(highscore_surf, (15, 40))
        self._screen.blit(diff_surf, (SCREEN_WIDTH - 150, 15))
        
        if self._state == 'gameover':
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            self._screen.blit(overlay, (0, 0))
            
            go = self._font_large.render('GAME OVER', True, COLORS['food'])
            score_f = self._font_medium.render(f'Final Score: {self._scores.score}', True, COLORS['text'])
            high_f = self._font_medium.render(f'High Score: {self._scores.highscore}', True, COLORS['text'])
            restart = self._font_medium.render('Press R to Restart', True, COLORS['text_dim'])
            quit_t = self._font_medium.render('Press Q to Quit', True, COLORS['text_dim'])
            
            self._screen.blit(go, go.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60)))
            self._screen.blit(score_f, score_f.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
            self._screen.blit(high_f, high_f.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 35)))
            self._screen.blit(restart, restart.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80)))
            self._screen.blit(quit_t, quit_t.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 115)))
        
        pygame.display.flip()

    def run(self):
        while True:
            self._handle_input()
            self._update()
            self._draw()
            self._clock.tick(self._speed)
