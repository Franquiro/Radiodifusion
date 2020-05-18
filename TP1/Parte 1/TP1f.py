#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: TP1f
# Author: Fran
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
import pmt
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import numpy as np
from gnuradio import qtgui

class TP1f(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "TP1f")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("TP1f")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "TP1f")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.taps_951 = taps_951 = firdes.low_pass(1.0, samp_rate, 80e3,5e3, firdes.WIN_RECTANGULAR, 6.76)
        self.fsk_deviation_hz = fsk_deviation_hz = 75e3

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_FLATTOP, #wintype
            0, #fc
            samp_rate, #bw
            "Señal FM recibida por cada emisora", #name
            8
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)



        labels = ['95.9', '95.5', '95.3', '95.1', '94.9',
            '94.7', '94.3', "No Filtrada", '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(8):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.freq_xlating_fir_filter_xxx_0_0_1_0 = filter.freq_xlating_fir_filter_ccc(1, taps_951, -400e3, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_0_1 = filter.freq_xlating_fir_filter_ccc(1, taps_951, 400e3, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_0_0_1 = filter.freq_xlating_fir_filter_ccc(1, taps_951, -200e3, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_0_0_0_0 = filter.freq_xlating_fir_filter_ccc(1, taps_951, -800e3, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_0_0_0 = filter.freq_xlating_fir_filter_ccc(1, taps_951, 800e3, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_0_0 = filter.freq_xlating_fir_filter_ccc(1, taps_951, 200e3, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_0 = filter.freq_xlating_fir_filter_ccc(1, taps_951, 0, samp_rate)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/fran/Documents/UCA/4to año/Radiodifusión/Prácticas/espectro_2M', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_0_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_0_0_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_0_0_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_0_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_0_1_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0_0, 7))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0, 0), (self.qtgui_freq_sink_x_0_0, 3))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0_0, 0), (self.qtgui_freq_sink_x_0_0, 4))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0_0_0, 0), (self.qtgui_freq_sink_x_0_0, 6))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0_0_0_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0_0_1, 0), (self.qtgui_freq_sink_x_0_0, 2))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0_1, 0), (self.qtgui_freq_sink_x_0_0, 5))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0_1_0, 0), (self.qtgui_freq_sink_x_0_0, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "TP1f")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)

    def get_taps_951(self):
        return self.taps_951

    def set_taps_951(self, taps_951):
        self.taps_951 = taps_951
        self.freq_xlating_fir_filter_xxx_0_0.set_taps(self.taps_951)
        self.freq_xlating_fir_filter_xxx_0_0_0.set_taps(self.taps_951)
        self.freq_xlating_fir_filter_xxx_0_0_0_0.set_taps(self.taps_951)
        self.freq_xlating_fir_filter_xxx_0_0_0_0_0.set_taps(self.taps_951)
        self.freq_xlating_fir_filter_xxx_0_0_0_1.set_taps(self.taps_951)
        self.freq_xlating_fir_filter_xxx_0_0_1.set_taps(self.taps_951)
        self.freq_xlating_fir_filter_xxx_0_0_1_0.set_taps(self.taps_951)

    def get_fsk_deviation_hz(self):
        return self.fsk_deviation_hz

    def set_fsk_deviation_hz(self, fsk_deviation_hz):
        self.fsk_deviation_hz = fsk_deviation_hz



def main(top_block_cls=TP1f, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
