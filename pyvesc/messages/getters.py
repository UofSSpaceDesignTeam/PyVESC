from pyvesc.messages.base import VESCMessage
class GetValues(metaclass=VESCMessage):
    """ Gets internal sensor data
    """
    id = 4

    fields = [
            ('temp_mos1', 'h', 10),
            ('temp_mos2', 'h', 10),
            ('temp_mos3', 'h', 10),
            ('temp_mos4', 'h', 10),
            ('temp_mos5', 'h', 10),
            ('temp_mos6', 'h', 10),
            ('temp_pcb',  'h', 10),
            ('current_motor', 'i', 100),
            ('current_in',  'i', 100),
            ('duty_now',    'h', 1000),
            ('rpm',         'i', 1),
            ('v_in',        'h', 10),
            ('amp_hours',   'i', 10000),
            ('amp_hours_charged', 'i', 10000),
            ('watt_hours',  'i', 10000),
            ('watt_hours_charged', 'i', 10000),
            ('tachometer', 'i', 1),
            ('tachometer_abs', 'i', 1),
            ('mc_fault_code', 'c')
    ]


class GetRotorPosition(metaclass=VESCMessage):
    """ Gets rotor position data
    
    Must be set to DISP_POS_MODE_ENCODER or DISP_POS_MODE_PID_POS (Mode 3 or 
    Mode 4). This is set by SetRotorPositionMode (id=21).
    """
    id = 21

    fields = [
            ('rotor_pos', 'i', 100000)
    ]

class ReqSubscription(metaclass=VESCMessage):
    """ Request what messages a device is subscribed to.

    """
    id = 36
    fields = [
            ('subscription', 's')
    ]

class LidarDataMessage(metaclass=VESCMessage):
    """ Data ascociated with the Lidar"""
    id = 41
    fields = [
            ('distance', 'i'),
            ('angle', 'i')
            ]

class CompassDataMessage(metaclass=VESCMessage):
	"""Data associated with the BNO055 Digital Compass"""
	id = 42
	fields = [
			('heading1', 'f'),
			('pitch1', 'f'),
			('roll1', 'f')
			]
