# Try to design a imaginary universe like the author of The Three-Body Problem mentioned in his book.

from random import randint

# Worlds Simulation
#
# The Universe
#   Defined as a plane
#
# World Attributes
#   world_size
#   resource
#   population
#   world_occupied_rate
#   life_standard
#   distance_between_worlds(a, b)
#   inter_world_activity
#   inter_world_population_change
#   inter_world_trade_efficiency
#   military_strength
#   invasion_tendency
#   society_lifetime_left
#     society is dead if society_lifetime_left =< 0
#
# Other considerations:
#   time


# Define Universe
universe_center = [0, 0]

print "\n"
print "The center of the Universe is:", universe_center



# 1st world: Equilibrium One

# Define inital state
world_name = "Equilibrium One"
world_size = randint(1, 100)
resource = world_size
population = world_size
life_standard = resource / population
inter_world_activity = 0
# inter_world_population_change =
# inter_world_trade_efficiency =
# military_strength =
# invation_tendency =

print "\n"
print world_name, "Status:"
print "world size =", world_size
print "resource =", resource
print "population =", population
print "life standard =", life_standard
print "inter world activity =", inter_world_activity


# 2nd world: Dying One

# Define initial state
world_name = "Dead One"
world_size = randint(1, 100)
resource_fraction_base = world_size
resource = randint(1, resource_fraction_base)
population_min = int(resource + 1)
population_max = int(world_size + 1)
population = randint(population_min, population_max)
world_occupied_rate = int(float(population) / float(world_size) * 1000) / 100.0
life_standard = int(float(resource) / float(population) * 1000) / 10.0
inter_world_activity = 0
society_lifetime_left = resource - population

print "\n"
print world_name, "Status:"
print "world size =", world_size
print "resource = ", resource
print "population =", population
print "world occupied rate =", world_occupied_rate, "%"
print "life standard =", life_standard, "%"
print "inter world activity =", inter_world_activity
print "society life time left =", society_lifetime_left



# 3rd world: Random One

# Define initial state
world_name = "Random One"
world_size = randint(1, 100)
resource_fraction_base = int(world_size)
resource = randint(0, resource_fraction_base)
population_min = 0
population_max = int(world_size)
population = randint(population_min, population_max)
world_occupied_rate = int(float(population) / float(world_size) * 1000) / 100.0
inter_world_activity = 0
coordinate_x = randint(0, 10 ** 14)
coordinate_y = randint(0, 10 ** 14)
planet_coordinates = [coordinate_x, coordinate_y]

if population == 0:
  life_standard = 0
else:
  life_standard = int(float(resource) / float(population) * 1000) / 10.0

if resource - population < 0:
  society_lifetime_left = 0
else:
  society_lifetime_left = resource - population


print "\n"
print world_name, "Status:"
print "planet coordinates =", planet_coordinates
print "world size =", world_size
print "resource = ", resource
print "population =", population
print "world occupied rate =", world_occupied_rate, "%"
print "life standard =", life_standard, "%"
print "inter world activity =", inter_world_activity
print "society life time left =", society_lifetime_left
