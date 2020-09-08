from PyQt5.QtGui import *
import os
import pathlib

__author__ = 'magnus'

icons_instance = None


def get_icon(name):
    global icons_instance
    if not icons_instance:
        icons_instance = Icons()
    return icons_instance.icon(name)


class Icons(object):
    def __init__(self):
        self._icons = {}
        self.make_icon("icon", "icons/icon.png")
        self.make_icon("default", "icons/folder.png")
        '''
        #文件
        self.make_icon('文件-帮助', "icons/文件/帮助.ico")
        self.make_icon('文件-查找', "icons/文件/查找.ico")
        self.make_icon('文件-打开', "icons/文件/打开.ico")
        self.make_icon('文件-关闭所有', "icons/文件/关闭所有.ico")
        self.make_icon('文件-新建', "icons/文件/新建.ico")
        self.make_icon('文件-最近访问', "icons/文件/最近访问.ico")
        #特征
        self.make_icon("特征-边倒圆", "icons/特征/边倒圆.ico")
        self.make_icon("特征-抽壳", "icons/特征/抽壳.ico")
        self.make_icon("特征-对特征形成图样", "icons/特征/对特征形成图样.ico")
        self.make_icon("特征-基准平面", "icons/特征/基准平面.ico")
        self.make_icon("特征-拉伸", "icons/特征/拉伸.ico")
        self.make_icon("特征-求和", "icons/特征/求和.ico")
        self.make_icon("特征-修剪体", "icons/特征/修剪体.ico")
        #属性设置
        self.make_icon("属性设置-拆分体", "icons/属性设置/拆分体.ico")
        self.make_icon("属性设置-仿真对象类型", "icons/属性设置/仿真对象类型.ico")
        self.make_icon("属性设置-仿真区域", "icons/属性设置/仿真区域.ico")
        self.make_icon("属性设置-分割面", "icons/属性设置/分割面.ico")
        self.make_icon("属性设置-缝合", "icons/属性设置/缝合.ico")
        self.make_icon("属性设置-管理材料", "icons/属性设置/管理材料.ico")
        self.make_icon("属性设置-管理库材料", "icons/属性设置/管理库材料.ico")
        self.make_icon("属性设置-建模对象", "icons/属性设置/建模对象.ico")
        self.make_icon("属性设置-结果测量", "icons/属性设置/结果测量.ico")
        self.make_icon("属性设置-物理属性", "icons/属性设置/物理属性.ico")
        self.make_icon("属性设置-用户定义中面", "icons/属性设置/用户定义中面.ico")
        self.make_icon("属性设置-约束类型", "icons/属性设置/约束类型.ico")
        self.make_icon("属性设置-载荷类型", "icons/属性设置/载荷类型.ico")
        self.make_icon("属性设置-指派材料", "icons/属性设置/指派材料.ico")
        #网格
        self.make_icon("网格-1D 连接", "icons/网格/1D 连接.ico")
        self.make_icon("网格-1D 网格", "icons/网格/1D 网格.ico")
        self.make_icon("网格-2D 局部重画网格", "icons/网格/2D 局部重画网格.ico")
        self.make_icon("网格-2D 网格", "icons/网格/2D 网格.ico")
        self.make_icon("网格-2D 相关网格", "icons/网格/2D 相关网格.ico")
        self.make_icon("网格-2D 映射网格", "icons/网格/2D 映射网格.ico")
        self.make_icon("网格-3D 扫略网格", "icons/网格/3D 扫略网格.ico")
        self.make_icon("网格-3D 四面体网格", "icons/网格/3D 四面体网格.ico")
        self.make_icon("网格-附加 FEM", "icons/网格/附加 FEM.ico")
        self.make_icon("网格-建模对象", "icons/网格/建模对象.ico")
        self.make_icon("网格-网格关联数据", "icons/网格/网格关联数据.ico")
        self.make_icon("网格-网格检查", "icons/网格/网格检查.ico")
        self.make_icon("网格-网格配对条件", "icons/网格/网格配对条件.ico")
        self.make_icon("网格-网格收集器", "icons/网格/网格收集器.ico")
        #直接建模
        self.make_icon("直接建模-编辑横截面", "icons/直接建模/编辑横截面.ico")
        self.make_icon("直接建模-调整圆角大小", "icons/直接建模/调整圆角大小.ico")
        self.make_icon("直接建模-复制面", "icons/直接建模/复制面.ico")
        self.make_icon("直接建模-剪切面", "icons/直接建模/剪切面.ico")
        self.make_icon("直接建模-角度尺寸", "icons/直接建模/角度尺寸.ico")
        self.make_icon("直接建模-镜像面", "icons/直接建模/镜像面.ico")
        self.make_icon("直接建模-拉出面", "icons/直接建模/拉出面.ico")
        self.make_icon("直接建模-删除面", "icons/直接建模/删除面.ico")
        self.make_icon("直接建模-设为对称", "icons/直接建模/设为对称.ico")
        self.make_icon("直接建模-设为共面", "icons/直接建模/设为共面.ico")
        self.make_icon("直接建模-设为共轴", "icons/直接建模/设为共轴.ico")
        self.make_icon("直接建模-线性尺寸", "icons/直接建模/线性尺寸.ico")
        self.make_icon("直接建模-移动面", "icons/直接建模/移动面.ico")
        self.make_icon("直接建模-圆角重新排序", "icons/直接建模/圆角重新排序.ico")        
        #模型清理
        self.make_icon("模型清理-拆分边", "icons/模型清理/拆分边.ico")
        self.make_icon("模型清理-拆分面", "icons/模型清理/拆分面.ico")
        self.make_icon("模型清理-缝合边", "icons/模型清理/缝合边.ico")
        self.make_icon("模型清理-合并边", "icons/模型清理/合并边.ico")
        self.make_icon("模型清理-合并面", "icons/模型清理/合并面.ico")
        self.make_icon("模型清理-仅显示", "icons/模型清理/仅显示.ico")
        self.make_icon("模型清理-来自网格的面", "icons/模型清理/来自网格的面.ico")
        self.make_icon("模型清理-面修复", "icons/模型清理/面修复.ico")
        self.make_icon("模型清理-取消缝合边", "icons/模型清理/取消缝合边.ico")
        self.make_icon("模型清理-塌陷边", "icons/模型清理/塌陷边.ico")
        self.make_icon("模型清理-抑制孔", "icons/模型清理/抑制孔.ico")
        self.make_icon("模型清理-圆形压印", "icons/模型清理/圆形压印.ico")
        self.make_icon("模型清理-重置", "icons/模型清理/重置.ico")
        self.make_icon("模型清理-自动修复几何体", "icons/模型清理/自动修复几何体.ico")
        #后处理
        self.make_icon("后处理-编辑后处理视图", "icons/后处理/编辑后处理视图.ico")
        self.make_icon("后处理-标记开关", "icons/后处理/标记开关.ico")
        self.make_icon("后处理-标记拖动", "icons/后处理/标记拖动.ico")
        self.make_icon("后处理-标识结果", "icons/后处理/标识结果.ico")
        self.make_icon("后处理-播放", "icons/后处理/播放.ico")
        self.make_icon("后处理-动画", "icons/后处理/动画.ico")
        self.make_icon("后处理-忽略背面", "icons/后处理/忽略背面.ico")
        self.make_icon("后处理-结果操控", "icons/后处理/结果操控.ico")
        self.make_icon("后处理-上一模态", "icons/后处理/上一模态.ico")
        self.make_icon("后处理-设置结果", "icons/后处理/设置结果.ico")
        self.make_icon("后处理-下一模态", "icons/后处理/下一模态.ico")
        # 求解器
        self.make_icon("求解器-几何优化", "icons/求解器/几何优化.ico")
        self.make_icon("求解器-解算方案", "icons/求解器/解算方案.ico")
        self.make_icon("求解器-耐久性仿真", "icons/求解器/耐久性仿真.ico")
        self.make_icon("求解器-适应性设置", "icons/求解器/适应性设置.ico")
        '''

    def make_icon(self, name, path):
        icon = QIcon()
        icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)
        self._icons[name] = icon

    def icon(self, name):
        icon = self._icons["default"]
        if self._icons.__contains__(name) == True:
            try:
                icon = self._icons[name]
            except KeyError:
                print("icon " + name + " not found")
        else:
            imgPath = os.path.join(os.getcwd(), 'icons', name.split('-')[0], name.split('-')[1] + '.ico')
            if pathlib.Path(imgPath).exists():
                print(imgPath)
                self.make_icon(name, imgPath)
                try:
                    icon = self._icons[name]
                except KeyError:
                    print("icon " + name + " not found")
        return icon
