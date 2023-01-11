import turtle



class Window:
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = turtle.Screen()
        self.screen.title('OOP Snake')
        self.screen.bgcolor((0.5, 0, 0.5))
        self.screen.setup(WIDTH, HEIGHT)
        self.screen.tracer(0)

        with open('high_score.txt') as f:
            self.high_score = int(f.read())
            print ('READ "high_score.txt"')
            


        self.hud = turtle.Turtle()

    def drawHUD(self, score):
        if score > self.high_score:
            self.high_score = score
            with open('high_score.txt', 'w') as f:
                f.write(str(score))
                print ('WRITE "high_score.txt"')
        self.hud.clear()
        self.hud.color('white')
        self.hud.penup()
        self.hud.hideturtle()
        frac= (3, 7)
        self.hud.goto(0,-frac[0]*self.HEIGHT//frac[1])

        self.hud.write(f'Score: {score} High Score: {self.high_score}', align = 'center', font=('Courier', 22, 'normal'))

        
