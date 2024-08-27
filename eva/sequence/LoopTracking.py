class LoopTracking:
    def __init__(self, name="Loop(1)", track_variable="VIN", expression="0+idx0*0.01"):
        self.name = name
        self.track_variable = track_variable
        self.expression = expression

    def __repr__(self):
        return f"{self.name}\t{self.track_variable}\t{self.expression}"

    @staticmethod
    def display_column_names():
        columns = [
            "TrackVariable", "Expression"
        ]
        return f"!Sequence_LoopTracking\t" + "\t".join(columns)
