# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camera.ui'
#
# Created: Wed Mar 26 10:55:52 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Camera(object):
    def setupUi(self, Camera):
        Camera.setObjectName(_fromUtf8("Camera"))
        Camera.resize(545, 768)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Camera)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter = QtGui.QSplitter(Camera)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.camera_image_widget = QtGui.QWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_image_widget.sizePolicy().hasHeightForWidth())
        self.camera_image_widget.setSizePolicy(sizePolicy)
        self.camera_image_widget.setMinimumSize(QtCore.QSize(9, 0))
        self.camera_image_widget.setObjectName(_fromUtf8("camera_image_widget"))
        self.cameraImageContainer = QtGui.QVBoxLayout(self.camera_image_widget)
        self.cameraImageContainer.setMargin(0)
        self.cameraImageContainer.setObjectName(_fromUtf8("cameraImageContainer"))
        self.tabWidget = QtGui.QTabWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.formLayout = QtGui.QFormLayout(self.tab)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label)
        self.acq_expo_time = MAXLineEdit(self.tab)
        self.acq_expo_time.setInputMask(_fromUtf8(""))
        self.acq_expo_time.setUseParentModel(False)
        self.acq_expo_time.setAutoApply(True)
        self.acq_expo_time.setObjectName(_fromUtf8("acq_expo_time"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.acq_expo_time)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.camera_type_label = QtGui.QLabel(self.tab)
        self.camera_type_label.setObjectName(_fromUtf8("camera_type_label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.camera_type_label)
        self.trigger_mode_combobox = TaurusValueComboBox(self.tab)
        self.trigger_mode_combobox.setAutoApply(True)
        self.trigger_mode_combobox.setObjectName(_fromUtf8("trigger_mode_combobox"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.trigger_mode_combobox)
        self.acq_status_label = TaurusLabel(self.tab)
        self.acq_status_label.setObjectName(_fromUtf8("acq_status_label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.acq_status_label)
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.gain_label = MAXLineEdit(self.tab)
        self.gain_label.setObjectName(_fromUtf8("gain_label"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.gain_label)
        self.label_16 = QtGui.QLabel(self.tab)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_16)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.start_acquisition_button = QtGui.QPushButton(self.tab)
        self.start_acquisition_button.setObjectName(_fromUtf8("start_acquisition_button"))
        self.horizontalLayout.addWidget(self.start_acquisition_button)
        self.stop_acquisition_button = QtGui.QPushButton(self.tab)
        self.stop_acquisition_button.setObjectName(_fromUtf8("stop_acquisition_button"))
        self.horizontalLayout.addWidget(self.stop_acquisition_button)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.tab_2)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.image_width_label = TaurusLabel(self.tab_2)
        self.image_width_label.setObjectName(_fromUtf8("image_width_label"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.image_width_label)
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_6)
        self.image_height_label = TaurusLabel(self.tab_2)
        self.image_height_label.setObjectName(_fromUtf8("image_height_label"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.image_height_label)
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_9)
        self.image_rotation_combobox = TaurusValueComboBox(self.tab_2)
        self.image_rotation_combobox.setAutoApply(True)
        self.image_rotation_combobox.setObjectName(_fromUtf8("image_rotation_combobox"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.image_rotation_combobox)
        self.label_8 = QtGui.QLabel(self.tab_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_8)
        self.image_bin_spinbox = QtGui.QSpinBox(self.tab_2)
        self.image_bin_spinbox.setMinimum(1)
        self.image_bin_spinbox.setObjectName(_fromUtf8("image_bin_spinbox"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.image_bin_spinbox)
        self.image_save_button = QtGui.QPushButton(self.tab_2)
        self.image_save_button.setObjectName(_fromUtf8("image_save_button"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.image_save_button)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_10 = QtGui.QLabel(self.tab_3)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_10)
        self.roi_label = TaurusLabel(self.tab_3)
        self.roi_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.roi_label.setObjectName(_fromUtf8("roi_label"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.roi_label)
        self.label_15 = QtGui.QLabel(self.tab_3)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_15)
        self.auto_roi_checkbox = TaurusValueCheckBox(self.tab_3)
        self.auto_roi_checkbox.setText(_fromUtf8(""))
        self.auto_roi_checkbox.setShowText(False)
        self.auto_roi_checkbox.setAutoApply(True)
        self.auto_roi_checkbox.setObjectName(_fromUtf8("auto_roi_checkbox"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.auto_roi_checkbox)
        self.bpm_show_position_checkbox = QtGui.QCheckBox(self.tab_3)
        self.bpm_show_position_checkbox.setText(_fromUtf8(""))
        self.bpm_show_position_checkbox.setObjectName(_fromUtf8("bpm_show_position_checkbox"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.bpm_show_position_checkbox)
        self.label_18 = QtGui.QLabel(self.tab_3)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_18)
        self.verticalLayout_3.addLayout(self.formLayout_3)
        self.groupBox = QtGui.QGroupBox(self.tab_3)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.beam_fwhm_x_label = TaurusLabel(self.groupBox)
        self.beam_fwhm_x_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.beam_fwhm_x_label.setObjectName(_fromUtf8("beam_fwhm_x_label"))
        self.gridLayout.addWidget(self.beam_fwhm_x_label, 2, 3, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 1)
        self.label_17 = QtGui.QLabel(self.groupBox)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 1)
        self.beam_fwhm_y_label = TaurusLabel(self.groupBox)
        self.beam_fwhm_y_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.beam_fwhm_y_label.setObjectName(_fromUtf8("beam_fwhm_y_label"))
        self.gridLayout.addWidget(self.beam_fwhm_y_label, 4, 3, 1, 1)
        self.beam_center_x_label = TaurusLabel(self.groupBox)
        self.beam_center_x_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.beam_center_x_label.setObjectName(_fromUtf8("beam_center_x_label"))
        self.gridLayout.addWidget(self.beam_center_x_label, 2, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 4, 2, 1, 1)
        self.beam_center_y_label = TaurusLabel(self.groupBox)
        self.beam_center_y_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.beam_center_y_label.setObjectName(_fromUtf8("beam_center_y_label"))
        self.gridLayout.addWidget(self.beam_center_y_label, 4, 1, 1, 1)
        self.beam_intensity_label = TaurusLabel(self.groupBox)
        self.beam_intensity_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.beam_intensity_label.setObjectName(_fromUtf8("beam_intensity_label"))
        self.gridLayout.addWidget(self.beam_intensity_label, 0, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 2, 2, 1, 1)
        self.bpm_profile_x_layout = QtGui.QVBoxLayout()
        self.bpm_profile_x_layout.setObjectName(_fromUtf8("bpm_profile_x_layout"))
        self.gridLayout.addLayout(self.bpm_profile_x_layout, 1, 0, 1, 4)
        self.bpm_profile_y_layout = QtGui.QVBoxLayout()
        self.bpm_profile_y_layout.setObjectName(_fromUtf8("bpm_profile_y_layout"))
        self.gridLayout.addLayout(self.bpm_profile_y_layout, 3, 0, 1, 4)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.bpm_layout = QtGui.QVBoxLayout()
        self.bpm_layout.setObjectName(_fromUtf8("bpm_layout"))
        self.verticalLayout_3.addLayout(self.bpm_layout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.splitter)

        self.retranslateUi(Camera)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Camera)

    def retranslateUi(self, Camera):
        Camera.setWindowTitle(_translate("Camera", "Camera", None))
        self.label.setText(_translate("Camera", "Exposure time (ms)", None))
        self.acq_expo_time.setModel(_translate("Camera", "acq_expo_time", None))
        self.label_2.setText(_translate("Camera", "Acquisition", None))
        self.label_3.setText(_translate("Camera", "Trigger mode", None))
        self.label_4.setText(_translate("Camera", "Camera type", None))
        self.camera_type_label.setText(_translate("Camera", "Unknown", None))
        self.label_7.setText(_translate("Camera", "Status", None))
        self.label_16.setText(_translate("Camera", "Gain", None))
        self.start_acquisition_button.setText(_translate("Camera", "Start", None))
        self.stop_acquisition_button.setText(_translate("Camera", "Stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Camera", "Acquisition", None))
        self.label_5.setText(_translate("Camera", "Image width", None))
        self.label_6.setText(_translate("Camera", "Image height", None))
        self.label_9.setText(_translate("Camera", "Rotation", None))
        self.label_8.setText(_translate("Camera", "Binning", None))
        self.image_save_button.setText(_translate("Camera", "Save Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Camera", "Image", None))
        self.label_10.setText(_translate("Camera", "ROI", None))
        self.label_15.setText(_translate("Camera", "Auto ROI", None))
        self.label_18.setText(_translate("Camera", "Show beam position", None))
        self.groupBox.setTitle(_translate("Camera", "Beam parameters", None))
        self.label_12.setText(_translate("Camera", "Center Y:", None))
        self.label_17.setText(_translate("Camera", "Intensity:", None))
        self.label_11.setText(_translate("Camera", "Center X:", None))
        self.label_14.setText(_translate("Camera", "FWHM Y:", None))
        self.label_13.setText(_translate("Camera", "FWHM X:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Camera", "BPM", None))

from taurus.qt.qtgui.display import TaurusLabel
from taurus.qt.qtgui.input import TaurusValueComboBox, TaurusValueCheckBox
from maxwidgets.input import MAXLineEdit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Camera = QtGui.QWidget()
    ui = Ui_Camera()
    ui.setupUi(Camera)
    Camera.show()
    sys.exit(app.exec_())

