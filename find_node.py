import pya
import re,pprint

class OriginalError(Exception):
    pass

class NodeColorSelectionDialog(pya.QDialog):
    def __init__(self, parent=None):
        super(NodeColorSelectionDialog, self).__init__(parent)
        self.setWindowTitle("ノード名入力フォーム")
        self.layout = pya.QVBoxLayout(self)
        
        # ノード名入力フィールド
        self.node_label = pya.QLabel("ノード名を入力してください:")
        self.layout.addWidget(self.node_label)
        self.node_input = pya.QLineEdit()
        self.layout.addWidget(self.node_input)
        
        # 色選択フィールド
        self.color_group = pya.QGroupBox("色を選択してください:")
        self.color_layout = pya.QHBoxLayout()
        self.color_group.setLayout(self.color_layout)
        
        self.color_buttons = {
            'red': pya.QRadioButton("赤"),
            'green': pya.QRadioButton("緑"),
            'blue': pya.QRadioButton("青"),
            'yellow': pya.QRadioButton("黄")
        }
        
        self.button_group = pya.QButtonGroup(self)
        
        for color, button in self.color_buttons.items():
            self.color_layout.addWidget(button)
            self.button_group.addButton(button)
        
        self.layout.addWidget(self.color_group)
        
        # OKボタンとキャンセルボタン
        self.button_box = pya.QHBoxLayout()
        self.ok_button = pya.QPushButton("OK")
        self.cancel_button = pya.QPushButton("キャンセル")
        self.button_box.addWidget(self.ok_button)
        self.button_box.addWidget(self.cancel_button)
        self.layout.addLayout(self.button_box)
        
        self.ok_button.clicked(self.accept_dialog)
        self.cancel_button.clicked(self.reject_dialog)
        
        self.selected_color = 'red'  # デフォルトで赤を選択
        self.color_buttons['red'].setChecked(True)

    def accept_dialog(self):
        self.accept()

    def reject_dialog(self):
        self.reject()

    def get_node_and_color(self):
        for color, button in self.color_buttons.items():
            if button.isChecked():
                self.selected_color = color
        return self.node_input.text.strip(), self.selected_color

def load_node_coordinate(name, cell, layout, trans, layer_index_list):
    coordinates = []
    
    # インスタンスを再帰的に処理
    for inst in cell.each_inst():
        inst_cell = layout.cell(inst.cell_index)
        new_trans = trans * inst.trans
        coordinates += load_node_coordinate(name+'.'+inst_cell.name,inst_cell, layout, new_trans,layer_index_list)
    
    # テキストオブジェクトの座標を取得
    for li1,li2 in layer_index_list:
        for shape in cell.shapes(layout.layer(li1, li2)):
            if shape.is_text():
                text = shape.text
                tmp_trans = trans * text.trans
                coordinates.append((name+'.'+text.string, tmp_trans.disp.x, tmp_trans.disp.y, li1, li2))
        
    return coordinates

def load_tech_connect(layout, tech):
    flag = 0
    print(layout)
    for line in layout.technology().to_xml().split('\n'):
        if 'connectivity' in line:
            flag = 1
        
        if flag == 1:
            target1 = 'connection'
            if target1 in line:
                words = re.split('[,]', line)
                tech.connection(words[0].strip()[len(target1)+2:], words[1], words[2].strip()[:-1*len(target1)-3])
            target2 = 'symbols'
            if target2 in line:
                words = [v for v in re.split("['=]", line) if v != '']
                tech.symbol(words[0].strip()[len(target2)+2:], words[1])
                
        if '/connectivity' in line:
            flag = 0

    return tech

def color_string_to_int(color_string):
    color_dict = {
        'red': 0xFF0000,
        'green': 0x00FF00,
        'blue': 0x0000FF,
        'yellow': 0xFFFF00
    }
    return color_dict.get(color_string.lower(), 0x000000)  # default to black if not found

def mark_node(tracer, tech, layout, cell, lv, DBU, tanshi_pos, layer_index, color):
    tracer.trace(tech, layout, cell,
                 pya.Point.new(tanshi_pos[0], tanshi_pos[1]),
                 layout.find_layer(pya.LayerInfo.new(layer_index[0], layer_index[1])))

    lv.add_marker = []
    
    for it in tracer.each_element():
        
        marker = pya.Marker(lv)
        marker.color = color
        p1 = it.bbox().p1
        p2 = it.bbox().p2
        p1x, p1y, p2x, p2y = p1.x, p1.y, p2.x, p2.y
        marker.set(pya.DBox(p1x / DBU, p1y / DBU, p2x / DBU, p2y / DBU))
        lv.add_marker.append(marker)

def get_full_path(item):
    path = []
    while item is not None:
        path.append(item.text(0))
        item = item.parent()
    return '.'.join(reversed(path))

def show_node_names_tree_by_cell():

    # Applicationクラスを起動
    app = pya.Application.instance()
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
    for i, num in zip(layout.layer_infos(), layout.layer_indexes()):
        index = ','.join([str(v) for v in str(i).split('/')])
        index_info[num] = index
    
    # Layoutの単位を獲得
    DBU = 1 / cell.layout().dbu
    
    # 座標情報を取得
    layer_index_list = [[34,10],[36,10],[42,10],[46,10],[81,10]]
    coordinates = load_node_coordinate(cell.name, cell, layout, pya.Trans(),layer_index_list)

    # 座標情報を保存
    label_dict = dict()
    for text_string, x, y, li1, li2 in coordinates:
        label_dict[text_string] = [[x,y],[li1,li2]]

    node_names = [name for name in label_dict.keys()]

    # ノード名のリストをツリー構造に変換
    tree_dict = {}
    for name in node_names:
        parts = name.split('.')
        d = tree_dict
        for part in parts[:-1]:
            if part not in d:
                d[part] = {}
            d = d[part]
        d[parts[-1]] = None  # ノード名の終端は None に設定

    # ツリービューを作成
    def add_items(tree_widget, parent, tree_dict):
        for key, value in tree_dict.items():
            item = pya.QTreeWidgetItem([key])
            parent.addChild(item)
            if isinstance(value, dict):
                add_items(tree_widget, item, value)
    
    def process_nodes(item, color):

        node_name = get_full_path(item)
    
        # net tracer
        tracer = pya.NetTracer()
        tech = load_tech_connect(layout, pya.NetTracerConnectivity())

        if node_name in label_dict.keys():
            mark_node(tracer, tech, layout, cell, lv, DBU,
                    label_dict[node_name][0], label_dict[node_name][1], color)

    
    def clear_marker():
        print("clear")
        for item in lv.add_marker:
            print(item)
        lv.add_marker = []  # Clear markers by setting the list to empty

    dialog = pya.QDialog()
    dialog.setWindowTitle("ノード名一覧（セルごと）")
    Qlayout = pya.QVBoxLayout()
    
    tree_widget = pya.QTreeWidget()
    tree_widget.setHeaderLabels(["ノード名"])
    add_items(tree_widget, tree_widget.invisibleRootItem(), tree_dict)
    
    tree_widget = pya.QTreeWidget()
    tree_widget.setHeaderLabels(["ノード名"])
    add_items(tree_widget, tree_widget.invisibleRootItem(), tree_dict)
    tree_widget.itemClicked(lambda item, column: process_nodes(item, color_string_to_int("red")))
    Qlayout.addWidget(tree_widget)

    # OKボタンを追加
    clear_button = pya.QPushButton("クリア")
    clear_button.clicked(clear_marker)
    Qlayout.addWidget(clear_button)

    dialog.setLayout(Qlayout)
    dialog.exec_()

# ユーザーインターフェースを表示する関数
def main():
    
    show_node_names_tree_by_cell()

main()
