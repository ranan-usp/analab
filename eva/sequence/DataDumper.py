class DataDumper:
    def __init__(self, 
                 sequence_number = 0,
                 variable_dumper = "TRUE", 
                 dump_variable_name = "value", 
                 store_mode = "Overwrite", 
                 report_enable = "TRUE", 
                 dump_value_type = None):

        self.sequence_number = sequence_number
        self.variable_dumper = variable_dumper
        self.dump_variable_name = dump_variable_name
        self.store_mode = store_mode
        self.report_enable = report_enable
        self.dump_value_type = dump_value_type

    def __repr__(self):
        return (f"{self.sequence_number}\t{self.variable_dumper}\t{self.dump_variable_name}\t"
                f"{self.store_mode}\t{self.report_enable}\t{self.dump_value_type}")

    @staticmethod
    def display_column_names():
        columns = [
            "VariableDumper", "DumpVariableName", "StoreMode", "ReportEnable", "DumpValueType"
        ]
        return f"!Sequence_DataDumper\t" + "\t".join(columns)