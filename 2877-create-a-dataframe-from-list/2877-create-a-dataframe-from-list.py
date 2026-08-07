import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    columnName=['student_id','age']
    result = pd.DataFrame(student_data, columns=columnName)
    return result

    