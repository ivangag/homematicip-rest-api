# coding=utf-8
from enum import auto, Enum


class AutoNameEnum(Enum):
    """ auto() will generate the name of the attribute as value """
    def _generate_next_value_(name, start, count, last_values):
        return name
    def __str__(self):
        return self.value

class AcousticAlarmTiming(AutoNameEnum):
    PERMANENT = auto()
    THREE_MINUTES = auto()
    SIX_MINUTES = auto()
    ONCE_PER_MINUTE = auto()

class WaterAlarmTrigger(AutoNameEnum):
    NO_ALARM = auto()
    MOISTURE_DETECTION = auto()
    WATER_DETECTION = auto()
    WATER_MOISTURE_DETECTION = auto()

class AcousticAlarmSignal(AutoNameEnum):
    DISABLE_ACOUSTIC_SIGNAL = auto()
    FREQUENCY_RISING = auto()
    FREQUENCY_FALLING = auto()
    FREQUENCY_RISING_AND_FALLING = auto()
    FREQUENCY_ALTERNATING_LOW_HIGH = auto()
    FREQUENCY_ALTERNATING_LOW_MID_HIGH = auto()
    FREQUENCY_HIGHON_OFF = auto()
    FREQUENCY_HIGHON_LONGOFF = auto()
    FREQUENCY_LOWON_OFF_HIGHON_OFF = auto()
    FREQUENCY_LOWON_LONGOFF_HIGHON_LONGOFF = auto()

class ClimateControlDisplay(AutoNameEnum):
    ACTUAL = auto()
    SETPOINT = auto()
    ACTUAL_HUMIDITY = auto()

class WindowState(AutoNameEnum):
    OPEN = auto()
    CLOSED = auto()
    TILTED = auto()

class ValveState(AutoNameEnum):
    STATE_NOT_AVAILABLE = auto()
    RUN_TO_START = auto()
    WAIT_FOR_ADAPTION = auto()
    ADAPTION_IN_PROGRESS = auto()
    ADAPTION_DONE = auto()
    TOO_TIGHT = auto()
    ADJUSTMENT_TOO_BIG = auto()
    ADJUSTMENT_TOO_SMALL = auto()
    ERROR_POSITION = auto()

class HeatingValveType(AutoNameEnum):
    NORMALLY_CLOSE = auto()
    NORMALLY_OPEN = auto()

class RGBColorState(AutoNameEnum):
    BLACK = auto()
    BLUE = auto()
    GREEN = auto()
    TURQUOISE = auto()
    RED = auto()
    PURPLE = auto()
    YELLOW = auto()
    WHITE = auto()