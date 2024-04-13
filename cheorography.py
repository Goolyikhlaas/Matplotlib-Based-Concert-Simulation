###cheorography.py###


import numpy as np

#lights.py

# List of background colors
color_back = ['color1', 'color2', 'color3', 'color4', 'color5']

# Function to cycle through over the backdrop colors.
def col_back_itera(i):
    colors_back = np.roll(color_back, 0)  # Roll the color_back list
    color_idx_back = i % len(colors_back)  # Get the index based on the iteration
    return colors_back[color_idx_back]  # Return the color at the specified index

# List of colors
color = ['darkmagenta', 'teal', 'red', 'blue', 'red']

# Iterate through the colors with this function.
def col_iterate(i):
    colors = np.roll(color, 0)  # Roll the color list
    color_idx = i % len(colors)  # Get the index based on the iteration
    return colors[color_idx]  # Return the color at the specified index


#backdrop.py

fileobj = open('backdroplights.csv', 'r')  # Open the 'backdroplights.csv' file in read mode
data = fileobj.readlines()  # Read through the entire file.
fileobj.close()  # Close the file
color_back = []

# Iterate through the data, one line at a time.
for line in data:
    splitline = line.strip().split(',')  # Divide/split the line with a comma.
    color_back.append(splitline[0])  #Include the first item in the color_backlist.

# Iterate over the backdrop colors with this function.
def col_back_itera(i):
    colors_back = np.roll(color_back, 0)  # Roll the color_back list
    color_idx_back = i % len(colors_back)  # Get the index based on the iteration
    return colors_back[color_idx_back]  # Return the color at the specified index


#smokemachine.py

#The code given by smokemachine is built on the foundation of Bubblemachine.py.

# Define a SmokeMachine class
class SmokeMachine():
    def __init__(self, pos):
        self.pos = pos  # The location of the smoke machine
        self.smoke = []  # Smoke particle storage list
        self.flow = 1  # Variable for flow control
        self.drift = np.random.uniform(0.2, 0.9)  # Smoke particle drift value

    def startSmoke(self):
        self.flow = 1  # To begin emitting smoke, set flow to 1.

    def stopSmoke(self):
        self.flow = 0  # To cease smoke emission, set flow to 0.

    def stepChange(self):
        if self.flow == 1:
            # Include new smoke particles in the list.
            for i in range(10):
                x = self.pos[0] + np.random.randint(-20, 20)  # Randomize the x position on the machine.
                y = self.pos[1] + np.random.randint(-20, 20)  # Randomize the y position on the machine.
                size = np.random.randint(70, 2700)  # Change the size of the smoke particle at random.
                opacity = np.random.uniform(0.1, 0.1)  # Change the opacity of the smoke particle at random.
                self.smoke.append([x, y, size, opacity])  # Include the smoke particle in the list.

            # Update the existing smoke particle placements
            for s in self.smoke:
                s[0] += np.random.randint(-10, 10) + self.drift * s[1]  # x position is being updated with a drift effect.
                s[1] += np.random.randint(-10, 10) + self.drift * s[2]  # y position is being updated with a drift effect.
                s[2] += np.random.randint(50, 100)  # The size of the smoke particle has been updated.

                # Remove any out-of-bounds smoke particles.
                if s[0] < 0 or s[0] > 500 or s[1] < 0 or s[1] > 500:
                    self.smoke.remove(s)

    def plotSmoke(self, ax):
        for s in self.smoke:
            x = s[0]
            y = s[1]
            size = s[2] * 5
            ax.scatter(x, y, s=[size], c="lightgrey", alpha=0.05)


