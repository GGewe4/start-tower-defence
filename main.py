import pygame

DIC_OF_TILES = {0: '', 1: 'Tile_road.png', 2: 'Tile_platform.png', 3: 'Tile_portal.png',
                4: 'Tile_base.png'}
DIR_RES = 'resources'
DIR_LEVELS = 'levels'

FPS = 60


class Game:

    def __init__(self, width, height, level=1):
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.towers = []
        self.level = level
        self.board = []
        self.len_tile = 70
        with open(f'{DIR_LEVELS}/level{level}.txt') as file:
            for line in file:
                self.board.append(list(map(int, line.split())))
        self.height_board = len(self.board)
        self.width_board = len(self.board[0])
        self.top = (self.height - self.height_board * self.len_tile) // 2
        self.left = (self.width - self.width_board * self.len_tile) // 2
        self.lives = 20
        self.money = 100

    def run(self):
        pygame.init()
        run = True
        clock = pygame.time.Clock()
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.render()
            clock.tick(FPS)
        pygame.quit()

    def render(self):
        self.win.fill((10, 10, 10))
        for i in range(self.height_board):
            for j in range(self.width_board):
                if self.board[i][j]:
                    img = pygame.image.load(f'{DIR_RES}/{DIC_OF_TILES[self.board[i][j]]}')
                    if self.board[i][j] != 1:
                        img = pygame.transform.scale(img, (self.len_tile - 3, self.len_tile - 3))
                        self.win.blit(img, (self.left + self.len_tile * j, self.top + self.len_tile * i))
                    else:
                        img = pygame.transform.scale(img, (self.len_tile, self.len_tile))
                        self.win.blit(img, (self.left + self.len_tile * j + 3, self.top + (self.len_tile + 3) * i))
        pygame.display.update()


game = Game(800, 800, 1)
game.run()
