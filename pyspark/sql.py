from pyspark.sql.types import DoubleType, StructType
from pyspark.sql.functions import lit, col
from pyspark.sql import DataFrame
import random
import numpy
from functools import reduce
import math
import string

DISTINCT_NOMINAL = 5
STDDEV_NAME = "_std"


class DataGenerator:

    def __init__(self, DISTINCT_NOMINAL, STDDEV_NAME):
        self.DISTINCT_NOMINAL = DISTINCT_NOMINAL
        self.STDDEV_NAME = STDDEV_NAME

    def modeFlag(self, mode: str):
        """ comments
        """

        modeVal = {
            "ascending": False,
            "descending": True
        }
        return modeVal.get(mode)

    def lfold(self, func, nums, exp):
        """ comments
        """

        acc = []
        for i in range(len(nums)):
            result = reduce(func, nums[:i + 1], exp)
            acc.append(result)
        return acc

    def generateDoublesData(self, targetCount: int, start: float, step: float, mode: str):

        """ comments
        """

        stoppingPoint = (targetCount * step) + start
        doubleArray = list(numpy.arange(start, stoppingPoint, step))
        try:
            doubleArray = sorted(doubleArray, reverse=self.modeFlag(mode))
        except:
            if (mode == 'random'):
                random.shuffle(doubleArray)
            else:
                raise Exception(mode, " is not supported.")

        return doubleArray

    def generateDoublesMod(self, targetCount: int, start: float, step: float, mode: str, exp: float):

        """ comments
        """

        doubles = self.generateDoublesData(targetCount, start, step, mode)
        res = (lambda x, y: x + ((x + y) / x))

        return self.lfold(res, doubles, exp)

    def generateDoublesMod2(self, targetCount: int, start: float, step: float, mode: str):

        """ comments
        """

        doubles = self.generateDoublesData(targetCount, start, step, mode)

        func = (lambda x, y: (math.pow((x - y) / math.sqrt(y), 2)))
        sequenceEval = reduce(func, doubles, 0)

        res = (lambda x, y: (x + (x / y)) / x)
        return self.lfold(res, doubles, sequenceEval)

    def generateIntData(self, targetCount: int, start: int, step: int, mode: str):

        """ comments
        """

        stoppingPoint = (targetCount * step) + start
        intArray = list(range(start, stoppingPoint, step))
        try:
            intArray = sorted(intArray, reverse=self.modeFlag(mode))
        except:
            if (mode == 'random'):
                random.shuffle(intArray)
            else:
                raise Exception(mode, " is not supported.")

        return intArray

    def generateRepeatingIntData(self, targetCount: int, start: int, step: int, mode: str, distinctValues: int):

        """ comments
        """

        subStopPoint = (distinctValues * step) + start - 1
        distinctArray = list(range(start, subStopPoint, step))
        try:
            sortedArray = sorted(distinctArray, reverse=self.modeFlag(mode))
        except:
            if (mode != 'random'):
                raise Exception(mode, " is not supported.")

        outputArray = numpy.full((int(targetCount / (len(sortedArray) - 1)), len(sortedArray)),
                                 sortedArray).flatten().tolist()[:targetCount]
        if (mode == 'random'):
            random.shuffle(outputArray)

        return outputArray

    def getDoubleCols(self, schema: StructType):

        """ comments
        """

        return [s.name for s in schema if s.dataType == DoubleType()]

    def normalizeDoubleTypes(self, df: DataFrame):

        """ comments
        """
        doubleTypes = self.getDoubleCols(df.schema)
        stddevValues = df.select(doubleTypes).summary("stddev").first()

        for indx in range(0, len(doubleTypes)):
            df = df.withColumn(doubleTypes[indx] + STDDEV_NAME, col(doubleTypes[indx]) / stddevValues[indx + 1])
        return df

    def generateData(self, targetCount: int):

        """ comments
        """

        seq1 = self.generateIntData(targetCount, 1, 1, "ascending")
        seq2 = self.generateDoublesData(targetCount, 1.0, 1.0, "descending")
        seq3 = self.generateDoublesMod(targetCount, 1.0, 1.0, "ascending", 2.0)
        seq4 = list(map(lambda x: x * -10, self.generateDoublesMod2(targetCount, 1.0, 1.0, "ascending")))
        seq5 = self.generateRepeatingIntData(targetCount, 0, 5, "ascending", DISTINCT_NOMINAL)
        seq6 = self.generateDoublesMod2(targetCount, 1.0, 1.0, "descending")

        seqData: List[DataStructure] = []

        for i in range(0, targetCount):
            seqData.append(
                DataStructure(value1=seq1[i], value2=seq2[i].item(), value3=seq3[i].item(), value4=seq4[i].item(),
                              value5=seq5[i], value6=seq6[i].item()))

        return self.normalizeDoubleTypes(spark.createDataFrame(seqData))

    def generateCoordData(self, targetCount: int):

        """ comments
        """

        coordData = self.generateData(targetCount).withColumnRenamed("value2_std", "x1").withColumnRenamed("value3_std",
                                                                                                           "x2").withColumnRenamed(
            "value4_std", "y1").withColumnRenamed("value6_std", "y2").select("x1", "x2", "y1", "y2")
        return coordData

    def generateStringData(self, targetCount: int, uniqueValueCount: int):

        """ comments
        """
        orderedColl = list(string.ascii_lowercase)
        factor = int(targetCount / len(orderedColl))
        remain = targetCount % len(orderedColl)
        uniqueBuffer = list(string.ascii_lowercase)

        if (uniqueValueCount > len(orderedColl)):
            for x in range(0, factor):
                for y in orderedColl:
                    uniqueBuffer.append(y + str(x))

        uniqueArray = uniqueBuffer[:uniqueValueCount]

        if (uniqueValueCount > len(orderedColl)):
            uniqueArrayFactor = uniqueArray * factor
            uniqueArrayFactor.extend(uniqueArray[:remain])
            utputArray = uniqueArrayFactor
        else:
            outputArray = uniqueArray * int(targetCount / (uniqueValueCount - 1))

        return outputArray[:targetCount]

    def generateConcurrentData(self, targetCount: int, uniqueKeys: int):

        """ comments
        """

        seq1 = self.generateStringData(targetCount, uniqueKeys)
        seq2 = self.generateDoublesData(targetCount, 1.0, 5.0, "ascending")
        seq3 = self.generateDoublesData(targetCount, 0.0, 0.1, "descending")

        seqData: List[ConcurrentStructure] = []

        for i in range(0, targetCount):
            seqData.append(ConcurrentStructure(group=seq1[i], value1=seq2[i].item(), value2=seq3[i].item()))

        return spark.createDataFrame(seqData)