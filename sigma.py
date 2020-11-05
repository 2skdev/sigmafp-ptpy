from construct import (
    Container, Enum, Struct,
    Int8ul, Int16ul, Int32ul
    )

import struct

import logging
### debug
# logging.getLogger('ptpy').setLevel(logging.DEBUG)

'''
ToDo:
 IFDのアドレス参照
'''

class IFD:
    cam_can_set_info5_tag = Enum(
        Int16ul,
        DriveMode                       = 1,
        ContinuousShootingSpeed         = 2,
        IntervalTimerShots              = 3,
        IntervalTimer                   = 4,
        SFD                             = 10,
        ImageQuality                    = 11,
        DNGImageQuality                 = 12,
        StillResolution                 = 20,
        AspectRatio                     = 21,
        StillMovieSwitching             = 100,
        AudioRecord                     = 110,
        AudioChannelCount               = 111,
        AudioGainMode                   = 112,
        AudioManualGain                 = 113,
        WindNoiseCanceller              = 114,
        RecordFormat                    = 150,
        CinemaDNGQuality                = 151,
        MOVQuality                      = 152,
        MovieResolution                 = 160,
        FrameRate                       = 161,
        Binning                         = 162,
        ExposureMode                    = 200,
        ProgramShift                    = 201,
        _Dummy209                       = 209,
        FNumberApex                     = 210,
        TNumberApex                     = 211,
        ShutterSpeedApex                = 212,
        ShutterSpeed                    = 213,
        ShutterAngle                    = 214,
        ISOApex                         = 215,
        ISOAuto                         = 216,
        ExposureCompensation            = 217,
        ExposureBracketCount            = 218,
        ExposureBracketOrder            = 219,
        ExposureBracketAmount           = 220,
        MeteringMode                    = 250,
        AELock                          = 251,
        Flash                           = 252,
        FlashExposureCompensation       = 253,
        CustomBracket                   = 300,
        WhiteBalance                    = 301,
        WhiteBalanceColorTemperature    = 302,
        WhiteBalanceCustomCapture       = 303,
        WhiteBalanceAjustment           = 304,
        WhiteBalanceBlacketCount        = 305,
        WhiteBalanceBlacketDirection    = 306,
        WhiteBalanceBlacketAmount       = 307,
        ColorMode                       = 320,
        ColorModeContrast               = 321,
        ColorModeSharpness              = 322,
        ColorModeSaturation             = 323,
        MonochromeFilteringEffect       = 324,
        MonochromeToningEffect          = 325,
        ColorModeBracketCount           = 327,
        FillLight                       = 340,
        FillLightBracket                = 341,
        FillLightAmount                 = 342,
        HDR                             = 350,
        DCCrop                          = 500,
        LensDistortion                  = 501,
        LensChromaticAberration         = 502,
        LensDiffraction                 = 503,
        LensVignetting                  = 504,
        LensColorShading                = 505,
        LensColorShadingCustomCapture   = 506,
        FocusMode                       = 600,
        AFLock                          = 601,
        FaceAFSetting                   = 602,
        FocusArea                       = 610,
        PointSelectMethod               = 611,
        FocusAreaOverall                = 612,
        FocusAreaValid                  = 613,
        DistanceMeasureWindowCount      = 614,
        DistanceMeasureWindowSize       = 615,
        DistanceMeasureWindowMove       = 616,
        PreContinuousAF                 = 650,
        FocusLimit                      = 651,
        AFSOperation                    = 656,
        AFCOperation                    = 657,
        LVImageTransfer                 = 700,
        LVMagnificationRate             = 701,
        FocusPeaking                    = 702,
        Date                            = 800,
        ShutterSound                    = 801,
        AFVolume                        = 802,
        TimerVolume                     = 803,
        ElectronicImageStabilization    = 810,
    )

    data_group_focus_tag = Enum(
        Int16ul,
        FocusMode                       = 1,
        AFLock                          = 2,
        FaceAFSetting                   = 3,
        FaceAFDetectStatus              = 4,
        FocusArea                       = 10,
        PointSelectMethod               = 11,
        DistanceMeasureWindowSize       = 12,
        DistanceMeasureWindowPosition   = 13,
        DistanceMeasureWindow           = 14,
        PreContinuousAF                 = 51,
        FocusLimit                      = 52,
    )

    data_group_movie_tag = Enum(
        Int16ul,
        StillCineMode                   = 1,
        _Dummy3                         = 3,
        _Dummy4                         = 4,
        TNumber                         = 5,
        ShutterSettingMode              = 6,
        ShutterAngle                    = 7,
        AudioRecoding                   = 10,
        AudioGainMode                   = 11,
        AudioManualGain                 = 12,
        WindNoiseCanceller              = 13,
        RecordFormat                    = 50,
        CinemaDNGQuality                = 51,
        MOVQuality                      = 52,
        MovieResolution                 = 60,
        FrameRate                       = 61,
        Binning                         = 62,
    )

    types = Enum(
        Int16ul,
        Byte        = 1,    # 1  byte
        ASCII       = 2,    # 9  byte
        Short       = 3,    # 2  byte
        Long        = 4,    # 4  byte
        Rational    = 5,    # 8  byte
        SByte       = 6,    # 1  byte
        Undefined   = 7,    # 8  byte
        SShort      = 8,    # 2  byte
        SLong       = 9,    # 4  byte
        SRatonal    = 10,   # 8  byte
        Float       = 11,   # 8  byte
        Double      = 12,   # 16 byte
    )

    @property
    def tag_id(self):
        return self._container.TagId

    @property
    def type(self):
        return self._container.Type
    @type.setter
    def type(self, data):
        self._container.Type = data

    @property
    def count(self):
        return self._container.Count
    @count.setter
    def count(self, data):
        self._container.Count = data

    @property
    def value(self):
        return self._container.Value
    @value.setter
    def value(self, data):
        self._container.Value = data

    @staticmethod
    def struct(tag):
        return Struct(
            'TagId' / tag,
            'Type' / IFD.types,
            'Count' / Int32ul,
            'Value' / Int32ul,
        )

    @staticmethod
    def sizeof():
        return IFD.struct(Int16ul).sizeof()

    @staticmethod
    def parse(tag, data):
        ifd = IFD(tag)
        ifd._container = ifd._struct.parse(data)
        return ifd

    def build(self):
        return self._struct.build(self._container)

    def __init__(self, tag, tag_id=None):
        # create struct
        self._struct = IFD.struct(tag)

        # init container
        self._container = self._struct.parse(b'\x00' * self._struct.sizeof())

        if tag_id:
            self._container.TagId = tag_id


class DG:
    data_group1_endian = [
        'ShutterSpeed' / Int8ul,
        'Aperture' / Int8ul,
        'ProgramShift' / Int8ul,
        'ISOAuto' / Int8ul,
        'ISOSpeed' / Int8ul,
        'ExpCompensation' / Int8ul,
        'ABValue' / Int8ul,
        'ABSetting' / Int8ul,
        'FrameBufferState' / Int8ul,
        'MediaFreeSpace' / Int16ul,
        'MediaStatus' / Int8ul,
        'CurrentLensFocalLength' / Int16ul,
        'BatteryState' / Int8ul,
        'AbShotRemainNumber' / Int8ul,
        'ExpCompExcludeAB' / Int8ul,
        'AfButtonSetting' / Int8ul,
    ]

    data_group2_endian = [
        'DriveMode' / Int8ul,
        'SpecialMode' / Int8ul,
        'ExposureMode' / Int8ul,
        'AEMeteringMode' / Int8ul,
        'AELock' / Int8ul,
        'AFMode' / Int8ul,
        'AFAreaMode' / Int8ul,
        'AFLock' / Int8ul,
        'FlashType' / Int8ul,
        'FlashFire' / Int8ul,
        'FlashMode' / Int8ul,
        'FlashSetting' / Int8ul,
        'FlashExpCompensation' / Int8ul,
        'WhiteBalance' / Int8ul,
        'Resolution' / Int8ul,
        'ImageQuality' / Int8ul,
    ]

    data_group3_endian = [
        'Contrast' / Int8ul,
        'Sharpness' / Int8ul,
        'Saturation' / Int8ul,
        'ColorSpace' / Int8ul,
        'ColorMode' / Int8ul,
        'BatteryKind' / Int8ul,
        'LensWideFocalLength' / Int16ul,
        'LensTeleFocalLength' / Int16ul,
        'AFAuxiliaryLight' / Int8ul,
        'AFBeep' / Int8ul,
        'UPSetting' / Int8ul,
        'ExtendedMode' / Int8ul,
        'AutoRotate' / Int8ul,
        'TimerSound' / Int8ul,
        'RCChannel' / Int8ul,
        'DestinationToSave' / Int8ul,
    ]

    data_group4_endian = [
        'ISOStepMode' / Int8ul,
        'ISOAutoMaxLimit' / Int8ul,
        'ISOAutoMinLimit' / Int8ul,
        'SFDMode' / Int8ul,
        'DCCropMode' / Int8ul,
        'LVMagnify' / Int8ul,
        'HighSensitivityISOExpansion' / Int8ul,
        'ContinuousShootingSpeed' / Int8ul,
        'HDR' / Int8ul,
        'DNG' / Int8ul,
        'FillLight' / Int8ul,
        'OpticalDistortion' / Int8ul,
        'OpticalAberration' / Int8ul,
        'OpticalDiffraction' / Int8ul,
        'OpticalLightIntensity' / Int8ul,
        'OpticalColorShading' / Int8ul,
        'OpticalColorShadingGet' / Int8ul,
        'ImageStabilization' / Int8ul,
        'ShutterSound' / Int8ul,
    ]

    data_group5_endian = [
        'IntervalTimerSecond' / Int16ul,
        'IntervalTimerFrame' / Int8ul,
        'RestTimerSecond' / Int16ul,
        'RestTimerFrame' / Int8ul,
        'ColorTemp' / Int8ul,
        'WBCorrectAB' / Int8ul,
        'WBCorrectGM' / Int8ul,
        'AspectRatio' / Int8ul,
        'FilterEffect' / Int8ul,
        'ToneEffect' / Int8ul,
        'ToneCtrl' / Int8ul,
        'PreviewExposureInMmode' / Int8ul,
        'FocusPeaking' / Int8ul,
        'FaceDetectionAF' / Int8ul,
        'AFautoExpand' / Int8ul,
        'AFautoExpandCancel' / Int8ul,
        'AFSelectPostion' / Int8ul,
        'AFAreaPosX' / Int8ul,
        'AFAreaPosY' / Int8ul,
        'AFAreaSize' / Int8ul,
        'BatteryStatePack1' / Int8ul,
        'BatteryStatePack2' / Int8ul,
        'FaceDetectionState' / Int8ul,
        'EyeFiCardState' / Int8ul,
        'WiFiStateEyeFiCard' / Int8ul,
        'EyeFiFunctionSetting' / Int8ul,
        'AFAuxLight' / Int8ul,
    ]

    @staticmethod
    def struct(field, endian):
        constructor = []

        for sft, e in enumerate(endian):
            if field & (1 << sft) != 0:
                constructor.append(e)
        
        return Struct(*constructor)

    @staticmethod
    def parse(field, endian, data):
        container = DG.struct(field, endian).parse(data)
        return DG(endian, container)

    def build(self):
        field = 0

        for sft, e in enumerate(self._endian):
            # bit on when data exist
            if e.name in self._container.keys():
                field |= (1 << sft)

        data = DG.struct(field, self._endian).build(self._container)

        return struct.pack('<H', field) + data

    def get_data(self, name):
        if not hasattr(self._container, name):
            return None
        return self._container[name]

    def set_data(self, name, data):
        if not hasattr(self._container, name):
            raise
        self._container[name] = data
    
    def keys(self):
        return list(self._container.keys())

    def __init__(self, endian, container):
        self._endian = endian
        self._container = container

class Sigma(object):

    def __init__(self, *args, **kwargs):
        print('Init Sigma')
        super(Sigma, self).__init__(*args, **kwargs)

    def _set_endian(self, endian):
        print('Set Sigma endianness')
        super(Sigma, self)._set_endian(endian)

    def _OperationCode(self, **product_operations):
        '''
        0x1002 sgm_CamOpen
        0x1003 sgm_CamClose
        0x9035 sgm_ConfigAPI
        0x9012 sgm_GetCamDataGrp1
        0x9016 sgm_SetCamDataGrp1
        0x9013 sgm_GetCamDataGrp2
        0x9017 sgm_SetCamDataGrp2
        0x9014 sgm_GetCamDataGrp3
        0x9018 sgm_SetCamDataGrp3
        0x9023 sgm_GetCamDataGrp4
        0x9024 sgm_SetCamDataGrp4
        0x9027 sgm_GetCamDataGrp5
        0x9028 sgm_SetCamDataGrp5
        0x9031 sgm_GetCamDataGroupFocus
        0x9032 sgm_SetCamDataGroupFocus
        0x9033 sgm_GetCamDataGroupMovie
        0x9034 sgm_SetCamDataGroupMovie
        sgm_GetCamCanSetInfo5
        sgm_SetCamClockAdj
        sgm_GetCamStatus2
        0x902b sgm_GetCamViewFrame
        0x901b sgm_SnapCommand
        0x9015 sgm_GetCamCaptStatus
        0x901c sgm_ClearImageDBSingle
        sgm_GetPictFileInfo2
        sgm_GetBigPartialPictFile
        0x9036 sgm_GetMovieFileInfo
        0x9037 sgm_GetPartialMovieFile
        sgm_CloseApplication
        sgm_FreeArrayMemory
        sgm_GetLastCommandData
        '''

        return super(Sigma, self)._OperationCode(
            GetCamDataGroup1        = 0x9012,
            GetCamDataGroup2        = 0x9013,
            GetCamDataGroup3        = 0x9014,
            GetCamCaptStatus        = 0x9015,
            SetCamDataGroup1        = 0x9016,
            SetCamDataGroup2        = 0x9017,
            SetCamDataGroup3        = 0x9018,
            _0x9019                 = 0x9019,
            SnapCommand             = 0x901b,
            ClearImageDBSingle      = 0x901c,

            _0x9022                 = 0x9022,
            GetCamDataGroup4        = 0x9023,
            SetCamDataGroup4        = 0x9024,
            GetCamDataGroup5        = 0x9027,
            SetCamDataGroup5        = 0x9028,
            _0x9029                 = 0x9029,
            _0x902a                 = 0x902a,
            GetViewFrame            = 0x902b,
            _0x902c                 = 0x902c,
            _0x902d                 = 0x902d,
            CloseApplication        = 0x902f,

            GetCamCanSetInfo5       = 0x9030,
            GetCamDataGroupFocus    = 0x9031,
            SetCamDataGroupFocus    = 0x9032,
            GetCamDataGroupMovie    = 0x9033,
            SetCamDataGroupMovie    = 0x9034,
            ConfigAPI               = 0x9035,
            GetMovieFileInfo        = 0x9036,
            GetParticalMovieFile    = 0x9037,

            _0x9401                 = 0x9401,
            _0x9402                 = 0x9402,
            _0x9403                 = 0x9403,
            _0x9404                 = 0x9404,
            _0x9405                 = 0x9405,
            _0x9411                 = 0x9411,
            _0x9412                 = 0x9412,
            _0x9413                 = 0x9413,
            _0x9414                 = 0x9414,
            _0x9421                 = 0x9421,
            _0x9422                 = 0x9422,
            _0x9423                 = 0x9423,
            _0x9424                 = 0x9424,
            _0x9431                 = 0x9431,
            **product_operations
        )

    def _parse_data_group(self, response, endian):
        '''
        format
        b0: length
        b1, b2: data field
        b3~: data
        b-1: check sum

        e.x.)
        change color mode to mono
          field: 0x10 0x00
          data: 0x02 (mono)
          length: field + data = 3
          check sum: field(0x10 + 0x00) + data(0x02) + length(3) = 0x15
          => send [0x03 0x10 0x00 0x02 0x15]
        '''
        if not hasattr(response, 'Data'):
            return None

        field = response.Data[2] << 8 | response.Data[1]

        return DG.parse(field, endian, response.Data[3:-1])

    def _build_data_group(self, datagroup, endian):
        send_data = datagroup.build()
        length    = len(send_data)

        send_data = struct.pack('<B', length) + send_data
        send_data += struct.pack('<B', sum(send_data) & 0xFF)

        return send_data


    def _parse_ifd(self, response, tag):
        '''
        format
        b0~4: length
        b5~8: count
        b9~: ifd
        b-1: checksum
        '''
        if not hasattr(response, 'Data'):
            return None

        length, count = struct.unpack_from('<II', response.Data, 0)

        sizeof = IFD.sizeof()
        ifds = {}

        for i in range(count):
            ifd = IFD.parse(tag, response.Data[i*sizeof+8:])
            ifds[ifd.tag_id] = ifd

        return ifds

    def _build_ifd(self, ifds, tag):
        send_data  = b''

        for ifd in ifds.values():
            send_data += ifd.build()
        
        length = len(send_data)
        count  = len(ifds)

        send_data = struct.pack('<II', length, count) + send_data
        send_data += struct.pack('<B', sum(send_data) & 0xFF)

        return send_data

    def config_api(self):
        ptp = Container(
            OperationCode='ConfigAPI',
            SessionID=self._session,
            TransactionID=self._transaction,
            Parameter=[]
        )
        return self.recv(ptp)

    def close_application(self):
        ptp = Container(
            OperationCode='CloseApplication',
            SessionID=self._session,
            TransactionID=self._transaction,
            Parameter=[]
        )
        return self.recv(ptp)

    def get_cam_data_group1(self):
        ptp = Container(
            OperationCode='GetCamDataGroup1',
            SessionID=self._session,
            TransactionID=self._transaction,
            Parameter=[]
        )
        return self._parse_data_group(self.recv(ptp), DG.data_group1_endian)
    
    def set_cam_data_group1(self, container):
        ptp = Container(
            OperationCode='SetCamDataGroup1',
            SessionID=self._session,
            TransactionID=self._transaction,
            Parameter=[]
        )
        return self.send(ptp, self._buil_parse_ifd_data
        )
        return self._parse_data_group(self.recv(ptp), DG.data_group2_endian)
    
    def set_cam_data_group2(self, container):
        ptp = Container(
            OperationCode='SetCamDataGroup2',
            SessionID=self._session,
            TransactionID=self._transaction,
            Parameter=[]
        )
        return self.send(ptp, self._build_data_group(container, DG.data_group2_endian))

    def get_cam_data_group3(self):
        ptp = Container(
            OperationCode='GetCamDataGroup3',
            SessionID=self._session,
            TransactionID=self._transaction,
            Parameter=[]
        )
        return self._parse_data_group(self.recv(ptp), DG.data_group3_endian)

    def set_cam_data_group3(self, container):
        ptp = Container(
            OperationCode='SetCamDataGroup3',
            SessionID=self._session,
            TransactionID=self._transaction,
            Parameter=[]
        )
        return self.send(ptp, self._build_data_group(container, DG.data_group3_endian))

    def get_cam_data_group4(self):
        ptp = Container(
            OperationCode='GetCamDataGroup4',
            SessionID=self._session,
            TransactionID=self._transaction,
            Parameter=[]
        )
        return self._parse_data_group(self.recv(ptp), DG.data_group4_endian)

    def set_cam_data_group4(self, container):
        ptp = Container(
            OperationCode='SetCamDataGroup4',
            SessionID=self._session,
            TransactionID=self._transaction,
            Parameter=[]
        )
        return self.send(ptp, self._build_data_group(container, DG.data_group4_endian))

    def get_cam_data_group5(self):
        ptp = Container(
            OperationCode='GetCamDataGroup5',
            SessionID=self._session,
            TransactionID=self._transaction,
            Parameter=[]
        )
        return self._parse_data_group(self.recv(ptp), DG.data_group5_endian)

    def set_cam_data_group5(self, container):
        ptp = Container(
            OperationCode='SetCamDataGroup5',
            SessionID=self._session,
            TransactionID=self._transaction,
            Parameter=[]
        )
        return self.send(ptp, self._build_data_group(container, DG.data_group5_endian))

    def get_view_frame(self):
        ptp = Container(
            OperationCode='GetViewFrame',
            SessionID=self._session,
            TransactionID=self._transaction,
            Parameter=[]
        )
        return self.recv(ptp)

    def get_cam_data_group_movie(self):
        ptp = Container(
            OperationCode='GetCamDataGroupMovie',
            SessionID=self._session,
            TransactionID=self._transaction,
            Parameter=[]
        )
        return self._parse_ifd(self.recv(ptp), IFD.data_group_movie_tag)

    def set_cam_data_group_focus(self, ifds):
        ptp = Container(
            OperationCode='SetCamDataGroupMovie',
            SessionID=self._session,
            TransactionID=self._transaction,
            Parameter=[]
        )
        return self.send(ptp, self._build_ifd(ifds, IFD.data_group_movie_tag))

    def get_cam_data_group_focus(self):
        ptp = Container(
            OperationCode='GetCamDataGroupFocus',
            SessionID=self._session,
            TransactionID=self._transaction,
            Parameter=[]
        )
        return self._parse_ifd(self.recv(ptp), IFD.data_group_focus_tag)

    def set_cam_data_group_focus(self, ifds):
        ptp = Container(
            OperationCode='SetCamDataGroupFocus',
            SessionID=self._session,
            TransactionID=self._transaction,
            Parameter=[]
        )
        return self.send(ptp, self._build_ifd(ifds, IFD.data_group_focus_tag))

    def get_cam_can_set_info5(self):
        ptp = Container(
            OperationCode='GetCamCanSetInfo5',
            SessionID=self._session,
            TransactionID=self._transaction,
            Parameter=[]
        )
        return self._parse_ifd(self.recv(ptp), IFD.cam_can_set_info5_tag)
