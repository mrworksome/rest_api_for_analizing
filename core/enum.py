from enum import IntEnum


class SexEnum(IntEnum):
    NOT_STATED = 0
    FEMALE = 1
    MALE = 2


class StateEnum(IntEnum):
    CREATED = 0
    RUNNING = 1
    COMPLETED = 2