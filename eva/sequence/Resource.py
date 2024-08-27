class Resource:
    setup_id_counter = 0  # クラス変数としてリソースのセットアップIDを管理

    def __init__(self, 
                 name, resource_type, 
                 initial_setup_id = 0, setup_condition = 0, 
                 pre_exec_id = None,post_exec_id = None,
                 initial_setup_enable = "TRUE",
                 pre_func_enable=False, post_func_enable=False):
        
        self.name = name
        self.resource_type = resource_type
        self.initial_setup_id = initial_setup_id  # 現在のセットアップIDを設定
        self.setup_condition = setup_condition  # 現在のセットアップ条件を設定

        self.pre_exec_id = pre_exec_id
        self.post_exec_id = post_exec_id
        self.initial_setup_enable = initial_setup_enable
        self.pre_func_enable = pre_func_enable
        self.post_func_enable = post_func_enable

    def __repr__(self):

        if self.resource_type == "Loop":
            self.initial_setup_id = None
            self.setup_condition = None
            self.initial_setup_enable = None

        return (f"{self.name}\t{self.resource_type}\t{self.initial_setup_id}\t{self.setup_condition}\t"
                f"{self.pre_exec_id}\t{self.post_exec_id}\t"
                f"{self.initial_setup_enable}\t{self.pre_func_enable}\t{self.post_func_enable}")
    
    @staticmethod
    def display_column_names():
        columns = [
            "ResourceType", "InitialSetupId", "SetupCondition", "PreExecId", "PostExecId",
            "InitialSetupEnable", "PreFuncEnable", "PostFuncEnable"
        ]
        return f"!Sequence_Resource\t" + "\t".join(columns)


