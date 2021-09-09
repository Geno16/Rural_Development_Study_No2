#Created <Put Creation Date in ISO here!>
#Copyright Spencer W. Leifeld

#Public Library Imports
import statistics

from pyspark.sql.types import StringType, StructField

def ZScore_UDF(column):
    mean = statistics.mean(column)
    std = statistics.stdev(column)

    for c in column:
        c = (c - mean)/std

    return column
        