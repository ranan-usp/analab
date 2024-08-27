class DataPlotter:
    def __init__(self, sequence_number = 0, enabled=0, name="", xlabel="", ylabel="", variable_name=""):
        
        self.sequence_number = sequence_number
        self.enabled = enabled
        self.name = name
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.variable_name = variable_name

    def __repr__(self):
        return (f"{self.sequence_number}\t{self.enabled}\t{self.name}\t{self.xlabel}\t"
                f"{self.ylabel}\t{self.variable_name}")

    @staticmethod
    def display_column_names():
        columns = [
            "Enabled", "Name", "XLabel", "YLabel", "VariableName(PlotEvent)"
        ]
        return f"!Sequence_DataPlotter\t" + "\t".join(columns)