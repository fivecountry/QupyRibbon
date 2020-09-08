from PyQt5.QtCore import *
from PyQt5.QtGui import QKeySequence as QKSec
from PyQt5.QtGui import QBrush, QColor, QIcon, QPixmap
from PyQt5.QtCore import Qt
from GUI.RibbonButton import RibbonButton
from GUI.Icons import get_icon
from GUI.RibbonTextbox import RibbonTextbox
from GUI.RibbonWidget import *
import os
import pathlib

__author__ = 'mamj'

'''
    主窗体
'''
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.resize(1280, 800)
        self.setWindowTitle("传热分析软件")
        self.setDockNestingEnabled(True)
        self.setWindowIcon(get_icon("icon"))
        self._tree_dock_widget = QDockWidget(self)
        self._tree_dock_widget.setObjectName("TreeDock")
        self._tree_dock_widget.setWindowTitle("资源管理器")
        self._tree_widget = QTreeWidget(self)
        # self._tree_widget.setHeaderHidden(True)
        self._tree_widget.setHeaderLabel('树标题')
        self._tree_dock_widget.setFixedWidth(300)
        self._tree_widget.clear()
        #设置根节点
        root=QTreeWidgetItem(self._tree_widget)
        root.setText(0,'根节点')
        #root.setIcon(0,QIcon('./images/root.png'))
        # todo 优化2 设置根节点的背景颜色
        #brush_red=QBrush(Qt.blue)
        #root.setBackground(0,brush_red)
        #设置子节点1
        child1=QTreeWidgetItem()
        child1.setText(0,'子节点1')
        #child1.setText(1,'ios')
        #child1.setIcon(0,QIcon('./images/IOS.png'))
        #todo 优化1 设置节点的状态
        child1.setCheckState(0,Qt.Checked)
        root.addChild(child1)
        #设置子节点2
        child2=QTreeWidgetItem(root)
        child2.setText(0,'子节点2')
        #child2.setText(1,'')
        #child2.setIcon(0,QIcon('./images/android.png'))
        #设置子节点3
        child3=QTreeWidgetItem(child2)
        child3.setText(0,'子节点3')
        #child3.setText(1,'android')
        #child3.setIcon(0,QIcon('./images/music.png'))
        #加载根节点的所有属性与子控件
        self._tree_widget.addTopLevelItem(root)

        self._tree_dock_widget.setWidget(self._tree_widget)
        self.addDockWidget(Qt.LeftDockWidgetArea, self._tree_dock_widget)
        self._main_dock_widget = QDockWidget(self)
        self._main_dock_widget.setObjectName("MainDock")
        self._main_dock_widget.setWindowTitle("工作区")
        self._label_widget = QLabel('', self)
        self._main_dock_widget.setWidget(self._label_widget)
        self.addDockWidget(Qt.RightDockWidgetArea, self._main_dock_widget)
        self.centralWidget()
        # Ribbon
        self._ribbon = RibbonWidget(self)
        self.addToolBar(self._ribbon)
        self.init_ribbon()

    '''
        添加动作
    '''
    def add_action(self, caption, icon_name, status_tip, icon_visible, connection, shortcut=None):
        action = QAction(get_icon(icon_name), caption, self)
        action.setStatusTip(status_tip)
        action.triggered.connect(connection)
        action.setIconVisibleInMenu(icon_visible)
        if shortcut is not None:
            action.setShortcuts(shortcut)
        self.addAction(action)
        return action

    '''
        创建菜单
    '''
    def buildPanelMenu(self, pName, actions):
        home_tab = self._ribbon.add_ribbon_tab(pName)
        jm_pane = home_tab.add_ribbon_pane("")
        for k, v in actions.items():
            tempDelegate = QActionClickedDelegate(pName, k, self._label_widget)
            tButton = RibbonButton(self, self.add_action(k, v, k, True, tempDelegate.on_action_click, None), True)
            tButton.tempDelegate = tempDelegate
            jm_pane.add_ribbon_widget(tButton)

    '''
        初始化
    '''
    def init_ribbon(self):
        kvv = {}
        kvv['新建'] = '文件-新建'
        kvv['打开'] = '文件-打开'
        kvv['关闭所有'] = '文件-关闭所有'
        kvv['最近访问'] = '文件-最近访问'
        kvv['查找'] = '文件-查找'
        kvv['帮助'] = '文件-帮助'
        self.buildPanelMenu('文件', kvv)
        kvv = {}
        kvv['边倒圆'] = '特征-边倒圆'
        kvv['抽壳'] = '特征-抽壳'
        kvv['对特征形成图样'] = '特征-对特征形成图样'
        kvv['基准平面'] = '特征-基准平面'
        kvv['拉伸'] = '特征-拉伸'
        kvv['求和'] = '特征-求和'
        kvv['修剪体'] = '特征-修剪体'
        self.buildPanelMenu('特征', kvv)
        kvv = {}
        kvv['拆分边'] = '模型清理-拆分边'
        kvv['拆分面'] = '模型清理-拆分面'
        kvv['缝合边'] = '模型清理-缝合边'
        kvv['合并边'] = '模型清理-合并边'
        kvv['合并面'] = '模型清理-合并面'
        kvv['仅显示'] = '模型清理-仅显示'
        kvv['来自网格的面'] = '模型清理-来自网格的面'
        kvv['面修复'] = '模型清理-面修复'
        kvv['取消缝合边'] = '模型清理-取消缝合边'
        kvv['塌陷边'] = '模型清理-塌陷边'
        kvv['抑制孔'] = '模型清理-抑制孔'
        kvv['圆形压印'] = '模型清理-圆形压印'
        kvv['重置'] = '模型清理-重置'
        kvv['自动修复几何体'] = '模型清理-自动修复几何体'
        self.buildPanelMenu('模型清理', kvv)
        kvv = {}
        kvv['拆分体'] = '属性设置-拆分体'
        kvv['仿真对象类型'] = '属性设置-仿真对象类型'
        kvv['仿真区域'] = '属性设置-仿真区域'
        kvv['分割面'] = '属性设置-分割面'
        kvv['缝合'] = '属性设置-缝合'
        kvv['管理材料'] = '属性设置-管理材料'
        kvv['管理库材料'] = '属性设置-管理库材料'
        kvv['建模对象'] = '属性设置-建模对象'
        kvv['结果测量'] = '属性设置-结果测量'
        kvv['物理属性'] = '属性设置-物理属性'
        kvv['用户定义中面'] = '属性设置-用户定义中面'
        kvv['约束类型'] = '属性设置-约束类型'
        kvv['载荷类型'] = '属性设置-载荷类型'
        kvv['指派材料'] = '属性设置-指派材料'
        self.buildPanelMenu('属性设置', kvv)
        kvv = {}
        kvv['1D 连接'] = '网格-1D 连接'
        kvv['1D 网格'] = '网格-1D 网格'
        kvv['2D 局部重画网格'] = '网格-2D 局部重画网格'
        kvv['2D 网格'] = '网格-2D 网格'
        kvv['2D 相关网格'] = '网格-2D 相关网格'
        kvv['2D 映射网格'] = '网格-2D 映射网格'
        kvv['3D 扫略网格'] = '网格-3D 扫略网格'
        kvv['3D 四面体网格'] = '网格-3D 四面体网格'
        kvv['附加 FEM'] = '网格-附加 FEM'
        kvv['建模对象'] = '网格-建模对象'
        kvv['网格关联数据'] = '网格-网格关联数据'
        kvv['网格检查'] = '网格-网格检查'
        kvv['网格配对条件'] = '网格-网格配对条件'
        kvv['网格收集器'] = '网格-网格收集器'
        self.buildPanelMenu('网格', kvv)
        kvv = {}
        kvv['编辑横截面'] = '直接建模-编辑横截面'
        kvv['调整圆角大小'] = '直接建模-调整圆角大小'
        kvv['复制面'] = '直接建模-复制面'
        kvv['剪切面'] = '直接建模-剪切面'
        kvv['角度尺寸'] = '直接建模-角度尺寸'
        kvv['镜像面'] = '直接建模-镜像面'
        kvv['拉出面'] = '直接建模-拉出面'
        kvv['删除面'] = '直接建模-删除面'
        kvv['设为对称'] = '直接建模-设为对称'
        kvv['设为共面'] = '直接建模-设为共面'
        kvv['设为共轴'] = '直接建模-设为共轴'
        kvv['线性尺寸'] = '直接建模-线性尺寸'
        kvv['移动面'] = '直接建模-移动面'
        kvv['圆角重新排序'] = '直接建模-圆角重新排序'
        self.buildPanelMenu('直接建模', kvv)
        kvv = {}
        kvv['几何优化'] = '求解器-几何优化'
        kvv['解算方案'] = '求解器-解算方案'
        kvv['耐久性仿真'] = '求解器-耐久性仿真'
        kvv['适应性设置'] = '求解器-适应性设置'
        self.buildPanelMenu('求解器', kvv)
        kvv = {}
        kvv['编辑后处理视图'] = '后处理-编辑后处理视图'
        kvv['标记开关'] = '后处理-标记开关'
        kvv['标记拖动'] = '后处理-标记拖动'
        kvv['标识结果'] = '后处理-标识结果'
        kvv['播放'] = '后处理-播放'
        kvv['动画'] = '后处理-动画'
        kvv['忽略背面'] = '后处理-忽略背面'
        kvv['结果操控'] = '后处理-结果操控'
        kvv['上一模态'] = '后处理-上一模态'
        kvv['设置结果'] = '后处理-设置结果'
        kvv['下一模态'] = '后处理-下一模态'
        self.buildPanelMenu('后处理', kvv)

    def closeEvent(self, close_event):
        pass

'''
    菜单项事件类
'''
class QActionClickedDelegate(object):
    def __init__(self, pName, aName, widget):
        super().__init__()
        self.panelName = pName
        self.actionName = aName
        self.labelWidget = widget

    def on_action_click(self):
        #拼装路径
        imgPath = os.path.join(os.getcwd(), 'bgImages', self.panelName, self.actionName + '.png')
        print(imgPath)
        if pathlib.Path(imgPath).exists():
            #显示Gif的方法如下：
            #self.gif = QMovie('qq.gif')
            #self.labelWidget.setMovie(self.gif)
            #self.gif.start()
            #显示一般图片
            self.labelWidget.setPixmap(QPixmap(imgPath))
