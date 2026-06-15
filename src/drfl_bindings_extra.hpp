#pragma once
#include "../library/API-DRFL/include/DRFL.h"
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>

namespace py = pybind11;

// ── RT Control ──────────────────────────────────────────────────────────────
void bConnectRtControl(py::class_<DRAFramework::CDRFLEx>& c);
void bDisconnectRtControl(py::class_<DRAFramework::CDRFLEx>& c);
void bGetRtControlOutputVersionList(py::class_<DRAFramework::CDRFLEx>& c);
void bGetRtControlInputVersionList(py::class_<DRAFramework::CDRFLEx>& c);
void bGetRtControlInputDataList(py::class_<DRAFramework::CDRFLEx>& c);
void bGetRtControlOutputDataList(py::class_<DRAFramework::CDRFLEx>& c);
void bSetRtControlInput(py::class_<DRAFramework::CDRFLEx>& c);
void bSetRtControlOutput(py::class_<DRAFramework::CDRFLEx>& c);
void bStartRtControl(py::class_<DRAFramework::CDRFLEx>& c);
void bStopRtControl(py::class_<DRAFramework::CDRFLEx>& c);
void bSetVeljRt(py::class_<DRAFramework::CDRFLEx>& c);
void bSetAccjRt(py::class_<DRAFramework::CDRFLEx>& c);
void bSetVelxRt(py::class_<DRAFramework::CDRFLEx>& c);
void bSetAccxRt(py::class_<DRAFramework::CDRFLEx>& c);
void bReadDataRt(py::class_<DRAFramework::CDRFLEx>& c);
void bWriteDataRt(py::class_<DRAFramework::CDRFLEx>& c);
void bServojRt(py::class_<DRAFramework::CDRFLEx>& c);
void bServolRt(py::class_<DRAFramework::CDRFLEx>& c);
void bSpeedjRt(py::class_<DRAFramework::CDRFLEx>& c);
void bSpeedlRt(py::class_<DRAFramework::CDRFLEx>& c);
void bTorqueRt(py::class_<DRAFramework::CDRFLEx>& c);
void bSetOnRtMonitoringData(py::class_<DRAFramework::CDRFLEx>& c);
void bSetOnRtLogAlarm(py::class_<DRAFramework::CDRFLEx>& c);
void bSetOnMonitoringSafetyStopType(py::class_<DRAFramework::CDRFLEx>& c);

// ── Hold-to-Run ─────────────────────────────────────────────────────────────
void bHold2Run(py::class_<DRAFramework::CDRFLEx>& c);
void bJogH2r(py::class_<DRAFramework::CDRFLEx>& c);
void bMovejH2r(py::class_<DRAFramework::CDRFLEx>& c);
void bMovelH2r(py::class_<DRAFramework::CDRFLEx>& c);

// ── Ethernet Registers ──────────────────────────────────────────────────────
void bSetOutputRegisterBit(py::class_<DRAFramework::CDRFLEx>& c);
void bSetOutputRegisterInt(py::class_<DRAFramework::CDRFLEx>& c);
void bSetOutputRegisterFloat(py::class_<DRAFramework::CDRFLEx>& c);
void bGetOutputRegisterBit(py::class_<DRAFramework::CDRFLEx>& c);
void bGetOutputRegisterInt(py::class_<DRAFramework::CDRFLEx>& c);
void bGetOutputRegisterFloat(py::class_<DRAFramework::CDRFLEx>& c);
void bGetInputRegisterBit(py::class_<DRAFramework::CDRFLEx>& c);
void bGetInputRegisterInt(py::class_<DRAFramework::CDRFLEx>& c);
void bGetInputRegisterFloat(py::class_<DRAFramework::CDRFLEx>& c);

// ── Motion extras ───────────────────────────────────────────────────────────
void bMultiJog(py::class_<DRAFramework::CDRFLEx>& c);
void bGetUserHome(py::class_<DRAFramework::CDRFLEx>& c);
void bSafeMovej(py::class_<DRAFramework::CDRFLEx>& c);
void bSafeMovel(py::class_<DRAFramework::CDRFLEx>& c);
void bSafeMovejx(py::class_<DRAFramework::CDRFLEx>& c);
void bServojG(py::class_<DRAFramework::CDRFLEx>& c);
void bServolG(py::class_<DRAFramework::CDRFLEx>& c);
void bMovesxG(py::class_<DRAFramework::CDRFLEx>& c);
void bMovesjG(py::class_<DRAFramework::CDRFLEx>& c);
void bIkinNorm(py::class_<DRAFramework::CDRFLEx>& c);
void bAddto(py::class_<DRAFramework::CDRFLEx>& c);

// ── Config extras ───────────────────────────────────────────────────────────
void bGetToolShape(py::class_<DRAFramework::CDRFLEx>& c);
void bSetSingularHandlingForce(py::class_<DRAFramework::CDRFLEx>& c);
void bSetAutoSafetyMoveStop(py::class_<DRAFramework::CDRFLEx>& c);

// ── System / LED / link ─────────────────────────────────────────────────────
void bSystemShutDown(py::class_<DRAFramework::CDRFLEx>& c);
void bStateLedReset(py::class_<DRAFramework::CDRFLEx>& c);
void bSetStateLedOff(py::class_<DRAFramework::CDRFLEx>& c);
void bSetStateLedColor(py::class_<DRAFramework::CDRFLEx>& c);
void bGetStateLedRule(py::class_<DRAFramework::CDRFLEx>& c);
void bGetRobotLinkInfo(py::class_<DRAFramework::CDRFLEx>& c);
