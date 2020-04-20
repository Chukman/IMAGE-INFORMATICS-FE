# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:24:13 2020

@author: Peter
"""

import sys
from PyQt5 import QtCore, QtWidgets
import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class ui_RightPanel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        
        super().__init__()
               
        hbox = QtWidgets.QVBoxLayout()
        text = QtWidgets.QLabel('Prag (sivinska vrednost)', self)
        
        self.initial_value = 150
        self.slider = QtWidgets.QSlider(QtCore.Qt.Vertical, self)
        self.slider.setTickPosition(QtWidgets.QSlider.TicksLeft)
        self.slider.setTickInterval(25)
        self.slider.setRange(0, 255)
        self.slider.setSingleStep(1)
        self.slider.setSliderPosition(self.initial_value )
        
        self.threshold = QtWidgets.QLineEdit(self)
        self.threshold.setText(str(self.initial_value ))
        self.threshold.setEnabled(False)
        self.threshold.setAlignment(QtCore.Qt.AlignCenter)
        
        hbox.addWidget(text, 0, QtCore.Qt.AlignHCenter)
        hbox.addWidget(self.slider, 0, QtCore.Qt.AlignHCenter)
        hbox.addWidget(self.threshold, 0, QtCore.Qt.AlignHCenter)
        
        self.setLayout(hbox)
        
        self.slider.valueChanged.connect(self.change_value)
        
    def change_value(self):
        self.threshold.setText(str(self.slider.value()))
        
        
class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        
        super().__init__()
        
        self.setWindowTitle('Slikovna informatika - Upodabljanje površine')
        
        self.rightpanel = ui_RightPanel(self)
        self.rightpanel.slider.valueChanged.connect(self.change_threshold)
        
        self.vtkWidget  = QVTKRenderWindowInteractor(self)
        
        self.renderer = vtk.vtkRenderer()
        self.vtkWidget.GetRenderWindow().AddRenderer(self.renderer)
        self.interactor = self.vtkWidget.GetRenderWindow().GetInteractor()
        
        hbox = QtWidgets.QHBoxLayout(self)
        hbox.addWidget(self.vtkWidget)
        hbox.addWidget(self.rightpanel)
        
        colors = vtk.vtkNamedColors()
        colors.SetColor("BkgColor", [51, 77, 102, 255])
        
        reader = vtk.vtkMetaImageReader()
        reader.SetFileName('visible-human.mhd')
        
        # s pomočjo algoritma Marching Cubes izračunamo trikotnike,
        # ki sestavljajo površino
        self.extractor = vtk.vtkMarchingCubes()
        self.extractor.SetInputConnection(reader.GetOutputPort())
        self.extractor.SetValue(0, self.rightpanel.initial_value)  # prag
        
        # mapiramo dobljene trikotnike
        self.surfaceMapper = vtk.vtkPolyDataMapper()
        self.surfaceMapper.SetInputConnection(self.extractor.GetOutputPort())
        self.surfaceMapper.ScalarVisibilityOff()
        
        # objekt za upodabljanje
        self.surfaceActor = vtk.vtkActor()
        self.surfaceActor.SetMapper(self.surfaceMapper)
        
        # zunanja obrobna linija
        outlineData = vtk.vtkOutlineFilter()
        outlineData.SetInputConnection(reader.GetOutputPort())
        
        mapOutline = vtk.vtkPolyDataMapper()
        mapOutline.SetInputConnection(outlineData.GetOutputPort())
        
        outline = vtk.vtkActor()
        outline.SetMapper(mapOutline)
        outline.GetProperty().SetColor(colors.GetColor3d("Black"))
        
        aCamera = vtk.vtkCamera()
        aCamera.SetViewUp(0, 0, -1)
        aCamera.SetPosition(0, -1, 0)
        aCamera.SetFocalPoint(0, 0, 0)
        aCamera.ComputeViewPlaneNormal()
        aCamera.Roll(90)
        aCamera.Yaw(-90)
        
        self.renderer.AddActor(outline)
        self.renderer.AddActor(self.surfaceActor)
        self.renderer.SetActiveCamera(aCamera)
        self.renderer.ResetCamera()
        
        # ozadje
        self.renderer.SetBackground(colors.GetColor3d("BkgColor"))
        
        self.renderer.ResetCameraClippingRange()
        
    def change_threshold(self):
        self.extractor.SetValue(0, self.rightpanel.slider.value())
        self.interactor.Render()
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = mainWindow()
    gui.show()
    gui.interactor.Initialize()
    sys.exit(app.exec())