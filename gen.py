#!/usr/bin/env python
from __future__ import print_function

import glob
import os
import shutil
import subprocess
import sys


def runcmd(args):
	p = subprocess.Popen(args, stderr=subprocess.PIPE)
	for line in iter(p.stderr.readline, b''):
		print(line.decode(sys.stderr.encoding), end='')


steps = 0
modelsdir = os.path.join(sys.argv[1], 'models')
if not os.path.exists(modelsdir):
	os.mkdir(modelsdir)
traindir = os.path.join(sys.argv[1], 'train')
if not os.path.exists(traindir):
	os.mkdir(traindir)
while True:
	steps += 10000
	print(str(steps) + " steps")
	model = os.path.join(traindir, 'model.ckpt-'+str(steps-1))
	if not os.path.exists(model + '.index'):
		runcmd([
				'python', os.path.join('tensorflow-wavenet', 'train.py'),
				'--num_steps', str(steps),
				'--data_dir', os.path.join(sys.argv[1], 'corpus'),
				'--wavenet_params', os.path.join('tensorflow-wavenet', 'wavenet_params.json'),
				'--logdir', traindir,
				'--silence_threshold', '0'
			])
		for file in glob.glob(model + '*'):
			shutil.copy(file, modelsdir)
	gendir = os.path.join(sys.argv[1], "gen", str(steps))
	if not os.path.exists(gendir):
		os.makedirs(gendir)
	for i in range(1,4):
		out = os.path.join(gendir, str(i)+'.wav')
		print(out)
		if (os.path.exists(out)):
			print("Skipped")
			continue
		runcmd([
				'python', os.path.join('tensorflow-wavenet', 'generate.py'),
				'--samples', '160000',
				'--wav_out_path', out,
				'--logdir', gendir,
				'--wavenet_params', os.path.join('tensorflow-wavenet', 'wavenet_params.json'),
				model
			])
