from p5 import *

def setup():
  createCanvas(400, 400)
  frameRate(5)

def draw():
  squareSize = 10
  # background("black")
  # drawTickAxes()
  for v in range(int(height/squareSize)):
    for i in range(int(width/squareSize)):
      if int(height/squareSize)-v<=5:
        fill(0,random(50,150),0)
      elif int(height/squareSize)-v<=41:
        fill("brown")
      elif:
        fill("white")
      square(i*squareSize,v*squareSize,squareSize)

  
# width ... squareSize ... -> how many squares
  