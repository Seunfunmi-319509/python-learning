# def double_syrup(pumps):
#     return pumps * 2


triple = lambda x:x+3
print(triple(5))

scale_syrup = lambda ml: ml/30.0
print(scale_syrup(60.0))

greet = lambda name: "Hello, " + name
print(greet("Oluwaseun"))

sugar_level = "High"
get_pump_count = lambda level: 4 if level == "High" else 2

pumps_to_dispense = get_pump_count(sugar_level)
print(pumps_to_dispense)

check_size = lambda ounces:"large" if ounces >= 16 else "small"
print(check_size(12))
print(check_size(16))
