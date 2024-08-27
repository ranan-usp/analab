class Loop:
    def __init__(self, name = "Loop(1)",loop_type="Counter", counter_variable="idx0", count=100, 
                 evaluate_timing="Begin", 
                 evaluate_condition=None, init_expr_status=0, 
                 init_expr=None, cond_expr_status="false", cond_expr=None, 
                 loop_expr_status=0, loop_expr=None, 
                 external_control_enabled=0):
        self.name = name
        self.loop_type = loop_type
        self.counter_variable = counter_variable
        self.count = count
        self.evaluate_timing = evaluate_timing
        self.evaluate_condition = evaluate_condition
        self.init_expr_status = init_expr_status
        self.init_expr = init_expr
        self.cond_expr_status = cond_expr_status
        self.cond_expr = cond_expr
        self.loop_expr_status = loop_expr_status
        self.loop_expr = loop_expr
        self.external_control_enabled = external_control_enabled

    def __repr__(self):
        return (f"{self.name}\t{self.loop_type}\t{self.counter_variable}\t{self.count}\t"
                f"{self.evaluate_timing}\t{self.evaluate_condition}\t{self.init_expr_status}\t"
                f"{self.init_expr}\t{self.cond_expr_status}\t{self.cond_expr}\t{self.loop_expr_status}\t"
                f"{self.loop_expr}\t{self.external_control_enabled}")

    @staticmethod
    def display_column_names():
        columns = [
            "LoopType", "CounterVariable", "Count", "EvaluateTiming", "EvaluateCondition", "InitExprStatus", 
            "InitExpr", "CondExprStatus", "CondExpr", "LoopExprStatus", "LoopExpr", "ExternalControlEnabled"
        ]
        return f"!Sequence_Loop\t" + "\t".join(columns)