class CallSequence:
    def __init__(self):
        pass

    @staticmethod
    def display_column_names():
        columns = [
            "Sequence",
            "MultipleDUTSettings",
            "ResultSettingsEnable",
            "ResultSettings",
            "ReturnCodeSettingsEnable",
            "ReturnCodeSettings"
        ]
        return f"!Sequence_CallSequence\t" + "\t".join(columns)