
import math as Math
def de(mode, imgdata):
    aa = Math.ceil(3 * mode / 8)
    n = imgdata.width * imgdata.height
    j = 0
    k = ""
    i = 1
    mlist = [1, 2, 4, 8, 16, 32, 64, 128]
    word = ""
    blist = None
    blength = 0


    while i < n and (word.length == 0 or word.slice(-1).charCodeAt(0) > 0):
        k = k + (imgdata.data[4 * i] + 256).toString(2).slice(-mode)
        k = k + (imgdata.data[4 * i + 1] + 256).toString(2).slice(-mode)
        k = k + (imgdata.data[4 * i + 2] + 256).toString(2).slice(-mode)
        i +=1
        for  ii in range(0,aa):
            if k.length >= 8 and (word.length == 0 or word.slice(-1).charCodeAt(0) > 0):
                word = word + chr(int(k.slice(0, 8), 2))
                k = k.slice(8)

    # // word分隔符: ","
    blength = int(word.split(chr(1))[0])
    if not (blength > -1):
        raise Exception("error")

    if not (word.split(chr(1)).length > 2):
        raise Exception("error")

    blist = Uint8Array(blength)

    if k.length >= 8 and j < blength:
        blist[j] = int(k.slice(0, 8), 2)
        k = k.slice(8)
        j+=1

    while i < n and j < blength:
        k = k + (imgdata.data[4 * i] + 256).toString(2).slice(-mode)
        k = k + (imgdata.data[4 * i + 1] + 256).toString(2).slice(-mode)
        k = k + (imgdata.data[4 * i + 2] + 256).toString(2).slice(-mode)
        i+=1
        for ii in range(0,aa):
            if k.length >= 8 and j < blength:
                blist[j] = int(k.slice(0, 8), 2)
                k = k.slice(8)
                j+=1

    return [word.split(chr(0))[0].split(chr(1)), blist]
