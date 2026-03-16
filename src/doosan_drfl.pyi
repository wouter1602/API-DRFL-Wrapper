"""
Python binding for Doosan Robotics API-DRFL using pybind11
"""
from __future__ import annotations
import collections.abc
import numpy
import numpy.typing
import typing
__all__: list[str] = ['ADD_UP', 'AM_RUN', 'Absolute', 'Add', 'Alarm', 'Autonomous', 'Avoid', 'Axis_1', 'Axis_2', 'Axis_3', 'Axis_4', 'Axis_5', 'Axis_6', 'Axis_A', 'Axis_B', 'Axis_C', 'Axis_X', 'Axis_Y', 'Axis_Z', 'BLENDING_SPEED_TYPE', 'BP_init', 'BP_start', 'BYTE_SIZE', 'Backdrive', 'Base', 'Bool', 'CALIBRATE_FTS_RESPONSE', 'CALIBRATE_JTS_RESPONSE', 'CALIBRATION_PARAM_DATA', 'CDRFLEx', 'CM_RUN', 'COG_REFERENCE', 'CONFIG_ADD_SAFETY_ZONE', 'CONFIG_COCKPIT_EX', 'CONFIG_COLLISION_MUTE_ZONE', 'CONFIG_COLLISION_MUTE_ZONE_PROPERTY', 'CONFIG_CONFIGURABLE_IO', 'CONFIG_CONFIGURABLE_IO_EX', 'CONFIG_DELETE_SAFETY_ZONE', 'CONFIG_ENCODER_MODE', 'CONFIG_ENCODER_POLARITY', 'CONFIG_GENERAL_RANGE', 'CONFIG_IDLE_OFF', 'CONFIG_INSTALL_POSE', 'CONFIG_IO_FUNC', 'CONFIG_JOINT_RANGE', 'CONFIG_NUDGE', 'CONFIG_PAYLOAD_EX', 'CONFIG_PROTECTED_ZONE', 'CONFIG_REMOTE_CONTROL', 'CONFIG_SAFETY_FUNCTION', 'CONFIG_SAFETY_IO', 'CONFIG_SAFETY_IO_EX', 'CONFIG_SAFETY_IO_OP', 'CONFIG_SAFETY_PARAM_ENABLE', 'CONFIG_SAFETY_ZONE', 'CONFIG_SAFE_ZONE', 'CONFIG_TCP', 'CONFIG_TCP_EX', 'CONFIG_TCP_LIST', 'CONFIG_TCP_LIST_EX', 'CONFIG_TCP_SYMBOL', 'CONFIG_TCP_SYMBOL_EX', 'CONFIG_TOOL', 'CONFIG_TOOL_LIST', 'CONFIG_TOOL_ORIENTATION_LIMIT_ZONE', 'CONFIG_TOOL_SHAPE', 'CONFIG_TOOL_SHAPE_LIST', 'CONFIG_TOOL_SHAPE_SYMBOL', 'CONFIG_TOOL_SYMBOL', 'CONFIG_USER_COORDINATE', 'CONFIG_USER_COORDINATE_EX', 'CONFIG_USER_COORDINATE_EX2', 'CONFIG_VIRTUAL_FENCE', 'CONFIG_WELDING_INTERFACE', 'CONFIG_WORLD_COORDINATE', 'CONFIG_WORLD_COORDINATE_EX', 'CONTROL_BRAKE', 'CONTROL_MODE', 'COORDINATE_SYSTEM', 'COUNTER_BALANCE_PARAM_DATA', 'CW_RUN', 'CW_SOS', 'Circle', 'Coils', 'Const', 'Coordinate_system_base', 'Coordinate_system_tool', 'Coordinate_system_user_max', 'Coordinate_system_user_min', 'Coordinate_system_world', 'Current', 'DATA_TYPE', 'DIGITAL_WELDING_COMM_STATE', 'DPOS', 'DRL_HG_MOVE', 'DRL_JH_SOS', 'DRL_PROGRAM_STATE', 'DR_MV_APP', 'DR_SERVOJ_TYPE', 'DVEL', 'Default', 'Delete', 'Deny', 'Discrete_inputs', 'Duplicate', 'ENABLE_SAFE_ZONE', 'EightBites', 'Emergency', 'Emergency_stop', 'Enter', 'Error', 'FLANGE_SERIAL_DATA', 'FLANGE_SER_RXD_INFO', 'FLANGE_SER_RXD_INFO_EX', 'FLANGE_VERSION', 'FORCE_AXIS', 'FORCE_MODE', 'FTS_PARAM_DATA', 'FiveBites', 'Fixed', 'Flange', 'Float', 'Force', 'Force_request', 'Forward', 'GENERAL_RANGE', 'GPIO_ANALOG_TYPE', 'GPIO_CTRLBOX_ANALOG_INDEX', 'GPIO_CTRLBOX_DIGITAL_INDEX', 'GPIO_PORT', 'GPIO_SETOUTPUT_BURST', 'GPIO_TOOL_DIGITAL_INDEX', 'Global', 'Grant', 'HG_MOVE', 'Hold', 'Holding_register', 'Homming', 'IETHERNET_SLAVE_DATA_EX', 'IETHERNET_SLAVE_RESPONSE_DATA_EX', 'INSTALL_SUB_SYSTEM', 'INVERSE_KINEMATIC_RESPONSE', 'Index_1', 'Index_10', 'Index_11', 'Index_12', 'Index_13', 'Index_14', 'Index_15', 'Index_16', 'Index_17', 'Index_18', 'Index_19', 'Index_2', 'Index_20', 'Index_21', 'Index_22', 'Index_23', 'Index_24', 'Index_25', 'Index_26', 'Index_27', 'Index_28', 'Index_29', 'Index_3', 'Index_30', 'Index_31', 'Index_32', 'Index_4', 'Index_5', 'Index_6', 'Index_7', 'Index_8', 'Index_9', 'Info', 'Init_config', 'Initialize', 'Initializing', 'Input_register', 'Install', 'Int', 'Intent', 'Intialize', 'Inverter', 'Inward', 'JH_MOVE', 'JH_SOS', 'JOG_AXIS', 'JOINT_AXIS', 'JOINT_RANGE', 'JTS_PARAM_DATA', 'Joint', 'Joint_1', 'Joint_2', 'Joint_3', 'Joint_4', 'Joint_5', 'Joint_6', 'KT_5G_CONFIG_PARAM', 'LICENSE_TEXT_PARAM', 'LINE', 'LINE_2D', 'LOCAL_ZONE_PROPERTY_COLLISION_STOPMODE', 'LOCAL_ZONE_PROPERTY_JOINT_RANGE', 'LOCAL_ZONE_PROPERTY_JOINT_SPEED', 'LOCAL_ZONE_PROPERTY_TCPSLF_STOPMODE', 'LOCAL_ZONE_PROPERTY_TOOL_ORIENTATION', 'LOG_ALARM', 'LOG_GROUP', 'LOG_LEVEL', 'Last', 'Line', 'Loss', 'MANAGE_ACCESS_CONTROL', 'MEASURE_FRICTION_RESPONSE', 'MEASURE_TCP_RESPONSE', 'MEASURE_TOOL_RESPONSE', 'MESSAGE_INPUT', 'MESSAGE_LEVEL', 'MESSAGE_POPUP', 'MESSAGE_PROGRESS', 'MODBUS_DATA', 'MODBUS_DATA_LIST', 'MODBUS_MULTI_REGISTER', 'MODBUS_REGISTER', 'MODBUS_REGISTER_BURST', 'MODBUS_REGISTER_MONITORING', 'MODBUS_REGISTER_TYPE', 'MONITORING_ACCESS_CONTROL', 'MONITORING_ALARM', 'MONITORING_AMODEL', 'MONITORING_COCKPIT', 'MONITORING_CONTROL', 'MONITORING_CONTROL_EX', 'MONITORING_CTRLIO', 'MONITORING_CTRLIO_EX', 'MONITORING_CTRLIO_EX2', 'MONITORING_DATA', 'MONITORING_DATA_EX', 'MONITORING_FLANGE_IO_CONFIG', 'MONITORING_FORCECONTROL', 'MONITORING_IE_GPR', 'MONITORING_IE_SLAVE', 'MONITORING_INPUT', 'MONITORING_MBUS_SLAVE_COIL', 'MONITORING_MBUS_SLAVE_HOILDING_REGISTER', 'MONITORING_MISC', 'MONITORING_MODBUS', 'MONITORING_POPUP', 'MONITORING_SPEED', 'MONITORING_WELDING', 'MOVEB_BLENDING_TYPE', 'MOVE_HOME', 'MOVE_MODE', 'MOVE_ORIENTATION', 'MOVE_POSB', 'MOVE_REFERENCE', 'Manual', 'Measure', 'Mechanic', 'MotionLIB', 'Move', 'Moving', 'NORMAL_VECTOR', 'NORMAL_VECTOR_RESPONSE', 'NPN', 'None', 'Normal', 'Normal_mode', 'Not_ready', 'OUTPUT_TYPE', 'One', 'Operation', 'Outward', 'Override', 'PARITY_CHECK', 'PATH_MODE', 'PNP', 'POINT_2D', 'POINT_3D', 'POPUP_RESPONSE', 'POSITION', 'POSITION_ADDTO', 'POSITION_ADDTO_RESPONSE', 'POSITION_EX', 'PROGRAM_ERROR', 'PROGRAM_EXECUTION_EX', 'PROGRAM_STOP_CAUSE', 'PROGRAM_SYNTAX_CHECK', 'PROGRAM_WATCH_VARIABLE', 'Play', 'PosJ', 'PosX', 'Queue', 'Quick', 'Quick_STO', 'READ_CTRLIO_INPUT', 'READ_CTRLIO_INPUT_EX', 'READ_CTRLIO_INPUT_EX2', 'READ_CTRLIO_OUTPUT', 'READ_CTRLIO_OUTPUT_EX', 'READ_CTRLIO_OUTPUT_EX2', 'READ_ENCODER_INPUT', 'READ_FLANGE_SERIAL', 'READ_FLANGE_SERIAL_EX', 'READ_PROCESS_INPUT', 'RELEASE_MODE', 'REPORT_TCP_CLIENT', 'ROBOT_CONTROL', 'ROBOT_FORCE', 'ROBOT_LED_CONFIG', 'ROBOT_LINK_INFO', 'ROBOT_MODE', 'ROBOT_MONITORING_AMODEL', 'ROBOT_MONITORING_DATA_EX', 'ROBOT_MONITORING_JOINT', 'ROBOT_MONITORING_SENSOR', 'ROBOT_MONITORING_STATE', 'ROBOT_MONITORING_TASK', 'ROBOT_MONITORING_TORQUE', 'ROBOT_MONITORING_USER', 'ROBOT_MONITORING_WORLD', 'ROBOT_POSE', 'ROBOT_SPACE', 'ROBOT_STATE', 'ROBOT_SYSTEM', 'ROBOT_TASK_POSE', 'ROBOT_VEL', 'ROBOT_WELDING_DATA', 'ROT_DIR', 'RT_INPUT_DATA_LIST', 'RT_OUTPUT_DATA_LIST', 'RV_BACK', 'RV_HG_MOVE', 'RV_MOVE', 'RV_SOS', 'Radial', 'Real', 'Recovery', 'Recovery_backdrive', 'Recovery_safe_off', 'Recovery_safe_stop', 'Reduced_mode', 'Relative', 'Release', 'Remove', 'Replace', 'Request', 'Reserved1', 'Reserved2', 'Reserved3', 'Reserved4', 'Reset', 'Reset_recovery', 'Reset_safe_off', 'Reset_safe_stop', 'Reset_safet_off', 'Reset_safet_stop', 'Response_no', 'Response_yes', 'Resume', 'Reverse', 'SAFETY_MODE', 'SAFETY_MODE_EVENT', 'SAFETY_OBJECT', 'SAFETY_OBJECT_CAPSULE', 'SAFETY_OBJECT_CUBE', 'SAFETY_OBJECT_DATA', 'SAFETY_OBJECT_OBB', 'SAFETY_OBJECT_POLYPRISM', 'SAFETY_OBJECT_SPHERE', 'SAFETY_STATE', 'SAFETY_TOOL_ORIENTATION_LIMIT', 'SAFETY_ZONE_PROPERTY_DATA', 'SAFETY_ZONE_PROPERTY_LOCAL_ZONE', 'SAFETY_ZONE_PROPERTY_SPACE_LIMIT', 'SAFETY_ZONE_SHAPE', 'SAFETY_ZONE_SHAPE_CAPSULE', 'SAFETY_ZONE_SHAPE_CUBOID', 'SAFETY_ZONE_SHAPE_CYLINDER', 'SAFETY_ZONE_SHAPE_DATA', 'SAFETY_ZONE_SHAPE_SPHERE', 'SAFETY_ZONE_SHAPE_TILTED_CUBOID', 'SAFE_STOP_RESET_TYPE', 'SERIAL_PORT_NAME', 'SERIAL_SEARCH', 'SINGULARITY_AVOIDANCE', 'SPEED_MODE', 'SPIRAL_DIR', 'SPLINE_VELOCITY_OPTION', 'STOP_BITS', 'STOP_TYPE', 'SUB_PROGRAM', 'SW_RUN', 'SW_SOS', 'SYSTEM_CPUUSAGE', 'SYSTEM_DISKSIZE', 'SYSTEM_IPADDRESS', 'SYSTEM_POWER', 'SYSTEM_TIME', 'SYSTEM_UPDATE_RESPONSE', 'SYSTEM_VERSION', 'Safe_off', 'Safe_off2', 'Safe_stop', 'Safe_stop2', 'SafetyController', 'Save', 'Servo_on', 'SevenBites', 'SixBites', 'Slow', 'SmartTP', 'Standby', 'Stop', 'String', 'Sys_info', 'Sys_last', 'Sys_warn', 'SystemFMK', 'TASK_AXIS', 'TCP', 'Task', 'Task_RX', 'Task_RY', 'Task_RZ', 'Task_X', 'Task_Y', 'Task_Z', 'Teach', 'Teaching', 'Tool', 'Two', 'UPDATE_MODBUS_MULTI_REGISTER', 'USER_COORDINATE', 'USER_COORDINATE_MATRIX_RESPONSE', 'USER_COORD_EXTERNAL_FORCE', 'USER_COORD_EXTERNAL_FORCE_INFO', 'Unknown', 'User', 'User_max', 'User_min', 'VARIABLE_TYPE', 'VD_SOS', 'VD_STO', 'VECTOR3D', 'VECTOR6D', 'VIRTUAL_FENCE_RESPONSE', 'Vel', 'Virtual', 'Voltage', 'WEAVING_OFFSET', 'WELDING_CHANNEL', 'WRITE_MODBUS_BURST', 'WRITE_MODBUS_DATA', 'WRITE_MODBUS_RTU_DATA', 'WRITE_MODBUS_TCP_DATA', 'WRITE_SERIAL_BURST', 'Warn', 'Weld', 'World', 'even', 'none', 'odd', 'position', 'torque']
class ADD_UP:
    """
    Members:
    
      Replace
    
      Add
    
      Remove
    """
    Add: typing.ClassVar[ADD_UP]  # value = <ADD_UP.Add: 1>
    Remove: typing.ClassVar[ADD_UP]  # value = <ADD_UP.Remove: 2>
    Replace: typing.ClassVar[ADD_UP]  # value = <ADD_UP.Replace: 0>
    __members__: typing.ClassVar[dict[str, ADD_UP]]  # value = {'Replace': <ADD_UP.Replace: 0>, 'Add': <ADD_UP.Add: 1>, 'Remove': <ADD_UP.Remove: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class BLENDING_SPEED_TYPE:
    """
    Members:
    
      Duplicate
    
      Override
    """
    Duplicate: typing.ClassVar[BLENDING_SPEED_TYPE]  # value = <BLENDING_SPEED_TYPE.Duplicate: 0>
    Override: typing.ClassVar[BLENDING_SPEED_TYPE]  # value = <BLENDING_SPEED_TYPE.Override: 1>
    __members__: typing.ClassVar[dict[str, BLENDING_SPEED_TYPE]]  # value = {'Duplicate': <BLENDING_SPEED_TYPE.Duplicate: 0>, 'Override': <BLENDING_SPEED_TYPE.Override: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class BYTE_SIZE:
    """
    Members:
    
      FiveBites
    
      SixBites
    
      SevenBites
    
      EightBites
    """
    EightBites: typing.ClassVar[BYTE_SIZE]  # value = <BYTE_SIZE.EightBites: 8>
    FiveBites: typing.ClassVar[BYTE_SIZE]  # value = <BYTE_SIZE.FiveBites: 5>
    SevenBites: typing.ClassVar[BYTE_SIZE]  # value = <BYTE_SIZE.SevenBites: 7>
    SixBites: typing.ClassVar[BYTE_SIZE]  # value = <BYTE_SIZE.SixBites: 6>
    __members__: typing.ClassVar[dict[str, BYTE_SIZE]]  # value = {'FiveBites': <BYTE_SIZE.FiveBites: 5>, 'SixBites': <BYTE_SIZE.SixBites: 6>, 'SevenBites': <BYTE_SIZE.SevenBites: 7>, 'EightBites': <BYTE_SIZE.EightBites: 8>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class CALIBRATION_PARAM_DATA:
    def __init__(self) -> None:
        ...
    @property
    def _Ax(self) -> float:
        ...
    @_Ax.setter
    def _Ax(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _Bx(self) -> float:
        ...
    @_Bx.setter
    def _Bx(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _Cx(self) -> float:
        ...
    @_Cx.setter
    def _Cx(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _Dx(self) -> float:
        ...
    @_Dx.setter
    def _Dx(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class CDRFLEx:
    @staticmethod
    def set_workpiece_weight(*args, **kwargs) -> bool:
        ...
    def __init__(self) -> None:
        ...
    def add_modbus_signal(self, strSymbol: str, strIpAddress: str, nPort: typing.SupportsInt | typing.SupportsIndex, eRegType: MODBUS_REGISTER_TYPE, iRegIndex: typing.SupportsInt | typing.SupportsIndex, nRegValue: typing.SupportsInt | typing.SupportsIndex = 0, nSlaveId: typing.SupportsInt | typing.SupportsIndex = 255) -> bool:
        ...
    def add_tcp(self, strSymbol: str, fPosition: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> bool:
        ...
    def add_tool(self, strSymbol: str, fWeight: typing.SupportsFloat | typing.SupportsIndex, fCog: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fInertia: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> bool:
        ...
    @typing.overload
    def align_axis(self, fTargetPos1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetPos2: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetPos3: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fSourceVec: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], eTaskAxis: TASK_AXIS, eSourceRef: COORDINATE_SYSTEM = ...) -> bool:
        ...
    @typing.overload
    def align_axis(self, fTargetVec: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fSourceVec: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], eTaskAxis: TASK_AXIS, eSourceRef: COORDINATE_SYSTEM) -> bool:
        ...
    def alter_motion(self, fTargetPos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> bool:
        ...
    def amove_periodic(self, fAmplitude: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fPeriodic: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fAccelTime: typing.SupportsFloat | typing.SupportsIndex, nRepeat: typing.SupportsInt | typing.SupportsIndex, eMoveReference: MOVE_REFERENCE = ...) -> bool:
        ...
    @typing.overload
    def amove_spiral(self, eTaskAxis: TASK_AXIS, fRevolution: typing.SupportsFloat | typing.SupportsIndex, fMaximuRadius: typing.SupportsFloat | typing.SupportsIndex, fMaximumLength: typing.SupportsFloat | typing.SupportsIndex, fTargetVel: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetAcc: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetTime: typing.SupportsFloat | typing.SupportsIndex = 0.0, eMoveReference: MOVE_REFERENCE = ...) -> bool:
        ...
    @typing.overload
    def amove_spiral(self, eTaskAxis: TASK_AXIS, fRevolution: typing.SupportsFloat | typing.SupportsIndex, fTargetPos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetVel: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetAcc: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetTime: typing.SupportsFloat | typing.SupportsIndex = 0.0, eMoveReference: MOVE_REFERENCE = ..., eMoveMode: MOVE_MODE = ..., eSpiralDir: SPIRAL_DIR = ..., eRotDir: ROT_DIR = ...) -> bool:
        ...
    def amoveb(self, tTargetPos: typing.Annotated[numpy.typing.ArrayLike, MOVE_POSB], nPosCount: typing.SupportsInt | typing.SupportsIndex, fTargetVel: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetAcc: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetTime: typing.SupportsFloat | typing.SupportsIndex = 0.0, eMoveMode: MOVE_MODE = ..., eMoveReference: MOVE_REFERENCE = ..., eAppType: DR_MV_APP = ...) -> bool:
        ...
    def amovec(self, fTargetPos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetVel: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetAcc: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetTime: typing.SupportsFloat | typing.SupportsIndex = 0.0, eMoveMode: MOVE_MODE = ..., eMoveReference: MOVE_REFERENCE = ..., fTargetAngle1: typing.SupportsFloat | typing.SupportsIndex = 0.0, fTargetAngle2: typing.SupportsFloat | typing.SupportsIndex = 0.0, eBlendingType: BLENDING_SPEED_TYPE = ..., eOrientation: MOVE_ORIENTATION = ..., eAppType: DR_MV_APP = ...) -> bool:
        ...
    def amovej(self, fTargetPos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetVel: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetAcc: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetTime: typing.SupportsFloat | typing.SupportsIndex = 0.0, eMoveMode: MOVE_MODE = ..., eBlendingType: BLENDING_SPEED_TYPE = ...) -> bool:
        ...
    def amovel(self, fTargetPos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetVel: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetAcc: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetTime: typing.SupportsFloat | typing.SupportsIndex = 0.0, eMoveMode: MOVE_MODE = ..., eMoveReference: MOVE_REFERENCE = ..., eBlendingType: BLENDING_SPEED_TYPE = ..., eAppType: DR_MV_APP = ...) -> bool:
        ...
    @typing.overload
    def amovesj(self, fTargetPos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], nPosCount: typing.SupportsInt | typing.SupportsIndex, fTargetVel: typing.SupportsFloat | typing.SupportsIndex, fTargetAcc: typing.SupportsFloat | typing.SupportsIndex, fTargetTime: typing.SupportsFloat | typing.SupportsIndex = 0.0, eMoveMode: MOVE_MODE = ...) -> bool:
        ...
    @typing.overload
    def amovesj(self, fTargetPos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], nPosCount: typing.SupportsInt | typing.SupportsIndex, fTargetVel: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetAcc: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetTime: typing.SupportsFloat | typing.SupportsIndex = 0.0, eMoveMode: MOVE_MODE = ...) -> bool:
        ...
    def amovesx(self, fTargetPos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], nPosCount: typing.SupportsInt | typing.SupportsIndex, fTargetVel: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetAcc: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetTime: typing.SupportsFloat | typing.SupportsIndex = 0.0, eMoveMode: MOVE_MODE = ..., eMoveReference: MOVE_REFERENCE = ..., eVelOpt: SPLINE_VELOCITY_OPTION = ...) -> bool:
        ...
    def calc_coord(self, nCnt: typing.SupportsInt | typing.SupportsIndex, nInputMode: typing.SupportsInt | typing.SupportsIndex, eTargetRef: COORDINATE_SYSTEM, fTargetPos1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetPos2: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetPos3: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetPos4: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> ROBOT_POSE:
        ...
    def change_collision_sensitivity(self, fSensitivity: typing.SupportsFloat | typing.SupportsIndex) -> bool:
        ...
    def change_operation_speed(self, fSpeed: typing.SupportsFloat | typing.SupportsIndex) -> bool:
        ...
    def check_force_condition(self, eForceAxis: FORCE_AXIS, fTargetMin: typing.SupportsFloat | typing.SupportsIndex, fTargetMax: typing.SupportsFloat | typing.SupportsIndex, eForceReference: COORDINATE_SYSTEM = ...) -> bool:
        ...
    @typing.overload
    def check_motion(self) -> int:
        ...
    @typing.overload
    def check_motion(self) -> int:
        ...
    @typing.overload
    def check_orientation_condition(self, eForceAxis: FORCE_AXIS, fTargetMin: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetMax: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], eForceReference: COORDINATE_SYSTEM = ...) -> bool:
        ...
    @typing.overload
    def check_orientation_condition(self, eForceAxis: FORCE_AXIS, fTargetMin: typing.SupportsFloat | typing.SupportsIndex, fTargetMax: typing.SupportsFloat | typing.SupportsIndex, fTargetPos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], eForceReference: COORDINATE_SYSTEM = ...) -> bool:
        ...
    def check_position_condition(self, eForceAxis: FORCE_AXIS, fTargetMin: typing.SupportsFloat | typing.SupportsIndex, fTargetMax: typing.SupportsFloat | typing.SupportsIndex, fTargetPos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], eMode: MOVE_MODE = ..., eForceReference: COORDINATE_SYSTEM = ...) -> bool:
        ...
    def check_position_condition_abs(self, eForceAxis: FORCE_AXIS, fTargetMin: typing.SupportsFloat | typing.SupportsIndex, fTargetMax: typing.SupportsFloat | typing.SupportsIndex, eForceReference: COORDINATE_SYSTEM = ...) -> bool:
        ...
    def check_position_condition_rel(self, eForceAxis: FORCE_AXIS, fTargetMin: typing.SupportsFloat | typing.SupportsIndex, fTargetMax: typing.SupportsFloat | typing.SupportsIndex, fTargetPos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], eForceReference: COORDINATE_SYSTEM = ...) -> bool:
        ...
    def close_connection(self) -> bool:
        """
        Close connection to the Doosan robot controller
        """
    def config_program_watch_variable(self, eDivision: VARIABLE_TYPE, eType: DATA_TYPE, strName: str, strData: str) -> bool:
        ...
    def coord_transform(self, fTargetPos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], eInCoordSystem: COORDINATE_SYSTEM, eOutCoordSystem: COORDINATE_SYSTEM) -> ROBOT_POSE:
        ...
    def del_modbus_signal(self, strSymbol: str) -> bool:
        ...
    def del_tcp(self, strSymbol: str) -> bool:
        ...
    def del_tool(self, strSymbol: str) -> bool:
        ...
    def disable_alter_motion(self) -> bool:
        ...
    def drl_pause(self) -> bool:
        ...
    def drl_resume(self) -> bool:
        ...
    def drl_start(self, eRobotSystem: ROBOT_SYSTEM, strDrlProgram: str) -> bool:
        ...
    def drl_stop(self, eStopType: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
        ...
    def enable_alter_motion(self, iCycleTime: typing.SupportsInt | typing.SupportsIndex, ePathMode: PATH_MODE, eTargetRef: COORDINATE_SYSTEM, fLimitDpos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fLimitDposPer: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> bool:
        ...
    def fkin(self, fSourcePos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], eTargetRef: COORDINATE_SYSTEM = ...) -> ROBOT_POSE:
        ...
    def flange_serial_close(self, nPort: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    def flange_serial_open(self, nPort: typing.SupportsInt | typing.SupportsIndex, baudrate: typing.SupportsInt | typing.SupportsIndex = 115200, eByteSize: BYTE_SIZE = ..., eParity: PARITY_CHECK = ..., eStopBits: STOP_BITS = ...) -> bool:
        ...
    def flange_serial_write(self, pSendData: bytes, nPort: typing.SupportsInt | typing.SupportsIndex = 1) -> bool:
        ...
    def get_analog_input(self, eGpioIndex: GPIO_CTRLBOX_ANALOG_INDEX) -> float:
        ...
    def get_control_mode(self) -> CONTROL_MODE:
        """
        Get the control mode
        """
    def get_control_space(self) -> ROBOT_SPACE:
        """
        Get the control space
        """
    def get_current_pose(self, spaceType: ROBOT_SPACE = ...) -> ROBOT_POSE:
        """
        Get the current pose
        """
    def get_current_posj(self) -> ROBOT_POSE:
        """
        Get the current position in joint space
        """
    def get_current_posx(self, coodType: COORDINATE_SYSTEM = ...) -> ROBOT_TASK_POSE:
        """
        Get the current position in Cartesian space
        """
    def get_current_rotm(self, targetRef: COORDINATE_SYSTEM = ...) -> numpy.typing.NDArray[numpy.float32]:
        """
        Get the current rotation matrix
        """
    def get_current_solution_space(self) -> int:
        """
        Get the current solution space
        """
    def get_current_tool_flange_posx(self) -> ROBOT_POSE:
        """
        Get the current tool flange position in Cartesian space
        """
    def get_current_velj(self) -> ROBOT_VEL:
        """
        Get the current velocity in joint space
        """
    def get_current_velx(self) -> ROBOT_VEL:
        """
        Get the current velocity in Cartesian space
        """
    def get_desired_posj(self) -> ROBOT_POSE:
        """
        Get the desired position in joint space
        """
    def get_desired_posx(self, coodType: COORDINATE_SYSTEM = ...) -> ROBOT_POSE:
        """
        Get the desired position in Cartesian space
        """
    def get_desired_velx(self) -> ROBOT_VEL:
        """
        Get the desired velocity in Cartesian space
        """
    def get_digital_input(self, eGpioIndex: GPIO_CTRLBOX_DIGITAL_INDEX) -> bool:
        ...
    def get_digital_output(self, eGpioIndex: GPIO_CTRLBOX_DIGITAL_INDEX) -> bool:
        ...
    def get_external_torque(self) -> ROBOT_FORCE:
        """
        Get the external torque
        """
    def get_joint_torque(self) -> ROBOT_FORCE:
        """
        Get the joint torque
        """
    def get_last_alarm(self) -> LOG_ALARM:
        """
        Get the last alarm
        """
    def get_library_version(self) -> str:
        """
        Get the library version
        """
    def get_modbus_input(self, strSymbol: str) -> int:
        ...
    def get_orientation_error(self, position1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], position2: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], taskAxis: TASK_AXIS) -> float:
        """
        Get the orientation error
        """
    def get_program_state(self) -> DRL_PROGRAM_STATE:
        """
        Get the program state
        """
    def get_robot_mode(self) -> ROBOT_MODE:
        """
        Get the robot mode
        """
    def get_robot_speed_mode(self) -> MONITORING_SPEED:
        """
        Get the robot speed mode
        """
    def get_robot_state(self) -> ROBOT_STATE:
        """
        Get the robot state
        """
    def get_robot_system(self) -> ROBOT_SYSTEM:
        """
        Get the robot system
        """
    def get_safety_configuration(self) -> _SAFETY_CONFIGURATION_EX2:
        """
        Get the safety configuration
        """
    def get_solution_space(self, targetPos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> int:
        """
        Get the solution space
        """
    def get_system_version(self, version: SYSTEM_VERSION) -> bool:
        """
        Get the system version
        """
    def get_tcp(self) -> str:
        ...
    def get_tool(self) -> str:
        ...
    def get_tool_analog_input(self, nCh: typing.SupportsInt | typing.SupportsIndex) -> float:
        ...
    def get_tool_digital_input(self, eGpioIndex: GPIO_TOOL_DIGITAL_INDEX) -> bool:
        ...
    def get_tool_digital_output(self, eGpioIndex: GPIO_TOOL_DIGITAL_INDEX) -> bool:
        ...
    def get_tool_force(self, targetRef: COORDINATE_SYSTEM = ...) -> ROBOT_FORCE:
        """
        Get the tool force
        """
    def get_user_cart_coord(self, iReqId: typing.SupportsInt | typing.SupportsIndex) -> USER_COORDINATE:
        ...
    def get_workpiece_weight(self) -> float:
        ...
    @typing.overload
    def ikin(self, fSourcePos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], iSolutionSpace: typing.SupportsInt | typing.SupportsIndex, eTargetRef: COORDINATE_SYSTEM = ...) -> ROBOT_POSE:
        ...
    @typing.overload
    def ikin(self, fSourcePos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], iSolutionSpace: typing.SupportsInt | typing.SupportsIndex, eTargetRef: COORDINATE_SYSTEM, iRefPosOpt: typing.SupportsInt | typing.SupportsIndex) -> INVERSE_KINEMATIC_RESPONSE:
        ...
    @typing.overload
    def ikin(self, fSourcePos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], iSolutionSpace: typing.SupportsInt | typing.SupportsIndex, eTargetRef: COORDINATE_SYSTEM, fIterThreshold: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> INVERSE_KINEMATIC_RESPONSE:
        ...
    def is_done_bolt_tightening(self, eForceAxis: FORCE_AXIS, fTargetTor: typing.SupportsFloat | typing.SupportsIndex = 0.0, fTimeout: typing.SupportsFloat | typing.SupportsIndex = 0.0) -> bool:
        ...
    def jog(self, axis: JOG_AXIS, reference: MOVE_REFERENCE, velocity: typing.SupportsFloat | typing.SupportsIndex) -> bool:
        """
        Jog the robot
        """
    def manage_access_control(self, accessControl: MANAGE_ACCESS_CONTROL = ...) -> bool:
        """
        Manage access control
        """
    def move_home(self, mode: MOVE_HOME = ..., run: typing.SupportsInt | typing.SupportsIndex = 1) -> bool:
        """
        Move the robot to home position
        """
    def move_pause(self) -> bool:
        ...
    def move_periodic(self, fAmplitude: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fPeriodic: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fAccelTime: typing.SupportsFloat | typing.SupportsIndex, nRepeat: typing.SupportsInt | typing.SupportsIndex, eMoveReference: MOVE_REFERENCE = ...) -> bool:
        ...
    def move_resume(self) -> bool:
        ...
    @typing.overload
    def move_spiral(self, eTaskAxis: TASK_AXIS, fRevolution: typing.SupportsFloat | typing.SupportsIndex, fMaximuRadius: typing.SupportsFloat | typing.SupportsIndex, fMaximumLength: typing.SupportsFloat | typing.SupportsIndex, fTargetVel: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetAcc: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetTime: typing.SupportsFloat | typing.SupportsIndex = 0.0, eMoveReference: MOVE_REFERENCE = ...) -> bool:
        ...
    @typing.overload
    def move_spiral(self, eTaskAxis: TASK_AXIS, fRevolution: typing.SupportsFloat | typing.SupportsIndex, fTargetPos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetVel: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetAcc: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetTime: typing.SupportsFloat | typing.SupportsIndex = 0.0, eMoveReference: MOVE_REFERENCE = ..., eMoveMode: MOVE_MODE = ..., eSpiralDir: SPIRAL_DIR = ..., eRotDir: ROT_DIR = ...) -> bool:
        ...
    def moveb(self, tTargetPos: typing.Annotated[numpy.typing.ArrayLike, MOVE_POSB], nPosCount: typing.SupportsInt | typing.SupportsIndex, fTargetVel: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetAcc: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetTime: typing.SupportsFloat | typing.SupportsIndex = 0.0, eMoveMode: MOVE_MODE = ..., eMoveReference: MOVE_REFERENCE = ..., eAppType: DR_MV_APP = ...) -> bool:
        ...
    def movec(self, pos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], vel: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], acc: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], time: typing.SupportsFloat | typing.SupportsIndex = 0.0, move_mode: MOVE_MODE = ..., move_reference: MOVE_REFERENCE = ..., target_angle1: typing.SupportsFloat | typing.SupportsIndex = 0.0, target_angle2: typing.SupportsFloat | typing.SupportsIndex = 0.0, blending_radius: typing.SupportsFloat | typing.SupportsIndex = 0.0, blending_type: BLENDING_SPEED_TYPE = ..., orientation: MOVE_ORIENTATION = ..., app_type: DR_MV_APP = ...) -> bool:
        ...
    @typing.overload
    def movej(self, pos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], vel: typing.SupportsFloat | typing.SupportsIndex, acc: typing.SupportsFloat | typing.SupportsIndex, time: typing.SupportsFloat | typing.SupportsIndex = 0.0, move_mode: MOVE_MODE = ..., blending_radius: typing.SupportsFloat | typing.SupportsIndex = 0.0, blending_type: BLENDING_SPEED_TYPE = ...) -> bool:
        """
        Movej array command
        """
    @typing.overload
    def movej(self, pos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], vel: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], acc: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], time: typing.SupportsFloat | typing.SupportsIndex = 0.0, move_mode: MOVE_MODE = ..., blending_radius: typing.SupportsFloat | typing.SupportsIndex = 0.0, blending_type: BLENDING_SPEED_TYPE = ...) -> bool:
        """
        Movej array command
        """
    @typing.overload
    def movejx(self, pos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], solution_space: typing.SupportsInt | typing.SupportsIndex, vel: typing.SupportsFloat | typing.SupportsIndex, acc: typing.SupportsFloat | typing.SupportsIndex, time: typing.SupportsFloat | typing.SupportsIndex = 0.0, move_mode: MOVE_MODE = ..., move_reference: MOVE_REFERENCE = ..., blending_radius: typing.SupportsFloat | typing.SupportsIndex = 0.10000000149011612, blending_type: BLENDING_SPEED_TYPE = ...) -> bool:
        """
        movejx command
        """
    @typing.overload
    def movejx(self, pos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], solution_space: typing.SupportsInt | typing.SupportsIndex, vel: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], acc: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], time: typing.SupportsFloat | typing.SupportsIndex = 0.0, move_mode: MOVE_MODE = ..., move_reference: MOVE_REFERENCE = ..., blending_radius: typing.SupportsFloat | typing.SupportsIndex = 0.10000000149011612, blending_type: BLENDING_SPEED_TYPE = ...) -> bool:
        """
        movejx command
        """
    def movel(self, pos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], vel: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], acc: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], time: typing.SupportsFloat | typing.SupportsIndex = 0.0, move_mode: MOVE_MODE = ..., move_reference: MOVE_REFERENCE = ..., blending_radius: typing.SupportsFloat | typing.SupportsIndex = 0.0, blending_type: BLENDING_SPEED_TYPE = ..., app_type: DR_MV_APP = ...) -> bool:
        """
        Movel command
        """
    @typing.overload
    def movesj(self, fTargetPos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], nPosCount: typing.SupportsInt | typing.SupportsIndex, fTargetVel: typing.SupportsFloat | typing.SupportsIndex, fTargetAcc: typing.SupportsFloat | typing.SupportsIndex, fTargetTime: typing.SupportsFloat | typing.SupportsIndex = 0.0, eMoveMode: MOVE_MODE = ...) -> bool:
        ...
    @typing.overload
    def movesj(self, fTargetPos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], nPosCount: typing.SupportsInt | typing.SupportsIndex, fTargetVel: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetAcc: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetTime: typing.SupportsFloat | typing.SupportsIndex = 0.0, eMoveMode: MOVE_MODE = ...) -> bool:
        ...
    def movesx(self, fTargetPos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], nPosCount: typing.SupportsInt | typing.SupportsIndex, fTargetVel: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetAcc: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetTime: typing.SupportsFloat | typing.SupportsIndex = 0.0, eMoveMode: MOVE_MODE = ..., eMoveReference: MOVE_REFERENCE = ..., eVelOpt: SPLINE_VELOCITY_OPTION = ...) -> bool:
        ...
    def mwait(self) -> bool:
        ...
    def open_connection(self, ip: str = '192.168.137.100', port: typing.SupportsInt | typing.SupportsIndex = 12345) -> bool:
        """
        Connect to the Doosan robot controller
        """
    def overwrite_user_cart_coord(self, bTargetUpdate: bool, iReqId: typing.SupportsInt | typing.SupportsIndex, fTargetPos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], eTargetRef: COORDINATE_SYSTEM = ...) -> int:
        ...
    @typing.overload
    def parallel_axis(self, fTargetPos1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetPos2: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetPos3: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], eTaskAxis: TASK_AXIS, eSourceRef: COORDINATE_SYSTEM = ...) -> bool:
        ...
    @typing.overload
    def parallel_axis(self, fTargetVec: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], eTaskAxis: TASK_AXIS, eSourceRef: COORDINATE_SYSTEM) -> bool:
        ...
    def query_modbus_data_list(self) -> MODBUS_DATA_LIST:
        ...
    def release_compliance_ctrl(self) -> bool:
        ...
    def release_force(self, fTargetTime: typing.SupportsFloat | typing.SupportsIndex = 0.0) -> bool:
        ...
    def release_protective_stop(self, eReleaseMode: RELEASE_MODE) -> bool:
        ...
    def reset_workpiece_weight(self) -> bool:
        ...
    def save_sub_program(self, iTargetType: typing.SupportsInt | typing.SupportsIndex, strFileName: str, strDrlProgram: str) -> bool:
        ...
    def servo_off(self, eStopType: STOP_TYPE) -> int:
        ...
    def servoj(self, fTargetPos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fLimitVel: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fLimitAcc: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetTime: typing.SupportsFloat | typing.SupportsIndex, eTargetMod: DR_SERVOJ_TYPE = ...) -> bool:
        ...
    def servol(self, fTargetPos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fLimitVel: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fLimitAcc: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetTime: typing.SupportsFloat | typing.SupportsIndex) -> bool:
        ...
    def set_analog_output(self, eGpioIndex: GPIO_CTRLBOX_ANALOG_INDEX, fValue: typing.SupportsFloat | typing.SupportsIndex) -> bool:
        ...
    def set_auto_servo_off(self, bFuncEnable: bool, fElapseTime: typing.SupportsFloat | typing.SupportsIndex) -> bool:
        ...
    def set_desired_force(self, fTargetForce: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], iTargetDirection: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8], eForceReference: COORDINATE_SYSTEM = ..., fTargetTime: typing.SupportsFloat | typing.SupportsIndex = 0.0, eForceMode: FORCE_MODE = ...) -> bool:
        ...
    def set_digital_output(self, eGpioIndex: GPIO_CTRLBOX_DIGITAL_INDEX, bOnOff: bool) -> bool:
        ...
    def set_modbus_output(self, strSymbol: str, nValue: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    def set_mode_analog_input(self, eGpioIndex: GPIO_CTRLBOX_ANALOG_INDEX, eAnalogType: GPIO_ANALOG_TYPE = ...) -> bool:
        ...
    def set_mode_analog_output(self, eGpioIndex: GPIO_CTRLBOX_ANALOG_INDEX, eAnalogType: GPIO_ANALOG_TYPE = ...) -> bool:
        ...
    def set_mode_tool_analog_input(self, nCh: typing.SupportsInt | typing.SupportsIndex, eAnalogType: GPIO_ANALOG_TYPE) -> bool:
        ...
    def set_on_disconnected(self, pCallbackFunc: collections.abc.Callable) -> None:
        ...
    def set_on_homming_completed(self, pCallbackFunc: collections.abc.Callable) -> None:
        ...
    def set_on_log_alarm(self, pCallbackFunc: collections.abc.Callable) -> None:
        ...
    def set_on_mastering_need(self, pCallbackFunc: collections.abc.Callable) -> None:
        ...
    def set_on_monitoring_access_control(self, pCallbackFunc: collections.abc.Callable) -> None:
        ...
    def set_on_monitoring_ctrl_io(self, pCallbackFunc: collections.abc.Callable) -> None:
        ...
    def set_on_monitoring_ctrl_io_ex(self, pCallbackFunc: collections.abc.Callable) -> None:
        ...
    def set_on_monitoring_data(self, pCallbackFunc: collections.abc.Callable) -> None:
        ...
    def set_on_monitoring_data_ex(self, pCallbackFunc: collections.abc.Callable) -> None:
        ...
    def set_on_monitoring_modbus(self, pCallbackFunc: collections.abc.Callable) -> None:
        ...
    def set_on_monitoring_robot_system(self, pCallbackFunc: collections.abc.Callable) -> None:
        ...
    def set_on_monitoring_safety_state(self, pCallbackFunc: collections.abc.Callable) -> None:
        ...
    def set_on_monitoring_speed_mode(self, pCallbackFunc: collections.abc.Callable) -> None:
        ...
    def set_on_monitoring_state(self, pCallbackFunc: collections.abc.Callable) -> None:
        ...
    def set_on_program_stopped(self, pCallbackFunc: collections.abc.Callable) -> None:
        ...
    def set_on_tp_get_user_input(self, pCallbackFunc: collections.abc.Callable) -> None:
        ...
    def set_on_tp_initializing_completed(self, pCallbackFunc: collections.abc.Callable) -> None:
        ...
    def set_on_tp_log(self, pCallbackFunc: collections.abc.Callable) -> None:
        ...
    def set_on_tp_popup(self, pCallbackFunc: collections.abc.Callable) -> None:
        ...
    def set_on_tp_progress(self, pCallbackFunc: collections.abc.Callable) -> None:
        ...
    def set_palletizing_mode(self, iMode: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    def set_ref_coord(self, eTargetCoordSystem: COORDINATE_SYSTEM) -> bool:
        ...
    def set_robot_control(self, control: ROBOT_CONTROL) -> bool:
        """
        Set the robot control
        """
    def set_robot_mode(self, mode: ROBOT_MODE) -> bool:
        """
        Set the robot mode
        """
    def set_robot_speed_mode(self, mode: MONITORING_SPEED) -> bool:
        """
        Set the robot speed mode
        """
    def set_robot_system(self, system: ROBOT_SYSTEM) -> bool:
        """
        Set the robot system
        """
    def set_safe_stop_reset_type(self, type: SAFE_STOP_RESET_TYPE) -> bool:
        """
        Set the safe stop reset type
        """
    def set_safety_mode(self, eSafetyMode: SAFETY_MODE, eSafetyEvent: SAFETY_MODE_EVENT) -> bool:
        ...
    def set_singularity_handling(self, eMode: SINGULARITY_AVOIDANCE) -> bool:
        ...
    def set_stiffnessx(self, fTargetStiffness: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], eForceReference: COORDINATE_SYSTEM = ..., fTargetTime: typing.SupportsFloat | typing.SupportsIndex = 0.0) -> bool:
        ...
    def set_tcp(self, strSymbol: str) -> bool:
        ...
    def set_tool_digital_output(self, eGpioIndex: GPIO_TOOL_DIGITAL_INDEX, bOnOff: bool) -> bool:
        ...
    def set_tool_digital_output_level(self, nLv: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    def set_tool_digital_output_type(self, nPort: typing.SupportsInt | typing.SupportsIndex, eOutputType: OUTPUT_TYPE) -> bool:
        ...
    def set_tool_shape(self, strSymbol: str) -> bool:
        ...
    @typing.overload
    def set_user_cart_coord(self, iReqId: typing.SupportsInt | typing.SupportsIndex, fTargetPos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], eTargetRef: COORDINATE_SYSTEM = ...) -> int:
        ...
    @typing.overload
    def set_user_cart_coord(self, fTargetPos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetOrg: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetRef: COORDINATE_SYSTEM = ...) -> int:
        ...
    def set_user_home(self) -> bool:
        ...
    def setup_monitoring_version(self, iVersion: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    def speedj(self, fTargetVel: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetAcc: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetTime: typing.SupportsFloat | typing.SupportsIndex) -> bool:
        ...
    def speedl(self, fTargetVel: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetAcc: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fTargetTime: typing.SupportsFloat | typing.SupportsIndex) -> bool:
        ...
    def stop(self, eStopType: STOP_TYPE = ...) -> bool:
        ...
    def task_compliance_ctrl(self, fTargetStiffness: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], eForceReference: COORDINATE_SYSTEM = ..., fTargetTime: typing.SupportsFloat | typing.SupportsIndex = 0.0) -> bool:
        ...
    def tp_get_user_input_response(self, strUserInput: str) -> bool:
        ...
    def tp_popup_response(self, eRes: POPUP_RESPONSE) -> bool:
        ...
    def trans(self, fSourcePos: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], fOffset: typing.Annotated[numpy.typing.ArrayLike, numpy.float32], eSourceRef: COORDINATE_SYSTEM = ..., eTargetRef: COORDINATE_SYSTEM = ...) -> ROBOT_POSE:
        ...
class COG_REFERENCE:
    """
    Members:
    
      TCP
    
      Flange
    """
    Flange: typing.ClassVar[COG_REFERENCE]  # value = <COG_REFERENCE.Flange: 1>
    TCP: typing.ClassVar[COG_REFERENCE]  # value = <COG_REFERENCE.TCP: 0>
    __members__: typing.ClassVar[dict[str, COG_REFERENCE]]  # value = {'TCP': <COG_REFERENCE.TCP: 0>, 'Flange': <COG_REFERENCE.Flange: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class CONFIG_ADD_SAFETY_ZONE:
    _szAlias: str
    _szIdentifier: str
    _tShape: SAFETY_ZONE_SHAPE
    _tZoneProperty: SAFETY_ZONE_PROPERTY_DATA
    def __init__(self) -> None:
        ...
    @property
    def _iZoneType(self) -> int:
        ...
    @_iZoneType.setter
    def _iZoneType(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class CONFIG_COCKPIT_EX:
    def __init__(self) -> None:
        ...
    @property
    def _bEnable(self) -> int:
        ...
    @_bEnable.setter
    def _bEnable(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _bRecoveryTeach(self) -> int:
        ...
    @_bRecoveryTeach.setter
    def _bRecoveryTeach(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iButton(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iButton.setter
    def _iButton(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class CONFIG_COLLISION_MUTE_ZONE:
    _tProperty: list
    def __init__(self) -> None:
        ...
    @property
    def _iValidity(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iValidity.setter
    def _iValidity(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class CONFIG_COLLISION_MUTE_ZONE_PROPERTY:
    _szIdentifier: str
    _tZone: SAFETY_OBJECT
    def __init__(self) -> None:
        ...
    @property
    def _fSensitivity(self) -> float:
        ...
    @_fSensitivity.setter
    def _fSensitivity(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _iOnOff(self) -> int:
        ...
    @_iOnOff.setter
    def _iOnOff(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iSafetyIO(self) -> int:
        ...
    @_iSafetyIO.setter
    def _iSafetyIO(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class CONFIG_CONFIGURABLE_IO:
    def __init__(self) -> None:
        ...
    @property
    def _iIO(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iIO.setter
    def _iIO(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class CONFIG_CONFIGURABLE_IO_EX:
    def __init__(self) -> None:
        ...
    @property
    def _iIO(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iIO.setter
    def _iIO(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class CONFIG_DELETE_SAFETY_ZONE:
    _szIdentifier: str
    def __init__(self) -> None:
        ...
class CONFIG_ENCODER_MODE:
    def __init__(self) -> None:
        ...
    @property
    def _iABMode(self) -> int:
        ...
    @_iABMode.setter
    def _iABMode(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iChannel(self) -> int:
        ...
    @_iChannel.setter
    def _iChannel(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iInvMode(self) -> int:
        ...
    @_iInvMode.setter
    def _iInvMode(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iSMode(self) -> int:
        ...
    @_iSMode.setter
    def _iSMode(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iZMode(self) -> int:
        ...
    @_iZMode.setter
    def _iZMode(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nPulseAZ(self) -> int:
        ...
    @_nPulseAZ.setter
    def _nPulseAZ(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class CONFIG_ENCODER_POLARITY:
    def __init__(self) -> None:
        ...
    @property
    def _iChannel(self) -> int:
        ...
    @_iChannel.setter
    def _iChannel(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iPolarity(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iPolarity.setter
    def _iPolarity(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class CONFIG_GENERAL_RANGE:
    _Normal: GENERAL_RANGE
    _Reduced: GENERAL_RANGE
    def __init__(self) -> None:
        ...
class CONFIG_IDLE_OFF:
    def __init__(self) -> None:
        ...
    @property
    def _bFuncEnable(self) -> int:
        ...
    @_bFuncEnable.setter
    def _bFuncEnable(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _fElapseTime(self) -> float:
        ...
    @_fElapseTime.setter
    def _fElapseTime(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class CONFIG_INSTALL_POSE:
    def __init__(self) -> None:
        ...
    @property
    def _fGradient(self) -> float:
        ...
    @_fGradient.setter
    def _fGradient(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fRotation(self) -> float:
        ...
    @_fRotation.setter
    def _fRotation(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class CONFIG_IO_FUNC:
    _bLevel: str
    _iPort: str
    def __init__(self) -> None:
        ...
class CONFIG_JOINT_RANGE:
    _Normal: JOINT_RANGE
    _Reduced: JOINT_RANGE
    def __init__(self) -> None:
        ...
class CONFIG_NUDGE:
    def __init__(self) -> None:
        ...
    @property
    def _bEnable(self) -> int:
        ...
    @_bEnable.setter
    def _bEnable(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _fDelayTime(self) -> float:
        ...
    @_fDelayTime.setter
    def _fDelayTime(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fInputForce(self) -> float:
        ...
    @_fInputForce.setter
    def _fInputForce(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class CONFIG_PAYLOAD_EX:
    def __init__(self) -> None:
        ...
    @property
    def _fStartTime(self) -> float:
        ...
    @_fStartTime.setter
    def _fStartTime(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fTransitionTime(self) -> float:
        ...
    @_fTransitionTime.setter
    def _fTransitionTime(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fWeight(self) -> float:
        ...
    @_fWeight.setter
    def _fWeight(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fXYZ(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fXYZ.setter
    def _fXYZ(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iAddUp(self) -> int:
        ...
    @_iAddUp.setter
    def _iAddUp(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iCogReference(self) -> int:
        ...
    @_iCogReference.setter
    def _iCogReference(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class CONFIG_PROTECTED_ZONE:
    _tZone: list
    def __init__(self) -> None:
        ...
    @property
    def _iValidity(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iValidity.setter
    def _iValidity(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class CONFIG_REMOTE_CONTROL:
    def __init__(self) -> None:
        ...
    @property
    def _bEnable(self) -> int:
        ...
    @_bEnable.setter
    def _bEnable(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _tFunc(self) -> numpy.typing.NDArray[CONFIG_IO_FUNC]:
        ...
    @_tFunc.setter
    def _tFunc(self, arg1: typing.Annotated[numpy.typing.ArrayLike, CONFIG_IO_FUNC]) -> None:
        ...
class CONFIG_SAFETY_FUNCTION:
    def __init__(self) -> None:
        ...
    @property
    def _iStopCode(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iStopCode.setter
    def _iStopCode(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class CONFIG_SAFETY_IO:
    def __init__(self) -> None:
        ...
    @property
    def _iIO(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iIO.setter
    def _iIO(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class CONFIG_SAFETY_IO_EX:
    def __init__(self) -> None:
        ...
    @property
    def _iIO(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iIO.setter
    def _iIO(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class CONFIG_SAFETY_IO_OP:
    def __init__(self) -> None:
        ...
    @property
    def _iIO(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iIO.setter
    def _iIO(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iIO_Op(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iIO_Op.setter
    def _iIO_Op(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iReserved(self) -> int:
        ...
    @_iReserved.setter
    def _iReserved(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iTBI_Op(self) -> int:
        ...
    @_iTBI_Op.setter
    def _iTBI_Op(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class CONFIG_SAFETY_PARAM_ENABLE:
    def __init__(self) -> None:
        ...
    @property
    def _iRefCrc32(self) -> int:
        ...
    @_iRefCrc32.setter
    def _iRefCrc32(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _wPreviousCmdid(self) -> int:
        ...
    @_wPreviousCmdid.setter
    def _wPreviousCmdid(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class CONFIG_SAFE_ZONE:
    _tLine: list
    _tPoint: list
    def __init__(self) -> None:
        ...
    @property
    def _iTargetRef(self) -> int:
        ...
    @_iTargetRef.setter
    def _iTargetRef(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class CONFIG_TCP:
    def __init__(self) -> None:
        ...
    @property
    def _fTargetPos(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTargetPos.setter
    def _fTargetPos(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
class CONFIG_TCP_LIST:
    _tTooList: list
    def __init__(self) -> None:
        ...
    @property
    def _iToolCount(self) -> int:
        ...
    @_iToolCount.setter
    def _iToolCount(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class CONFIG_TCP_LIST_EX:
    _tTooList: list
    def __init__(self) -> None:
        ...
    @property
    def _iToolCount(self) -> int:
        ...
    @_iToolCount.setter
    def _iToolCount(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class CONFIG_TCP_SYMBOL:
    _szSymbol: str
    _tTCP: CONFIG_TCP
    def __init__(self) -> None:
        ...
class CONFIG_TCP_SYMBOL_EX:
    _szSymbol: str
    _tTCP: POSITION_EX
    def __init__(self) -> None:
        ...
class CONFIG_TOOL:
    def __init__(self) -> None:
        ...
    @property
    def _fInertia(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fInertia.setter
    def _fInertia(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fWeight(self) -> float:
        ...
    @_fWeight.setter
    def _fWeight(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fXYZ(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fXYZ.setter
    def _fXYZ(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
class CONFIG_TOOL_LIST:
    _tTooList: list
    def __init__(self) -> None:
        ...
    @property
    def _iToolCount(self) -> int:
        ...
    @_iToolCount.setter
    def _iToolCount(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class CONFIG_TOOL_ORIENTATION_LIMIT_ZONE:
    _tLimit: list
    _tZone: list
    def __init__(self) -> None:
        ...
    @property
    def _iValidity(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iValidity.setter
    def _iValidity(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class CONFIG_TOOL_SHAPE:
    _tShape: list
    def __init__(self) -> None:
        ...
    @property
    def _iValidity(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iValidity.setter
    def _iValidity(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class CONFIG_TOOL_SHAPE_LIST:
    _tTooList: list
    def __init__(self) -> None:
        ...
    @property
    def _iToolCount(self) -> int:
        ...
    @_iToolCount.setter
    def _iToolCount(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class CONFIG_TOOL_SHAPE_SYMBOL:
    _szSymbol: str
    _tToolShape: CONFIG_TOOL_SHAPE
    def __init__(self) -> None:
        ...
class CONFIG_TOOL_SYMBOL:
    _szSymbol: str
    _tTool: CONFIG_TOOL
    def __init__(self) -> None:
        ...
class CONFIG_USER_COORDINATE:
    def __init__(self) -> None:
        ...
    @property
    def _fTargetPos(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTargetPos.setter
    def _fTargetPos(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iReqId(self) -> int:
        ...
    @_iReqId.setter
    def _iReqId(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class CONFIG_USER_COORDINATE_EX:
    def __init__(self) -> None:
        ...
    @property
    def _fTargetPos(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTargetPos.setter
    def _fTargetPos(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iTargetRef(self) -> int:
        ...
    @_iTargetRef.setter
    def _iTargetRef(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iUserID(self) -> int:
        ...
    @_iUserID.setter
    def _iUserID(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class CONFIG_USER_COORDINATE_EX2:
    _tTargetPos: POSITION_EX
    def __init__(self) -> None:
        ...
    @property
    def _iTargetRef(self) -> int:
        ...
    @_iTargetRef.setter
    def _iTargetRef(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iUserID(self) -> int:
        ...
    @_iUserID.setter
    def _iUserID(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class CONFIG_VIRTUAL_FENCE:
    def __init__(self) -> None:
        ...
    @property
    def _iBuffer(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iBuffer.setter
    def _iBuffer(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iFenceType(self) -> int:
        ...
    @_iFenceType.setter
    def _iFenceType(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iTargetRef(self) -> int:
        ...
    @_iTargetRef.setter
    def _iTargetRef(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class CONFIG_WELDING_INTERFACE:
    _tChIn: list
    _tChOut: list
    def __init__(self) -> None:
        ...
    @property
    def _bEnable(self) -> int:
        ...
    @_bEnable.setter
    def _bEnable(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iArcOnDO(self) -> int:
        ...
    @_iArcOnDO.setter
    def _iArcOnDO(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iGasOnDO(self) -> int:
        ...
    @_iGasOnDO.setter
    def _iGasOnDO(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iInchNDO(self) -> int:
        ...
    @_iInchNDO.setter
    def _iInchNDO(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iInchPDO(self) -> int:
        ...
    @_iInchPDO.setter
    def _iInchPDO(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class CONFIG_WORLD_COORDINATE:
    def __init__(self) -> None:
        ...
    @property
    def _fPosition(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fPosition.setter
    def _fPosition(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iType(self) -> int:
        ...
    @_iType.setter
    def _iType(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class CONFIG_WORLD_COORDINATE_EX:
    _tPosition: POSITION_EX
    def __init__(self) -> None:
        ...
    @property
    def _iType(self) -> int:
        ...
    @_iType.setter
    def _iType(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class CONTROL_BRAKE:
    def __init__(self) -> None:
        ...
    @property
    def _bValue(self) -> int:
        ...
    @_bValue.setter
    def _bValue(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iTargetAxs(self) -> int:
        ...
    @_iTargetAxs.setter
    def _iTargetAxs(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class CONTROL_MODE:
    """
    Members:
    
      position
    
      torque
    """
    __members__: typing.ClassVar[dict[str, CONTROL_MODE]]  # value = {'position': <CONTROL_MODE.position: 3>, 'torque': <CONTROL_MODE.torque: 4>}
    position: typing.ClassVar[CONTROL_MODE]  # value = <CONTROL_MODE.position: 3>
    torque: typing.ClassVar[CONTROL_MODE]  # value = <CONTROL_MODE.torque: 4>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class COORDINATE_SYSTEM:
    """
    Members:
    
      Coordinate_system_base
    
      Coordinate_system_tool
    
      Coordinate_system_world
    
      Coordinate_system_user_min
    
      Coordinate_system_user_max
    """
    Coordinate_system_base: typing.ClassVar[COORDINATE_SYSTEM]  # value = <COORDINATE_SYSTEM.Coordinate_system_base: 0>
    Coordinate_system_tool: typing.ClassVar[COORDINATE_SYSTEM]  # value = <COORDINATE_SYSTEM.Coordinate_system_tool: 1>
    Coordinate_system_user_max: typing.ClassVar[COORDINATE_SYSTEM]  # value = <COORDINATE_SYSTEM.Coordinate_system_user_max: 200>
    Coordinate_system_user_min: typing.ClassVar[COORDINATE_SYSTEM]  # value = <COORDINATE_SYSTEM.Coordinate_system_user_min: 101>
    Coordinate_system_world: typing.ClassVar[COORDINATE_SYSTEM]  # value = <COORDINATE_SYSTEM.Coordinate_system_world: 2>
    __members__: typing.ClassVar[dict[str, COORDINATE_SYSTEM]]  # value = {'Coordinate_system_base': <COORDINATE_SYSTEM.Coordinate_system_base: 0>, 'Coordinate_system_tool': <COORDINATE_SYSTEM.Coordinate_system_tool: 1>, 'Coordinate_system_world': <COORDINATE_SYSTEM.Coordinate_system_world: 2>, 'Coordinate_system_user_min': <COORDINATE_SYSTEM.Coordinate_system_user_min: 101>, 'Coordinate_system_user_max': <COORDINATE_SYSTEM.Coordinate_system_user_max: 200>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class COUNTER_BALANCE_PARAM_DATA:
    def __init__(self) -> None:
        ...
    @property
    def _fIrod(self) -> float:
        ...
    @_fIrod.setter
    def _fIrod(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fK(self) -> float:
        ...
    @_fK.setter
    def _fK(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fR(self) -> float:
        ...
    @_fR.setter
    def _fR(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fSi(self) -> float:
        ...
    @_fSi.setter
    def _fSi(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class DATA_TYPE:
    """
    Members:
    
      Bool
    
      Int
    
      Float
    
      String
    
      PosJ
    
      PosX
    
      Unknown
    """
    Bool: typing.ClassVar[DATA_TYPE]  # value = <DATA_TYPE.Bool: 0>
    Float: typing.ClassVar[DATA_TYPE]  # value = <DATA_TYPE.Float: 2>
    Int: typing.ClassVar[DATA_TYPE]  # value = <DATA_TYPE.Int: 1>
    PosJ: typing.ClassVar[DATA_TYPE]  # value = <DATA_TYPE.PosJ: 4>
    PosX: typing.ClassVar[DATA_TYPE]  # value = <DATA_TYPE.PosX: 5>
    String: typing.ClassVar[DATA_TYPE]  # value = <DATA_TYPE.String: 3>
    Unknown: typing.ClassVar[DATA_TYPE]  # value = <DATA_TYPE.Unknown: 6>
    __members__: typing.ClassVar[dict[str, DATA_TYPE]]  # value = {'Bool': <DATA_TYPE.Bool: 0>, 'Int': <DATA_TYPE.Int: 1>, 'Float': <DATA_TYPE.Float: 2>, 'String': <DATA_TYPE.String: 3>, 'PosJ': <DATA_TYPE.PosJ: 4>, 'PosX': <DATA_TYPE.PosX: 5>, 'Unknown': <DATA_TYPE.Unknown: 6>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class DIGITAL_WELDING_COMM_STATE:
    def __init__(self) -> None:
        ...
    @property
    def _cWeldingEipSlaveState(self) -> int:
        ...
    @_cWeldingEipSlaveState.setter
    def _cWeldingEipSlaveState(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _cWeldingMachineOnline(self) -> int:
        ...
    @_cWeldingMachineOnline.setter
    def _cWeldingMachineOnline(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class DRL_PROGRAM_STATE:
    """
    Members:
    
      Play
    
      Stop
    
      Hold
    
      Last
    """
    Hold: typing.ClassVar[DRL_PROGRAM_STATE]  # value = <DRL_PROGRAM_STATE.Hold: 2>
    Last: typing.ClassVar[DRL_PROGRAM_STATE]  # value = <DRL_PROGRAM_STATE.Last: 3>
    Play: typing.ClassVar[DRL_PROGRAM_STATE]  # value = <DRL_PROGRAM_STATE.Play: 0>
    Stop: typing.ClassVar[DRL_PROGRAM_STATE]  # value = <DRL_PROGRAM_STATE.Stop: 1>
    __members__: typing.ClassVar[dict[str, DRL_PROGRAM_STATE]]  # value = {'Play': <DRL_PROGRAM_STATE.Play: 0>, 'Stop': <DRL_PROGRAM_STATE.Stop: 1>, 'Hold': <DRL_PROGRAM_STATE.Hold: 2>, 'Last': <DRL_PROGRAM_STATE.Last: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class DR_MV_APP:
    """
    Members:
    
      None
    
      Weld
    """
    None: typing.ClassVar[DR_MV_APP]  # value = <DR_MV_APP.None: 0>
    Weld: typing.ClassVar[DR_MV_APP]  # value = <DR_MV_APP.Weld: 1>
    __members__: typing.ClassVar[dict[str, DR_MV_APP]]  # value = {'None': <DR_MV_APP.None: 0>, 'Weld': <DR_MV_APP.Weld: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class DR_SERVOJ_TYPE:
    """
    Members:
    
      Override
    
      Queue
    """
    Override: typing.ClassVar[DR_SERVOJ_TYPE]  # value = <DR_SERVOJ_TYPE.Override: 0>
    Queue: typing.ClassVar[DR_SERVOJ_TYPE]  # value = <DR_SERVOJ_TYPE.Queue: 1>
    __members__: typing.ClassVar[dict[str, DR_SERVOJ_TYPE]]  # value = {'Override': <DR_SERVOJ_TYPE.Override: 0>, 'Queue': <DR_SERVOJ_TYPE.Queue: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ENABLE_SAFE_ZONE:
    def __init__(self) -> None:
        ...
    @property
    def _iRegion(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iRegion.setter
    def _iRegion(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class FLANGE_SERIAL_DATA:
    _szValue: str
    def __init__(self) -> None:
        ...
    @property
    def _iCommand(self) -> int:
        ...
    @_iCommand.setter
    def _iCommand(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iLength(self) -> int:
        ...
    @_iLength.setter
    def _iLength(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _szBaudrate(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_szBaudrate.setter
    def _szBaudrate(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _szDataLength(self) -> int:
        ...
    @_szDataLength.setter
    def _szDataLength(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _szParity(self) -> int:
        ...
    @_szParity.setter
    def _szParity(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _szStopBit(self) -> int:
        ...
    @_szStopBit.setter
    def _szStopBit(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class FLANGE_SER_RXD_INFO:
    def __init__(self) -> None:
        ...
    @property
    def _cRxd(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_cRxd.setter
    def _cRxd(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iSize(self) -> int:
        ...
    @_iSize.setter
    def _iSize(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class FLANGE_SER_RXD_INFO_EX:
    def __init__(self) -> None:
        ...
    @property
    def _cRxd(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_cRxd.setter
    def _cRxd(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iSize(self) -> int:
        ...
    @_iSize.setter
    def _iSize(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _portNum(self) -> int:
        ...
    @_portNum.setter
    def _portNum(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class FLANGE_VERSION:
    def __init__(self) -> None:
        ...
    @property
    def BoardNo(self) -> int:
        ...
    @BoardNo.setter
    def BoardNo(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def PacketType(self) -> int:
        ...
    @PacketType.setter
    def PacketType(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def iFlangeHwVer(self) -> int:
        ...
    @iFlangeHwVer.setter
    def iFlangeHwVer(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def res(self) -> int:
        ...
    @res.setter
    def res(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class FORCE_AXIS:
    """
    Members:
    
      Axis_X
    
      Axis_Y
    
      Axis_Z
    
      Axis_A
    
      Axis_B
    
      Axis_C
    """
    Axis_A: typing.ClassVar[FORCE_AXIS]  # value = <FORCE_AXIS.Axis_A: 10>
    Axis_B: typing.ClassVar[FORCE_AXIS]  # value = <FORCE_AXIS.Axis_B: 11>
    Axis_C: typing.ClassVar[FORCE_AXIS]  # value = <FORCE_AXIS.Axis_C: 12>
    Axis_X: typing.ClassVar[FORCE_AXIS]  # value = <FORCE_AXIS.Axis_X: 0>
    Axis_Y: typing.ClassVar[FORCE_AXIS]  # value = <FORCE_AXIS.Axis_Y: 1>
    Axis_Z: typing.ClassVar[FORCE_AXIS]  # value = <FORCE_AXIS.Axis_Z: 2>
    __members__: typing.ClassVar[dict[str, FORCE_AXIS]]  # value = {'Axis_X': <FORCE_AXIS.Axis_X: 0>, 'Axis_Y': <FORCE_AXIS.Axis_Y: 1>, 'Axis_Z': <FORCE_AXIS.Axis_Z: 2>, 'Axis_A': <FORCE_AXIS.Axis_A: 10>, 'Axis_B': <FORCE_AXIS.Axis_B: 11>, 'Axis_C': <FORCE_AXIS.Axis_C: 12>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class FORCE_MODE:
    """
    Members:
    
      Absolute
    
      Relative
    """
    Absolute: typing.ClassVar[FORCE_MODE]  # value = <FORCE_MODE.Absolute: 0>
    Relative: typing.ClassVar[FORCE_MODE]  # value = <FORCE_MODE.Relative: 1>
    __members__: typing.ClassVar[dict[str, FORCE_MODE]]  # value = {'Absolute': <FORCE_MODE.Absolute: 0>, 'Relative': <FORCE_MODE.Relative: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class FTS_PARAM_DATA:
    def __init__(self) -> None:
        ...
    @property
    def _fOffset(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fOffset.setter
    def _fOffset(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
class GENERAL_RANGE:
    def __init__(self) -> None:
        ...
    @property
    def _fMaxForce(self) -> float:
        ...
    @_fMaxForce.setter
    def _fMaxForce(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fMaxMomentum(self) -> float:
        ...
    @_fMaxMomentum.setter
    def _fMaxMomentum(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fMaxPower(self) -> float:
        ...
    @_fMaxPower.setter
    def _fMaxPower(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fMaxSpeed(self) -> float:
        ...
    @_fMaxSpeed.setter
    def _fMaxSpeed(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class GPIO_ANALOG_TYPE:
    """
    Members:
    
      Current
    
      Voltage
    """
    Current: typing.ClassVar[GPIO_ANALOG_TYPE]  # value = <GPIO_ANALOG_TYPE.Current: 0>
    Voltage: typing.ClassVar[GPIO_ANALOG_TYPE]  # value = <GPIO_ANALOG_TYPE.Voltage: 1>
    __members__: typing.ClassVar[dict[str, GPIO_ANALOG_TYPE]]  # value = {'Current': <GPIO_ANALOG_TYPE.Current: 0>, 'Voltage': <GPIO_ANALOG_TYPE.Voltage: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class GPIO_CTRLBOX_ANALOG_INDEX:
    """
    Members:
    
      Index_1
    
      Index_2
    """
    Index_1: typing.ClassVar[GPIO_CTRLBOX_ANALOG_INDEX]  # value = <GPIO_CTRLBOX_ANALOG_INDEX.Index_1: 0>
    Index_2: typing.ClassVar[GPIO_CTRLBOX_ANALOG_INDEX]  # value = <GPIO_CTRLBOX_ANALOG_INDEX.Index_2: 1>
    __members__: typing.ClassVar[dict[str, GPIO_CTRLBOX_ANALOG_INDEX]]  # value = {'Index_1': <GPIO_CTRLBOX_ANALOG_INDEX.Index_1: 0>, 'Index_2': <GPIO_CTRLBOX_ANALOG_INDEX.Index_2: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class GPIO_CTRLBOX_DIGITAL_INDEX:
    """
    Members:
    
      Index_1
    
      Index_2
    
      Index_3
    
      Index_4
    
      Index_5
    
      Index_6
    
      Index_7
    
      Index_8
    
      Index_9
    
      Index_10
    
      Index_11
    
      Index_12
    
      Index_13
    
      Index_14
    
      Index_15
    
      Index_16
    
      Index_17
    
      Index_18
    
      Index_19
    
      Index_20
    
      Index_21
    
      Index_22
    
      Index_23
    
      Index_24
    
      Index_25
    
      Index_26
    
      Index_27
    
      Index_28
    
      Index_29
    
      Index_30
    
      Index_31
    
      Index_32
    """
    Index_1: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_1: 0>
    Index_10: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_10: 9>
    Index_11: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_11: 10>
    Index_12: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_12: 11>
    Index_13: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_13: 12>
    Index_14: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_14: 13>
    Index_15: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_15: 14>
    Index_16: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_16: 15>
    Index_17: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_17: 16>
    Index_18: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_18: 17>
    Index_19: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_19: 18>
    Index_2: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_2: 1>
    Index_20: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_20: 19>
    Index_21: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_21: 20>
    Index_22: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_22: 21>
    Index_23: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_23: 22>
    Index_24: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_24: 23>
    Index_25: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_25: 24>
    Index_26: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_26: 25>
    Index_27: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_27: 26>
    Index_28: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_28: 27>
    Index_29: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_29: 28>
    Index_3: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_3: 2>
    Index_30: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_30: 29>
    Index_31: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_31: 30>
    Index_32: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_32: 31>
    Index_4: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_4: 3>
    Index_5: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_5: 4>
    Index_6: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_6: 5>
    Index_7: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_7: 6>
    Index_8: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_8: 7>
    Index_9: typing.ClassVar[GPIO_CTRLBOX_DIGITAL_INDEX]  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_9: 8>
    __members__: typing.ClassVar[dict[str, GPIO_CTRLBOX_DIGITAL_INDEX]]  # value = {'Index_1': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_1: 0>, 'Index_2': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_2: 1>, 'Index_3': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_3: 2>, 'Index_4': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_4: 3>, 'Index_5': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_5: 4>, 'Index_6': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_6: 5>, 'Index_7': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_7: 6>, 'Index_8': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_8: 7>, 'Index_9': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_9: 8>, 'Index_10': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_10: 9>, 'Index_11': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_11: 10>, 'Index_12': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_12: 11>, 'Index_13': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_13: 12>, 'Index_14': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_14: 13>, 'Index_15': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_15: 14>, 'Index_16': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_16: 15>, 'Index_17': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_17: 16>, 'Index_18': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_18: 17>, 'Index_19': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_19: 18>, 'Index_20': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_20: 19>, 'Index_21': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_21: 20>, 'Index_22': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_22: 21>, 'Index_23': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_23: 22>, 'Index_24': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_24: 23>, 'Index_25': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_25: 24>, 'Index_26': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_26: 25>, 'Index_27': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_27: 26>, 'Index_28': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_28: 27>, 'Index_29': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_29: 28>, 'Index_30': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_30: 29>, 'Index_31': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_31: 30>, 'Index_32': <GPIO_CTRLBOX_DIGITAL_INDEX.Index_32: 31>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class GPIO_PORT:
    def __init__(self) -> None:
        ...
    @property
    def _fValue(self) -> float:
        ...
    @_fValue.setter
    def _fValue(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _iIndex(self) -> int:
        ...
    @_iIndex.setter
    def _iIndex(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class GPIO_TOOL_DIGITAL_INDEX:
    """
    Members:
    
      Index_1
    
      Index_2
    
      Index_3
    
      Index_4
    
      Index_5
    
      Index_6
    """
    Index_1: typing.ClassVar[GPIO_TOOL_DIGITAL_INDEX]  # value = <GPIO_TOOL_DIGITAL_INDEX.Index_1: 0>
    Index_2: typing.ClassVar[GPIO_TOOL_DIGITAL_INDEX]  # value = <GPIO_TOOL_DIGITAL_INDEX.Index_2: 1>
    Index_3: typing.ClassVar[GPIO_TOOL_DIGITAL_INDEX]  # value = <GPIO_TOOL_DIGITAL_INDEX.Index_3: 2>
    Index_4: typing.ClassVar[GPIO_TOOL_DIGITAL_INDEX]  # value = <GPIO_TOOL_DIGITAL_INDEX.Index_4: 3>
    Index_5: typing.ClassVar[GPIO_TOOL_DIGITAL_INDEX]  # value = <GPIO_TOOL_DIGITAL_INDEX.Index_5: 4>
    Index_6: typing.ClassVar[GPIO_TOOL_DIGITAL_INDEX]  # value = <GPIO_TOOL_DIGITAL_INDEX.Index_6: 5>
    __members__: typing.ClassVar[dict[str, GPIO_TOOL_DIGITAL_INDEX]]  # value = {'Index_1': <GPIO_TOOL_DIGITAL_INDEX.Index_1: 0>, 'Index_2': <GPIO_TOOL_DIGITAL_INDEX.Index_2: 1>, 'Index_3': <GPIO_TOOL_DIGITAL_INDEX.Index_3: 2>, 'Index_4': <GPIO_TOOL_DIGITAL_INDEX.Index_4: 3>, 'Index_5': <GPIO_TOOL_DIGITAL_INDEX.Index_5: 4>, 'Index_6': <GPIO_TOOL_DIGITAL_INDEX.Index_6: 5>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class IETHERNET_SLAVE_DATA_EX:
    def __init__(self) -> None:
        ...
    @property
    def _iGprAddr(self) -> int:
        ...
    @_iGprAddr.setter
    def _iGprAddr(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iGprType(self) -> int:
        ...
    @_iGprType.setter
    def _iGprType(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iInOut(self) -> int:
        ...
    @_iInOut.setter
    def _iInOut(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class IETHERNET_SLAVE_RESPONSE_DATA_EX:
    _szData: str
    def __init__(self) -> None:
        ...
    @property
    def _iGprAddr(self) -> int:
        ...
    @_iGprAddr.setter
    def _iGprAddr(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iGprType(self) -> int:
        ...
    @_iGprType.setter
    def _iGprType(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iInOut(self) -> int:
        ...
    @_iInOut.setter
    def _iInOut(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class INSTALL_SUB_SYSTEM:
    def __init__(self) -> None:
        ...
    @property
    def _bCockpit(self) -> int:
        ...
    @_bCockpit.setter
    def _bCockpit(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _bFTS(self) -> int:
        ...
    @_bFTS.setter
    def _bFTS(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _bProcessButton(self) -> int:
        ...
    @_bProcessButton.setter
    def _bProcessButton(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class INVERSE_KINEMATIC_RESPONSE:
    def __init__(self) -> None:
        ...
    @property
    def _fTargetPos(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTargetPos.setter
    def _fTargetPos(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iStatus(self) -> int:
        ...
    @_iStatus.setter
    def _iStatus(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class JOG_AXIS:
    """
    Members:
    
      Joint_1
    
      Joint_2
    
      Joint_3
    
      Joint_4
    
      Joint_5
    
      Joint_6
    
      Task_X
    
      Task_Y
    
      Task_Z
    
      Task_RX
    
      Task_RY
    
      Task_RZ
    """
    Joint_1: typing.ClassVar[JOG_AXIS]  # value = <JOG_AXIS.Joint_1: 0>
    Joint_2: typing.ClassVar[JOG_AXIS]  # value = <JOG_AXIS.Joint_2: 1>
    Joint_3: typing.ClassVar[JOG_AXIS]  # value = <JOG_AXIS.Joint_3: 2>
    Joint_4: typing.ClassVar[JOG_AXIS]  # value = <JOG_AXIS.Joint_4: 3>
    Joint_5: typing.ClassVar[JOG_AXIS]  # value = <JOG_AXIS.Joint_5: 4>
    Joint_6: typing.ClassVar[JOG_AXIS]  # value = <JOG_AXIS.Joint_6: 5>
    Task_RX: typing.ClassVar[JOG_AXIS]  # value = <JOG_AXIS.Task_RX: 9>
    Task_RY: typing.ClassVar[JOG_AXIS]  # value = <JOG_AXIS.Task_RY: 10>
    Task_RZ: typing.ClassVar[JOG_AXIS]  # value = <JOG_AXIS.Task_RZ: 11>
    Task_X: typing.ClassVar[JOG_AXIS]  # value = <JOG_AXIS.Task_X: 6>
    Task_Y: typing.ClassVar[JOG_AXIS]  # value = <JOG_AXIS.Task_Y: 7>
    Task_Z: typing.ClassVar[JOG_AXIS]  # value = <JOG_AXIS.Task_Z: 8>
    __members__: typing.ClassVar[dict[str, JOG_AXIS]]  # value = {'Joint_1': <JOG_AXIS.Joint_1: 0>, 'Joint_2': <JOG_AXIS.Joint_2: 1>, 'Joint_3': <JOG_AXIS.Joint_3: 2>, 'Joint_4': <JOG_AXIS.Joint_4: 3>, 'Joint_5': <JOG_AXIS.Joint_5: 4>, 'Joint_6': <JOG_AXIS.Joint_6: 5>, 'Task_X': <JOG_AXIS.Task_X: 6>, 'Task_Y': <JOG_AXIS.Task_Y: 7>, 'Task_Z': <JOG_AXIS.Task_Z: 8>, 'Task_RX': <JOG_AXIS.Task_RX: 9>, 'Task_RY': <JOG_AXIS.Task_RY: 10>, 'Task_RZ': <JOG_AXIS.Task_RZ: 11>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class JOINT_AXIS:
    """
    Members:
    
      Axis_1
    
      Axis_2
    
      Axis_3
    
      Axis_4
    
      Axis_5
    
      Axis_6
    """
    Axis_1: typing.ClassVar[JOINT_AXIS]  # value = <JOINT_AXIS.Axis_1: 0>
    Axis_2: typing.ClassVar[JOINT_AXIS]  # value = <JOINT_AXIS.Axis_2: 1>
    Axis_3: typing.ClassVar[JOINT_AXIS]  # value = <JOINT_AXIS.Axis_3: 2>
    Axis_4: typing.ClassVar[JOINT_AXIS]  # value = <JOINT_AXIS.Axis_4: 3>
    Axis_5: typing.ClassVar[JOINT_AXIS]  # value = <JOINT_AXIS.Axis_5: 4>
    Axis_6: typing.ClassVar[JOINT_AXIS]  # value = <JOINT_AXIS.Axis_6: 5>
    __members__: typing.ClassVar[dict[str, JOINT_AXIS]]  # value = {'Axis_1': <JOINT_AXIS.Axis_1: 0>, 'Axis_2': <JOINT_AXIS.Axis_2: 1>, 'Axis_3': <JOINT_AXIS.Axis_3: 2>, 'Axis_4': <JOINT_AXIS.Axis_4: 3>, 'Axis_5': <JOINT_AXIS.Axis_5: 4>, 'Axis_6': <JOINT_AXIS.Axis_6: 5>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class JOINT_RANGE:
    def __init__(self) -> None:
        ...
    @property
    def _fMaxRange(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fMaxRange.setter
    def _fMaxRange(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fMaxVelocity(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fMaxVelocity.setter
    def _fMaxVelocity(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fMinRange(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fMinRange.setter
    def _fMinRange(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
class JTS_PARAM_DATA:
    def __init__(self) -> None:
        ...
    @property
    def _fOffset(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fOffset.setter
    def _fOffset(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fScale(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fScale.setter
    def _fScale(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
class KT_5G_CONFIG_PARAM:
    _szDeviceId: str
    _szDevicePw: str
    _szGatewayId: str
    _szIpAddress: str
    def __init__(self) -> None:
        ...
    @property
    def _bEnable(self) -> int:
        ...
    @_bEnable.setter
    def _bEnable(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _fPeriod(self) -> float:
        ...
    @_fPeriod.setter
    def _fPeriod(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _nPort(self) -> int:
        ...
    @_nPort.setter
    def _nPort(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class LICENSE_TEXT_PARAM:
    def __init__(self) -> None:
        ...
    @property
    def _bLicenseInController(self) -> int:
        ...
    @_bLicenseInController.setter
    def _bLicenseInController(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _szLicenseKey(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_szLicenseKey.setter
    def _szLicenseKey(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class LINE:
    _tFromPoint: POINT_2D
    _tToPoint: POINT_2D
    def __init__(self) -> None:
        ...
class LOCAL_ZONE_PROPERTY_COLLISION_STOPMODE:
    def __init__(self) -> None:
        ...
    @property
    def _iOverride(self) -> int:
        ...
    @_iOverride.setter
    def _iOverride(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iStopMode(self) -> int:
        ...
    @_iStopMode.setter
    def _iStopMode(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class LOCAL_ZONE_PROPERTY_JOINT_RANGE:
    def __init__(self) -> None:
        ...
    @property
    def _fMaxRange(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fMaxRange.setter
    def _fMaxRange(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fMinRange(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fMinRange.setter
    def _fMinRange(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iOverride(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iOverride.setter
    def _iOverride(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class LOCAL_ZONE_PROPERTY_JOINT_SPEED:
    def __init__(self) -> None:
        ...
    @property
    def _fSpeed(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fSpeed.setter
    def _fSpeed(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iOverride(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iOverride.setter
    def _iOverride(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class LOCAL_ZONE_PROPERTY_TCPSLF_STOPMODE:
    def __init__(self) -> None:
        ...
    @property
    def _iOverride(self) -> int:
        ...
    @_iOverride.setter
    def _iOverride(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iStopMode(self) -> int:
        ...
    @_iStopMode.setter
    def _iStopMode(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class LOCAL_ZONE_PROPERTY_TOOL_ORIENTATION:
    def __init__(self) -> None:
        ...
    @property
    def _fAngle(self) -> float:
        ...
    @_fAngle.setter
    def _fAngle(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fDirection(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fDirection.setter
    def _fDirection(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iOverride(self) -> int:
        ...
    @_iOverride.setter
    def _iOverride(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class LOG_ALARM:
    _szParam: list
    def __init__(self) -> None:
        ...
    @property
    def _iGroup(self) -> int:
        ...
    @_iGroup.setter
    def _iGroup(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iIndex(self) -> int:
        ...
    @_iIndex.setter
    def _iIndex(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iLevel(self) -> int:
        ...
    @_iLevel.setter
    def _iLevel(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class LOG_GROUP:
    """
    Members:
    
      SystemFMK
    
      MotionLIB
    
      SmartTP
    
      Inverter
    
      SafetyController
    
      Last
    """
    Inverter: typing.ClassVar[LOG_GROUP]  # value = <LOG_GROUP.Inverter: 4>
    Last: typing.ClassVar[LOG_GROUP]  # value = <LOG_GROUP.Last: 6>
    MotionLIB: typing.ClassVar[LOG_GROUP]  # value = <LOG_GROUP.MotionLIB: 2>
    SafetyController: typing.ClassVar[LOG_GROUP]  # value = <LOG_GROUP.SafetyController: 5>
    SmartTP: typing.ClassVar[LOG_GROUP]  # value = <LOG_GROUP.SmartTP: 3>
    SystemFMK: typing.ClassVar[LOG_GROUP]  # value = <LOG_GROUP.SystemFMK: 1>
    __members__: typing.ClassVar[dict[str, LOG_GROUP]]  # value = {'SystemFMK': <LOG_GROUP.SystemFMK: 1>, 'MotionLIB': <LOG_GROUP.MotionLIB: 2>, 'SmartTP': <LOG_GROUP.SmartTP: 3>, 'Inverter': <LOG_GROUP.Inverter: 4>, 'SafetyController': <LOG_GROUP.SafetyController: 5>, 'Last': <LOG_GROUP.Last: 6>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class LOG_LEVEL:
    """
    Members:
    
      Sys_info
    
      Sys_warn
    
      Sys error
    
      Sys_last
    """
    Sys_info: typing.ClassVar[LOG_LEVEL]  # value = <LOG_LEVEL.Sys_info: 1>
    Sys_last: typing.ClassVar[LOG_LEVEL]  # value = <LOG_LEVEL.Sys_last: 4>
    Sys_warn: typing.ClassVar[LOG_LEVEL]  # value = <LOG_LEVEL.Sys_warn: 2>
    __members__: typing.ClassVar[dict[str, LOG_LEVEL]]  # value = {'Sys_info': <LOG_LEVEL.Sys_info: 1>, 'Sys_warn': <LOG_LEVEL.Sys_warn: 2>, 'Sys error': <LOG_LEVEL.Sys error: 3>, 'Sys_last': <LOG_LEVEL.Sys_last: 4>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class MANAGE_ACCESS_CONTROL:
    """
    Members:
    
      Force_request
    
      Request
    
      Response_yes
    
      Response_no
    """
    Force_request: typing.ClassVar[MANAGE_ACCESS_CONTROL]  # value = <MANAGE_ACCESS_CONTROL.Force_request: 0>
    Request: typing.ClassVar[MANAGE_ACCESS_CONTROL]  # value = <MANAGE_ACCESS_CONTROL.Request: 1>
    Response_no: typing.ClassVar[MANAGE_ACCESS_CONTROL]  # value = <MANAGE_ACCESS_CONTROL.Response_no: 3>
    Response_yes: typing.ClassVar[MANAGE_ACCESS_CONTROL]  # value = <MANAGE_ACCESS_CONTROL.Response_yes: 2>
    __members__: typing.ClassVar[dict[str, MANAGE_ACCESS_CONTROL]]  # value = {'Force_request': <MANAGE_ACCESS_CONTROL.Force_request: 0>, 'Request': <MANAGE_ACCESS_CONTROL.Request: 1>, 'Response_yes': <MANAGE_ACCESS_CONTROL.Response_yes: 2>, 'Response_no': <MANAGE_ACCESS_CONTROL.Response_no: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class MEASURE_FRICTION_RESPONSE:
    def __init__(self) -> None:
        ...
    @property
    def _fError(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fError.setter
    def _fError(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fNegative(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fNegative.setter
    def _fNegative(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fPositive(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fPositive.setter
    def _fPositive(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fTemperature(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTemperature.setter
    def _fTemperature(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iResult(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iResult.setter
    def _iResult(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class MEASURE_TCP_RESPONSE:
    _tTCP: CONFIG_TCP
    def __init__(self) -> None:
        ...
    @property
    def _fError(self) -> float:
        ...
    @_fError.setter
    def _fError(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class MEASURE_TOOL_RESPONSE:
    def __init__(self) -> None:
        ...
    @property
    def _fWeight(self) -> float:
        ...
    @_fWeight.setter
    def _fWeight(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fXYZ(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fXYZ.setter
    def _fXYZ(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
class MESSAGE_INPUT:
    _szText: str
    def __init__(self) -> None:
        ...
    @property
    def _iType(self) -> int:
        ...
    @_iType.setter
    def _iType(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class MESSAGE_LEVEL:
    """
    Members:
    
      Info
    
      Warn
    
      Alarm
    """
    Alarm: typing.ClassVar[MESSAGE_LEVEL]  # value = <MESSAGE_LEVEL.Alarm: 2>
    Info: typing.ClassVar[MESSAGE_LEVEL]  # value = <MESSAGE_LEVEL.Info: 0>
    Warn: typing.ClassVar[MESSAGE_LEVEL]  # value = <MESSAGE_LEVEL.Warn: 1>
    __members__: typing.ClassVar[dict[str, MESSAGE_LEVEL]]  # value = {'Info': <MESSAGE_LEVEL.Info: 0>, 'Warn': <MESSAGE_LEVEL.Warn: 1>, 'Alarm': <MESSAGE_LEVEL.Alarm: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class MESSAGE_POPUP:
    _szText: str
    def __init__(self) -> None:
        ...
    @property
    def _iBtnType(self) -> int:
        ...
    @_iBtnType.setter
    def _iBtnType(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iLevel(self) -> int:
        ...
    @_iLevel.setter
    def _iLevel(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class MESSAGE_PROGRESS:
    def __init__(self) -> None:
        ...
    @property
    def _iCurrentCount(self) -> int:
        ...
    @_iCurrentCount.setter
    def _iCurrentCount(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iTotalCount(self) -> int:
        ...
    @_iTotalCount.setter
    def _iTotalCount(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class MODBUS_DATA:
    _rtu: WRITE_MODBUS_RTU_DATA
    _tcp: WRITE_MODBUS_DATA
    def __init__(self) -> None:
        ...
    @property
    def _iType(self) -> int:
        ...
    @_iType.setter
    def _iType(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class MODBUS_DATA_LIST:
    _tRegister: list
    def __init__(self) -> None:
        ...
    @property
    def _nCount(self) -> int:
        ...
    @_nCount.setter
    def _nCount(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class MODBUS_MULTI_REGISTER:
    _szSymbol: str
    def __init__(self) -> None:
        ...
    @property
    def _iRegCount(self) -> int:
        ...
    @_iRegCount.setter
    def _iRegCount(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iRegIndex(self) -> int:
        ...
    @_iRegIndex.setter
    def _iRegIndex(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iRegValue(self) -> numpy.typing.NDArray[numpy.uint16]:
        ...
    @_iRegValue.setter
    def _iRegValue(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint16]) -> None:
        ...
    @property
    def _iSlaveID(self) -> int:
        ...
    @_iSlaveID.setter
    def _iSlaveID(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class MODBUS_REGISTER:
    _szSymbol: str
    def __init__(self) -> None:
        ...
    @property
    def _iValue(self) -> int:
        ...
    @_iValue.setter
    def _iValue(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class MODBUS_REGISTER_MONITORING:
    _szSymbol: str
    def __init__(self) -> None:
        ...
    @property
    def _iRegValue(self) -> int:
        ...
    @_iRegValue.setter
    def _iRegValue(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class MODBUS_REGISTER_TYPE:
    """
    Members:
    
      Discrete_inputs
    
      Coils
    
      Input_register
    
      Holding_register
    """
    Coils: typing.ClassVar[MODBUS_REGISTER_TYPE]  # value = <MODBUS_REGISTER_TYPE.Coils: 1>
    Discrete_inputs: typing.ClassVar[MODBUS_REGISTER_TYPE]  # value = <MODBUS_REGISTER_TYPE.Discrete_inputs: 0>
    Holding_register: typing.ClassVar[MODBUS_REGISTER_TYPE]  # value = <MODBUS_REGISTER_TYPE.Holding_register: 3>
    Input_register: typing.ClassVar[MODBUS_REGISTER_TYPE]  # value = <MODBUS_REGISTER_TYPE.Input_register: 2>
    __members__: typing.ClassVar[dict[str, MODBUS_REGISTER_TYPE]]  # value = {'Discrete_inputs': <MODBUS_REGISTER_TYPE.Discrete_inputs: 0>, 'Coils': <MODBUS_REGISTER_TYPE.Coils: 1>, 'Input_register': <MODBUS_REGISTER_TYPE.Input_register: 2>, 'Holding_register': <MODBUS_REGISTER_TYPE.Holding_register: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class MONITORING_ACCESS_CONTROL:
    """
    Members:
    
      Request
    
      Deny
    
      Grant
    
      Loss
    
      Last
    """
    Deny: typing.ClassVar[MONITORING_ACCESS_CONTROL]  # value = <MONITORING_ACCESS_CONTROL.Deny: 1>
    Grant: typing.ClassVar[MONITORING_ACCESS_CONTROL]  # value = <MONITORING_ACCESS_CONTROL.Grant: 2>
    Last: typing.ClassVar[MONITORING_ACCESS_CONTROL]  # value = <MONITORING_ACCESS_CONTROL.Last: 4>
    Loss: typing.ClassVar[MONITORING_ACCESS_CONTROL]  # value = <MONITORING_ACCESS_CONTROL.Loss: 3>
    Request: typing.ClassVar[MONITORING_ACCESS_CONTROL]  # value = <MONITORING_ACCESS_CONTROL.Request: 0>
    __members__: typing.ClassVar[dict[str, MONITORING_ACCESS_CONTROL]]  # value = {'Request': <MONITORING_ACCESS_CONTROL.Request: 0>, 'Deny': <MONITORING_ACCESS_CONTROL.Deny: 1>, 'Grant': <MONITORING_ACCESS_CONTROL.Grant: 2>, 'Loss': <MONITORING_ACCESS_CONTROL.Loss: 3>, 'Last': <MONITORING_ACCESS_CONTROL.Last: 4>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class MONITORING_COCKPIT:
    def __init__(self) -> None:
        ...
    @property
    def _iActualBS(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iActualBS.setter
    def _iActualBS(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class MONITORING_CONTROL:
    _tJoint: ROBOT_MONITORING_JOINT
    _tState: ROBOT_MONITORING_STATE
    _tTask: ROBOT_MONITORING_TASK
    _tTorque: ROBOT_MONITORING_TORQUE
    def __init__(self) -> None:
        ...
class MONITORING_CTRLIO:
    _tInput: READ_CTRLIO_INPUT
    _tOutput: READ_CTRLIO_OUTPUT
    def __init__(self) -> None:
        ...
class MONITORING_CTRLIO_EX:
    _tEncoder: READ_ENCODER_INPUT
    _tInput: READ_CTRLIO_INPUT_EX
    _tOutput: READ_CTRLIO_OUTPUT_EX
    def __init__(self) -> None:
        ...
class MONITORING_CTRLIO_EX2:
    _tEncoder: READ_ENCODER_INPUT
    _tInput: READ_CTRLIO_INPUT_EX2
    _tOutput: READ_CTRLIO_OUTPUT_EX2
    def __init__(self) -> None:
        ...
class MONITORING_DATA:
    _tCtrl: MONITORING_CONTROL
    _tMisc: MONITORING_MISC
    def __init__(self) -> None:
        ...
class MONITORING_DATA_EX:
    _tAModel: ROBOT_MONITORING_AMODEL
    _tConfig: MONITORING_FLANGE_IO_CONFIG
    _tCtrl: ROBOT_MONITORING_DATA_EX
    _tCtrlEx: MONITORING_FORCECONTROL
    _tMisc: MONITORING_MISC
    def __init__(self) -> None:
        ...
class MONITORING_FLANGE_IO_CONFIG:
    def __init__(self) -> None:
        ...
    @property
    def _iActualAI(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_iActualAI.setter
    def _iActualAI(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iFAI0Mode(self) -> int:
        ...
    @_iFAI0Mode.setter
    def _iFAI0Mode(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iFAI1Mode(self) -> int:
        ...
    @_iFAI1Mode.setter
    def _iFAI1Mode(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iFAI2Mode(self) -> int:
        ...
    @_iFAI2Mode.setter
    def _iFAI2Mode(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iFAI3Mode(self) -> int:
        ...
    @_iFAI3Mode.setter
    def _iFAI3Mode(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iInterruptSafetyMode(self) -> int:
        ...
    @_iInterruptSafetyMode.setter
    def _iInterruptSafetyMode(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iServoSafetyMode(self) -> int:
        ...
    @_iServoSafetyMode.setter
    def _iServoSafetyMode(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iVoutLevel(self) -> int:
        ...
    @_iVoutLevel.setter
    def _iVoutLevel(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iX1DOBjtType(self) -> int:
        ...
    @_iX1DOBjtType.setter
    def _iX1DOBjtType(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iX1Rs485FAIPinMux(self) -> int:
        ...
    @_iX1Rs485FAIPinMux.setter
    def _iX1Rs485FAIPinMux(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iX2DOBjtType(self) -> int:
        ...
    @_iX2DOBjtType.setter
    def _iX2DOBjtType(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iX2Rs485FAIPinMux(self) -> int:
        ...
    @_iX2Rs485FAIPinMux.setter
    def _iX2Rs485FAIPinMux(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _szX1Baudrate(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_szX1Baudrate.setter
    def _szX1Baudrate(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _szX1DataLength(self) -> int:
        ...
    @_szX1DataLength.setter
    def _szX1DataLength(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _szX1Parity(self) -> int:
        ...
    @_szX1Parity.setter
    def _szX1Parity(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _szX1StopBit(self) -> int:
        ...
    @_szX1StopBit.setter
    def _szX1StopBit(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _szX2Baudrate(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_szX2Baudrate.setter
    def _szX2Baudrate(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _szX2DataLength(self) -> int:
        ...
    @_szX2DataLength.setter
    def _szX2DataLength(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _szX2Parity(self) -> int:
        ...
    @_szX2Parity.setter
    def _szX2Parity(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _szX2StopBit(self) -> int:
        ...
    @_szX2StopBit.setter
    def _szX2StopBit(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class MONITORING_FORCECONTROL:
    def __init__(self) -> None:
        ...
    @property
    def _fActualCS(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualCS.setter
    def _fActualCS(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fActualHDT(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualHDT.setter
    def _fActualHDT(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fSingularity(self) -> float:
        ...
    @_fSingularity.setter
    def _fSingularity(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fToolActualETT(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fToolActualETT.setter
    def _fToolActualETT(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iActualBS(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iActualBS.setter
    def _iActualBS(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iAutoAccMode(self) -> int:
        ...
    @_iAutoAccMode.setter
    def _iAutoAccMode(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iForceControlMode(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iForceControlMode.setter
    def _iForceControlMode(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iReferenceCoord(self) -> int:
        ...
    @_iReferenceCoord.setter
    def _iReferenceCoord(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iSingularHandlingMode(self) -> int:
        ...
    @_iSingularHandlingMode.setter
    def _iSingularHandlingMode(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _isMoving(self) -> int:
        ...
    @_isMoving.setter
    def _isMoving(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class MONITORING_IE_GPR:
    def __init__(self) -> None:
        ...
    @property
    def _nGpr(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_nGpr.setter
    def _nGpr(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class MONITORING_IE_SLAVE:
    _tIndustrialEthernetGPR: MONITORING_IE_GPR
    _tMbusCoil: MONITORING_MBUS_SLAVE_COIL
    _tMbusHoldingRegister: MONITORING_MBUS_SLAVE_HOILDING_REGISTER
    def __init__(self) -> None:
        ...
class MONITORING_MBUS_SLAVE_COIL:
    def __init__(self) -> None:
        ...
    @property
    def _nCtrlDigitalInput(self) -> int:
        ...
    @_nCtrlDigitalInput.setter
    def _nCtrlDigitalInput(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nCtrlDigitalOutput(self) -> int:
        ...
    @_nCtrlDigitalOutput.setter
    def _nCtrlDigitalOutput(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nDirectTeachButtonPress(self) -> int:
        ...
    @_nDirectTeachButtonPress.setter
    def _nDirectTeachButtonPress(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nEmergencyStopped(self) -> int:
        ...
    @_nEmergencyStopped.setter
    def _nEmergencyStopped(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nPowerButtonPress(self) -> int:
        ...
    @_nPowerButtonPress.setter
    def _nPowerButtonPress(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nSafetyStopped(self) -> int:
        ...
    @_nSafetyStopped.setter
    def _nSafetyStopped(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nSafetyStoppedRequiredRecoveryMode(self) -> int:
        ...
    @_nSafetyStoppedRequiredRecoveryMode.setter
    def _nSafetyStoppedRequiredRecoveryMode(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nServoOnRobot(self) -> int:
        ...
    @_nServoOnRobot.setter
    def _nServoOnRobot(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nToolDigitalInput(self) -> int:
        ...
    @_nToolDigitalInput.setter
    def _nToolDigitalInput(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nToolDigitalOutput(self) -> int:
        ...
    @_nToolDigitalOutput.setter
    def _nToolDigitalOutput(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class MONITORING_MBUS_SLAVE_HOILDING_REGISTER:
    def __init__(self) -> None:
        ...
    @property
    def _nCtrlAnalogInput1(self) -> int:
        ...
    @_nCtrlAnalogInput1.setter
    def _nCtrlAnalogInput1(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nCtrlAnalogInput1Type(self) -> int:
        ...
    @_nCtrlAnalogInput1Type.setter
    def _nCtrlAnalogInput1Type(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nCtrlAnalogInput2(self) -> int:
        ...
    @_nCtrlAnalogInput2.setter
    def _nCtrlAnalogInput2(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nCtrlAnalogInput2Type(self) -> int:
        ...
    @_nCtrlAnalogInput2Type.setter
    def _nCtrlAnalogInput2Type(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nCtrlAnalogOutput1(self) -> int:
        ...
    @_nCtrlAnalogOutput1.setter
    def _nCtrlAnalogOutput1(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nCtrlAnalogOutput1Type(self) -> int:
        ...
    @_nCtrlAnalogOutput1Type.setter
    def _nCtrlAnalogOutput1Type(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nCtrlAnalogOutput2(self) -> int:
        ...
    @_nCtrlAnalogOutput2.setter
    def _nCtrlAnalogOutput2(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nCtrlAnalogOutput2Type(self) -> int:
        ...
    @_nCtrlAnalogOutput2Type.setter
    def _nCtrlAnalogOutput2Type(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nCtrlDigitalInput(self) -> int:
        ...
    @_nCtrlDigitalInput.setter
    def _nCtrlDigitalInput(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nCtrlDigitalOutput(self) -> int:
        ...
    @_nCtrlDigitalOutput.setter
    def _nCtrlDigitalOutput(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nCtrlMajorVer(self) -> int:
        ...
    @_nCtrlMajorVer.setter
    def _nCtrlMajorVer(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nCtrlMinorVer(self) -> int:
        ...
    @_nCtrlMinorVer.setter
    def _nCtrlMinorVer(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nCtrlPatchVer(self) -> int:
        ...
    @_nCtrlPatchVer.setter
    def _nCtrlPatchVer(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nCtrlToolDigitalInput(self) -> int:
        ...
    @_nCtrlToolDigitalInput.setter
    def _nCtrlToolDigitalInput(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nCtrlToolDigitalOutput(self) -> int:
        ...
    @_nCtrlToolDigitalOutput.setter
    def _nCtrlToolDigitalOutput(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nDirectTeachButtonPressed(self) -> int:
        ...
    @_nDirectTeachButtonPressed.setter
    def _nDirectTeachButtonPressed(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nEmergencyStopped(self) -> int:
        ...
    @_nEmergencyStopped.setter
    def _nEmergencyStopped(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nGPR(self) -> numpy.typing.NDArray[numpy.uint16]:
        ...
    @_nGPR.setter
    def _nGPR(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint16]) -> None:
        ...
    @property
    def _nJointMotorCurrent(self) -> numpy.typing.NDArray[numpy.uint16]:
        ...
    @_nJointMotorCurrent.setter
    def _nJointMotorCurrent(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint16]) -> None:
        ...
    @property
    def _nJointMotorTemp(self) -> numpy.typing.NDArray[numpy.uint16]:
        ...
    @_nJointMotorTemp.setter
    def _nJointMotorTemp(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint16]) -> None:
        ...
    @property
    def _nJointPosition(self) -> numpy.typing.NDArray[numpy.uint16]:
        ...
    @_nJointPosition.setter
    def _nJointPosition(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint16]) -> None:
        ...
    @property
    def _nJointTorque(self) -> numpy.typing.NDArray[numpy.uint16]:
        ...
    @_nJointTorque.setter
    def _nJointTorque(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint16]) -> None:
        ...
    @property
    def _nJointVelocity(self) -> numpy.typing.NDArray[numpy.uint16]:
        ...
    @_nJointVelocity.setter
    def _nJointVelocity(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint16]) -> None:
        ...
    @property
    def _nPowerButtonPressed(self) -> int:
        ...
    @_nPowerButtonPressed.setter
    def _nPowerButtonPressed(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nRobotState(self) -> int:
        ...
    @_nRobotState.setter
    def _nRobotState(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nSafetyStopped(self) -> int:
        ...
    @_nSafetyStopped.setter
    def _nSafetyStopped(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nServoOnRobot(self) -> int:
        ...
    @_nServoOnRobot.setter
    def _nServoOnRobot(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nTaskExternalForce(self) -> numpy.typing.NDArray[numpy.uint16]:
        ...
    @_nTaskExternalForce.setter
    def _nTaskExternalForce(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint16]) -> None:
        ...
    @property
    def _nTaskPosition(self) -> numpy.typing.NDArray[numpy.uint16]:
        ...
    @_nTaskPosition.setter
    def _nTaskPosition(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint16]) -> None:
        ...
    @property
    def _nTaskVelocity(self) -> numpy.typing.NDArray[numpy.uint16]:
        ...
    @_nTaskVelocity.setter
    def _nTaskVelocity(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint16]) -> None:
        ...
    @property
    def _nToolOffsetLength(self) -> numpy.typing.NDArray[numpy.uint16]:
        ...
    @_nToolOffsetLength.setter
    def _nToolOffsetLength(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint16]) -> None:
        ...
class MONITORING_MISC:
    def __init__(self) -> None:
        ...
    @property
    def _dSyncTime(self) -> float:
        ...
    @_dSyncTime.setter
    def _dSyncTime(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fActualMC(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualMC.setter
    def _fActualMC(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fActualMT(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualMT.setter
    def _fActualMT(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iActualBK(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iActualBK.setter
    def _iActualBK(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iActualBT(self) -> numpy.typing.NDArray[numpy.uint32]:
        ...
    @_iActualBT.setter
    def _iActualBT(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint32]) -> None:
        ...
    @property
    def _iActualDI(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iActualDI.setter
    def _iActualDI(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iActualDO(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iActualDO.setter
    def _iActualDO(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class MONITORING_MODBUS:
    _tRegister: list
    def __init__(self) -> None:
        ...
    @property
    def _iRegCount(self) -> int:
        ...
    @_iRegCount.setter
    def _iRegCount(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class MONITORING_SPEED:
    """
    Members:
    
      Normal_mode
    
      Reduced_mode
    """
    Normal_mode: typing.ClassVar[MONITORING_SPEED]  # value = <MONITORING_SPEED.Normal_mode: 0>
    Reduced_mode: typing.ClassVar[MONITORING_SPEED]  # value = <MONITORING_SPEED.Reduced_mode: 1>
    __members__: typing.ClassVar[dict[str, MONITORING_SPEED]]  # value = {'Normal_mode': <MONITORING_SPEED.Normal_mode: 0>, 'Reduced_mode': <MONITORING_SPEED.Reduced_mode: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class MOVEB_BLENDING_TYPE:
    """
    Members:
    
      Line
    
      Circle
    """
    Circle: typing.ClassVar[MOVEB_BLENDING_TYPE]  # value = <MOVEB_BLENDING_TYPE.Circle: 1>
    Line: typing.ClassVar[MOVEB_BLENDING_TYPE]  # value = <MOVEB_BLENDING_TYPE.Line: 0>
    __members__: typing.ClassVar[dict[str, MOVEB_BLENDING_TYPE]]  # value = {'Line': <MOVEB_BLENDING_TYPE.Line: 0>, 'Circle': <MOVEB_BLENDING_TYPE.Circle: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class MOVE_HOME:
    """
    Members:
    
      Mechanic
    
      User
    """
    Mechanic: typing.ClassVar[MOVE_HOME]  # value = <MOVE_HOME.Mechanic: 0>
    User: typing.ClassVar[MOVE_HOME]  # value = <MOVE_HOME.User: 1>
    __members__: typing.ClassVar[dict[str, MOVE_HOME]]  # value = {'Mechanic': <MOVE_HOME.Mechanic: 0>, 'User': <MOVE_HOME.User: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class MOVE_MODE:
    """
    Members:
    
      Absolute
    
      Relative
    """
    Absolute: typing.ClassVar[MOVE_MODE]  # value = <MOVE_MODE.Absolute: 0>
    Relative: typing.ClassVar[MOVE_MODE]  # value = <MOVE_MODE.Relative: 1>
    __members__: typing.ClassVar[dict[str, MOVE_MODE]]  # value = {'Absolute': <MOVE_MODE.Absolute: 0>, 'Relative': <MOVE_MODE.Relative: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class MOVE_ORIENTATION:
    """
    Members:
    
      Teach
    
      Fixed
    
      Radial
    
      Intent
    """
    Fixed: typing.ClassVar[MOVE_ORIENTATION]  # value = <MOVE_ORIENTATION.Fixed: 1>
    Intent: typing.ClassVar[MOVE_ORIENTATION]  # value = <MOVE_ORIENTATION.Intent: 3>
    Radial: typing.ClassVar[MOVE_ORIENTATION]  # value = <MOVE_ORIENTATION.Radial: 2>
    Teach: typing.ClassVar[MOVE_ORIENTATION]  # value = <MOVE_ORIENTATION.Teach: 0>
    __members__: typing.ClassVar[dict[str, MOVE_ORIENTATION]]  # value = {'Teach': <MOVE_ORIENTATION.Teach: 0>, 'Fixed': <MOVE_ORIENTATION.Fixed: 1>, 'Radial': <MOVE_ORIENTATION.Radial: 2>, 'Intent': <MOVE_ORIENTATION.Intent: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class MOVE_POSB:
    def __init__(self) -> None:
        ...
    @property
    def _fBlendRad(self) -> float:
        ...
    @_fBlendRad.setter
    def _fBlendRad(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fTargetPos(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTargetPos.setter
    def _fTargetPos(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iBlendType(self) -> int:
        ...
    @_iBlendType.setter
    def _iBlendType(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class MOVE_REFERENCE:
    """
    Members:
    
      Base
    
      Tool
    
      World
    
      User_min
    
      User_max
    """
    Base: typing.ClassVar[MOVE_REFERENCE]  # value = <MOVE_REFERENCE.Base: 0>
    Tool: typing.ClassVar[MOVE_REFERENCE]  # value = <MOVE_REFERENCE.Tool: 1>
    User_max: typing.ClassVar[MOVE_REFERENCE]  # value = <MOVE_REFERENCE.User_max: 200>
    User_min: typing.ClassVar[MOVE_REFERENCE]  # value = <MOVE_REFERENCE.User_min: 101>
    World: typing.ClassVar[MOVE_REFERENCE]  # value = <MOVE_REFERENCE.World: 2>
    __members__: typing.ClassVar[dict[str, MOVE_REFERENCE]]  # value = {'Base': <MOVE_REFERENCE.Base: 0>, 'Tool': <MOVE_REFERENCE.Tool: 1>, 'World': <MOVE_REFERENCE.World: 2>, 'User_min': <MOVE_REFERENCE.User_min: 101>, 'User_max': <MOVE_REFERENCE.User_max: 200>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class NORMAL_VECTOR:
    def __init__(self) -> None:
        ...
    @property
    def _fTargetPos(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTargetPos.setter
    def _fTargetPos(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
class OUTPUT_TYPE:
    """
    Members:
    
      PNP
    
      NPN
    """
    NPN: typing.ClassVar[OUTPUT_TYPE]  # value = <OUTPUT_TYPE.NPN: 1>
    PNP: typing.ClassVar[OUTPUT_TYPE]  # value = <OUTPUT_TYPE.PNP: 0>
    __members__: typing.ClassVar[dict[str, OUTPUT_TYPE]]  # value = {'PNP': <OUTPUT_TYPE.PNP: 0>, 'NPN': <OUTPUT_TYPE.NPN: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class PARITY_CHECK:
    """
    Members:
    
      none
    
      even
    
      odd
    """
    __members__: typing.ClassVar[dict[str, PARITY_CHECK]]  # value = {'none': <PARITY_CHECK.none: 0>, 'even': <PARITY_CHECK.even: 1>, 'odd': <PARITY_CHECK.odd: 2>}
    even: typing.ClassVar[PARITY_CHECK]  # value = <PARITY_CHECK.even: 1>
    none: typing.ClassVar[PARITY_CHECK]  # value = <PARITY_CHECK.none: 0>
    odd: typing.ClassVar[PARITY_CHECK]  # value = <PARITY_CHECK.odd: 2>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class PATH_MODE:
    """
    Members:
    
      DPOS
    
      DVEL
    """
    DPOS: typing.ClassVar[PATH_MODE]  # value = <PATH_MODE.DPOS: 0>
    DVEL: typing.ClassVar[PATH_MODE]  # value = <PATH_MODE.DVEL: 1>
    __members__: typing.ClassVar[dict[str, PATH_MODE]]  # value = {'DPOS': <PATH_MODE.DPOS: 0>, 'DVEL': <PATH_MODE.DVEL: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class POINT_2D:
    def __init__(self) -> None:
        ...
    @property
    def _fXPos(self) -> float:
        ...
    @_fXPos.setter
    def _fXPos(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fYPos(self) -> float:
        ...
    @_fYPos.setter
    def _fYPos(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class POINT_3D:
    def __init__(self) -> None:
        ...
    @property
    def _fXPos(self) -> float:
        ...
    @_fXPos.setter
    def _fXPos(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fYPos(self) -> float:
        ...
    @_fYPos.setter
    def _fYPos(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fZPos(self) -> float:
        ...
    @_fZPos.setter
    def _fZPos(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class POPUP_RESPONSE:
    """
    Members:
    
      Stop
    
      Resume
    """
    Resume: typing.ClassVar[POPUP_RESPONSE]  # value = <POPUP_RESPONSE.Resume: 1>
    Stop: typing.ClassVar[POPUP_RESPONSE]  # value = <POPUP_RESPONSE.Stop: 0>
    __members__: typing.ClassVar[dict[str, POPUP_RESPONSE]]  # value = {'Stop': <POPUP_RESPONSE.Stop: 0>, 'Resume': <POPUP_RESPONSE.Resume: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class POSITION:
    def __init__(self) -> None:
        ...
    @property
    def _fTargetPos(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTargetPos.setter
    def _fTargetPos(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
class POSITION_ADDTO:
    def __init__(self) -> None:
        ...
    @property
    def _fTargetPos(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTargetPos.setter
    def _fTargetPos(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fTargetVal(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTargetVal.setter
    def _fTargetVal(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
class POSITION_EX:
    def __init__(self) -> None:
        ...
    @property
    def _multi_turn(self) -> int:
        ...
    @_multi_turn.setter
    def _multi_turn(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _ori_type(self) -> int:
        ...
    @_ori_type.setter
    def _ori_type(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _pos_type(self) -> int:
        ...
    @_pos_type.setter
    def _pos_type(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _sol_space(self) -> int:
        ...
    @_sol_space.setter
    def _sol_space(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def posj_pos(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @posj_pos.setter
    def posj_pos(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def posx_pos(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @posx_pos.setter
    def posx_pos(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
class PROGRAM_ERROR:
    _szFile: str
    def __init__(self) -> None:
        ...
    @property
    def _iError(self) -> int:
        ...
    @_iError.setter
    def _iError(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _nLine(self) -> int:
        ...
    @_nLine.setter
    def _nLine(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class PROGRAM_EXECUTION_EX:
    _szFile: str
    def __init__(self) -> None:
        ...
    @property
    def _fElapseTime(self) -> float:
        ...
    @_fElapseTime.setter
    def _fElapseTime(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _iLineNumber(self) -> int:
        ...
    @_iLineNumber.setter
    def _iLineNumber(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class PROGRAM_STOP_CAUSE:
    """
    Members:
    
      Normal
    
      Force
    
      Error
    
      Last
    """
    Error: typing.ClassVar[PROGRAM_STOP_CAUSE]  # value = <PROGRAM_STOP_CAUSE.Error: 2>
    Force: typing.ClassVar[PROGRAM_STOP_CAUSE]  # value = <PROGRAM_STOP_CAUSE.Force: 1>
    Last: typing.ClassVar[PROGRAM_STOP_CAUSE]  # value = <PROGRAM_STOP_CAUSE.Last: 3>
    Normal: typing.ClassVar[PROGRAM_STOP_CAUSE]  # value = <PROGRAM_STOP_CAUSE.Normal: 0>
    __members__: typing.ClassVar[dict[str, PROGRAM_STOP_CAUSE]]  # value = {'Normal': <PROGRAM_STOP_CAUSE.Normal: 0>, 'Force': <PROGRAM_STOP_CAUSE.Force: 1>, 'Error': <PROGRAM_STOP_CAUSE.Error: 2>, 'Last': <PROGRAM_STOP_CAUSE.Last: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class PROGRAM_SYNTAX_CHECK:
    def __init__(self) -> None:
        ...
    @property
    def _iTextLength(self) -> int:
        ...
    @_iTextLength.setter
    def _iTextLength(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class PROGRAM_WATCH_VARIABLE:
    _szData: str
    _szName: str
    def __init__(self) -> None:
        ...
    @property
    def _iDivision(self) -> int:
        ...
    @_iDivision.setter
    def _iDivision(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iType(self) -> int:
        ...
    @_iType.setter
    def _iType(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class READ_CTRLIO_INPUT:
    def __init__(self) -> None:
        ...
    @property
    def _fActualAI(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualAI.setter
    def _fActualAI(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iActualDI(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iActualDI.setter
    def _iActualDI(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iActualEI(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iActualEI.setter
    def _iActualEI(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iActualSI(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iActualSI.setter
    def _iActualSI(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iActualSW(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iActualSW.setter
    def _iActualSW(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iAcutualED(self) -> numpy.typing.NDArray[numpy.uint32]:
        ...
    @_iAcutualED.setter
    def _iAcutualED(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint32]) -> None:
        ...
class READ_CTRLIO_INPUT_EX:
    def __init__(self) -> None:
        ...
    @property
    def _fActualAI(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualAI.setter
    def _fActualAI(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iActualAT(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iActualAT.setter
    def _iActualAT(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iActualDI(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iActualDI.setter
    def _iActualDI(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iActualSI(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iActualSI.setter
    def _iActualSI(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iActualSW(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iActualSW.setter
    def _iActualSW(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class READ_CTRLIO_INPUT_EX2:
    def __init__(self) -> None:
        ...
    @property
    def _fActualAI(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualAI.setter
    def _fActualAI(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iActualAT(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iActualAT.setter
    def _iActualAT(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iActualDI(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iActualDI.setter
    def _iActualDI(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iActualSI(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iActualSI.setter
    def _iActualSI(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iActualSW(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iActualSW.setter
    def _iActualSW(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class READ_CTRLIO_OUTPUT:
    def __init__(self) -> None:
        ...
    @property
    def _fTargetAO(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTargetAO.setter
    def _fTargetAO(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iTargetDO(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iTargetDO.setter
    def _iTargetDO(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class READ_CTRLIO_OUTPUT_EX:
    def __init__(self) -> None:
        ...
    @property
    def _fTargetAO(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTargetAO.setter
    def _fTargetAO(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iTargetAT(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iTargetAT.setter
    def _iTargetAT(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iTargetDO(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iTargetDO.setter
    def _iTargetDO(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class READ_CTRLIO_OUTPUT_EX2:
    def __init__(self) -> None:
        ...
    @property
    def _fTargetAO(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTargetAO.setter
    def _fTargetAO(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iTargetAT(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iTargetAT.setter
    def _iTargetAT(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iTargetDO(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iTargetDO.setter
    def _iTargetDO(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class READ_ENCODER_INPUT:
    def __init__(self) -> None:
        ...
    @property
    def _iActualED(self) -> numpy.typing.NDArray[numpy.uint32]:
        ...
    @_iActualED.setter
    def _iActualED(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint32]) -> None:
        ...
    @property
    def _iActualER(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iActualER.setter
    def _iActualER(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iActualES(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iActualES.setter
    def _iActualES(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class READ_FLANGE_SERIAL:
    def __init__(self) -> None:
        ...
    @property
    def _bRecvFlag(self) -> int:
        ...
    @_bRecvFlag.setter
    def _bRecvFlag(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class READ_FLANGE_SERIAL_EX:
    def __init__(self) -> None:
        ...
    @property
    def _bRecvFlag(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_bRecvFlag.setter
    def _bRecvFlag(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class READ_PROCESS_INPUT:
    def __init__(self) -> None:
        ...
    @property
    def _iActualDI(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iActualDI.setter
    def _iActualDI(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class RELEASE_MODE:
    """
    Members:
    
      Stop
    
      Resume
    
      Release
    
      Reset
    """
    Release: typing.ClassVar[RELEASE_MODE]  # value = <RELEASE_MODE.Release: 2>
    Reset: typing.ClassVar[RELEASE_MODE]  # value = <RELEASE_MODE.Reset: 3>
    Resume: typing.ClassVar[RELEASE_MODE]  # value = <RELEASE_MODE.Resume: 1>
    Stop: typing.ClassVar[RELEASE_MODE]  # value = <RELEASE_MODE.Stop: 0>
    __members__: typing.ClassVar[dict[str, RELEASE_MODE]]  # value = {'Stop': <RELEASE_MODE.Stop: 0>, 'Resume': <RELEASE_MODE.Resume: 1>, 'Release': <RELEASE_MODE.Release: 2>, 'Reset': <RELEASE_MODE.Reset: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class REPORT_TCP_CLIENT:
    def __init__(self) -> None:
        ...
    @property
    def _iCount(self) -> int:
        ...
    @_iCount.setter
    def _iCount(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iId(self) -> int:
        ...
    @_iId.setter
    def _iId(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class ROBOT_CONTROL:
    """
    Members:
    
      Init_config
    
      Operation
    
      Reset_safet_stop
    
      Reset_safe_stop
    
      Reset_safet_off
    
      Reset_safe_off
    
      Servo_on
    
      Recovery_safe_stop
    
      Recovery_safe_off
    
      Recovery_backdrive
    
      Reset_recovery
    
      Last
    """
    Init_config: typing.ClassVar[ROBOT_CONTROL]  # value = <ROBOT_CONTROL.Init_config: 0>
    Last: typing.ClassVar[ROBOT_CONTROL]  # value = <ROBOT_CONTROL.Last: 8>
    Operation: typing.ClassVar[ROBOT_CONTROL]  # value = <ROBOT_CONTROL.Operation: 1>
    Recovery_backdrive: typing.ClassVar[ROBOT_CONTROL]  # value = <ROBOT_CONTROL.Recovery_backdrive: 6>
    Recovery_safe_off: typing.ClassVar[ROBOT_CONTROL]  # value = <ROBOT_CONTROL.Recovery_safe_off: 5>
    Recovery_safe_stop: typing.ClassVar[ROBOT_CONTROL]  # value = <ROBOT_CONTROL.Recovery_safe_stop: 4>
    Reset_recovery: typing.ClassVar[ROBOT_CONTROL]  # value = <ROBOT_CONTROL.Reset_recovery: 7>
    Reset_safe_off: typing.ClassVar[ROBOT_CONTROL]  # value = <ROBOT_CONTROL.Reset_safet_off: 3>
    Reset_safe_stop: typing.ClassVar[ROBOT_CONTROL]  # value = <ROBOT_CONTROL.Reset_safet_stop: 2>
    Reset_safet_off: typing.ClassVar[ROBOT_CONTROL]  # value = <ROBOT_CONTROL.Reset_safet_off: 3>
    Reset_safet_stop: typing.ClassVar[ROBOT_CONTROL]  # value = <ROBOT_CONTROL.Reset_safet_stop: 2>
    Servo_on: typing.ClassVar[ROBOT_CONTROL]  # value = <ROBOT_CONTROL.Reset_safet_off: 3>
    __members__: typing.ClassVar[dict[str, ROBOT_CONTROL]]  # value = {'Init_config': <ROBOT_CONTROL.Init_config: 0>, 'Operation': <ROBOT_CONTROL.Operation: 1>, 'Reset_safet_stop': <ROBOT_CONTROL.Reset_safet_stop: 2>, 'Reset_safe_stop': <ROBOT_CONTROL.Reset_safet_stop: 2>, 'Reset_safet_off': <ROBOT_CONTROL.Reset_safet_off: 3>, 'Reset_safe_off': <ROBOT_CONTROL.Reset_safet_off: 3>, 'Servo_on': <ROBOT_CONTROL.Reset_safet_off: 3>, 'Recovery_safe_stop': <ROBOT_CONTROL.Recovery_safe_stop: 4>, 'Recovery_safe_off': <ROBOT_CONTROL.Recovery_safe_off: 5>, 'Recovery_backdrive': <ROBOT_CONTROL.Recovery_backdrive: 6>, 'Reset_recovery': <ROBOT_CONTROL.Reset_recovery: 7>, 'Last': <ROBOT_CONTROL.Last: 8>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ROBOT_FORCE:
    def __init__(self) -> None:
        ...
    @property
    def _fForce(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fForce.setter
    def _fForce(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
class ROBOT_LED_CONFIG:
    def __init__(self) -> None:
        ...
    @property
    def _szCommandColor(self) -> int:
        ...
    @_szCommandColor.setter
    def _szCommandColor(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _szLedRule(self) -> int:
        ...
    @_szLedRule.setter
    def _szLedRule(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _szStateColor(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_szStateColor.setter
    def _szStateColor(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class ROBOT_LINK_INFO:
    def __init__(self) -> None:
        ...
    @property
    def a(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @a.setter
    def a(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def alpha(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @alpha.setter
    def alpha(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def d(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @d.setter
    def d(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def gradient(self) -> float:
        ...
    @gradient.setter
    def gradient(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def offset(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @offset.setter
    def offset(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def rotation(self) -> float:
        ...
    @rotation.setter
    def rotation(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def theta(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @theta.setter
    def theta(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
class ROBOT_MODE:
    """
    Members:
    
      Manual
    
      Autonomous
    
      Recovery
    
      Backdrive
    
      Measure
    
      Intialize
    
      Last
    """
    Autonomous: typing.ClassVar[ROBOT_MODE]  # value = <ROBOT_MODE.Autonomous: 1>
    Backdrive: typing.ClassVar[ROBOT_MODE]  # value = <ROBOT_MODE.Backdrive: 3>
    Intialize: typing.ClassVar[ROBOT_MODE]  # value = <ROBOT_MODE.Intialize: 5>
    Last: typing.ClassVar[ROBOT_MODE]  # value = <ROBOT_MODE.Last: 6>
    Manual: typing.ClassVar[ROBOT_MODE]  # value = <ROBOT_MODE.Manual: 0>
    Measure: typing.ClassVar[ROBOT_MODE]  # value = <ROBOT_MODE.Measure: 4>
    Recovery: typing.ClassVar[ROBOT_MODE]  # value = <ROBOT_MODE.Recovery: 2>
    __members__: typing.ClassVar[dict[str, ROBOT_MODE]]  # value = {'Manual': <ROBOT_MODE.Manual: 0>, 'Autonomous': <ROBOT_MODE.Autonomous: 1>, 'Recovery': <ROBOT_MODE.Recovery: 2>, 'Backdrive': <ROBOT_MODE.Backdrive: 3>, 'Measure': <ROBOT_MODE.Measure: 4>, 'Intialize': <ROBOT_MODE.Intialize: 5>, 'Last': <ROBOT_MODE.Last: 6>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ROBOT_MONITORING_AMODEL:
    _tSensor: ROBOT_MONITORING_SENSOR
    def __init__(self) -> None:
        ...
    @property
    def _fSingularity(self) -> float:
        ...
    @_fSingularity.setter
    def _fSingularity(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class ROBOT_MONITORING_DATA_EX:
    _tJoint: ROBOT_MONITORING_JOINT
    _tState: ROBOT_MONITORING_STATE
    _tTask: ROBOT_MONITORING_TASK
    _tTorque: ROBOT_MONITORING_TORQUE
    _tUser: ROBOT_MONITORING_USER
    _tWorld: ROBOT_MONITORING_WORLD
    def __init__(self) -> None:
        ...
class ROBOT_MONITORING_JOINT:
    def __init__(self) -> None:
        ...
    @property
    def _fActualAbs(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualAbs.setter
    def _fActualAbs(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fActualErr(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualErr.setter
    def _fActualErr(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fActualPos(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualPos.setter
    def _fActualPos(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fActualVel(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualVel.setter
    def _fActualVel(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fTargetPos(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTargetPos.setter
    def _fTargetPos(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fTargetVel(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTargetVel.setter
    def _fTargetVel(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
class ROBOT_MONITORING_SENSOR:
    def __init__(self) -> None:
        ...
    @property
    def _fActualACS(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualACS.setter
    def _fActualACS(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fActualCS(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualCS.setter
    def _fActualCS(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fActualFTS(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualFTS.setter
    def _fActualFTS(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
class ROBOT_MONITORING_STATE:
    def __init__(self) -> None:
        ...
    @property
    def _iActualMode(self) -> int:
        ...
    @_iActualMode.setter
    def _iActualMode(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iActualSpace(self) -> int:
        ...
    @_iActualSpace.setter
    def _iActualSpace(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class ROBOT_MONITORING_TASK:
    def __init__(self) -> None:
        ...
    @property
    def _fActualErr(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualErr.setter
    def _fActualErr(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fActualPos(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualPos.setter
    def _fActualPos(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fActualVel(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualVel.setter
    def _fActualVel(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fRotationMatrix(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fRotationMatrix.setter
    def _fRotationMatrix(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fTargetPos(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTargetPos.setter
    def _fTargetPos(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fTargetVel(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTargetVel.setter
    def _fTargetVel(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iSolutionSpace(self) -> int:
        ...
    @_iSolutionSpace.setter
    def _iSolutionSpace(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class ROBOT_MONITORING_TORQUE:
    def __init__(self) -> None:
        ...
    @property
    def _fActualEJT(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualEJT.setter
    def _fActualEJT(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fActualETT(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualETT.setter
    def _fActualETT(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fActualJTS(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualJTS.setter
    def _fActualJTS(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fDynamicTor(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fDynamicTor.setter
    def _fDynamicTor(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
class ROBOT_MONITORING_USER:
    def __init__(self) -> None:
        ...
    @property
    def _fActualETT(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualETT.setter
    def _fActualETT(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fActualPos(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualPos.setter
    def _fActualPos(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fActualVel(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualVel.setter
    def _fActualVel(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fRotationMatrix(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fRotationMatrix.setter
    def _fRotationMatrix(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fTargetPos(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTargetPos.setter
    def _fTargetPos(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fTargetVel(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTargetVel.setter
    def _fTargetVel(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iActualUCN(self) -> int:
        ...
    @_iActualUCN.setter
    def _iActualUCN(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iParent(self) -> int:
        ...
    @_iParent.setter
    def _iParent(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class ROBOT_MONITORING_WORLD:
    def __init__(self) -> None:
        ...
    @property
    def _fActualETT(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualETT.setter
    def _fActualETT(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fActualPos(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualPos.setter
    def _fActualPos(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fActualVel(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualVel.setter
    def _fActualVel(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fActualW2B(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fActualW2B.setter
    def _fActualW2B(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fRotationMatrix(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fRotationMatrix.setter
    def _fRotationMatrix(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fTargetPos(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTargetPos.setter
    def _fTargetPos(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fTargetVel(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTargetVel.setter
    def _fTargetVel(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
class ROBOT_POSE:
    def __init__(self) -> None:
        ...
    @property
    def _fPosition(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fPosition.setter
    def _fPosition(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
class ROBOT_SPACE:
    """
    Members:
    
      Joint
    
      Task
    """
    Joint: typing.ClassVar[ROBOT_SPACE]  # value = <ROBOT_SPACE.Joint: 0>
    Task: typing.ClassVar[ROBOT_SPACE]  # value = <ROBOT_SPACE.Task: 1>
    __members__: typing.ClassVar[dict[str, ROBOT_SPACE]]  # value = {'Joint': <ROBOT_SPACE.Joint: 0>, 'Task': <ROBOT_SPACE.Task: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ROBOT_STATE:
    """
    Members:
    
      Initializing
    
      Standby
    
      Moving
    
      Safe_off
    
      Teaching
    
      Safe_stop
    
      Emergency_stop
    
      Homming
    
      Recovery
    
      Safe_stop2
    
      Safe_off2
    
      Reserved1
    
      Reserved2
    
      Reserved3
    
      Reserved4
    
      Not_ready
    
      Last
    """
    Emergency_stop: typing.ClassVar[ROBOT_STATE]  # value = <ROBOT_STATE.Emergency_stop: 6>
    Homming: typing.ClassVar[ROBOT_STATE]  # value = <ROBOT_STATE.Homming: 7>
    Initializing: typing.ClassVar[ROBOT_STATE]  # value = <ROBOT_STATE.Initializing: 0>
    Last: typing.ClassVar[ROBOT_STATE]  # value = <ROBOT_STATE.Last: 16>
    Moving: typing.ClassVar[ROBOT_STATE]  # value = <ROBOT_STATE.Moving: 2>
    Not_ready: typing.ClassVar[ROBOT_STATE]  # value = <ROBOT_STATE.Not_ready: 15>
    Recovery: typing.ClassVar[ROBOT_STATE]  # value = <ROBOT_STATE.Recovery: 8>
    Reserved1: typing.ClassVar[ROBOT_STATE]  # value = <ROBOT_STATE.Reserved1: 11>
    Reserved2: typing.ClassVar[ROBOT_STATE]  # value = <ROBOT_STATE.Reserved2: 12>
    Reserved3: typing.ClassVar[ROBOT_STATE]  # value = <ROBOT_STATE.Reserved3: 13>
    Reserved4: typing.ClassVar[ROBOT_STATE]  # value = <ROBOT_STATE.Reserved4: 14>
    Safe_off: typing.ClassVar[ROBOT_STATE]  # value = <ROBOT_STATE.Safe_off: 3>
    Safe_off2: typing.ClassVar[ROBOT_STATE]  # value = <ROBOT_STATE.Safe_off2: 10>
    Safe_stop: typing.ClassVar[ROBOT_STATE]  # value = <ROBOT_STATE.Safe_stop: 5>
    Safe_stop2: typing.ClassVar[ROBOT_STATE]  # value = <ROBOT_STATE.Safe_stop2: 9>
    Standby: typing.ClassVar[ROBOT_STATE]  # value = <ROBOT_STATE.Standby: 1>
    Teaching: typing.ClassVar[ROBOT_STATE]  # value = <ROBOT_STATE.Teaching: 4>
    __members__: typing.ClassVar[dict[str, ROBOT_STATE]]  # value = {'Initializing': <ROBOT_STATE.Initializing: 0>, 'Standby': <ROBOT_STATE.Standby: 1>, 'Moving': <ROBOT_STATE.Moving: 2>, 'Safe_off': <ROBOT_STATE.Safe_off: 3>, 'Teaching': <ROBOT_STATE.Teaching: 4>, 'Safe_stop': <ROBOT_STATE.Safe_stop: 5>, 'Emergency_stop': <ROBOT_STATE.Emergency_stop: 6>, 'Homming': <ROBOT_STATE.Homming: 7>, 'Recovery': <ROBOT_STATE.Recovery: 8>, 'Safe_stop2': <ROBOT_STATE.Safe_stop2: 9>, 'Safe_off2': <ROBOT_STATE.Safe_off2: 10>, 'Reserved1': <ROBOT_STATE.Reserved1: 11>, 'Reserved2': <ROBOT_STATE.Reserved2: 12>, 'Reserved3': <ROBOT_STATE.Reserved3: 13>, 'Reserved4': <ROBOT_STATE.Reserved4: 14>, 'Not_ready': <ROBOT_STATE.Not_ready: 15>, 'Last': <ROBOT_STATE.Last: 16>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ROBOT_SYSTEM:
    """
    Members:
    
      Real
    
      Virtual
    
      Last
    """
    Last: typing.ClassVar[ROBOT_SYSTEM]  # value = <ROBOT_SYSTEM.Last: 2>
    Real: typing.ClassVar[ROBOT_SYSTEM]  # value = <ROBOT_SYSTEM.Real: 0>
    Virtual: typing.ClassVar[ROBOT_SYSTEM]  # value = <ROBOT_SYSTEM.Virtual: 1>
    __members__: typing.ClassVar[dict[str, ROBOT_SYSTEM]]  # value = {'Real': <ROBOT_SYSTEM.Real: 0>, 'Virtual': <ROBOT_SYSTEM.Virtual: 1>, 'Last': <ROBOT_SYSTEM.Last: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ROBOT_TASK_POSE:
    def __init__(self) -> None:
        ...
    @property
    def _fTargetPos(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTargetPos.setter
    def _fTargetPos(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iTargetSol(self) -> int:
        ...
    @_iTargetSol.setter
    def _iTargetSol(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class ROBOT_VEL:
    def __init__(self) -> None:
        ...
    @property
    def _fVelocity(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fVelocity.setter
    def _fVelocity(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
class ROBOT_WELDING_DATA:
    def __init__(self) -> None:
        ...
    @property
    def _fActualCur(self) -> float:
        ...
    @_fActualCur.setter
    def _fActualCur(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fActualVol(self) -> float:
        ...
    @_fActualVol.setter
    def _fActualVol(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fOffsetY(self) -> float:
        ...
    @_fOffsetY.setter
    def _fOffsetY(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fOffsetZ(self) -> float:
        ...
    @_fOffsetZ.setter
    def _fOffsetZ(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fTargetCur(self) -> float:
        ...
    @_fTargetCur.setter
    def _fTargetCur(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fTargetVel(self) -> float:
        ...
    @_fTargetVel.setter
    def _fTargetVel(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fTargetVol(self) -> float:
        ...
    @_fTargetVol.setter
    def _fTargetVol(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _iAdjAvail(self) -> int:
        ...
    @_iAdjAvail.setter
    def _iAdjAvail(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iArcOnDO(self) -> int:
        ...
    @_iArcOnDO.setter
    def _iArcOnDO(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iGasOnDO(self) -> int:
        ...
    @_iGasOnDO.setter
    def _iGasOnDO(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iInchNPO(self) -> int:
        ...
    @_iInchNPO.setter
    def _iInchNPO(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iInchPDO(self) -> int:
        ...
    @_iInchPDO.setter
    def _iInchPDO(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iStatus(self) -> int:
        ...
    @_iStatus.setter
    def _iStatus(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class ROT_DIR:
    """
    Members:
    
      Forward
    
      Reverse
    """
    Forward: typing.ClassVar[ROT_DIR]  # value = <ROT_DIR.Forward: 0>
    Reverse: typing.ClassVar[ROT_DIR]  # value = <ROT_DIR.Reverse: 1>
    __members__: typing.ClassVar[dict[str, ROT_DIR]]  # value = {'Forward': <ROT_DIR.Forward: 0>, 'Reverse': <ROT_DIR.Reverse: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class RT_INPUT_DATA_LIST:
    def __init__(self) -> None:
        ...
    @property
    def _fExternalAnalogInput(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fExternalAnalogInput.setter
    def _fExternalAnalogInput(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fExternalAnalogOutput(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fExternalAnalogOutput.setter
    def _fExternalAnalogOutput(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fExternalForceTorque(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fExternalForceTorque.setter
    def _fExternalForceTorque(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iExternalDI(self) -> int:
        ...
    @_iExternalDI.setter
    def _iExternalDI(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iExternalDO(self) -> int:
        ...
    @_iExternalDO.setter
    def _iExternalDO(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class RT_OUTPUT_DATA_LIST:
    def __init__(self) -> None:
        ...
    @property
    def actual_flange_position(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @actual_flange_position.setter
    def actual_flange_position(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def actual_flange_velocity(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @actual_flange_velocity.setter
    def actual_flange_velocity(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def actual_joint_position(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @actual_joint_position.setter
    def actual_joint_position(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def actual_joint_position_abs(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @actual_joint_position_abs.setter
    def actual_joint_position_abs(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def actual_joint_torque(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @actual_joint_torque.setter
    def actual_joint_torque(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def actual_joint_velocity(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @actual_joint_velocity.setter
    def actual_joint_velocity(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def actual_joint_velocity_abs(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @actual_joint_velocity_abs.setter
    def actual_joint_velocity_abs(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def actual_motor_torque(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @actual_motor_torque.setter
    def actual_motor_torque(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def actual_tcp_position(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @actual_tcp_position.setter
    def actual_tcp_position(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def actual_tcp_velocity(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @actual_tcp_velocity.setter
    def actual_tcp_velocity(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def control_mode(self) -> int:
        ...
    @control_mode.setter
    def control_mode(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def controller_analog_input(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @controller_analog_input.setter
    def controller_analog_input(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def controller_analog_input_type(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @controller_analog_input_type.setter
    def controller_analog_input_type(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def controller_analog_output(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @controller_analog_output.setter
    def controller_analog_output(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def controller_analog_output_type(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @controller_analog_output_type.setter
    def controller_analog_output_type(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def controller_digital_input(self) -> int:
        ...
    @controller_digital_input.setter
    def controller_digital_input(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def controller_digital_output(self) -> int:
        ...
    @controller_digital_output.setter
    def controller_digital_output(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def coriolis_matrix(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @coriolis_matrix.setter
    def coriolis_matrix(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def external_encoder_count(self) -> numpy.typing.NDArray[numpy.uint32]:
        ...
    @external_encoder_count.setter
    def external_encoder_count(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint32]) -> None:
        ...
    @property
    def external_encoder_strobe_count(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @external_encoder_strobe_count.setter
    def external_encoder_strobe_count(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def external_joint_torque(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @external_joint_torque.setter
    def external_joint_torque(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def external_tcp_force(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @external_tcp_force.setter
    def external_tcp_force(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def flange_analog_input(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @flange_analog_input.setter
    def flange_analog_input(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def flange_digital_input(self) -> int:
        ...
    @flange_digital_input.setter
    def flange_digital_input(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def flange_digital_output(self) -> int:
        ...
    @flange_digital_output.setter
    def flange_digital_output(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def goal_joint_position(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @goal_joint_position.setter
    def goal_joint_position(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def goal_tcp_position(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @goal_tcp_position.setter
    def goal_tcp_position(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def gravity_torque(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @gravity_torque.setter
    def gravity_torque(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def jacobian_matrix(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @jacobian_matrix.setter
    def jacobian_matrix(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def joint_temperature(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @joint_temperature.setter
    def joint_temperature(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def mass_matrix(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @mass_matrix.setter
    def mass_matrix(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def operation_speed_rate(self) -> float:
        ...
    @operation_speed_rate.setter
    def operation_speed_rate(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def raw_force_torque(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @raw_force_torque.setter
    def raw_force_torque(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def raw_joint_torque(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @raw_joint_torque.setter
    def raw_joint_torque(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def robot_mode(self) -> int:
        ...
    @robot_mode.setter
    def robot_mode(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def robot_state(self) -> int:
        ...
    @robot_state.setter
    def robot_state(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def singularity(self) -> float:
        ...
    @singularity.setter
    def singularity(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def solution_space(self) -> int:
        ...
    @solution_space.setter
    def solution_space(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def target_joint_acceleration(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @target_joint_acceleration.setter
    def target_joint_acceleration(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def target_joint_position(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @target_joint_position.setter
    def target_joint_position(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def target_joint_velocity(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @target_joint_velocity.setter
    def target_joint_velocity(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def target_motor_torque(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @target_motor_torque.setter
    def target_motor_torque(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def target_tcp_position(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @target_tcp_position.setter
    def target_tcp_position(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def target_tcp_velocity(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @target_tcp_velocity.setter
    def target_tcp_velocity(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def time_stamp(self) -> float:
        ...
    @time_stamp.setter
    def time_stamp(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class SAFETY_MODE:
    """
    Members:
    
      Manual
    
      Autonomous
    
      Recovery
    
      Backdrive
    
      Measure
    
      Initialize
    
      Last
    """
    Autonomous: typing.ClassVar[SAFETY_MODE]  # value = <SAFETY_MODE.Autonomous: 1>
    Backdrive: typing.ClassVar[SAFETY_MODE]  # value = <SAFETY_MODE.Backdrive: 3>
    Initialize: typing.ClassVar[SAFETY_MODE]  # value = <SAFETY_MODE.Initialize: 5>
    Last: typing.ClassVar[SAFETY_MODE]  # value = <SAFETY_MODE.Last: 6>
    Manual: typing.ClassVar[SAFETY_MODE]  # value = <SAFETY_MODE.Manual: 0>
    Measure: typing.ClassVar[SAFETY_MODE]  # value = <SAFETY_MODE.Measure: 4>
    Recovery: typing.ClassVar[SAFETY_MODE]  # value = <SAFETY_MODE.Recovery: 2>
    __members__: typing.ClassVar[dict[str, SAFETY_MODE]]  # value = {'Manual': <SAFETY_MODE.Manual: 0>, 'Autonomous': <SAFETY_MODE.Autonomous: 1>, 'Recovery': <SAFETY_MODE.Recovery: 2>, 'Backdrive': <SAFETY_MODE.Backdrive: 3>, 'Measure': <SAFETY_MODE.Measure: 4>, 'Initialize': <SAFETY_MODE.Initialize: 5>, 'Last': <SAFETY_MODE.Last: 6>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class SAFETY_MODE_EVENT:
    """
    Members:
    
      Enter
    
      Move
    
      Stop
    
      Last
    """
    Enter: typing.ClassVar[SAFETY_MODE_EVENT]  # value = <SAFETY_MODE_EVENT.Enter: 0>
    Last: typing.ClassVar[SAFETY_MODE_EVENT]  # value = <SAFETY_MODE_EVENT.Last: 3>
    Move: typing.ClassVar[SAFETY_MODE_EVENT]  # value = <SAFETY_MODE_EVENT.Move: 1>
    Stop: typing.ClassVar[SAFETY_MODE_EVENT]  # value = <SAFETY_MODE_EVENT.Stop: 2>
    __members__: typing.ClassVar[dict[str, SAFETY_MODE_EVENT]]  # value = {'Enter': <SAFETY_MODE_EVENT.Enter: 0>, 'Move': <SAFETY_MODE_EVENT.Move: 1>, 'Stop': <SAFETY_MODE_EVENT.Stop: 2>, 'Last': <SAFETY_MODE_EVENT.Last: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class SAFETY_OBJECT:
    _tObject: SAFETY_OBJECT_DATA
    def __init__(self) -> None:
        ...
    @property
    def _iObjectType(self) -> int:
        ...
    @_iObjectType.setter
    def _iObjectType(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iTargetRef(self) -> int:
        ...
    @_iTargetRef.setter
    def _iTargetRef(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class SAFETY_OBJECT_CAPSULE:
    _tTargetPos: list
    def __init__(self) -> None:
        ...
    @property
    def _fRadius(self) -> float:
        ...
    @_fRadius.setter
    def _fRadius(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class SAFETY_OBJECT_CUBE:
    _tTargetPos: list
    def __init__(self) -> None:
        ...
class SAFETY_OBJECT_DATA:
    def __init__(self) -> None:
        ...
    @property
    def _iBuffer(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iBuffer.setter
    def _iBuffer(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class SAFETY_OBJECT_OBB:
    _tTargetPos: list
    def __init__(self) -> None:
        ...
class SAFETY_OBJECT_POLYPRISM:
    _tPoint: list
    def __init__(self) -> None:
        ...
    @property
    def _fZLoLimit(self) -> float:
        ...
    @_fZLoLimit.setter
    def _fZLoLimit(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fZUpLimit(self) -> float:
        ...
    @_fZUpLimit.setter
    def _fZUpLimit(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _iPointCount(self) -> int:
        ...
    @_iPointCount.setter
    def _iPointCount(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class SAFETY_OBJECT_SPHERE:
    _tTargetPos: POINT_3D
    def __init__(self) -> None:
        ...
    @property
    def _fRadius(self) -> float:
        ...
    @_fRadius.setter
    def _fRadius(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class SAFETY_STATE:
    """
    Members:
    
      BP_start
    
      BP_init
    
      VD_STO
    
      VD_SOS
    
      JH_SOS
    
      JH_MOVE
    
      HG_MOVE
    
      RV_SOS
    
      RV_MOVE
    
      RV_BACK
    
      RV_HG_MOVE
    
      SW_SOS
    
      SW_RUN
    
      CW_SOS
    
      CW_RUN
    
      CM_RUN
    
      AM_RUN
    
      DRL_JH_SOS
    
      DRL_HG_MOVE
    
      Last
    """
    AM_RUN: typing.ClassVar[SAFETY_STATE]  # value = <SAFETY_STATE.AM_RUN: 16>
    BP_init: typing.ClassVar[SAFETY_STATE]  # value = <SAFETY_STATE.BP_init: 1>
    BP_start: typing.ClassVar[SAFETY_STATE]  # value = <SAFETY_STATE.BP_start: 0>
    CM_RUN: typing.ClassVar[SAFETY_STATE]  # value = <SAFETY_STATE.CM_RUN: 15>
    CW_RUN: typing.ClassVar[SAFETY_STATE]  # value = <SAFETY_STATE.CW_RUN: 14>
    CW_SOS: typing.ClassVar[SAFETY_STATE]  # value = <SAFETY_STATE.CW_SOS: 13>
    DRL_HG_MOVE: typing.ClassVar[SAFETY_STATE]  # value = <SAFETY_STATE.DRL_HG_MOVE: 18>
    DRL_JH_SOS: typing.ClassVar[SAFETY_STATE]  # value = <SAFETY_STATE.DRL_JH_SOS: 17>
    HG_MOVE: typing.ClassVar[SAFETY_STATE]  # value = <SAFETY_STATE.HG_MOVE: 6>
    JH_MOVE: typing.ClassVar[SAFETY_STATE]  # value = <SAFETY_STATE.JH_MOVE: 5>
    JH_SOS: typing.ClassVar[SAFETY_STATE]  # value = <SAFETY_STATE.JH_SOS: 4>
    Last: typing.ClassVar[SAFETY_STATE]  # value = <SAFETY_STATE.Last: 19>
    RV_BACK: typing.ClassVar[SAFETY_STATE]  # value = <SAFETY_STATE.RV_BACK: 9>
    RV_HG_MOVE: typing.ClassVar[SAFETY_STATE]  # value = <SAFETY_STATE.RV_HG_MOVE: 10>
    RV_MOVE: typing.ClassVar[SAFETY_STATE]  # value = <SAFETY_STATE.RV_MOVE: 8>
    RV_SOS: typing.ClassVar[SAFETY_STATE]  # value = <SAFETY_STATE.RV_SOS: 7>
    SW_RUN: typing.ClassVar[SAFETY_STATE]  # value = <SAFETY_STATE.SW_RUN: 12>
    SW_SOS: typing.ClassVar[SAFETY_STATE]  # value = <SAFETY_STATE.SW_SOS: 11>
    VD_SOS: typing.ClassVar[SAFETY_STATE]  # value = <SAFETY_STATE.VD_SOS: 3>
    VD_STO: typing.ClassVar[SAFETY_STATE]  # value = <SAFETY_STATE.VD_STO: 2>
    __members__: typing.ClassVar[dict[str, SAFETY_STATE]]  # value = {'BP_start': <SAFETY_STATE.BP_start: 0>, 'BP_init': <SAFETY_STATE.BP_init: 1>, 'VD_STO': <SAFETY_STATE.VD_STO: 2>, 'VD_SOS': <SAFETY_STATE.VD_SOS: 3>, 'JH_SOS': <SAFETY_STATE.JH_SOS: 4>, 'JH_MOVE': <SAFETY_STATE.JH_MOVE: 5>, 'HG_MOVE': <SAFETY_STATE.HG_MOVE: 6>, 'RV_SOS': <SAFETY_STATE.RV_SOS: 7>, 'RV_MOVE': <SAFETY_STATE.RV_MOVE: 8>, 'RV_BACK': <SAFETY_STATE.RV_BACK: 9>, 'RV_HG_MOVE': <SAFETY_STATE.RV_HG_MOVE: 10>, 'SW_SOS': <SAFETY_STATE.SW_SOS: 11>, 'SW_RUN': <SAFETY_STATE.SW_RUN: 12>, 'CW_SOS': <SAFETY_STATE.CW_SOS: 13>, 'CW_RUN': <SAFETY_STATE.CW_RUN: 14>, 'CM_RUN': <SAFETY_STATE.CM_RUN: 15>, 'AM_RUN': <SAFETY_STATE.AM_RUN: 16>, 'DRL_JH_SOS': <SAFETY_STATE.DRL_JH_SOS: 17>, 'DRL_HG_MOVE': <SAFETY_STATE.DRL_HG_MOVE: 18>, 'Last': <SAFETY_STATE.Last: 19>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class SAFETY_TOOL_ORIENTATION_LIMIT:
    _tTargetDir: POINT_3D
    def __init__(self) -> None:
        ...
    @property
    def _fTargetAng(self) -> float:
        ...
    @_fTargetAng.setter
    def _fTargetAng(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class SAFETY_ZONE_PROPERTY_DATA:
    _tLocalZone: SAFETY_ZONE_PROPERTY_LOCAL_ZONE
    _tSpaceLimitZone: SAFETY_ZONE_PROPERTY_SPACE_LIMIT
    def __init__(self) -> None:
        ...
class SAFETY_ZONE_PROPERTY_LOCAL_ZONE:
    _tCollisionOverride: _LOCAL_ZONE_PROPERTY_COLLISION
    _tCollisionViolationStopmodeOverride: LOCAL_ZONE_PROPERTY_COLLISION_STOPMODE
    _tForceViolationStopmodeOverride: LOCAL_ZONE_PROPERTY_TCPSLF_STOPMODE
    _tJointRangeOverride: LOCAL_ZONE_PROPERTY_JOINT_RANGE
    _tJointSpeedOverride: LOCAL_ZONE_PROPERTY_JOINT_SPEED
    _tSpeedRate: _LOCAL_ZONE_PROPERTY_SPEED_RATE
    _tTcpForceOverride: _LOCAL_ZONE_PROPERTY_TCP_FORCE
    _tTcpMomentumOverride: _LOCAL_ZONE_PROPERTY_TCP_MOMENTUM
    _tTcpPowerOverride: _LOCAL_ZONE_PROPERTY_TCP_POWER
    _tTcpSpeedOverride: _LOCAL_ZONE_PROPERTY_TCP_SPEED
    _tToolOrientationLimitOverride: LOCAL_ZONE_PROPERTY_TOOL_ORIENTATION
    def __init__(self) -> None:
        ...
    @property
    def _bCollaborativeZone(self) -> int:
        ...
    @_bCollaborativeZone.setter
    def _bCollaborativeZone(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iAllowLessSafeWork(self) -> int:
        ...
    @_iAllowLessSafeWork.setter
    def _iAllowLessSafeWork(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iDynamicZoneEnable(self) -> int:
        ...
    @_iDynamicZoneEnable.setter
    def _iDynamicZoneEnable(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iInsideZoneDectection(self) -> int:
        ...
    @_iInsideZoneDectection.setter
    def _iInsideZoneDectection(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iLedOverride(self) -> int:
        ...
    @_iLedOverride.setter
    def _iLedOverride(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iNundgeEanble(self) -> int:
        ...
    @_iNundgeEanble.setter
    def _iNundgeEanble(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iOverrideReduce(self) -> int:
        ...
    @_iOverrideReduce.setter
    def _iOverrideReduce(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class SAFETY_ZONE_PROPERTY_SPACE_LIMIT:
    _tJointRangeOverride: LOCAL_ZONE_PROPERTY_JOINT_RANGE
    def __init__(self) -> None:
        ...
    @property
    def _iDynamicZoneEnable(self) -> int:
        ...
    @_iDynamicZoneEnable.setter
    def _iDynamicZoneEnable(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iInsideZoneDectection(self) -> int:
        ...
    @_iInsideZoneDectection.setter
    def _iInsideZoneDectection(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iInspectionType(self) -> int:
        ...
    @_iInspectionType.setter
    def _iInspectionType(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class SAFETY_ZONE_SHAPE:
    _tShapeData: SAFETY_ZONE_SHAPE_DATA
    def __init__(self) -> None:
        ...
    @property
    def _fMargin(self) -> float:
        ...
    @_fMargin.setter
    def _fMargin(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _iCoordinate(self) -> int:
        ...
    @_iCoordinate.setter
    def _iCoordinate(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iShapeType(self) -> int:
        ...
    @_iShapeType.setter
    def _iShapeType(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iValidSpace(self) -> int:
        ...
    @_iValidSpace.setter
    def _iValidSpace(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class SAFETY_ZONE_SHAPE_CAPSULE:
    _tCenter1: POINT_3D
    _tCenter2: POINT_3D
    def __init__(self) -> None:
        ...
    @property
    def _fRadius(self) -> float:
        ...
    @_fRadius.setter
    def _fRadius(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class SAFETY_ZONE_SHAPE_CUBOID:
    def __init__(self) -> None:
        ...
    @property
    def _fXLoLimit(self) -> float:
        ...
    @_fXLoLimit.setter
    def _fXLoLimit(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fXUpLimit(self) -> float:
        ...
    @_fXUpLimit.setter
    def _fXUpLimit(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fYLoLimit(self) -> float:
        ...
    @_fYLoLimit.setter
    def _fYLoLimit(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fYUpLimit(self) -> float:
        ...
    @_fYUpLimit.setter
    def _fYUpLimit(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fZLoLimit(self) -> float:
        ...
    @_fZLoLimit.setter
    def _fZLoLimit(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fZUpLimit(self) -> float:
        ...
    @_fZUpLimit.setter
    def _fZUpLimit(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class SAFETY_ZONE_SHAPE_CYLINDER:
    _tCenter: POINT_2D
    def __init__(self) -> None:
        ...
    @property
    def _fRadius(self) -> float:
        ...
    @_fRadius.setter
    def _fRadius(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fZLoLimit(self) -> float:
        ...
    @_fZLoLimit.setter
    def _fZLoLimit(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fZUpLimit(self) -> float:
        ...
    @_fZUpLimit.setter
    def _fZUpLimit(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class SAFETY_ZONE_SHAPE_DATA:
    def __init__(self) -> None:
        ...
    @property
    def _iBuffer(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iBuffer.setter
    def _iBuffer(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class SAFETY_ZONE_SHAPE_SPHERE:
    _tCenter: POINT_3D
    def __init__(self) -> None:
        ...
    @property
    def _fRadius(self) -> float:
        ...
    @_fRadius.setter
    def _fRadius(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class SAFETY_ZONE_SHAPE_TILTED_CUBOID:
    _tOrigin: POINT_3D
    _tUAxisEnd: POINT_3D
    _tVAxisEnd: POINT_3D
    _tWAxisEnd: POINT_3D
    def __init__(self) -> None:
        ...
class SAFE_STOP_RESET_TYPE:
    """
    Members:
    
      Default
    
      Stop
    
      Resume
    """
    Default: typing.ClassVar[SAFE_STOP_RESET_TYPE]  # value = <SAFE_STOP_RESET_TYPE.Default: 0>
    Resume: typing.ClassVar[SAFE_STOP_RESET_TYPE]  # value = <SAFE_STOP_RESET_TYPE.Resume: 1>
    Stop: typing.ClassVar[SAFE_STOP_RESET_TYPE]  # value = <SAFE_STOP_RESET_TYPE.Default: 0>
    __members__: typing.ClassVar[dict[str, SAFE_STOP_RESET_TYPE]]  # value = {'Default': <SAFE_STOP_RESET_TYPE.Default: 0>, 'Stop': <SAFE_STOP_RESET_TYPE.Default: 0>, 'Resume': <SAFE_STOP_RESET_TYPE.Resume: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class SERIAL_PORT_NAME:
    _szName: str
    _szPort: str
    def __init__(self) -> None:
        ...
class SERIAL_SEARCH:
    _tSerial: list
    def __init__(self) -> None:
        ...
    @property
    def _nCount(self) -> int:
        ...
    @_nCount.setter
    def _nCount(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class SINGULARITY_AVOIDANCE:
    """
    Members:
    
      Avoid
    
      Stop
    
      Vel
    """
    Avoid: typing.ClassVar[SINGULARITY_AVOIDANCE]  # value = <SINGULARITY_AVOIDANCE.Avoid: 0>
    Stop: typing.ClassVar[SINGULARITY_AVOIDANCE]  # value = <SINGULARITY_AVOIDANCE.Stop: 1>
    Vel: typing.ClassVar[SINGULARITY_AVOIDANCE]  # value = <SINGULARITY_AVOIDANCE.Vel: 2>
    __members__: typing.ClassVar[dict[str, SINGULARITY_AVOIDANCE]]  # value = {'Avoid': <SINGULARITY_AVOIDANCE.Avoid: 0>, 'Stop': <SINGULARITY_AVOIDANCE.Stop: 1>, 'Vel': <SINGULARITY_AVOIDANCE.Vel: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class SPIRAL_DIR:
    """
    Members:
    
      Outward
    
      Inward
    """
    Inward: typing.ClassVar[SPIRAL_DIR]  # value = <SPIRAL_DIR.Inward: 1>
    Outward: typing.ClassVar[SPIRAL_DIR]  # value = <SPIRAL_DIR.Outward: 0>
    __members__: typing.ClassVar[dict[str, SPIRAL_DIR]]  # value = {'Outward': <SPIRAL_DIR.Outward: 0>, 'Inward': <SPIRAL_DIR.Inward: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class SPLINE_VELOCITY_OPTION:
    """
    Members:
    
      Default
    
      Const
    """
    Const: typing.ClassVar[SPLINE_VELOCITY_OPTION]  # value = <SPLINE_VELOCITY_OPTION.Const: 1>
    Default: typing.ClassVar[SPLINE_VELOCITY_OPTION]  # value = <SPLINE_VELOCITY_OPTION.Default: 0>
    __members__: typing.ClassVar[dict[str, SPLINE_VELOCITY_OPTION]]  # value = {'Default': <SPLINE_VELOCITY_OPTION.Default: 0>, 'Const': <SPLINE_VELOCITY_OPTION.Const: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class STOP_BITS:
    """
    Members:
    
      One
    
      Two
    """
    One: typing.ClassVar[STOP_BITS]  # value = <STOP_BITS.One: 1>
    Two: typing.ClassVar[STOP_BITS]  # value = <STOP_BITS.Two: 2>
    __members__: typing.ClassVar[dict[str, STOP_BITS]]  # value = {'One': <STOP_BITS.One: 1>, 'Two': <STOP_BITS.Two: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class STOP_TYPE:
    """
    Members:
    
      Quick_STO
    
      Quick
    
      Slow
    
      Hold
    
      Emergency
    """
    Emergency: typing.ClassVar[STOP_TYPE]  # value = <STOP_TYPE.Hold: 3>
    Hold: typing.ClassVar[STOP_TYPE]  # value = <STOP_TYPE.Hold: 3>
    Quick: typing.ClassVar[STOP_TYPE]  # value = <STOP_TYPE.Quick: 1>
    Quick_STO: typing.ClassVar[STOP_TYPE]  # value = <STOP_TYPE.Quick_STO: 0>
    Slow: typing.ClassVar[STOP_TYPE]  # value = <STOP_TYPE.Slow: 2>
    __members__: typing.ClassVar[dict[str, STOP_TYPE]]  # value = {'Quick_STO': <STOP_TYPE.Quick_STO: 0>, 'Quick': <STOP_TYPE.Quick: 1>, 'Slow': <STOP_TYPE.Slow: 2>, 'Hold': <STOP_TYPE.Hold: 3>, 'Emergency': <STOP_TYPE.Hold: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class SUB_PROGRAM:
    """
    Members:
    
      Delete
    
      Save
    """
    Delete: typing.ClassVar[SUB_PROGRAM]  # value = <SUB_PROGRAM.Delete: 0>
    Save: typing.ClassVar[SUB_PROGRAM]  # value = <SUB_PROGRAM.Save: 1>
    __members__: typing.ClassVar[dict[str, SUB_PROGRAM]]  # value = {'Delete': <SUB_PROGRAM.Delete: 0>, 'Save': <SUB_PROGRAM.Save: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class SYSTEM_CPUUSAGE:
    def __init__(self) -> None:
        ...
    @property
    def _iProcessUsage(self) -> float:
        ...
    @_iProcessUsage.setter
    def _iProcessUsage(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _iTotalUsage(self) -> float:
        ...
    @_iTotalUsage.setter
    def _iTotalUsage(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class SYSTEM_DISKSIZE:
    def __init__(self) -> None:
        ...
    @property
    def _iTotalDiskSize(self) -> int:
        ...
    @_iTotalDiskSize.setter
    def _iTotalDiskSize(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iUsedDiskSize(self) -> int:
        ...
    @_iUsedDiskSize.setter
    def _iUsedDiskSize(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class SYSTEM_IPADDRESS:
    _szDNS: list
    _szGateway: str
    _szHotsIp: str
    _szSubnet: str
    def __init__(self) -> None:
        ...
    @property
    def _iIpType(self) -> int:
        ...
    @_iIpType.setter
    def _iIpType(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iUsage(self) -> int:
        ...
    @_iUsage.setter
    def _iUsage(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class SYSTEM_POWER:
    def __init__(self) -> None:
        ...
    @property
    def _iPower(self) -> int:
        ...
    @_iPower.setter
    def _iPower(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iTarget(self) -> int:
        ...
    @_iTarget.setter
    def _iTarget(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class SYSTEM_TIME:
    _szDate: str
    _szTime: str
    def __init__(self) -> None:
        ...
class SYSTEM_UPDATE_RESPONSE:
    def __init__(self) -> None:
        ...
    @property
    def _iInverter(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iInverter.setter
    def _iInverter(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iProcess(self) -> int:
        ...
    @_iProcess.setter
    def _iProcess(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class SYSTEM_VERSION:
    _szController: str
    _szFlangeBoard: str
    _szInterpreter: str
    _szInverter: str
    _szJTSBoard: str
    _szRobotModel: str
    _szRobotSerial: str
    _szSafetyBoard: str
    _szSmartTp: str
    def __init__(self) -> None:
        ...
class TASK_AXIS:
    """
    Members:
    
      Axis_X
    
      Axis_Y
    
      Axis_Z
    """
    Axis_X: typing.ClassVar[TASK_AXIS]  # value = <TASK_AXIS.Axis_X: 0>
    Axis_Y: typing.ClassVar[TASK_AXIS]  # value = <TASK_AXIS.Axis_Y: 1>
    Axis_Z: typing.ClassVar[TASK_AXIS]  # value = <TASK_AXIS.Axis_Z: 2>
    __members__: typing.ClassVar[dict[str, TASK_AXIS]]  # value = {'Axis_X': <TASK_AXIS.Axis_X: 0>, 'Axis_Y': <TASK_AXIS.Axis_Y: 1>, 'Axis_Z': <TASK_AXIS.Axis_Z: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class UPDATE_MODBUS_MULTI_REGISTER:
    _szSymbol: str
    def __init__(self) -> None:
        ...
    @property
    def _iRegCount(self) -> int:
        ...
    @_iRegCount.setter
    def _iRegCount(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iRegValue(self) -> numpy.typing.NDArray[numpy.uint16]:
        ...
    @_iRegValue.setter
    def _iRegValue(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint16]) -> None:
        ...
class USER_COORDINATE:
    def __init__(self) -> None:
        ...
    @property
    def _fTargetPos(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTargetPos.setter
    def _fTargetPos(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iReqId(self) -> int:
        ...
    @_iReqId.setter
    def _iReqId(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iTargetRef(self) -> int:
        ...
    @_iTargetRef.setter
    def _iTargetRef(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class USER_COORDINATE_MATRIX_RESPONSE:
    def __init__(self) -> None:
        ...
    @property
    def _fOrientXYZ(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fOrientXYZ.setter
    def _fOrientXYZ(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _fTranslXYZ(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTranslXYZ.setter
    def _fTranslXYZ(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
class USER_COORD_EXTERNAL_FORCE:
    def __init__(self) -> None:
        ...
    @property
    def _fExternalForce(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fExternalForce.setter
    def _fExternalForce(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _iUserId(self) -> int:
        ...
    @_iUserId.setter
    def _iUserId(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class USER_COORD_EXTERNAL_FORCE_INFO:
    def __init__(self) -> None:
        ...
    @property
    def bIsMonitoring(self) -> int:
        ...
    @bIsMonitoring.setter
    def bIsMonitoring(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def iUserID(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @iUserID.setter
    def iUserID(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class VARIABLE_TYPE:
    """
    Members:
    
      Install
    
      Global
    """
    Global: typing.ClassVar[VARIABLE_TYPE]  # value = <VARIABLE_TYPE.Global: 1>
    Install: typing.ClassVar[VARIABLE_TYPE]  # value = <VARIABLE_TYPE.Install: 0>
    __members__: typing.ClassVar[dict[str, VARIABLE_TYPE]]  # value = {'Install': <VARIABLE_TYPE.Install: 0>, 'Global': <VARIABLE_TYPE.Global: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class VECTOR3D:
    def __init__(self) -> None:
        ...
    @property
    def _fTargetPos(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_fTargetPos.setter
    def _fTargetPos(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
class VIRTUAL_FENCE_RESPONSE:
    def __init__(self) -> None:
        ...
    @property
    def _iCubeResult(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iCubeResult.setter
    def _iCubeResult(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
    @property
    def _iCylinderResult(self) -> int:
        ...
    @_iCylinderResult.setter
    def _iCylinderResult(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iPolyResult(self) -> numpy.typing.NDArray[numpy.uint8]:
        ...
    @_iPolyResult.setter
    def _iPolyResult(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None:
        ...
class WEAVING_OFFSET:
    def __init__(self) -> None:
        ...
    @property
    def _fOffsetY(self) -> float:
        ...
    @_fOffsetY.setter
    def _fOffsetY(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fOffsetZ(self) -> float:
        ...
    @_fOffsetZ.setter
    def _fOffsetZ(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class WELDING_CHANNEL:
    def __init__(self) -> None:
        ...
    @property
    def _ConstValue(self) -> numpy.typing.NDArray[numpy.float32]:
        ...
    @_ConstValue.setter
    def _ConstValue(self, arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> None:
        ...
    @property
    def _bTargetAT(self) -> int:
        ...
    @_bTargetAT.setter
    def _bTargetAT(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _bTargetCh(self) -> int:
        ...
    @_bTargetCh.setter
    def _bTargetCh(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _fMaxValue(self) -> float:
        ...
    @_fMaxValue.setter
    def _fMaxValue(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def _fMinValue(self) -> float:
        ...
    @_fMinValue.setter
    def _fMinValue(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class WRITE_MODBUS_BURST:
    _tRegister: list
    def __init__(self) -> None:
        ...
    @property
    def _iCount(self) -> int:
        ...
    @_iCount.setter
    def _iCount(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class WRITE_MODBUS_DATA:
    _szIpAddr: str
    _szSymbol: str
    def __init__(self) -> None:
        ...
    @property
    def _iPort(self) -> int:
        ...
    @_iPort.setter
    def _iPort(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iRegIndex(self) -> int:
        ...
    @_iRegIndex.setter
    def _iRegIndex(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iRegType(self) -> int:
        ...
    @_iRegType.setter
    def _iRegType(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iRegValue(self) -> int:
        ...
    @_iRegValue.setter
    def _iRegValue(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iSlaveID(self) -> int:
        ...
    @_iSlaveID.setter
    def _iSlaveID(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class WRITE_MODBUS_RTU_DATA:
    _szParity: str
    _szSymbol: str
    _szttyPort: str
    def __init__(self) -> None:
        ...
    @property
    def _iBaudRate(self) -> int:
        ...
    @_iBaudRate.setter
    def _iBaudRate(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iByteSize(self) -> int:
        ...
    @_iByteSize.setter
    def _iByteSize(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iRegIndex(self) -> int:
        ...
    @_iRegIndex.setter
    def _iRegIndex(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iRegType(self) -> int:
        ...
    @_iRegType.setter
    def _iRegType(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iRegValue(self) -> int:
        ...
    @_iRegValue.setter
    def _iRegValue(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iSlaveID(self) -> int:
        ...
    @_iSlaveID.setter
    def _iSlaveID(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iStopBit(self) -> int:
        ...
    @_iStopBit.setter
    def _iStopBit(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class WRITE_SERIAL_BURST:
    _tPort: list
    def __init__(self) -> None:
        ...
    @property
    def _iCount(self) -> int:
        ...
    @_iCount.setter
    def _iCount(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def _iLocation(self) -> int:
        ...
    @_iLocation.setter
    def _iLocation(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
AM_RUN: SAFETY_STATE  # value = <SAFETY_STATE.AM_RUN: 16>
Absolute: FORCE_MODE  # value = <FORCE_MODE.Absolute: 0>
Add: ADD_UP  # value = <ADD_UP.Add: 1>
Alarm: MESSAGE_LEVEL  # value = <MESSAGE_LEVEL.Alarm: 2>
Autonomous: SAFETY_MODE  # value = <SAFETY_MODE.Autonomous: 1>
Avoid: SINGULARITY_AVOIDANCE  # value = <SINGULARITY_AVOIDANCE.Avoid: 0>
Axis_1: JOINT_AXIS  # value = <JOINT_AXIS.Axis_1: 0>
Axis_2: JOINT_AXIS  # value = <JOINT_AXIS.Axis_2: 1>
Axis_3: JOINT_AXIS  # value = <JOINT_AXIS.Axis_3: 2>
Axis_4: JOINT_AXIS  # value = <JOINT_AXIS.Axis_4: 3>
Axis_5: JOINT_AXIS  # value = <JOINT_AXIS.Axis_5: 4>
Axis_6: JOINT_AXIS  # value = <JOINT_AXIS.Axis_6: 5>
Axis_A: FORCE_AXIS  # value = <FORCE_AXIS.Axis_A: 10>
Axis_B: FORCE_AXIS  # value = <FORCE_AXIS.Axis_B: 11>
Axis_C: FORCE_AXIS  # value = <FORCE_AXIS.Axis_C: 12>
Axis_X: FORCE_AXIS  # value = <FORCE_AXIS.Axis_X: 0>
Axis_Y: FORCE_AXIS  # value = <FORCE_AXIS.Axis_Y: 1>
Axis_Z: FORCE_AXIS  # value = <FORCE_AXIS.Axis_Z: 2>
BP_init: SAFETY_STATE  # value = <SAFETY_STATE.BP_init: 1>
BP_start: SAFETY_STATE  # value = <SAFETY_STATE.BP_start: 0>
Backdrive: SAFETY_MODE  # value = <SAFETY_MODE.Backdrive: 3>
Base: MOVE_REFERENCE  # value = <MOVE_REFERENCE.Base: 0>
Bool: DATA_TYPE  # value = <DATA_TYPE.Bool: 0>
CM_RUN: SAFETY_STATE  # value = <SAFETY_STATE.CM_RUN: 15>
CW_RUN: SAFETY_STATE  # value = <SAFETY_STATE.CW_RUN: 14>
CW_SOS: SAFETY_STATE  # value = <SAFETY_STATE.CW_SOS: 13>
Circle: MOVEB_BLENDING_TYPE  # value = <MOVEB_BLENDING_TYPE.Circle: 1>
Coils: MODBUS_REGISTER_TYPE  # value = <MODBUS_REGISTER_TYPE.Coils: 1>
Const: SPLINE_VELOCITY_OPTION  # value = <SPLINE_VELOCITY_OPTION.Const: 1>
Coordinate_system_base: COORDINATE_SYSTEM  # value = <COORDINATE_SYSTEM.Coordinate_system_base: 0>
Coordinate_system_tool: COORDINATE_SYSTEM  # value = <COORDINATE_SYSTEM.Coordinate_system_tool: 1>
Coordinate_system_user_max: COORDINATE_SYSTEM  # value = <COORDINATE_SYSTEM.Coordinate_system_user_max: 200>
Coordinate_system_user_min: COORDINATE_SYSTEM  # value = <COORDINATE_SYSTEM.Coordinate_system_user_min: 101>
Coordinate_system_world: COORDINATE_SYSTEM  # value = <COORDINATE_SYSTEM.Coordinate_system_world: 2>
Current: GPIO_ANALOG_TYPE  # value = <GPIO_ANALOG_TYPE.Current: 0>
DPOS: PATH_MODE  # value = <PATH_MODE.DPOS: 0>
DRL_HG_MOVE: SAFETY_STATE  # value = <SAFETY_STATE.DRL_HG_MOVE: 18>
DRL_JH_SOS: SAFETY_STATE  # value = <SAFETY_STATE.DRL_JH_SOS: 17>
DVEL: PATH_MODE  # value = <PATH_MODE.DVEL: 1>
Default: SPLINE_VELOCITY_OPTION  # value = <SPLINE_VELOCITY_OPTION.Default: 0>
Delete: SUB_PROGRAM  # value = <SUB_PROGRAM.Delete: 0>
Deny: MONITORING_ACCESS_CONTROL  # value = <MONITORING_ACCESS_CONTROL.Deny: 1>
Discrete_inputs: MODBUS_REGISTER_TYPE  # value = <MODBUS_REGISTER_TYPE.Discrete_inputs: 0>
Duplicate: BLENDING_SPEED_TYPE  # value = <BLENDING_SPEED_TYPE.Duplicate: 0>
EightBites: BYTE_SIZE  # value = <BYTE_SIZE.EightBites: 8>
Emergency: STOP_TYPE  # value = <STOP_TYPE.Hold: 3>
Emergency_stop: ROBOT_STATE  # value = <ROBOT_STATE.Emergency_stop: 6>
Enter: SAFETY_MODE_EVENT  # value = <SAFETY_MODE_EVENT.Enter: 0>
Error: PROGRAM_STOP_CAUSE  # value = <PROGRAM_STOP_CAUSE.Error: 2>
FiveBites: BYTE_SIZE  # value = <BYTE_SIZE.FiveBites: 5>
Fixed: MOVE_ORIENTATION  # value = <MOVE_ORIENTATION.Fixed: 1>
Flange: COG_REFERENCE  # value = <COG_REFERENCE.Flange: 1>
Float: DATA_TYPE  # value = <DATA_TYPE.Float: 2>
Force: PROGRAM_STOP_CAUSE  # value = <PROGRAM_STOP_CAUSE.Force: 1>
Force_request: MANAGE_ACCESS_CONTROL  # value = <MANAGE_ACCESS_CONTROL.Force_request: 0>
Forward: ROT_DIR  # value = <ROT_DIR.Forward: 0>
Global: VARIABLE_TYPE  # value = <VARIABLE_TYPE.Global: 1>
Grant: MONITORING_ACCESS_CONTROL  # value = <MONITORING_ACCESS_CONTROL.Grant: 2>
HG_MOVE: SAFETY_STATE  # value = <SAFETY_STATE.HG_MOVE: 6>
Hold: DRL_PROGRAM_STATE  # value = <DRL_PROGRAM_STATE.Hold: 2>
Holding_register: MODBUS_REGISTER_TYPE  # value = <MODBUS_REGISTER_TYPE.Holding_register: 3>
Homming: ROBOT_STATE  # value = <ROBOT_STATE.Homming: 7>
Index_1: GPIO_TOOL_DIGITAL_INDEX  # value = <GPIO_TOOL_DIGITAL_INDEX.Index_1: 0>
Index_10: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_10: 9>
Index_11: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_11: 10>
Index_12: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_12: 11>
Index_13: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_13: 12>
Index_14: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_14: 13>
Index_15: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_15: 14>
Index_16: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_16: 15>
Index_17: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_17: 16>
Index_18: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_18: 17>
Index_19: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_19: 18>
Index_2: GPIO_TOOL_DIGITAL_INDEX  # value = <GPIO_TOOL_DIGITAL_INDEX.Index_2: 1>
Index_20: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_20: 19>
Index_21: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_21: 20>
Index_22: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_22: 21>
Index_23: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_23: 22>
Index_24: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_24: 23>
Index_25: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_25: 24>
Index_26: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_26: 25>
Index_27: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_27: 26>
Index_28: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_28: 27>
Index_29: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_29: 28>
Index_3: GPIO_TOOL_DIGITAL_INDEX  # value = <GPIO_TOOL_DIGITAL_INDEX.Index_3: 2>
Index_30: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_30: 29>
Index_31: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_31: 30>
Index_32: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_32: 31>
Index_4: GPIO_TOOL_DIGITAL_INDEX  # value = <GPIO_TOOL_DIGITAL_INDEX.Index_4: 3>
Index_5: GPIO_TOOL_DIGITAL_INDEX  # value = <GPIO_TOOL_DIGITAL_INDEX.Index_5: 4>
Index_6: GPIO_TOOL_DIGITAL_INDEX  # value = <GPIO_TOOL_DIGITAL_INDEX.Index_6: 5>
Index_7: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_7: 6>
Index_8: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_8: 7>
Index_9: GPIO_CTRLBOX_DIGITAL_INDEX  # value = <GPIO_CTRLBOX_DIGITAL_INDEX.Index_9: 8>
Info: MESSAGE_LEVEL  # value = <MESSAGE_LEVEL.Info: 0>
Init_config: ROBOT_CONTROL  # value = <ROBOT_CONTROL.Init_config: 0>
Initialize: SAFETY_MODE  # value = <SAFETY_MODE.Initialize: 5>
Initializing: ROBOT_STATE  # value = <ROBOT_STATE.Initializing: 0>
Input_register: MODBUS_REGISTER_TYPE  # value = <MODBUS_REGISTER_TYPE.Input_register: 2>
Install: VARIABLE_TYPE  # value = <VARIABLE_TYPE.Install: 0>
Int: DATA_TYPE  # value = <DATA_TYPE.Int: 1>
Intent: MOVE_ORIENTATION  # value = <MOVE_ORIENTATION.Intent: 3>
Intialize: ROBOT_MODE  # value = <ROBOT_MODE.Intialize: 5>
Inverter: LOG_GROUP  # value = <LOG_GROUP.Inverter: 4>
Inward: SPIRAL_DIR  # value = <SPIRAL_DIR.Inward: 1>
JH_MOVE: SAFETY_STATE  # value = <SAFETY_STATE.JH_MOVE: 5>
JH_SOS: SAFETY_STATE  # value = <SAFETY_STATE.JH_SOS: 4>
Joint: ROBOT_SPACE  # value = <ROBOT_SPACE.Joint: 0>
Joint_1: JOG_AXIS  # value = <JOG_AXIS.Joint_1: 0>
Joint_2: JOG_AXIS  # value = <JOG_AXIS.Joint_2: 1>
Joint_3: JOG_AXIS  # value = <JOG_AXIS.Joint_3: 2>
Joint_4: JOG_AXIS  # value = <JOG_AXIS.Joint_4: 3>
Joint_5: JOG_AXIS  # value = <JOG_AXIS.Joint_5: 4>
Joint_6: JOG_AXIS  # value = <JOG_AXIS.Joint_6: 5>
Last: LOG_GROUP  # value = <LOG_GROUP.Last: 6>
Line: MOVEB_BLENDING_TYPE  # value = <MOVEB_BLENDING_TYPE.Line: 0>
Loss: MONITORING_ACCESS_CONTROL  # value = <MONITORING_ACCESS_CONTROL.Loss: 3>
Manual: SAFETY_MODE  # value = <SAFETY_MODE.Manual: 0>
Measure: SAFETY_MODE  # value = <SAFETY_MODE.Measure: 4>
Mechanic: MOVE_HOME  # value = <MOVE_HOME.Mechanic: 0>
MotionLIB: LOG_GROUP  # value = <LOG_GROUP.MotionLIB: 2>
Move: SAFETY_MODE_EVENT  # value = <SAFETY_MODE_EVENT.Move: 1>
Moving: ROBOT_STATE  # value = <ROBOT_STATE.Moving: 2>
NPN: OUTPUT_TYPE  # value = <OUTPUT_TYPE.NPN: 1>
None: DR_MV_APP  # value = <DR_MV_APP.None: 0>
Normal: PROGRAM_STOP_CAUSE  # value = <PROGRAM_STOP_CAUSE.Normal: 0>
Normal_mode: MONITORING_SPEED  # value = <MONITORING_SPEED.Normal_mode: 0>
Not_ready: ROBOT_STATE  # value = <ROBOT_STATE.Not_ready: 15>
One: STOP_BITS  # value = <STOP_BITS.One: 1>
Operation: ROBOT_CONTROL  # value = <ROBOT_CONTROL.Operation: 1>
Outward: SPIRAL_DIR  # value = <SPIRAL_DIR.Outward: 0>
Override: DR_SERVOJ_TYPE  # value = <DR_SERVOJ_TYPE.Override: 0>
PNP: OUTPUT_TYPE  # value = <OUTPUT_TYPE.PNP: 0>
Play: DRL_PROGRAM_STATE  # value = <DRL_PROGRAM_STATE.Play: 0>
PosJ: DATA_TYPE  # value = <DATA_TYPE.PosJ: 4>
PosX: DATA_TYPE  # value = <DATA_TYPE.PosX: 5>
Queue: DR_SERVOJ_TYPE  # value = <DR_SERVOJ_TYPE.Queue: 1>
Quick: STOP_TYPE  # value = <STOP_TYPE.Quick: 1>
Quick_STO: STOP_TYPE  # value = <STOP_TYPE.Quick_STO: 0>
RV_BACK: SAFETY_STATE  # value = <SAFETY_STATE.RV_BACK: 9>
RV_HG_MOVE: SAFETY_STATE  # value = <SAFETY_STATE.RV_HG_MOVE: 10>
RV_MOVE: SAFETY_STATE  # value = <SAFETY_STATE.RV_MOVE: 8>
RV_SOS: SAFETY_STATE  # value = <SAFETY_STATE.RV_SOS: 7>
Radial: MOVE_ORIENTATION  # value = <MOVE_ORIENTATION.Radial: 2>
Real: ROBOT_SYSTEM  # value = <ROBOT_SYSTEM.Real: 0>
Recovery: SAFETY_MODE  # value = <SAFETY_MODE.Recovery: 2>
Recovery_backdrive: ROBOT_CONTROL  # value = <ROBOT_CONTROL.Recovery_backdrive: 6>
Recovery_safe_off: ROBOT_CONTROL  # value = <ROBOT_CONTROL.Recovery_safe_off: 5>
Recovery_safe_stop: ROBOT_CONTROL  # value = <ROBOT_CONTROL.Recovery_safe_stop: 4>
Reduced_mode: MONITORING_SPEED  # value = <MONITORING_SPEED.Reduced_mode: 1>
Relative: FORCE_MODE  # value = <FORCE_MODE.Relative: 1>
Release: RELEASE_MODE  # value = <RELEASE_MODE.Release: 2>
Remove: ADD_UP  # value = <ADD_UP.Remove: 2>
Replace: ADD_UP  # value = <ADD_UP.Replace: 0>
Request: MONITORING_ACCESS_CONTROL  # value = <MONITORING_ACCESS_CONTROL.Request: 0>
Reserved1: ROBOT_STATE  # value = <ROBOT_STATE.Reserved1: 11>
Reserved2: ROBOT_STATE  # value = <ROBOT_STATE.Reserved2: 12>
Reserved3: ROBOT_STATE  # value = <ROBOT_STATE.Reserved3: 13>
Reserved4: ROBOT_STATE  # value = <ROBOT_STATE.Reserved4: 14>
Reset: RELEASE_MODE  # value = <RELEASE_MODE.Reset: 3>
Reset_recovery: ROBOT_CONTROL  # value = <ROBOT_CONTROL.Reset_recovery: 7>
Reset_safe_off: ROBOT_CONTROL  # value = <ROBOT_CONTROL.Reset_safet_off: 3>
Reset_safe_stop: ROBOT_CONTROL  # value = <ROBOT_CONTROL.Reset_safet_stop: 2>
Reset_safet_off: ROBOT_CONTROL  # value = <ROBOT_CONTROL.Reset_safet_off: 3>
Reset_safet_stop: ROBOT_CONTROL  # value = <ROBOT_CONTROL.Reset_safet_stop: 2>
Response_no: MANAGE_ACCESS_CONTROL  # value = <MANAGE_ACCESS_CONTROL.Response_no: 3>
Response_yes: MANAGE_ACCESS_CONTROL  # value = <MANAGE_ACCESS_CONTROL.Response_yes: 2>
Resume: RELEASE_MODE  # value = <RELEASE_MODE.Resume: 1>
Reverse: ROT_DIR  # value = <ROT_DIR.Reverse: 1>
SW_RUN: SAFETY_STATE  # value = <SAFETY_STATE.SW_RUN: 12>
SW_SOS: SAFETY_STATE  # value = <SAFETY_STATE.SW_SOS: 11>
Safe_off: ROBOT_STATE  # value = <ROBOT_STATE.Safe_off: 3>
Safe_off2: ROBOT_STATE  # value = <ROBOT_STATE.Safe_off2: 10>
Safe_stop: ROBOT_STATE  # value = <ROBOT_STATE.Safe_stop: 5>
Safe_stop2: ROBOT_STATE  # value = <ROBOT_STATE.Safe_stop2: 9>
SafetyController: LOG_GROUP  # value = <LOG_GROUP.SafetyController: 5>
Save: SUB_PROGRAM  # value = <SUB_PROGRAM.Save: 1>
Servo_on: ROBOT_CONTROL  # value = <ROBOT_CONTROL.Reset_safet_off: 3>
SevenBites: BYTE_SIZE  # value = <BYTE_SIZE.SevenBites: 7>
SixBites: BYTE_SIZE  # value = <BYTE_SIZE.SixBites: 6>
Slow: STOP_TYPE  # value = <STOP_TYPE.Slow: 2>
SmartTP: LOG_GROUP  # value = <LOG_GROUP.SmartTP: 3>
Standby: ROBOT_STATE  # value = <ROBOT_STATE.Standby: 1>
Stop: SAFETY_MODE_EVENT  # value = <SAFETY_MODE_EVENT.Stop: 2>
String: DATA_TYPE  # value = <DATA_TYPE.String: 3>
Sys_info: LOG_LEVEL  # value = <LOG_LEVEL.Sys_info: 1>
Sys_last: LOG_LEVEL  # value = <LOG_LEVEL.Sys_last: 4>
Sys_warn: LOG_LEVEL  # value = <LOG_LEVEL.Sys_warn: 2>
SystemFMK: LOG_GROUP  # value = <LOG_GROUP.SystemFMK: 1>
TCP: COG_REFERENCE  # value = <COG_REFERENCE.TCP: 0>
Task: ROBOT_SPACE  # value = <ROBOT_SPACE.Task: 1>
Task_RX: JOG_AXIS  # value = <JOG_AXIS.Task_RX: 9>
Task_RY: JOG_AXIS  # value = <JOG_AXIS.Task_RY: 10>
Task_RZ: JOG_AXIS  # value = <JOG_AXIS.Task_RZ: 11>
Task_X: JOG_AXIS  # value = <JOG_AXIS.Task_X: 6>
Task_Y: JOG_AXIS  # value = <JOG_AXIS.Task_Y: 7>
Task_Z: JOG_AXIS  # value = <JOG_AXIS.Task_Z: 8>
Teach: MOVE_ORIENTATION  # value = <MOVE_ORIENTATION.Teach: 0>
Teaching: ROBOT_STATE  # value = <ROBOT_STATE.Teaching: 4>
Tool: MOVE_REFERENCE  # value = <MOVE_REFERENCE.Tool: 1>
Two: STOP_BITS  # value = <STOP_BITS.Two: 2>
Unknown: DATA_TYPE  # value = <DATA_TYPE.Unknown: 6>
User: MOVE_HOME  # value = <MOVE_HOME.User: 1>
User_max: MOVE_REFERENCE  # value = <MOVE_REFERENCE.User_max: 200>
User_min: MOVE_REFERENCE  # value = <MOVE_REFERENCE.User_min: 101>
VD_SOS: SAFETY_STATE  # value = <SAFETY_STATE.VD_SOS: 3>
VD_STO: SAFETY_STATE  # value = <SAFETY_STATE.VD_STO: 2>
Vel: SINGULARITY_AVOIDANCE  # value = <SINGULARITY_AVOIDANCE.Vel: 2>
Virtual: ROBOT_SYSTEM  # value = <ROBOT_SYSTEM.Virtual: 1>
Voltage: GPIO_ANALOG_TYPE  # value = <GPIO_ANALOG_TYPE.Voltage: 1>
Warn: MESSAGE_LEVEL  # value = <MESSAGE_LEVEL.Warn: 1>
Weld: DR_MV_APP  # value = <DR_MV_APP.Weld: 1>
World: MOVE_REFERENCE  # value = <MOVE_REFERENCE.World: 2>
even: PARITY_CHECK  # value = <PARITY_CHECK.even: 1>
none: PARITY_CHECK  # value = <PARITY_CHECK.none: 0>
odd: PARITY_CHECK  # value = <PARITY_CHECK.odd: 2>
position: CONTROL_MODE  # value = <CONTROL_MODE.position: 3>
torque: CONTROL_MODE  # value = <CONTROL_MODE.torque: 4>
CALIBRATE_FTS_RESPONSE = FTS_PARAM_DATA
CALIBRATE_JTS_RESPONSE = JTS_PARAM_DATA
CONFIG_SAFETY_ZONE = CONFIG_ADD_SAFETY_ZONE
CONFIG_TCP_EX = POSITION_EX
GPIO_SETOUTPUT_BURST = WRITE_SERIAL_BURST
LINE_2D = LINE
MODBUS_REGISTER_BURST = WRITE_MODBUS_BURST
MONITORING_ALARM = LOG_ALARM
MONITORING_AMODEL = ROBOT_MONITORING_AMODEL
MONITORING_CONTROL_EX = ROBOT_MONITORING_DATA_EX
MONITORING_INPUT = MESSAGE_INPUT
MONITORING_POPUP = MESSAGE_POPUP
MONITORING_WELDING = ROBOT_WELDING_DATA
NORMAL_VECTOR_RESPONSE = VECTOR3D
POSITION_ADDTO_RESPONSE = POSITION
SPEED_MODE = MONITORING_SPEED
VECTOR6D = POSITION
WRITE_MODBUS_TCP_DATA = WRITE_MODBUS_DATA
