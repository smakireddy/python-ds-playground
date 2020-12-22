class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        for i in range(len(self.__elements)):
            for j in range(i+1,len(self.__elements)):
                diff = abs(self.__elements[i] - self.__elements[j])
                if diff > self.maximumDifference:
                    self.maximumDifference = diff


# End of Difference class

# _ = input()
# a = [int(e) for e in input().split(' ')]
a = [1,2,5]
d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
