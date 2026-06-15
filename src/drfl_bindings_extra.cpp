/**
 * Additional bindings for DRFLEx functions:
 *   - Real-time (RT) control subsystem
 *   - Hold-to-Run motion
 *   - Ethernet input/output registers
 *   - Misc motion (Safe_*, *_g, multi_jog, ikin_norm, addto, get_user_home)
 *   - LED control, system shutdown, link info
 *   - SINGULARITY_FORCE_HANDLING enum + helpers
 */

#include "./cdrflex_bindings.hpp"
#include "./drfl_bindings_extra.hpp"

#include <optional>
#include <pybind11/cast.h>
#include <pybind11/functional.h>
#include <pybind11/pytypes.h>
#include <pybind11/stl.h>
#include <stdexcept>
#include <string>

using Class = py::class_<DRAFramework::CDRFLEx>;

// ────────────────────────────────────────────────────────────────────────────
// Small validation helpers (1-D float arrays)
// ────────────────────────────────────────────────────────────────────────────
static float *
check1D(py::array_t<float, py::array::c_style | py::array::forcecast> &arr,
        int expected, const char *name) {
  if (arr.size() != expected)
    throw std::runtime_error(std::string(name) + " must have exactly " +
                             std::to_string(expected) + " elements");
  return const_cast<float *>(arr.data());
}

// ============================================================================
// 1. RT CONTROL
// ============================================================================

void bConnectRtControl(Class &c) {
  c.def(
      "connect_rt_control",
      [](DRAFramework::CDRFLEx &self, std::string ip, unsigned int port) {
        return self.connect_rt_control(ip, port);
      },
      py::arg("ip") = "192.168.137.100", py::arg("port") = 12347,
      "Connect to the real-time UDP control channel");
}

void bDisconnectRtControl(Class &c) {
  c.def("disconnect_rt_control", [](DRAFramework::CDRFLEx &self) {
    return self.disconnect_rt_control();
  });
}

void bGetRtControlOutputVersionList(Class &c) {
  c.def("get_rt_control_output_version_list",
        [](DRAFramework::CDRFLEx &self) {
          return self.get_rt_control_output_version_list();
        });
}

void bGetRtControlInputVersionList(Class &c) {
  c.def("get_rt_control_input_version_list", [](DRAFramework::CDRFLEx &self) {
    return self.get_rt_control_input_version_list();
  });
}

void bGetRtControlInputDataList(Class &c) {
  c.def(
      "get_rt_control_input_data_list",
      [](DRAFramework::CDRFLEx &self, const std::string &version) {
        return self.get_rt_control_input_data_list(version);
      },
      py::arg("version"));
}

void bGetRtControlOutputDataList(Class &c) {
  c.def(
      "get_rt_control_output_data_list",
      [](DRAFramework::CDRFLEx &self, const std::string &version) {
        return self.get_rt_control_output_data_list(version);
      },
      py::arg("version"));
}

void bSetRtControlInput(Class &c) {
  c.def(
      "set_rt_control_input",
      [](DRAFramework::CDRFLEx &self, const std::string &version, float period,
         int lossCnt) {
        return self.set_rt_control_input(version, period, lossCnt);
      },
      py::arg("version"), py::arg("period"), py::arg("loss_count"));
}

void bSetRtControlOutput(Class &c) {
  c.def(
      "set_rt_control_output",
      [](DRAFramework::CDRFLEx &self, const std::string &version, float period,
         int lossCnt) {
        return self.set_rt_control_output(version, period, lossCnt);
      },
      py::arg("version"), py::arg("period"), py::arg("loss_count"));
}

void bStartRtControl(Class &c) {
  c.def("start_rt_control",
        [](DRAFramework::CDRFLEx &self) { return self.start_rt_control(); });
}

void bStopRtControl(Class &c) {
  c.def("stop_rt_control",
        [](DRAFramework::CDRFLEx &self) { return self.stop_rt_control(); });
}

void bSetVeljRt(Class &c) {
  c.def(
      "set_velj_rt",
      [](DRAFramework::CDRFLEx &self, arr_f vel) {
        return self.set_velj_rt(check1D(vel, NUM_JOINT, "vel"));
      },
      py::arg("vel"));
}

void bSetAccjRt(Class &c) {
  c.def(
      "set_accj_rt",
      [](DRAFramework::CDRFLEx &self, arr_f acc) {
        return self.set_accj_rt(check1D(acc, NUM_JOINT, "acc"));
      },
      py::arg("acc"));
}

void bSetVelxRt(Class &c) {
  c.def(
      "set_velx_rt",
      [](DRAFramework::CDRFLEx &self, float transVel, float rotVel) {
        return self.set_velx_rt(transVel, rotVel);
      },
      py::arg("trans_vel"), py::arg("rot_vel") = -10000.f);
}

void bSetAccxRt(Class &c) {
  c.def(
      "set_accx_rt",
      [](DRAFramework::CDRFLEx &self, float transAcc, float rotAcc) {
        return self.set_accx_rt(transAcc, rotAcc);
      },
      py::arg("trans_acc"), py::arg("rot_acc") = -10000.f);
}

void bReadDataRt(Class &c) {
  c.def(
      "read_data_rt",
      [](DRAFramework::CDRFLEx &self) {
        auto *p = self.read_data_rt();
        if (!p)
          throw std::runtime_error("read_data_rt returned null");
        return *p;
      },
      "Read the latest RT_OUTPUT_DATA_LIST snapshot");
}

void bWriteDataRt(Class &c) {
  c.def(
      "write_data_rt",
      [](DRAFramework::CDRFLEx &self, arr_f forceTorque, int iExternalDI,
         int iExternalDO, arr_f analogIn, arr_f analogOut) {
        return self.write_data_rt(check1D(forceTorque, NUM_JOINT, "force"),
                                  iExternalDI, iExternalDO,
                                  check1D(analogIn, 6, "analog_in"),
                                  check1D(analogOut, 6, "analog_out"));
      },
      py::arg("external_force_torque"), py::arg("external_di"),
      py::arg("external_do"), py::arg("external_analog_input"),
      py::arg("external_analog_output"));
}

void bServojRt(Class &c) {
  c.def(
      "servoj_rt",
      [](DRAFramework::CDRFLEx &self, arr_f pos, arr_f vel, arr_f acc,
         float time) {
        return self.servoj_rt(check1D(pos, NUM_JOINT, "pos"),
                              check1D(vel, NUM_JOINT, "vel"),
                              check1D(acc, NUM_JOINT, "acc"), time);
      },
      py::arg("pos"), py::arg("vel"), py::arg("acc"), py::arg("time"));
}

void bServolRt(Class &c) {
  c.def(
      "servol_rt",
      [](DRAFramework::CDRFLEx &self, arr_f pos, arr_f vel, arr_f acc,
         float time) {
        return self.servol_rt(check1D(pos, NUM_TASK, "pos"),
                              check1D(vel, NUM_TASK, "vel"),
                              check1D(acc, NUM_TASK, "acc"), time);
      },
      py::arg("pos"), py::arg("vel"), py::arg("acc"), py::arg("time"));
}

void bSpeedjRt(Class &c) {
  c.def(
      "speedj_rt",
      [](DRAFramework::CDRFLEx &self, arr_f vel, arr_f acc, float time) {
        return self.speedj_rt(check1D(vel, NUM_JOINT, "vel"),
                              check1D(acc, NUM_JOINT, "acc"), time);
      },
      py::arg("vel"), py::arg("acc"), py::arg("time"));
}

void bSpeedlRt(Class &c) {
  c.def(
      "speedl_rt",
      [](DRAFramework::CDRFLEx &self, arr_f vel, arr_f acc, float time) {
        return self.speedl_rt(check1D(vel, NUM_TASK, "vel"),
                              check1D(acc, NUM_TASK, "acc"), time);
      },
      py::arg("vel"), py::arg("acc"), py::arg("time"));
}

void bTorqueRt(Class &c) {
  c.def(
      "torque_rt",
      [](DRAFramework::CDRFLEx &self, arr_f torque, float time) {
        return self.torque_rt(check1D(torque, NUM_JOINT, "torque"), time);
      },
      py::arg("motor_torque"), py::arg("time"));
}

// ── RT callbacks ────────────────────────────────────────────────────────────
static py::function s_cb_rt_monitoring_data;
static void trampoline_rt_monitoring_data(const LPRT_OUTPUT_DATA_LIST p) {
  py::gil_scoped_acquire gil;
  if (s_cb_rt_monitoring_data)
    s_cb_rt_monitoring_data(py::capsule(p, "LPRT_OUTPUT_DATA_LIST"));
}
void bSetOnRtMonitoringData(Class &c) {
  c.def(
      "set_on_rt_monitoring_data",
      [](DRAFramework::CDRFLEx &self, py::function fn) {
        s_cb_rt_monitoring_data = std::move(fn);
        self.set_on_rt_monitoring_data(s_cb_rt_monitoring_data.is_none()
                                           ? nullptr
                                           : trampoline_rt_monitoring_data);
      },
      py::arg("pCallbackFunc"));
}

static py::function s_cb_rt_log_alarm;
static void trampoline_rt_log_alarm(LPLOG_ALARM p) {
  py::gil_scoped_acquire gil;
  if (s_cb_rt_log_alarm)
    s_cb_rt_log_alarm(py::capsule(p, "LPLOG_ALARM"));
}
void bSetOnRtLogAlarm(Class &c) {
  c.def(
      "set_on_rt_log_alarm",
      [](DRAFramework::CDRFLEx &self, py::function fn) {
        s_cb_rt_log_alarm = std::move(fn);
        self.set_on_rt_log_alarm(
            s_cb_rt_log_alarm.is_none() ? nullptr : trampoline_rt_log_alarm);
      },
      py::arg("pCallbackFunc"));
}

static py::function s_cb_monitoring_safety_stop_type;
static void trampoline_monitoring_safety_stop_type(const unsigned char v) {
  py::gil_scoped_acquire gil;
  if (s_cb_monitoring_safety_stop_type)
    s_cb_monitoring_safety_stop_type(static_cast<int>(v));
}
void bSetOnMonitoringSafetyStopType(Class &c) {
  c.def(
      "set_on_monitoring_safety_stop_type",
      [](DRAFramework::CDRFLEx &self, py::function fn) {
        s_cb_monitoring_safety_stop_type = std::move(fn);
        self.set_on_monitoring_safety_stop_type(
            s_cb_monitoring_safety_stop_type.is_none()
                ? nullptr
                : trampoline_monitoring_safety_stop_type);
      },
      py::arg("pCallbackFunc"));
}

// ============================================================================
// 2. HOLD-TO-RUN
// ============================================================================

void bHold2Run(Class &c) {
  c.def("hold2run",
        [](DRAFramework::CDRFLEx &self) { return self.hold2run(); });
}

void bJogH2r(Class &c) {
  c.def(
      "jog_h2r",
      [](DRAFramework::CDRFLEx &self, JOG_AXIS axis, MOVE_REFERENCE ref,
         float vel) { return self.jog_h2r(axis, ref, vel); },
      py::arg("axis"), py::arg("reference"), py::arg("velocity"));
}

void bMovejH2r(Class &c) {
  c.def(
      "movej_h2r",
      [](DRAFramework::CDRFLEx &self, arr_f pos, arr_f vel, arr_f acc,
         float time, MOVE_MODE mode, float blendRad,
         BLENDING_SPEED_TYPE blendType) {
        return self.movej_h2r(
            check1D(pos, NUM_JOINT, "pos"), check1D(vel, NUM_JOINT, "vel"),
            check1D(acc, NUM_JOINT, "acc"), time, mode, blendRad, blendType);
      },
      py::arg("pos"), py::arg("vel"), py::arg("acc"), py::arg("time") = 0.f,
      py::arg_v("move_mode", MOVE_MODE::MOVE_MODE_ABSOLUTE,
                "MOVE_MODE.Absolute"),
      py::arg("blending_radius") = 0.f,
      py::arg_v("blending_type",
                BLENDING_SPEED_TYPE::BLENDING_SPEED_TYPE_DUPLICATE,
                "BLENDING_SPEED_TYPE.Duplicate"));
}

void bMovelH2r(Class &c) {
  c.def(
      "movel_h2r",
      [](DRAFramework::CDRFLEx &self, arr_f pos, arr_f vel, arr_f acc,
         float time, MOVE_MODE mode, MOVE_REFERENCE ref, float blendRad,
         BLENDING_SPEED_TYPE blendType) {
        return self.movel_h2r(check1D(pos, NUM_TASK, "pos"),
                              check1D(vel, 2, "vel"), check1D(acc, 2, "acc"),
                              time, mode, ref, blendRad, blendType);
      },
      py::arg("pos"), py::arg("vel"), py::arg("acc"), py::arg("time") = 0.f,
      py::arg_v("move_mode", MOVE_MODE::MOVE_MODE_ABSOLUTE,
                "MOVE_MODE.Absolute"),
      py::arg_v("move_reference", MOVE_REFERENCE::MOVE_REFERENCE_BASE,
                "MOVE_REFERENCE.Base"),
      py::arg("blending_radius") = 0.f,
      py::arg_v("blending_type",
                BLENDING_SPEED_TYPE::BLENDING_SPEED_TYPE_DUPLICATE,
                "BLENDING_SPEED_TYPE.Duplicate"));
}

// ============================================================================
// 3. ETHERNET REGISTERS  (getters return (success, value) tuples)
// ============================================================================

void bSetOutputRegisterBit(Class &c) {
  c.def(
      "set_output_register_bit",
      [](DRAFramework::CDRFLEx &self, unsigned short addr, int val) {
        return self.set_output_register_bit(addr, val);
      },
      py::arg("address"), py::arg("value"));
}
void bSetOutputRegisterInt(Class &c) {
  c.def(
      "set_output_register_int",
      [](DRAFramework::CDRFLEx &self, unsigned short addr, int val) {
        return self.set_output_register_int(addr, val);
      },
      py::arg("address"), py::arg("value"));
}
void bSetOutputRegisterFloat(Class &c) {
  c.def(
      "set_output_register_float",
      [](DRAFramework::CDRFLEx &self, unsigned short addr, float val) {
        return self.set_output_register_float(addr, val);
      },
      py::arg("address"), py::arg("value"));
}

void bGetOutputRegisterBit(Class &c) {
  c.def(
      "get_output_register_bit",
      [](DRAFramework::CDRFLEx &self, unsigned short addr, int timeout_ms) {
        int out = 0;
        bool ok = self.get_output_register_bit(addr, out, timeout_ms);
        return py::make_tuple(ok, out);
      },
      py::arg("address"), py::arg("timeout_ms") = 300);
}
void bGetOutputRegisterInt(Class &c) {
  c.def(
      "get_output_register_int",
      [](DRAFramework::CDRFLEx &self, unsigned short addr, int timeout_ms) {
        int out = 0;
        bool ok = self.get_output_register_int(addr, out, timeout_ms);
        return py::make_tuple(ok, out);
      },
      py::arg("address"), py::arg("timeout_ms") = 300);
}
void bGetOutputRegisterFloat(Class &c) {
  c.def(
      "get_output_register_float",
      [](DRAFramework::CDRFLEx &self, unsigned short addr, int timeout_ms) {
        float out = 0.f;
        bool ok = self.get_output_register_float(addr, out, timeout_ms);
        return py::make_tuple(ok, out);
      },
      py::arg("address"), py::arg("timeout_ms") = 300);
}

void bGetInputRegisterBit(Class &c) {
  c.def(
      "get_input_register_bit",
      [](DRAFramework::CDRFLEx &self, unsigned short addr, int timeout_ms) {
        int out = 0;
        bool ok = self.get_input_register_bit(addr, out, timeout_ms);
        return py::make_tuple(ok, out);
      },
      py::arg("address"), py::arg("timeout_ms") = 300);
}
void bGetInputRegisterInt(Class &c) {
  c.def(
      "get_input_register_int",
      [](DRAFramework::CDRFLEx &self, unsigned short addr, int timeout_ms) {
        int out = 0;
        bool ok = self.get_input_register_int(addr, out, timeout_ms);
        return py::make_tuple(ok, out);
      },
      py::arg("address"), py::arg("timeout_ms") = 300);
}
void bGetInputRegisterFloat(Class &c) {
  c.def(
      "get_input_register_float",
      [](DRAFramework::CDRFLEx &self, unsigned short addr, int timeout_ms) {
        float out = 0.f;
        bool ok = self.get_input_register_float(addr, out, timeout_ms);
        return py::make_tuple(ok, out);
      },
      py::arg("address"), py::arg("timeout_ms") = 300);
}

// ============================================================================
// 4. MOTION EXTRAS
// ============================================================================

void bMultiJog(Class &c) {
  c.def(
      "multi_jog",
      [](DRAFramework::CDRFLEx &self, arr_f pos, MOVE_REFERENCE ref,
         float vel) {
        return self.multi_jog(check1D(pos, NUM_TASK, "pos"), ref, vel);
      },
      py::arg("pos"), py::arg("reference"), py::arg("velocity"));
}

void bGetUserHome(Class &c) {
  c.def("get_user_home", [](DRAFramework::CDRFLEx &self) {
    auto *p = self.get_user_home();
    if (!p)
      throw std::runtime_error("get_user_home returned null");
    return *p;
  });
}

// Safe_MoveJ — scalar and array vel/acc overloads
void bSafeMovej(Class &c) {
  c.def(
      "safe_movej",
      [](DRAFramework::CDRFLEx &self, arr_f pos, float vel, float acc,
         float time, MOVE_MODE mode, float blendRad,
         BLENDING_SPEED_TYPE blendType) {
        return self.Safe_MoveJ(check1D(pos, NUM_JOINT, "pos"), vel, acc, time,
                               mode, blendRad, blendType);
      },
      py::arg("pos"), py::arg("vel"), py::arg("acc"), py::arg("time") = 0.f,
      py::arg_v("move_mode", MOVE_MODE::MOVE_MODE_ABSOLUTE,
                "MOVE_MODE.Absolute"),
      py::arg("blending_radius") = 0.f,
      py::arg_v("blending_type",
                BLENDING_SPEED_TYPE::BLENDING_SPEED_TYPE_DUPLICATE,
                "BLENDING_SPEED_TYPE.Duplicate"));

  c.def(
      "safe_movej",
      [](DRAFramework::CDRFLEx &self, arr_f pos, arr_f vel, arr_f acc,
         float time, MOVE_MODE mode, float blendRad,
         BLENDING_SPEED_TYPE blendType) {
        return self.Safe_MoveJ(
            check1D(pos, NUM_JOINT, "pos"), check1D(vel, NUM_JOINT, "vel"),
            check1D(acc, NUM_JOINT, "acc"), time, mode, blendRad, blendType);
      },
      py::arg("pos"), py::arg("vel"), py::arg("acc"), py::arg("time") = 0.f,
      py::arg_v("move_mode", MOVE_MODE::MOVE_MODE_ABSOLUTE,
                "MOVE_MODE.Absolute"),
      py::arg("blending_radius") = 0.f,
      py::arg_v("blending_type",
                BLENDING_SPEED_TYPE::BLENDING_SPEED_TYPE_DUPLICATE,
                "BLENDING_SPEED_TYPE.Duplicate"));
}

void bSafeMovel(Class &c) {
  c.def(
      "safe_movel",
      [](DRAFramework::CDRFLEx &self, arr_f pos, arr_f vel, arr_f acc,
         float time, MOVE_MODE mode, MOVE_REFERENCE ref, float blendRad,
         BLENDING_SPEED_TYPE blendType) {
        return self.Safe_MoveL(check1D(pos, NUM_TASK, "pos"),
                               check1D(vel, 2, "vel"), check1D(acc, 2, "acc"),
                               time, mode, ref, blendRad, blendType);
      },
      py::arg("pos"), py::arg("vel"), py::arg("acc"), py::arg("time") = 0.f,
      py::arg_v("move_mode", MOVE_MODE::MOVE_MODE_ABSOLUTE,
                "MOVE_MODE.Absolute"),
      py::arg_v("move_reference", MOVE_REFERENCE::MOVE_REFERENCE_BASE,
                "MOVE_REFERENCE.Base"),
      py::arg("blending_radius") = 0.f,
      py::arg_v("blending_type",
                BLENDING_SPEED_TYPE::BLENDING_SPEED_TYPE_DUPLICATE,
                "BLENDING_SPEED_TYPE.Duplicate"));
}

void bSafeMovejx(Class &c) {
  c.def(
      "safe_movejx",
      [](DRAFramework::CDRFLEx &self, arr_f pos, unsigned char solSpace,
         float vel, float acc, float time, MOVE_MODE mode, MOVE_REFERENCE ref,
         float blendRad, BLENDING_SPEED_TYPE blendType) {
        return self.Safe_MoveJX(check1D(pos, NUM_JOINT, "pos"), solSpace, vel,
                                acc, time, mode, ref, blendRad, blendType);
      },
      py::arg("pos"), py::arg("solution_space"), py::arg("vel"), py::arg("acc"),
      py::arg("time") = 0.f,
      py::arg_v("move_mode", MOVE_MODE::MOVE_MODE_ABSOLUTE,
                "MOVE_MODE.Absolute"),
      py::arg_v("move_reference", MOVE_REFERENCE::MOVE_REFERENCE_BASE,
                "MOVE_REFERENCE.Base"),
      py::arg("blending_radius") = 0.f,
      py::arg_v("blending_type",
                BLENDING_SPEED_TYPE::BLENDING_SPEED_TYPE_DUPLICATE,
                "BLENDING_SPEED_TYPE.Duplicate"));
}

void bServojG(Class &c) {
  c.def(
      "servoj_g",
      [](DRAFramework::CDRFLEx &self, arr_f pos, arr_f vel, arr_f acc,
         float time) {
        return self.servoj_g(check1D(pos, NUM_JOINT, "pos"),
                             check1D(vel, NUM_JOINT, "vel"),
                             check1D(acc, NUM_JOINT, "acc"), time);
      },
      py::arg("pos"), py::arg("vel"), py::arg("acc"), py::arg("time") = 0.f);
}

void bServolG(Class &c) {
  c.def(
      "servol_g",
      [](DRAFramework::CDRFLEx &self, arr_f pos, arr_f vel, arr_f acc,
         float time) {
        return self.servol_g(check1D(pos, NUM_TASK, "pos"),
                             check1D(vel, 2, "vel"), check1D(acc, 2, "acc"),
                             time);
      },
      py::arg("pos"), py::arg("vel"), py::arg("acc"), py::arg("time") = 0.f);
}

void bMovesxG(Class &c) {
  c.def(
      "movesx_g",
      [](DRAFramework::CDRFLEx &self, arr_f pos, unsigned char nPosCount,
         arr_f vel, arr_f acc, float time, MOVE_MODE mode, MOVE_REFERENCE ref,
         SPLINE_VELOCITY_OPTION velOpt) {
        if (pos.ndim() != 2 || pos.shape(0) != MAX_SPLINE_POINT ||
            pos.shape(1) != NUM_TASK)
          throw std::runtime_error(
              "pos must have shape (MAX_SPLINE_POINT, NUM_TASK)");
        float(*pp)[NUM_TASK] =
            reinterpret_cast<float(*)[NUM_TASK]>(pos.mutable_data());
        return self.movesx_g(pp, nPosCount, check1D(vel, 2, "vel"),
                             check1D(acc, 2, "acc"), time, mode, ref, velOpt);
      },
      py::arg("pos"), py::arg("pos_count"), py::arg("vel"), py::arg("acc"),
      py::arg("time") = 0.f,
      py::arg_v("move_mode", MOVE_MODE::MOVE_MODE_ABSOLUTE,
                "MOVE_MODE.Absolute"),
      py::arg_v("move_reference", MOVE_REFERENCE::MOVE_REFERENCE_BASE,
                "MOVE_REFERENCE.Base"),
      py::arg_v("vel_option",
                SPLINE_VELOCITY_OPTION::SPLINE_VELOCITY_OPTION_DEFAULT,
                "SPLINE_VELOCITY_OPTION.Default"));
}

void bMovesjG(Class &c) {
  c.def(
      "movesj_g",
      [](DRAFramework::CDRFLEx &self, arr_f pos, unsigned char nPosCount,
         float vel, float acc, float time, MOVE_MODE mode) {
        if (pos.ndim() != 2 || pos.shape(0) != MAX_SPLINE_POINT ||
            pos.shape(1) != NUM_JOINT)
          throw std::runtime_error(
              "pos must have shape (MAX_SPLINE_POINT, NUM_JOINT)");
        float(*pp)[NUM_JOINT] =
            reinterpret_cast<float(*)[NUM_JOINT]>(pos.mutable_data());
        return self.movesj_g(pp, nPosCount, vel, acc, time, mode);
      },
      py::arg("pos"), py::arg("pos_count"), py::arg("vel"), py::arg("acc"),
      py::arg("time") = 0.f,
      py::arg_v("move_mode", MOVE_MODE::MOVE_MODE_ABSOLUTE,
                "MOVE_MODE.Absolute"));
}

void bIkinNorm(Class &c) {
  c.def(
      "ikin_norm",
      [](DRAFramework::CDRFLEx &self, arr_f src, unsigned char solSpace,
         COORDINATE_SYSTEM targetRef, unsigned char refPosOpt) {
        auto *p = self.ikin_norm(check1D(src, NUM_TASK, "src"), solSpace,
                                 targetRef, refPosOpt);
        if (!p)
          throw std::runtime_error("ikin_norm returned null");
        return *p;
      },
      py::arg("src_pos"), py::arg("solution_space"),
      py::arg_v("target_ref", COORDINATE_SYSTEM::COORDINATE_SYSTEM_BASE,
                "COORDINATE_SYSTEM.Base"),
      py::arg("ref_pos_opt") = (unsigned char)0);
}

void bAddto(Class &c) {
  c.def(
      "addto",
      [](DRAFramework::CDRFLEx &self, arr_f src, arr_f offset) {
        auto *p = self.addto(check1D(src, NUM_JOINT, "src"),
                             check1D(offset, NUM_JOINT, "offset"));
        if (!p)
          throw std::runtime_error("addto returned null");
        return *p;
      },
      py::arg("src_pos"), py::arg("offset"));
}

// ============================================================================
// 5. CONFIG EXTRAS
// ============================================================================

void bGetToolShape(Class &c) {
  c.def("get_tool_shape",
        [](DRAFramework::CDRFLEx &self) { return self.get_tool_shape(); });
}

void bSetSingularHandlingForce(Class &c) {
  c.def(
      "set_singular_handling_force",
      [](DRAFramework::CDRFLEx &self, SINGULARITY_FORCE_HANDLING mode) {
        return self.set_singular_handling_force(mode);
      },
      py::arg("mode"));
}

void bSetAutoSafetyMoveStop(Class &c) {
  c.def(
      "set_auto_safety_move_stop",
      [](DRAFramework::CDRFLEx &self, bool enable) {
        return self.set_auto_safety_move_stop(enable);
      },
      py::arg("enable"));
}

// ============================================================================
// 6. SYSTEM / LED / LINK
// ============================================================================

void bSystemShutDown(Class &c) {
  c.def("system_shut_down",
        [](DRAFramework::CDRFLEx &self) { return self.system_shut_down(); });
}

void bStateLedReset(Class &c) {
  c.def("state_led_reset",
        [](DRAFramework::CDRFLEx &self) { return self.state_led_reset(); });
}

void bSetStateLedOff(Class &c) {
  c.def("set_state_led_off",
        [](DRAFramework::CDRFLEx &self) { return self.set_state_led_off(); });
}

void bSetStateLedColor(Class &c) {
  c.def(
      "set_state_led_color",
      [](DRAFramework::CDRFLEx &self, int r, int g, int b) {
        return self.set_state_led_color(r, g, b);
      },
      py::arg("red"), py::arg("green"), py::arg("blue"));
}

void bGetStateLedRule(Class &c) {
  c.def("get_state_led_rule",
        [](DRAFramework::CDRFLEx &self) { return self.get_state_led_rule(); });
}

void bGetRobotLinkInfo(Class &c) {
  c.def(
      "get_robot_link_info",
      [](DRAFramework::CDRFLEx &self, int timeout_ms) {
        ROBOT_LINK_INFO info{};
        bool ok = self.get_robot_link_info(info, timeout_ms);
        return py::make_tuple(ok, info);
      },
      py::arg("timeout_ms") = 300,
      "Returns (success, ROBOT_LINK_INFO)");
}
