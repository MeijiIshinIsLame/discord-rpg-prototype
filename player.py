class Player:
	def __init__(self, hp, x, y, items, strength, luck):
		self.hp = hp
		self.x = x
		self.y = y
		self.items = items
		self.strength = strength
		self.action_points = 50
		self.luck = luck # for item scavaging
		
	def take_damage(self, damage):
		self.hp -= damage
		
	def pick_up_item(self, item):
		self.items.append(item)
		
	def use_ap(self, action_point_amount):
		if self.action_points >= action_point_amount:
			ability_name.use()
			self.action_points -= action_point_amount
		else:
			print("Not enough ability points!")