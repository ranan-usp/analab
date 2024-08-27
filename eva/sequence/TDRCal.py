class TDRCal:
    def __init__(self):
        pass

    @staticmethod
    def display_column_names():
        columns = [
            "ExecutionMode",
            "TDRFolder",
            "PBName",
            "OutputToConsole",
            "SelectPinToCalibrate",
            "PinName"
        ]
        return f"!Sequence_TDRCal\t" + "\t".join(columns)