from collections import Counter

HALIBUT = 'halibut'
MACKEREL = 'mackerel'
SALMON = 'salmon'
SNAPPER = 'snapper'
SQUID = 'squid'
TUNA = 'tuna'

scramble = input()
c = Counter(scramble)

# squid is the only fish with 'q'
# remove squid
# halibut is the only fish with 'i'
# remove halibut
# tuna is the only fish with 'u'
# remove tuna
# snapper is the only fish with 'p'
# remove snapper
# salmon is the only fish with 's'
# remove salmon
# mackerel is the only fish left


def removeFish(fish, counter, numFish):
    for ch in fish:
        counter[ch] -= numFish


numSquid = c['q']
removeFish(SQUID, c, numSquid)
numHalibut = c['i']
removeFish(HALIBUT, c, numHalibut)
numTuna = c['u']
removeFish(TUNA, c, numTuna)
numSnapper = c['p'] // 2
removeFish(SNAPPER, c, numSnapper)
numSalmon = c['s']
removeFish(SALMON, c, numSalmon)
numMackerel = c['m']
removeFish(MACKEREL, c, numMackerel)

print(f'''halibut:{numHalibut}
mackerel:{numMackerel}
salmon:{numSalmon}
snapper:{numSnapper}
squid:{numSquid}
tuna:{numTuna}''')


# Alternative method:
# halibut is the only fish with 'i'
# remove halibut
# tuna is the only fish with 't'
# squid is the only fish with 'q'
# snapper is the only fish with 'p'
# salmon is the only fish with 'o'
# mackerel is the only fish with 'k'
