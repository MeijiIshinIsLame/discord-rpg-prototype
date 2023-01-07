from tile import MapTile
from itertools import repeat
import random
from PIL import Image, ImageDraw
from tqdm import tqdm

tiles = []
TILE_SIZE = 32

grass_tile = MapTile(tile_id=1, density=0, icon="./grass1.png", name="Grass", attributes=[], probability=90)
tiles.extend(repeat(grass_tile,grass_tile.probability))

tree_tile = MapTile(tile_id=2, density=1, icon="./tree1.png", name="Tree", attributes=["chopable"], probability=5)
tiles.extend(repeat(tree_tile,tree_tile.probability))

rock_tile = MapTile(tile_id=3, density=1, icon="./rock1.png", name="Rock", attributes=["chopable"], probability=4)
tiles.extend(repeat(rock_tile,rock_tile.probability))

class Map:
	def __init__(self, width, height, tiles):
		self.width = width
		self.height = height
		self.tiles = tiles
		self.tilegrid = self.create_random_map()

	def create_random_map(self):
		# Create an empty map
		the_map = []
		for i in range(self.height):
			the_map.append([])
			for j in range(self.width):
				the_map[i].append(None)
		
		# Iterate through each tile in the map
		for i in range(self.height):
			for j in range(self.width):
				# Roll a die to determine which tile to place
				tile = random.choice(self.tiles)
				the_map[i][j] = tile
		
		return the_map

	def print_map(self):
		for row in self.tilegrid:
			for tile in row:
				print(tile.tile_id, end=" ")
			print()

	def render_map_to_image(self, filename):
		# Determine the size of the image in pixels
		self.width = len(self.tilegrid[0]) * TILE_SIZE
		self.height = len(self.tilegrid) * TILE_SIZE
		
		# Create a new image with a white background
		image = Image.new("RGBA", (self.width, self.height), "white")
		
		# Create a draw object
		draw = ImageDraw.Draw(image)
		
		# Iterate through each tile in the map
		#for i in tqdm(range(self.width * self.height)):
		for y, row in enumerate(self.tilegrid):
			for x, tile in enumerate(row):
				# Calculate the position of the tile in pixels
				x1 = x * TILE_SIZE
				y1 = y * TILE_SIZE
				image_to_paste = Image.open(tile.icon)
				image.paste(image_to_paste, (x1, y1))

		# Save the image to a file
		image.save(filename, "PNG")

new_map = Map(100, 50, tiles)
new_map.print_map()
new_map.render_map_to_image("test.png")