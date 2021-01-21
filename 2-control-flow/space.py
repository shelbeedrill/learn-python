# Space Boxer 🥊
# Shelbeedrill

print("I have information for the following planets:\n")

print("   1. Mercury   2. Venus    3. Mars")
print("   4. Jupiter  5. Saturn  6. Uranus")
print("   7. Neptune\n")

weight = 185
planet = 3

# Write an if statement below:
if planet == 1:
  weight = weight * .38
elif planet == 2:
  weight = weight * .91
elif planet == 3:
  weight = weight * .38
elif planet == 4:
  weight = weight * 2.34
elif planet == 5:
  weight = weight * 1.06
elif planet == 6:
  weight = weight * .92
elif planet == 7:
  weight = weight * 1.19
else:
  print("I do not have data for that planet.")

print("Your weight: ", weight)
