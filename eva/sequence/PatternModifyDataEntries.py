class PatternModifyDataEntries:
    def __init__(self):
        pass

    @staticmethod
    def display_column_names():
        columns = [
            "DataEntry",
            "Pin",
        ]
        return f"!Sequence_PatternModifyDataEntries\t" + "\t".join(columns)