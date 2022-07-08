#!/usr/bin/env python3
#coding: utf-8

from zengraph import flowplot, plot, show
import threading
import rxsignal
import pycrow
import pycrow.rxcrow
import json

pycrow.start_client()

source = rxsignal.observable(pycrow.rxcrow.rxsubscribe("termux/accel"))
jdata = source.map(lambda x: json.loads(x.decode("utf-8")))


t = rxsignal.rxrange(0, 100000)
accel = jdata['LSM6DSL Accelerometer']
accx = accel['values'][0]
accy = accel['values'][1]
accz = accel['values'][2]

gyro = jdata['LSM6DSL Gyroscope']
gyrx = gyro['values'][0]
gyry = gyro['values'][1]
gyrz = gyro['values'][2]

gyrl = rxsignal.zip(gyrx, gyry, gyrz).norm()
accl = rxsignal.zip(accx, accy, accz).norm()

flowplot(t, gyrl, position=(1,1,1,1))
flowplot(t, gyrx, gyry, gyrz, position=(2,1,1,1))

flowplot(t, accl, position=(1,2,1,1))
flowplot(t, accx, accy, accz, position=(2,2,1,1))
show()

while True:
	pass