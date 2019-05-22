import json
import math
import functools
from PIL import Image, ImageDraw

def floor(point, paddingX, paddingY):
  return ((point[0] - paddingX) * 4, (point[1] - paddingY) * 4)

img = Image.new('RGBA', (1280, 1280))
draw = ImageDraw.Draw(img)

with open('map.json') as json_file:
  data = json.load(json_file)
  pathpoint = []
  minX = (min(data['image']['pixels']['floor'], key = lambda t: t[0]))[0] - 20
  minY = (min(data['image']['pixels']['floor'], key = lambda t: t[1]))[1] - 20
  for path in data['path']['points']:
    pathpoint.append((math.floor((path[0]/50 - data['image']['position']['left'] - minX) * 4), math.floor((path[1]/50 - data['image']['position']['top'] - minY) * 4)))

  draw.line(tuple(map(functools.partial(floor, paddingX=minX, paddingY=minY), data['image']['pixels']['obstacle_strong'])), fill=(82, 174, 255, 255), width=3)
  draw.line(tuple(map(functools.partial(floor, paddingX=minX, paddingY=minY), data['image']['pixels']['floor'])), fill=(0, 118, 255, 255), width=4)
  draw.line(pathpoint, fill=(255, 255, 255, 255), width=1)
  img.show()
