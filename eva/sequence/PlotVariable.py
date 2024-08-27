class PlotVariable:
    def __init__(self, sequence_number = 0, enabled=0, name=""):
        
        self.sequence_number = sequence_number
        self.enabled = enabled
        self.name = name

    def __repr__(self):
        return (f"{self.sequence_number}\t{self.enabled}\t{self.name}")

    @staticmethod
    def display_column_names():
        columns = [
            "Enabled", "Name"
        ]
        return f"!Sequence_PlotVariable\t" + "\t".join(columns)