class Solution:
    def flipAndInvertImage(self, image):
        
        arrInvert = []
        arrReverse = []
        for i in  image:
            i.reverse()
            arrInvert = []
            for j in i:
                if j == 0:
                    j = 1
                else:
                    j = 0
                arrInvert.append(j)
            arrReverse.append(arrInvert)
        return arrReverse