class MVICondition:
    
    sequence_counter = 0  # クラス変数としてシーケンス番号を管理

    def __init__(self, 
                 sequence_number = 0,
                 source_type="V", 
                 source_mode="DC", 
                 output=0, 
                 source_range="Auto", 
                 slew_rate=None, 
                 band="Normal", 
                 clamp_hi=None, clamp_lo=None, 
                 swg_def_level=0, swg_def_time=0, 
                 swg_start=0, swg_stop=0, swg_step=0, swg_delta_time="5u", 
                 awg_file='""', awg_loop_count=1, awg_step_time="2u", awg_coefficient=1, awg_dc_offset=None, 
                 measure_type='I', measure_mode='Single', measure_range=0.08, 
                 filter_="2K", 
                 average="false", average_count=1, average_time='5u', 
                 swg_wait=0, swg_edge='P', swg_comp_type=None, swg_level=0, 
                 sampling_count=1, sampling_time=0, 
                 trigger='FreeRun', trigger_edge='P', trigger_type=None, trigger_level=0, trigger_delay=0, 
                 compare_ch='Self-CH', sweep_ch='Self-CH', 
                 file_name_variable="true", 
                 parallel_sts='false', parallel_pin_name=None):
        
        self.sequence_number = sequence_number
        self.source_type = source_type
        self.source_mode = source_mode
        self.output = output
        self.source_range = source_range
        self.slew_rate = slew_rate
        self.band = band
        self.clamp_hi = clamp_hi
        self.clamp_lo = clamp_lo
        self.swg_def_level = swg_def_level
        self.swg_def_time = swg_def_time
        self.swg_start = swg_start
        self.swg_stop = swg_stop
        self.swg_step = swg_step
        self.swg_delta_time = swg_delta_time
        self.awg_file = awg_file
        self.awg_loop_count = awg_loop_count
        self.awg_step_time = awg_step_time
        self.awg_coefficient = awg_coefficient
        self.awg_dc_offset = awg_dc_offset
        self.measure_type = measure_type
        self.measure_mode = measure_mode
        self.measure_range = measure_range
        self.filter = filter_
        self.average = average
        self.average_count = average_count
        self.average_time = average_time
        self.swg_wait = swg_wait
        self.swg_edge = swg_edge
        self.swg_comp_type = swg_comp_type
        self.swg_level = swg_level
        self.sampling_count = sampling_count
        self.sampling_time = sampling_time
        self.trigger = trigger
        self.trigger_edge = trigger_edge
        self.trigger_type = trigger_type
        self.trigger_level = trigger_level
        self.trigger_delay = trigger_delay
        self.compare_ch = compare_ch
        self.sweep_ch = sweep_ch
        self.file_name_variable = file_name_variable
        self.parallel_sts = parallel_sts
        self.parallel_pin_name = parallel_pin_name

    def __repr__(self):
        return (f"{self.sequence_number}\t{self.source_type}\t{self.source_mode}\t{self.output}\t{self.source_range}\t"
                f"{self.slew_rate}\t{self.band}\t{self.clamp_hi}\t{self.clamp_lo}\t{self.swg_def_level}\t"
                f"{self.swg_def_time}\t{self.swg_start}\t{self.swg_stop}\t{self.swg_step}\t{self.swg_delta_time}\t"
                f"{self.awg_file}\t{self.awg_loop_count}\t{self.awg_step_time}\t{self.awg_coefficient}\t"
                f"{self.awg_dc_offset}\t{self.measure_type}\t{self.measure_mode}\t{self.measure_range}\t"
                f"{self.filter}\t{self.average}\t{self.average_count}\t{self.average_time}\t"
                f"{self.swg_wait}\t{self.swg_edge}\t{self.swg_comp_type}\t{self.swg_level}\t{self.sampling_count}\t"
                f"{self.sampling_time}\t{self.trigger}\t{self.trigger_edge}\t{self.trigger_type}\t{self.trigger_level}\t"
                f"{self.trigger_delay}\t{self.compare_ch}\t{self.sweep_ch}\t{self.file_name_variable}\t"
                f"{self.parallel_sts}\t{self.parallel_pin_name}")
    
    @staticmethod
    def display_column_names():
        columns = [
            "SequenceNumber", "SourceType", "SourceMode", "Output", "SourceRange", "SlewRate", "Band",
            "ClampHi", "ClampLo", "SwgDefLevel", "SwgDefTime", "SwgStart", "SwgStop", "SwgStep", "SwgDeltaTime",
            "AwgFile", "AwgLoopCount", "AwgStepTime", "AwgCoefficient", "AwgDCOffset", "MeasureType", "MeasureMode",
            "MeasureRange", "Filter", "Average", "AverageCount", "AverageTime", "SwgWait", "SwgEdge", "SwgCompType",
            "SwgLevel", "SamplingCount", "SamplingTime", "Trigger", "TriggerEdge", "TriggerType", "TriggerLevel",
            "TriggerDelay", "CompareCh", "SweepCh", "FileNameVariable", "ParallelSts", "ParallelPinName"
        ]
        return f"!Sequence_MVICondition\t" + "\t".join(columns)
