from pyson import PySON

schema = file("sample.json", "r").read()

obj = PySON(schema)

print("Orig Schema:")
print("------------")
print(obj)
print("\n\n")


for i in range(0, obj.backpack.slots):
    propId = obj.backpack.items[i][0]
    propName = obj.props.getValue(propId)
    print("Carrying: %s" % propName)

#"true" or "false" values strings are convert to boolean
print("\nOld CanHeal: %s" % obj.backpack.items[1][1].CanHeal)

#Change value
obj.backpack.items[1][1].CanHeal = True

print("New CanHeal: %s\n" % obj.backpack.items[1][1].CanHeal)


print("\nOld Health: %s" % obj.player.health)

#Change value
obj.player.health = 100

print("New Health: %s\n" % obj.player.health)


print("Player: %s" % obj.player.name)
print("Location: %i, %i" % (obj.player.pos.x, obj.player.pos.y))
print("\n\n")

print "Updated Schema reflecting changes:"
print "----------------------------------"
print(obj)
print("\n\n")

print("Using dump to get an overview of hiearchy:")
print("----------------------------------------")
obj.dump()
