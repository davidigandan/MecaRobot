from ophyd import Device, EpicsSignal, EpicsSignalRO
from ophyd import Component as Cpt
from ophyd.utils import set_and_wait
from bluesky.plan_stubs import mv
from bluesky import RunEngine

RE = RunEngine()

class Robot(Device):
    buffer_step = Cpt(EpicsSignal, 'BufferSize')
    crossover = Cpt(EpicsSignal, 'BufferCross')
    frequency = Cpt(EpicsSignal, 'Frequency')
    file = Cpt(EpicsSignal, 'IKfile')
    parse = Cpt(EpicsSignal, 'Parse.PROC')
    buffer = Cpt(EpicsSignal, 'BufferAll.PROC')
    
    checkpoint = Cpt(EpicsSignalRO, 'Checkpoint')
    capture = 0

class Camera(Device):
    acquire = Cpt(EpicsSignal, 'Acquire')

my_robot = Robot('mecaRobot:', name = 'my_robot', read_attrs = ["checkpoint"])
my_camera = Camera('LA84R-DI-DCAM-01:CAM:', name = 'my_camera')

def scan(file,frequency = 10, buffer_step = 100, crossover = 1, capture = 0):
    my_robot.capture = capture
    yield from mv(my_robot.file, file)
    yield from mv(my_robot.frequency, frequency)
    yield from mv(my_robot.buffer_step, buffer_step)
    yield from mv(my_robot.crossover, crossover)
    yield from mv(my_robot.parse, 1)
    yield from mv(my_robot.buffer, 1)

def capture(**kwargs):
    if my_robot.capture:
        my_camera.acquire.put(1)

my_robot.checkpoint.subscribe(capture)