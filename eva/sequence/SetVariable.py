class SetVariable:

    def __init__(self, sequence_number=0, variable_name="value", mode="Set", value=0):
        self.sequence_number = sequence_number
        self.variable_name = variable_name
        self.mode = mode
        self.value = value

    def __repr__(self):
        return f"{self.sequence_number}\t{self.variable_name}\t{self.mode}\t{self.value}"

    @staticmethod
    def display_column_names():
        columns = [
            "VariableName", "Mode", "Value"
        ]
        return f"!Sequence_SetVariable\t" + "\t".join(columns)