import json
import math
import functools
from PIL import Image, ImageDraw

def floor(point, paddingX, paddingY, width):
  return [((point[0] - paddingX) * 4), ((point[1] - paddingY) * 4),(((point[0] - paddingX) * 4) + width), (((point[1] - paddingY) * 4) + width)]

img = Image.new('RGBA', (1280, 1280))
draw = ImageDraw.Draw(img)

with open('map.json') as json_file:
  data = json.load(json_file)
  pathpoint = []
  minX = (min(data['image']['pixels']['floor'], key = lambda t: t[0]))[0] - 20
  minY = (min(data['image']['pixels']['floor'], key = lambda t: t[1]))[1] - 20
  for path in data['path']['points']:
    pathpoint.append((math.floor((path[0]/50 - data['image']['position']['left'] - minX) * 4), math.floor((path[1]/50 - data['image']['position']['top'] - minY) * 4)))

  #draw.line(tuple(map(functools.partial(floor, paddingX=minX, paddingY=minY), data['image']['pixels']['obstacle_strong'])), fill=(82, 174, 255, 255), width=3)
  #draw.line(tuple(map(functools.partial(floor, paddingX=minX, paddingY=minY), data['image']['pixels']['floor'])), fill=(0, 118, 255, 255), width=4)
  for point in data['image']['pixels']['floor']:
    draw.ellipse(floor(point,minX,minY,4), fill=(0, 118, 255, 255))
  for point in data['image']['pixels']['obstacle_strong']:
    draw.ellipse(floor(point,minX,minY,3), fill=(82, 174, 255, 255))
  #robot = (math.floor(data['robot'][0]/50 - data['image']['position']['left']), math.floor(data['robot'][1]/50 - data['image']['position']['top']))
  #draw.ellipse(floor(robot, minX, minY, 5), fill=(255, 255, 255, 255))
  draw.line(pathpoint, fill=(255, 255, 255, 255), width=1)
  img.show()
