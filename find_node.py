
# Enter your Python code here

from pya import *
import re,pprint

class OriginalError(Exception):
    pass

def find_node():

    # Applicationクラスを起動
    app = Application.instance()
    mw = app.main_window()

    # layoutのcurrent_viewを取得
    try:
        lv = mw.current_view()
        if lv is None:
            raise OriginalError('Cancelled')
    except OriginalError as e:
        print(e)
    
    # cellの取得
    cell = lv.active_cellview().cell

    # layoutの取得
    layout = cell.layout()

    # layer index information
    index_info = dict()
    for i,num in zip(layout.layer_infos(),layout.layer_indexes()):
      index = ','.join([str(v) for v in str(i).split('/')])
      index_info[num] = index
    
    # menubarから全選択を実行
    menu = mw.menu()
    menu.action("edit_menu.select_menu.select_all").trigger()
    
    # Layoutの単位を獲得
    DBU = 1 / cell.layout().dbu
    
    tanshi_position = dict()
    
    # それぞれのレイアウトのオブジェクトについて処理
    
    for sel in lv.each_object_selected():
        
        layer = sel.layer
        layer_index = index_info[layer]
        shape = sel.shape

        if shape.is_text():
            text = shape.text
            text_pos = list(map(int,text.trans.to_s().split()[1].split(",")))
            tanshi_position[text.string] = [text_pos, [int(v) for v in layer_index.split(",")]]

    # net tracer
    tracer = NetTracer()
    tech = NetTracerConnectivity()
    flag = 0
    for line in layout.technology().to_xml().split('\n'):
      if 'connectivity' in line:
        flag = 1
        
      if flag == 1:
        target1 =  'connection'
        if target1 in line:
          words = re.split('[,]',line)
          print(words[0].strip()[len(target1)+2:],words[1],words[2].strip()[:-1*len(target1)-3])
          tech.connection(words[0].strip()[len(target1)+2:],words[1],words[2].strip()[:-1*len(target1)-3])
        target2 = 'symbols'
        if target2 in line:
          words = [v for v in re.split("['=]",line) if v != '']
          print(words[0].strip()[len(target2)+2:],words[1])
          tech.symbol(words[0].strip()[len(target2)+2:],words[1])
            
      if '/connectivity' in line:
        flag = 0
    
    name = 'outp'
    print(tanshi_position[name][0],tanshi_position[name][1])
    tanshi_pos = tanshi_position[name][0]
    layer_index = tanshi_position[name][1]
    tracer.trace(tech,layout,cell,
                 Point.new(tanshi_pos[0],tanshi_pos[1]),
                 layout.find_layer(LayerInfo.new(layer_index[0], layer_index[1])))

    trace_result_cell = layout.create_cell("trace_result")
    
    
    lv.markers = []
    

    print("="*10)
    for it in tracer.each_element():
      print(it.layer(),it.shape,it.trans)
      trace_result_cell.shapes(layout.layer(5,0) ).insert(it.shape(),it.trans())
      
      marker = Marker(lv)
      print(it.bbox().p1)
      p1 = it.bbox().p1
      p2 = it.bbox().p2
      p1x,p1y,p2x,p2y = p1.x,p1.y,p2.x,p2.y
      marker.set(DBox(p1x/DBU,p1y/DBU,p2x/DBU,p2y/DBU))
      lv.markers.append(marker)
      
    print("="*10)
    print(marker.color)
    print("="*10)
    
find_node()
    
    
    
