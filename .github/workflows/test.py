def testformny(index, money):
    shouldmny = smtlst[index-1]["money"]
    user = zzrlst[-1]["user"]
    if money > shouldmny:
        pass
    if money < shouldmny:
        zzrmoney(zzrmnys[index])
    else:
        startsz(zzrmnys["user"],smtlst[index-1]["count"])
