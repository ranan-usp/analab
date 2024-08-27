class TitleCondition:

    def __init__(self, title = "", 
                 auto_power_off = "TRUE",
                 timeout_enabled = 0,
                 timeout_value = None,
                 timeout_ignore = 0,
                 dutiteration_mode = "Parallel",
                 comment = None,
                 default_code = 0,
                 default_code_comment = None,
                 num_of_return_code = 0,
                 return_code = None):
        self.title = title
        self.auto_power_off = auto_power_off
        self.timeout_enabled = timeout_enabled
        self.timeout_value = timeout_value
        self.timeout_ignore = timeout_ignore
        self.dutiteration_mode = dutiteration_mode
        self.comment = comment
        self.default_code = default_code
        self.default_code_comment = default_code_comment
        self.num_of_return_code = num_of_return_code
        self.return_code = return_code
    
        
    def __repr__(self):
        return (f"\t{self.title}\t{self.auto_power_off}\t{self.timeout_enabled}\t{self.timeout_value}\t"
                f"{self.timeout_ignore}\t{self.dut_iteration_mode}\t{self.comment}\t{self.default_code}\t"
                f"{self.default_code_comment}\t{self.num_of_return_code}\t{self.return_code}")

    @staticmethod
    def display_column_names():
        columns = [
            "!Sequence", "AutoPowerOff", "TimeoutEnabled", "TimeoutValue", "TimeoutIgnore", 
            "DUTIterationMode", "Comment", "DefaultCode", "DefaultCodeComment", 
            "NumOfReturnCode", "ReturnCode"
        ]
        return f"!Sequence\t" + "\t".join(columns)
