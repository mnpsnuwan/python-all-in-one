class Ball:

    def __int__(self, canvas, x, y, diameter, x_velocity, y_velocity, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, diameter, diameter, fill=color)
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def move(self):
        coordinates = self.canvas.coords(self.image)

        if coordinates[2] >= self.canvas.winfo_width() or coordinates[0] < 0:
            self.x_velocity = -self.x_velocity

        if coordinates[3] >= self.canvas.winfo_height() or coordinates[1] < 0:
            self.y_velocity = -self.y_velocity

        self.canvas.move(self.image, self.x_velocity, self.y_velocity)

