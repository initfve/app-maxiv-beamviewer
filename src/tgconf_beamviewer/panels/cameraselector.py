
from taurus.qt import QtCore, QtGui
from PyTango import Database


class CameraSelector(QtGui.QComboBox):
    domain = 'lima'
    family = 'limaccd'
    pos = '__s_cen'

    def __init__(self, parent=None):
        QtGui.QComboBox.__init__(self, parent)
        self._addItems()
    
    def _addItems(self):
        # Access the database
        db = Database()
        device_dct = {}
        wildcard = "/".join((self.domain, self.family, '*'))
        # Build device to postion dictionary
        for member in db.get_device_member(wildcard):
            device = "/".join((self.domain, self.family, member))
            prop = db.get_device_property(device, self.pos)[self.pos]
            try:
                device_dct[device] = float(prop[0])
            except (ValueError, IndexError):
                device_dct[device] = float('inf')
        # Add item in sorted order
        for device in sorted(device_dct, key=device_dct.get):
            self.addItem(device)


def main():
    import sys
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication(sys.argv)

    form = CameraSelector()
    form.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
