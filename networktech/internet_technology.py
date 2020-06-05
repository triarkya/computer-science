import math


# calculate data rate in Bit/s according to nyquist theorem
# freq in Hz
# signal_levels = 16 if 16-QAM
def nyquist(freq, signal_levels):
    return 2 * freq * math.log2(signal_levels)


# calculate data rate for ODFM
# time per signal in seconds
def odfm_datarate(subcarriers, qam, time_per_signal):
    return (math.log2(qam) * subcarriers) / time_per_signal


if __name__ == '__main__':
    print(nyquist(1200, 16))
    print(odfm_datarate(48, 64, 0.000004))
