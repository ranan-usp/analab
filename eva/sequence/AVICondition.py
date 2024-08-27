class AVICondition:
    sequence_counter = 0  # クラス変数としてシーケンス番号を管理

    def __init__(self, sequence_number = 0, high_accuracy_src=0, high_accuracy_meas=0, 
                 source_type="V", source_mode="DC", output=0, 
                 source_range="Auto", slew_rate=None, band="Normal", 
                 clamp_hi=None, clamp_lo=None, 
                 swg_def_level=0, swg_def_time=0, swg_start=0, swg_stop=0, 
                 swg_step=0, swg_delta_time="5u", 
                 awg_file='""', awg_loop_count=1, awg_step_time="2u", awg_coefficient=1, awg_dc_offset=None, 
                 measure_type='I', measure_mode='Single', measure_range='0.08', 
                 filter_="2K", average=None, average_count=1, average_time='5u', 
                 swg_wait="1u", swg_comp_type="High", swg_level=0, 
                 sampling_count=1, sampling_time='5u', 
                 trigger='FreeRun',trigger_type="High", trigger_level=0, trigger_delay='1u', 
                 compare_ch='Self-CH', sweep_ch='Self-CH', 
                 stack_count="true", stack_sts=None, stack_individual_setting="false", 
                 slave_ch1=0, slave_ch2=0, slave_ch3=0, slave_ch4=0, slave_ch5=0, 
                 file_name_variable='true', parallel_sts='false', parallel_pin_name=None):
        
        self.sequence_number = sequence_number
        self.high_accuracy_src = high_accuracy_src
        self.high_accuracy_meas = high_accuracy_meas
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
        self.swg_comp_type = swg_comp_type
        self.swg_level = swg_level
        self.sampling_count = sampling_count
        self.sampling_time = sampling_time
        self.trigger = trigger
        self.trigger_type = trigger_type
        self.trigger_level = trigger_level
        self.trigger_delay = trigger_delay
        self.compare_ch = compare_ch
        self.sweep_ch = sweep_ch
        self.stack_count = stack_count
        self.stack_sts = stack_sts
        self.stack_individual_setting = stack_individual_setting
        self.slave_ch1 = slave_ch1
        self.slave_ch2 = slave_ch2
        self.slave_ch3 = slave_ch3
        self.slave_ch4 = slave_ch4
        self.slave_ch5 = slave_ch5
        self.file_name_variable = file_name_variable
        self.parallel_sts = parallel_sts
        self.parallel_pin_name = parallel_pin_name

    def __repr__(self):
        return (f"{self.sequence_number}\t{self.sequence_number}\t{self.high_accuracy_src}\t{self.high_accuracy_meas}\t{self.source_type}\t"
                f"{self.source_mode}\t{self.output}\t{self.source_range}\t{self.slew_rate}\t{self.band}\t{self.clamp_hi}\t"
                f"{self.clamp_lo}\t{self.swg_def_level}\t{self.swg_def_time}\t{self.swg_start}\t{self.swg_stop}\t"
                f"{self.swg_step}\t{self.swg_delta_time}\t{self.awg_file}\t{self.awg_loop_count}\t{self.awg_step_time}\t"
                f"{self.awg_coefficient}\t{self.awg_dc_offset}\t{self.measure_type}\t{self.measure_mode}\t"
                f"{self.measure_range}\t{self.filter}\t{self.average}\t{self.average_count}\t{self.average_time}\t"
                f"{self.swg_wait}\t{self.swg_comp_type}\t{self.swg_level}\t{self.sampling_count}\t{self.sampling_time}\t"
                f"{self.trigger}\t{self.trigger_type}\t{self.trigger_level}\t{self.trigger_delay}\t{self.compare_ch}\t"
                f"{self.sweep_ch}\t{self.stack_count}\t{self.stack_sts}\t{self.stack_individual_setting}\t"
                f"{self.slave_ch1}\t{self.slave_ch2}\t{self.slave_ch3}\t{self.slave_ch4}\t{self.slave_ch5}\t"
                f"{self.file_name_variable}\t{self.parallel_sts}\t{self.parallel_pin_name}")

    @staticmethod
    def display_column_names():
        columns = [
            "SequenceNumber", "HighAccracySrc", "HighAccracyMeas", "SourceType", "SourceMode", "Output", 
            "SourceRange", "SlewRate", "Band", "ClampHi", "ClampLo", "SwgDefLevel", "SwgDefTime", 
            "SwgStart", "SwgStop", "SwgStep", "SwgDeltaTime", "AwgFile", "AwgLoopCount", "AwgStepTime", 
            "AwgCoefficient", "AwgDCOffset", "MeasureType", "MeasureMode", "MeasureRange", "Filter", 
            "Average", "AverageCount", "AverageTime", "SwgWait", "SwgCompType", "SwgLevel", "SamplingCount", 
            "SamplingTime", "Trigger", "TriggerType", "TriggerLevel", "TriggerDelay", "CompareCh", 
            "SweepCh", "StackCount", "StackSts", "StackIndividualSetting", "SlaveCh1", "SlaveCh2", 
            "SlaveCh3", "SlaveCh4", "SlaveCh5", "FileNameVariable", "ParallelSts", "ParallelPinName"
        ]
        return f"!Sequence_AVICondition\t" + "\t".join(columns)
