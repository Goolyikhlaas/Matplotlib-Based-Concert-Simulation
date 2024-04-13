###spinal-tap.py###

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mping
from cheorography import SmokeMachine
from cheorography import col_iterate, col_back_itera
from cheorography import col_back_itera

print("Welcome to the StageView Generator!")

# Prompt for user preferences
smoke_choice = input("Would you like to include smoke? (yes/no): ")
lights_choice = input("Would you like to have concert lights? (yes/no): ")
backdrop_choice = input("Would you like to have a stage backdrop? (yes/no): ")

for i in range(7):
    fig, (ax0, ax1) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 10]}, figsize=(10, 10))
    plt.suptitle("STAGEVIEW", fontsize="20")

    ax0.set_xlim([0, 500])
    ax0.set_ylim([0, 50])
    ax1.set_xlim([0, 500])
    ax1.set_ylim([0, 500])

    # Adding iterating lights to be shown from the top
    ax0.set_aspect("equal")
    ax0.fill([0, 500, 500, 0], [0, 0, 50, 50], color='black')
    circle1 = plt.Circle([50, 25], 20, color=col_iterate(i))
    ax0.add_patch(circle1)
    circle1 = plt.Circle([150, 25], 20, color=col_iterate(i + 1))
    ax0.add_patch(circle1)
    circle1 = plt.Circle([250, 25], 20, color=col_iterate(i + 2))
    ax0.add_patch(circle1)
    circle1 = plt.Circle([350, 25], 20, color=col_iterate(i + 3))
    ax0.add_patch(circle1)
    circle1 = plt.Circle([450, 25], 20, color=col_iterate(i + 4))
    ax0.add_patch(circle1)
    ax0.axis('off')  # Removing axis

    ax1.set_aspect("equal")
    # Iterating on the backdrop lighting
    if backdrop_choice.lower() == "yes":
        ax1.fill([0, 500, 500, 0], [0, 0, 500, 500], color=col_back_itera(i))
    else:
        ax1.fill([0, 500, 500, 0], [0, 0, 500, 500], color='black')  # Single color for backdrop

    if lights_choice.lower() == "yes":
        ax1.fill([0, 30, 70, 130], [0, 500, 500, 0], color=col_iterate(i), alpha=0.4)
        ax1.fill([70, 130, 170, 230], [0, 500, 500, 0], color=col_iterate(i + 1), alpha=0.4)
        ax1.fill([170, 230, 270, 330], [0, 500, 500, 0], color=col_iterate(i + 2), alpha=0.4)
        ax1.fill([270, 330, 370, 430], [0, 500, 500, 0], color=col_iterate(i + 3), alpha=0.4)
        ax1.fill([370, 430, 470, 500], [0, 500, 500, 0], color=col_iterate(i + 4), alpha=0.4)
        
    else:
         ax1.fill([0, 30, 70, 130], [0, 500, 500, 0], color='yellow', alpha=0.4)
         ax1.fill([370, 430, 470, 500], [0, 500, 500, 0], color='yellow', alpha=0.4)

    # Adding a stage for the band and lighting to the stage
    ax1.fill([0, 500, 470, 30], [0, 0, 140, 140], color='black', alpha=0.9)
    ax1.axis('off')

    # Adding band image
    band = mping.imread("/Users/ikhlaasgooly/Desktop/FOP_Assignment_21619513/Code/Band silhouette.png")
    # Adding people image
    crowd = mping.imread("/Users/ikhlaasgooly/Desktop/FOP_Assignment_21619513/Code/Audience.png")
   
   
    ax1.imshow(band, extent=[55, 455, 135, 360], zorder=10)        # Extent will shift the image size
    ax1.imshow(crowd, extent=[0, 500, 0, 575], zorder=10)          # Zorder will make image come in foreground


    # Check the user preferences and include the appropriate smoke machine, lights, and backdrop.
    if smoke_choice.lower() == "yes":
        
        #Instances of the SmokeMachine class are used to generate smoke effects.
        
        for j in range(3):                        #The loop is repeated three times to generate several instances at different places.
            smoke = SmokeMachine((250, 400))      
            smoke.stepChange()                    #The stepChange() method changes the positions of smoke particles.
            smoke.plotSmoke(ax1)                  #plotSmoke() method plots the smoke particles on ax1 subplot.
            smoke = SmokeMachine((450, 400))
            smoke.stepChange()
            smoke.plotSmoke(ax1)
            smoke = SmokeMachine((350, 250))
            smoke.stepChange()
            smoke.plotSmoke(ax1)
            smoke = SmokeMachine((200, 350))
            smoke.stepChange()
            smoke.plotSmoke(ax1)
            smoke = SmokeMachine((100, 300))
            smoke.stepChange()
            smoke.plotSmoke(ax1)

    plt.pause(0.1)    #introduces a 0.1-second break in execution to give time for the plot to be displayed before continue.

plt.show()

