#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PyQt4.QtCore import Qt, QString
from PyQt4.QtGui import (QWidget, QIcon, QAction, QLabel, QTextBrowser,
                         QTreeWidget, QTreeWidgetItem, QAbstractItemView,
                         QHeaderView, QVBoxLayout)
from ninja_ide.core import plugin
from ninja_ide.gui.editor import editor
from ninja_ide import resources
from ninja_ide.gui.explorer import explorer_container

import res
from pdb4qt import set_trace
import nose
from nose.loader import TestLoader
from ninja_nose_plugin import NinjaNosePlugin


class TreeResultWidget(QTreeWidget):

    def __init__(self):
        QTreeWidget.__init__(self)
        self.setHeaderLabels((self.tr('File'), self.tr('Line')))
        self.header().setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.header().setResizeMode(0, QHeaderView.ResizeToContents)
        self.header().setResizeMode(1, QHeaderView.ResizeToContents)
        self.header().setStretchLastSection(False)
        self.sortByColumn(0, Qt.AscendingOrder)

    def update_result(self, dir_name_root, error_description, items):
        if items:
            root_item = FindInFilesRootItem(self, (error_description, ''),
                dir_name_root)
            root_item.setExpanded(True)
            for file_name, line in items:
                QTreeWidgetItem(root_item, (file_name, QString.number(line + 1)))


class FindInFilesRootItem(QTreeWidgetItem):
    def __init__(self, parent, names, dir_name_root):
        QTreeWidgetItem.__init__(self, parent, names)
        self.dir_name_root = dir_name_root


class NinjaTesting(QWidget, plugin.Plugin):

    def initialize(self):

        self._explorer_container = explorer_container.ExplorerContainer()
        self.misc_s = self.locator.get_service('misc')
        self.toolbar_s = self.locator.get_service('toolbar')

        self.aboutLabel = QLabel('run test', self)

        self.result_widget = TreeResultWidget()

        self.misc_s.add_widget(self.result_widget,
                               res.get("results.png"),
                               self.tr("Test results"))

        self.action_run_tests = QAction(QIcon(res.get("runner.png")),
                                     self.tr("Run tests"),
                                     self)
        self.action_run_tests.triggered.connect(self.run_tests)
        self.toolbar_s.add_action(self.action_run_tests)

    def run_tests(self):
        project_path = self._explorer_container.get_actual_project()
        loader = TestLoader(workingDir=project_path)
        set_trace()
        nose.main(testLoader=loader, addplugins=[NinjaNosePlugin()])


    def finish(self):
        pass

