
from sequence.SequenceManager import *
from sequence.TitleCondition import *
from sequence.AVICondition import *
from sequence.MVICondition import *
from sequence.Resource import *
from sequence.Loop import *
from sequence.LoopTracking import *
from sequence.Event import *
from sequence.UserFunction import *
from sequence.SetVariable import *
from sequence.DataDumper import *
from sequence.JudgeDumper import *
from sequence.Judge import *
from sequence.DataPlotter import *
from sequence.PlotVariable import *
from sequence.Breakpoint import *
from sequence.DMEMReadCondition import *
from sequence.PatternModify import *
from sequence.PatternModifyDataEntries import *
from sequence.TDRCal import *
from sequence.ShmooCondition import *
from sequence.SetResult import *
from sequence.Power import *
from sequence.CallSequence import *
from sequence.Wait import *

if __name__ == '__main__':

    # SequenceManagerのインスタンスを作成
    sequence_manager = SequenceManager()

    print(TitleCondition.display_column_names())
    # テスト: インスタンス作成と出力
    title_inst = TitleCondition(title="EN_Input_Current")
    print(title_inst)    

    # すべてのシーケンスクラスの列名を表示
    print(MVICondition.display_column_names())
    mvi_inst = MVICondition(sequence_number=36,source_type="V",output="VIN_TYP")
    print(mvi_inst)

    print(AVICondition.display_column_names())
    avi_inst = AVICondition(sequence_number=1,source_type="V",output=0,source_range=8)
    print(avi_inst)
    avi_inst = AVICondition(sequence_number=55,source_type="V",output=5,source_range=8)
    print(avi_inst)

    print(Resource.display_column_names())
    resource_inst = Resource(name="VIN",resource_type="MVI",initial_setup_id=36)

    print(Loop.display_column_names())
    print()

    print(LoopTracking.display_column_names())
    print()

    print(Event.display_column_names())
    # "RelayOnEvent","PowerOnEvent","PowerOffEvent","RelayOffEvent
    # "CallFunctionEvent","MeasureEvent", "SetupEvent"
    event_inst = Event(sequence_number=38,resource="VIN",type="PowerOnEvent",base_id=None)
    event_inst = Event(sequence_number=4,resource="EN",type="PowerOnEvent",base_id=None)
    event_inst = Event(sequence_number=53,resource="EN",type="CallFunctionEvent",base_id=4)
    event_inst = Event(sequence_number=55,resource="EN",type= "SetupEvent",base_id=53)
    event_inst = Event(sequence_number=56,resource="EN",type="MeasureEvent",base_id=55)
    event_inst = Event(sequence_number=12,resource="EN",type="PowerOffEvent",base_id=56)
    event_inst = Event(sequence_number=45,resource="VIN",type="PowerOffEvent",base_id=12)

    print(UserFunction.display_column_names())
    userfunc_inst = UserFunction(sequence_number=53,function="Wait")
    print()
    print(SetVariable.display_column_names())
    print()

    print(DataDumper.display_column_names())
    print()
    print(JudgeDumper.display_column_names())
    print()
    print(Judge.display_column_names())
    print()
    print(DataPlotter.display_column_names())
    print()
    
    print(PlotVariable.display_column_names())
    print()
    print(Breakpoint.display_column_names())
    print()
    print(DMEMReadCondition.display_column_names())
    print()
    print(PatternModify.display_column_names())
    print()
    print(PatternModifyDataEntries.display_column_names())
    print()
    print(TDRCal.display_column_names())
    print()
    print(ShmooCondition.display_column_names())
    print()
    print(SetResult.display_column_names())
    print()
    print(Power.display_column_names())
    print()
    print(CallSequence.display_column_names())
    print()
    print(Wait.display_column_names())
    print()
