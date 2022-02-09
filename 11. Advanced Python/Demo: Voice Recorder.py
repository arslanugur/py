# Libraries
# - pip install sounddevice, scipy, win10toast

import sounddevice
from scipy.io.wavfile import write
import win10toast

ntfr = win10toast.ToastNotifier()    # bildirim
scnd = int(input("How many seconds to record?: "))  # saniye
print("Recording ...\n")

rcrd = sounddevice.rec(int(scnd * 44100), samplerate = 44100, channels = 2) # kayıt
sounddevice.wait()
write("Output.wav", 44100, rcrd)
print("Recorded. File name: Output.wav")
ntfr.show_toast("Welldone.", duration = 10)


