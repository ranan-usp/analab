class SequenceManager:
    def __init__(self):
        self.sequence = {}
        self.sequence['!Sequence'] = []
        self.sequence['!Sequence_MVICondition'] = []
        self.sequence['!Sequence_AVICondition'] = []
        self.sequence['!Sequence_Resource'] = []
        self.sequence['!Sequence_Loop'] = []
        self.sequence['!Sequence_LoopTracking'] = []
        self.sequence['!Sequence_Event'] = []
        self.sequence['!Sequence_UserFunction'] = []
        self.sequence['!Sequence_SetVariable'] = []
        self.sequence['!Sequence_DataDumper'] = []
        self.sequence['!Sequence_JudgeDumper'] = []
        self.sequence['!Sequence_Judge'] = []
        self.sequence['!Sequence_DataPlotter'] = []
        self.sequence['!Sequence_PlotVariable'] = []
        self.sequence['!Sequence_Breakpoint'] = []
        self.sequence['!Sequence_DMEMReadCondition'] = []
        self.sequence['!Sequence_PatternModify'] = []
        self.sequence['!Sequence_PatternModifyDataEntries'] = []
        self.sequence['!Sequence_TDRCal'] = []
        self.sequence['!Sequence_ShmooCondition'] = []
        self.sequence['!Sequence_SetResult'] = []
        self.sequence['!Sequence_Power'] = []
        self.sequence['!Sequence_CallSequence'] = []
        self.sequence['!Sequence_Wait'] = []

    def add_to_sequence(self, key, value):
        if key in self.sequence:
            self.sequence[key].append(value)
