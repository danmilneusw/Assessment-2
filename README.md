# Assessment-2
## Provided Files
For Assessment 2, you have been given fps.py, PyParticles.py, and RunPyParticles.py.

**fps.py**: Contains 3 classes that are used in RunPyParticles.py for displaying FPS statistics.<br>
**PyParticles.py**: Contains functions that can be called in RunPyparticles.py to change the physics simulation system.<br>
**RunPyParticles.py**: This is the python file to run. Here you can change the number of particles to simulate

<div align="center">
  <a href="Images\RunPyParticles.png" target="_blank">
    <img src="Images\RunPyParticles.png" style="height:400px;"/>
  </a>
</div>
<br>


I have implemented an FPS counter for you. Just un-comment the line of your chosing inside RunPyParticles.py to select how detailed you want the FPS display to be. BasicFPS displays instantly as the remaining options require frames to run to be able to show minimum and maximum values for the past 300 frames (MinMaxFPS) or to show minimum and maximum values and the average FPS for the last 300 frames (FullFPS):

<div align="center">
  <a href="Images\FPS.png" target="_blank">
    <img src="Images\FPS.png" style="height:100px;"/>
  </a>
</div>
<br>

## Setup
For installing and setting up Python and Pygame on your own PC I have made a [tutorial](https://github.com/danmilneusw/Extra/blob/main/How%20to%20Setup%20Python%20and%20Pygame.md). Please email/Teams me if you need any help setting up.

## Task Summary
Please check the official PDF on Blackboard. Here is a quick summary of it:

You are required to implement optimisation into the RunPyParticles.py and/or PyParticles.py to improve performance. The code is set to run at 60 FPS, but currently performance is more likely to be around half this. You are welcome to alter these to use different combinations and optimise any combination of your choosing.

<div align="center">
  <a href="Images\Functions.png" target="_blank">
    <img src="Images\Functions.png" style="height:50px;"/>
  </a>
</div>
<br>

Then make a PDF report that showcases your assessment of performance before optimisation, what technique you used to optimise the code (spatial-partitioning: grid system, Quad-tree system...) and how the theory works and how your code works, then your performance after optimisation (how many particles can you display at > 60 FPS?...). Include an overall introduction and conclusion too.