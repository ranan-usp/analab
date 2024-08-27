class Judge:
    def __init__(self, 
                 sequence_number = 0,
                 enabled = 0, 
                 limit_named = 0, 
                 limit_name = None, 
                 upper_flag = 0, 
                 upper_limit = None, 
                 lower_flag = 0, 
                 lower_limit = None):
        
        self.sequence_number = sequence_number
        self.enabled = enabled
        self.limit_named = limit_named
        self.limit_name = limit_name
        self.upper_flag = upper_flag
        self.upper_limit = upper_limit
        self.lower_flag = lower_flag
        self.lower_limit = lower_limit

    def __repr__(self):
        return (f"{self.sequence_number}\t{self.enabled}\t{self.limit_named}\t{self.limit_name}\t"
                f"{self.upper_flag}\t{self.upper_limit}\t{self.lower_flag}\t{self.lower_limit}")

    @staticmethod
    def display_column_names():
        columns = [
            "Enabled", "LimitNamed", "LimitName", "UpperFlag", "UpperLimit", "LowerFlag", "LowerLimit"
        ]
        return f"!Sequence_Judge\t" + "\t".join(columns)