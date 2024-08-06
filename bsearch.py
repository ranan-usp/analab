import copy
import time

def binary_search_threshold_increasing(low,high,epsilon):

    low_ = copy.deepcopy(low)
    while high - low > epsilon:
        mid = low_
        output = measure_output_vthh(mid)  # 入力 mid に対する出力を計測
        mid = (low + high) / 2.0
        output = measure_output_vthh(mid)  # 入力 mid に対する出力を計測
        print(mid,output)
        if output == 0:
            low = mid  # しきい値はより高い位置にある
        else:
            high = mid  # しきい値はより低い位置にある
        

    return low

def binary_search_threshold_decreasing(low,high,epsilon):
    
    high_ = copy.deepcopy(high)
    while high - low > epsilon:
        mid = high_
        output = measure_output_vthl(mid)  # 入力 mid に対する出力を計測
        mid = (low + high) / 2.0
        output = measure_output_vthl(mid)  # 入力 mid に対する出力を計測

        if output == 1:
            low = mid  # しきい値はより低い位置にある
        else:
            high = mid  # しきい値はより高い位置にある

    return low

def linear_search_threshold_increasing(low,high,epsilon):
    
    mid = low
    while True:
        output = measure_output_vthh(mid)  # 入力 mid に対する出力を計測
        if output == 1:
            break
        mid = mid + epsilon

    return mid - epsilon

def linear_search_threshold_decreasing(low,high,epsilon):
    
    mid = high
    while True:
        output = measure_output_vthl(mid)  # 入力 mid に対する出力を計測
        if output == 1:
            break
        mid = mid - epsilon

    return mid + epsilon

# 測定関数（例）
def measure_output_vthh(input_voltage):
    # 実際のシステムの出力を取得するロジックを記述する
    # ここでは例として、しきい値を3.6Vおよび2.8Vとする
    if input_voltage >= 63.07:
        return 1
    else:
        return 0
    
# 測定関数（例）
def measure_output_vthl(input_voltage):
    # 実際のシステムの出力を取得するロジックを記述する
    # ここでは例として、しきい値を3.6Vおよび2.8Vとする
    if input_voltage <= 49.87:
        return 1
    else:
        return 0


low = 0.0
high = 100.0
epsilon = 0.00001  # 精度を設定


# 使用例
start = time.time()  # 現在時刻（処理開始前）を取得
threshold_increase = binary_search_threshold_increasing(low,high,epsilon)
threshold_decrease = binary_search_threshold_decreasing(low,high,epsilon)
end = time.time()  # 現在時刻（処理完了後）を取得
print("入力が増加する場合のしきい値:", threshold_increase)
print("入力が減少する場合のしきい値:", threshold_decrease)

time_diff = end - start  # 処理完了後の時刻から処理開始前の時刻を減算する
print("処理時間:", time_diff)  # 処理にかかった時間データを使用
# print()
# start = time.time()  # 現在時刻（処理開始前）を取得
# threshold_increase = linear_search_threshold_increasing(low,high,epsilon)
# threshold_decrease = linear_search_threshold_decreasing(low,high,epsilon)
# end = time.time()  # 現在時刻（処理完了後）を取得
# print("入力が増加する場合のしきい値:", threshold_increase)
# print("入力が減少する場合のしきい値:", threshold_decrease)
# time_diff = end - start  # 処理完了後の時刻から処理開始前の時刻を減算する
# print("処理時間:", time_diff)  # 処理にかかった時間データを使用