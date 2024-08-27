class UserFunction:
    def __init__(self, sequence_number=0, function="Wait", unit="", siprefix="Auto", num_of_args="TRUE", args=None):

        self.sesquence_number=sequence_number
        self.function = function
        self.unit = unit
        self.siprefix = siprefix
        self.num_of_args = num_of_args
        self.args = args

    def __repr__(self):
        return (f"{self.sesquence_number}\t{self.function}\t{self.unit}\t{self.siprefix}\t"
                f"{self.num_of_args}\t'Variable'\t{self.args}")

    @staticmethod
    def display_column_names():
        columns = [
            "Function", "Unit", "SIPrefix", "NumOfArgs", "Args"
        ]
        return f"!Sequence_UserFunction\t" + "\t".join(columns)