class Event:
    def __init__(self, sequence_number = 0, resource = "VIN", event_type="RelayOnEvent", base_id=None, delta_time=0.002, setup_condition=None, overlap_area_order=None,
                 hw_sync_delay=None, loop_break_continue=None, start_id=None, sub_test_id=None, pattern_result_enabled=None,
                 comment=None, comment_left=None, comment_top=None, comment_width=None, comment_height=None, 
                 comment_visible=None, expand_all_judgements=None, add_offset_to_sub_test_id=None, 
                 conditional_branch_expression=None, is_enable="true", si_prefix=None, optimize=0, test_description=None):
        
        self.sequence_number = sequence_number
        self.resource = resource
        self.event_type = event_type
        self.base_id = base_id
        self.delta_time = delta_time
        self.setup_condition = setup_condition
        self.overlap_area_order = overlap_area_order
        self.hw_sync_delay = hw_sync_delay
        self.loop_break_continue = loop_break_continue
        self.start_id = start_id
        self.sub_test_id = sub_test_id
        self.pattern_result_enabled = pattern_result_enabled
        self.comment = comment
        self.comment_left = comment_left
        self.comment_top = comment_top
        self.comment_width = comment_width
        self.comment_height = comment_height
        self.comment_visible = comment_visible
        self.expand_all_judgements = expand_all_judgements
        self.add_offset_to_sub_test_id = add_offset_to_sub_test_id
        self.conditional_branch_expression = conditional_branch_expression
        self.is_enable = is_enable
        self.si_prefix = si_prefix
        self.optimize = optimize
        self.test_description = test_description

    def __repr__(self):

        if self.event_type in ["RelayOnEvent","PowerOnEvent","PowerOffEvent","RelayOffEvent"]:
            pass
        elif self.event_type in ["CallFunctionEvent","MeasureEvent"]:
            self.comment_visible = 0
            self.expand_all_judgements = 0
            self.add_offset_to_sub_test_id = 0
            self.si_prefix = "Auto"
        
        return (f"{self.event_id}\t{self.resource}\t{self.event_type}\t{self.base_id}\t{self.delta_time}\t"
                f"{self.setup_condition}\t{self.overlap_area_order}\t{self.hw_sync_delay}\t{self.loop_break_continue}\t"
                f"{self.start_id}\t{self.sub_test_id}\t{self.pattern_result_enabled}\t{self.comment}\t"
                f"{self.comment_left}\t{self.comment_top}\t{self.comment_width}\t{self.comment_height}\t"
                f"{self.comment_visible}\t{self.expand_all_judgements}\t{self.add_offset_to_sub_test_id}\t"
                f"{self.conditional_branch_expression}\t{self.is_enable}\t{self.si_prefix}\t{self.optimize}\t"
                f"{self.test_description}")


    @staticmethod
    def display_column_names():
        columns = [
            "Resource", "Type", "BaseId", "DeltaTime", "SetupCondition", "OverlapAreaOrder", "HWSyncDelay", 
            "LoopBreakContinue", "StartId", "SubTestId", "PatternResultEnabled", "Comment", "CommentLeft", 
            "CommentTop", "CommentWidth", "CommentHeight", "CommentVisible", "ExpandAllJudgements", 
            "AddOffsetToSubTestID", "ConditionalBranchExpression", "IsEnable", "SIPrefix", "Optimize", 
            "TestDescription"
        ]
        return f"!Sequence_Event\t" + "\t".join(columns)