class PatternModify:
    def __init__(self):
        pass

    @staticmethod
    def display_column_names():
        columns = [
            "Type",
            "Start",
        ]
        return f"!Sequence_PatternModify\t" + "\t".join(columns)