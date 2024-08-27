class DMEMReadCondition:
    def __init__(self):
        pass

    @staticmethod
    def display_column_names():
        columns = [
            "BitLength",
            "FormatType",
            "OutputType",
            "CaptureVariable",
            "Pin"
        ]
        return f"!Sequence_DMEMReadCondition\t" + "\t".join(columns)