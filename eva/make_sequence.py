
from sequence.SequenceManager import *
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

    # すべてのシーケンスクラスの列名を表示
    print(MVICondition.display_column_names())
    print(AVICondition.display_column_names())
    print(Resource.display_column_names())
    print(Loop.display_column_names())
    print(LoopTracking.display_column_names())
    print(Event.display_column_names())
    print(UserFunction.display_column_names())
    print(SetVariable.display_column_names())
    print(DataDumper.display_column_names())
    print(JudgeDumper.display_column_names())
    print(Judge.display_column_names())
    print(DataPlotter.display_column_names())
    print(PlotVariable.display_column_names())
    print(Breakpoint.display_column_names())
    print(DMEMReadCondition.display_column_names())
    print(PatternModify.display_column_names())
    print(PatternModifyDataEntries.display_column_names())
    print(TDRCal.display_column_names())
    print(ShmooCondition.display_column_names())
    print(SetResult.display_column_names())
    print(Power.display_column_names())
    print(CallSequence.display_column_names())
    print(Wait.display_column_names())
