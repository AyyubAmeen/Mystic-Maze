class gameUI:
    def __init__(self):
        self.healthSize = 5
        self.healthX = 15
        self.healthY = 15
        self.healthHeight = 25
        self.itemBoxesX = 750
        self.itemBoxesY = 450
        self.itemBoxesWidth = 25
        self.itemBoxesHeight = 25

    def healthbarUpdate(self, playerObj):
        self.healthWidth = (100 * (playerObj.currentHp / playerObj.hp)) * self.healthSize
        self.healthBackWidth = 100 * self.healthSize

        self.healthRect = pygame.Rect(self.healthX, self.healthY, self.healthWidth, self.healthHeight)
        self.healthBackRect = pygame.Rect(self.healthX, self.healthY, self.healthBackWidth, self.healthHeight)

    def healthbarDraw(self, window, colour):
        pygame.draw.rect(window, colour["black"], self.healthBackRect)
        pygame.draw.rect(window, colour["red"], self.healthRect)        

    def itemBoxesDraw(self, window, colour):
        for i in range(5):
            self.itemBoxesX += i * 10
            self.itemBoxesRect = pygame.Rect(self.itemBoxesX, self.itemBoxesY, self.itemBoxesWidth, self.itemBoxesHeight)
            pygame.draw.rect(window, colour["brown"], self.itemBoxesRect)
    
    def update(self, playerObj):
        self.healthbarUpdate(playerObj)

    def draw(self, window, colour):
        self.itemBoxesDraw(window, colour)
        self.healthbarDraw(window, colour)
