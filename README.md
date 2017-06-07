[Examples](http://www.andrew.cmu.edu/user/mmendell/nn-audio/)
# Generating Audio with WaveNet
1. [Install the WaveNet dependencies.](#installing-wavenet-dependencies)
2. Download and unzip [this repo](https://github.com/MarkMendell/nn-audio/archive/master.zip).
3. [Download](https://github.com/ibab/tensorflow-wavenet/archive/master.zip), unzip, and move the tensorflow-wavenet-master folder into this repo's folder under the name 'tensorflow-wavenet'.
4. Make a new folder for a sound in this repo's folder.
5. Make a folder in that folder called 'corpus'.
6. Put [16kHz mono wav files](#making-16khz-mono-wav-files) of the sound in the corpus folder.
7. Open a shell active in this repo's directory.
8. Run `python gen.py sound-folder-name-here` to train indefinitely, generating three 10-second examples every 10000 steps in `sound-folder-name-here/gen/training-step-here/`.
9. Interrupt whenever you want to stop, then run the command again to pick up where you left off or repeat the steps for a different sound.

# Installing WaveNet Dependencies
If you aren't using Windows with an NVIDIA GPU, see [here](https://www.tensorflow.org/install/), and then `$ pip install librosa`. Otherwise, follow the instructions below.

## NVIDIA GPU Support on Windows
This guide worked for Windows 10 64-bit as of May 2017.
1. Make sure your [GPU drivers](http://www.nvidia.com/Download/index.aspx) are up to date.
2. [Download](https://developer.nvidia.com/cuda-downloads) and run the CUDA installer.
3. [Download](https://developer.nvidia.com/rdp/cudnn-download) CUDNN *v5.1* for CUDA 8.0 (you have to make an account).
4. Move `cuda\bin\cudnn64_5.dll` to `where-you-installed-CUDA\v8.0\bin\`.
5. Move `cuda\include\cudnn.h` to `where-you-installed-CUDA\v8.0\include\`.
6. Move `cuda\lib\x64\cudnn.lib` to `where-you-installed-CUDA\v8.0\lib\x64\`.
7. Add `where-you-installed-CUDA\v8.0\bin\` to the [PATH environment variable](https://superuser.com/a/949577).
8. [Install python *3.5*](https://www.python.org/downloads/).
9. Download the latest prebuilt [numpy+mkl](http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy) and [scipy](http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy) wheels for Windows 64-bit CPython 3.5.  
10. With a shell open to the folder you downloaded those wheels, install them with the following command:  
`$ pip install numpy‑1.13.0rc2+mkl‑cp35‑cp35m‑win_amd64.whl scipy‑0.19.0‑cp35‑cp35m‑win_amd64.whl`
11. Install tensorflow-gpu.  
`$ pip install tensorflow-gpu`
12. Make sure you have the [Visual Studio Visual C++ Build Tools](http://landinghub.visualstudio.com/visual-cpp-build-tools) installed.
13. Install resampy from source following [the instructions under "Advanced users and developers [...]"](http://resampy.readthedocs.io/en/latest/#installation).
14. Install librosa.  
`$ pip install librosa`

# Making 16KHz Mono Wav Files
## Audacity
1. File -> Import -> Audio... your original file.
2. Project Rate (Hz) (in the bottom left corner): 16000
3. If stereo, click on the down arrow by the name of the track, then Split Stereo to Mono.
4. File -> Export...
5. Format: WAV (Microsoft) signed 16 bit PCM
## ffmpeg
`$ ffmpeg -i input-file-here.mp3 -ar 16000 -ac 1 output-file-here.wav`
