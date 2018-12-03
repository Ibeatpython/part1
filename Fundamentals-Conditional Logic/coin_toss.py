from random import randint

trails = 10000
flips = 0

for trail in range(0, trails):
	flips += 1      # first flips
	if randint(0, 1) == 0:     # flipped tails on first flips
		while randint(0, 1) == 0:  # keep flipping tails
			flips += 1    
		flips += 1   # finnally flipped heads

	else:   # otherwise flipped heads on first flips
		while randint(0, 1) == 1:    #keeping flipping heads
			flips += 1

		flips += 1    #finally flipped tails


print(flips / trails)
