class MapTile:
	def __init__(self, tile_id, density, icon, name, attributes, probability):
		self.tile_id = tile_id
		self.density = density #0 for noclip, 1 for solid
		self.icon = icon
		self.name = name
		self.attributes = attributes
		self.probability = probability