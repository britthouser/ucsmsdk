"""This module contains the general information for CommSvcEpFsmStage ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class CommSvcEpFsmStageConsts:
    LAST_UPDATE_TIME_ = ""
    NAME_NOP = "nop"
    NAME_RESTART_WEB_SVC_BEGIN = "restartWebSvcBegin"
    NAME_RESTART_WEB_SVC_FAIL = "restartWebSvcFail"
    NAME_RESTART_WEB_SVC_LOCAL = "restartWebSvcLocal"
    NAME_RESTART_WEB_SVC_PEER = "restartWebSvcPeer"
    NAME_RESTART_WEB_SVC_SUCCESS = "restartWebSvcSuccess"
    NAME_UPDATE_SVC_EP_BEGIN = "updateSvcEpBegin"
    NAME_UPDATE_SVC_EP_FAIL = "updateSvcEpFail"
    NAME_UPDATE_SVC_EP_INIT_IPTABLES_LOCAL = "updateSvcEpInitIptablesLocal"
    NAME_UPDATE_SVC_EP_INIT_IPTABLES_PEER = "updateSvcEpInitIptablesPeer"
    NAME_UPDATE_SVC_EP_PROPOGATE_EP_SETTINGS = "updateSvcEpPropogateEpSettings"
    NAME_UPDATE_SVC_EP_PROPOGATE_EP_TIME_ZONE_SETTINGS_LOCAL = "updateSvcEpPropogateEpTimeZoneSettingsLocal"
    NAME_UPDATE_SVC_EP_PROPOGATE_EP_TIME_ZONE_SETTINGS_PEER = "updateSvcEpPropogateEpTimeZoneSettingsPeer"
    NAME_UPDATE_SVC_EP_PROPOGATE_EP_TIME_ZONE_SETTINGS_TO_ADAPTORS_LOCAL = "updateSvcEpPropogateEpTimeZoneSettingsToAdaptorsLocal"
    NAME_UPDATE_SVC_EP_PROPOGATE_EP_TIME_ZONE_SETTINGS_TO_ADAPTORS_PEER = "updateSvcEpPropogateEpTimeZoneSettingsToAdaptorsPeer"
    NAME_UPDATE_SVC_EP_PROPOGATE_EP_TIME_ZONE_SETTINGS_TO_FEX_IOM_LOCAL = "updateSvcEpPropogateEpTimeZoneSettingsToFexIomLocal"
    NAME_UPDATE_SVC_EP_PROPOGATE_EP_TIME_ZONE_SETTINGS_TO_FEX_IOM_PEER = "updateSvcEpPropogateEpTimeZoneSettingsToFexIomPeer"
    NAME_UPDATE_SVC_EP_SET_EP_LOCAL = "updateSvcEpSetEpLocal"
    NAME_UPDATE_SVC_EP_SET_EP_PEER = "updateSvcEpSetEpPeer"
    NAME_UPDATE_SVC_EP_SUCCESS = "updateSvcEpSuccess"
    STAGE_STATUS_FAIL = "fail"
    STAGE_STATUS_IN_PROGRESS = "inProgress"
    STAGE_STATUS_NOP = "nop"
    STAGE_STATUS_PENDING = "pending"
    STAGE_STATUS_SKIP = "skip"
    STAGE_STATUS_SUCCESS = "success"
    STAGE_STATUS_THROTTLED = "throttled"


class CommSvcEpFsmStage(ManagedObject):
    """This is CommSvcEpFsmStage class."""

    consts = CommSvcEpFsmStageConsts()
    naming_props = set(['name'])

    mo_meta = MoMeta("CommSvcEpFsmStage", "commSvcEpFsmStage", "stage-[name]", VersionMeta.Version211a, "OutputOnly", 0xf, [], [""], ['commSvcEpFsm'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "last_update_time": MoPropertyMeta("last_update_time", "lastUpdateTime", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [""], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, None, None, None, None, ["nop", "restartWebSvcBegin", "restartWebSvcFail", "restartWebSvcLocal", "restartWebSvcPeer", "restartWebSvcSuccess", "updateSvcEpBegin", "updateSvcEpFail", "updateSvcEpInitIptablesLocal", "updateSvcEpInitIptablesPeer", "updateSvcEpPropogateEpSettings", "updateSvcEpPropogateEpTimeZoneSettingsLocal", "updateSvcEpPropogateEpTimeZoneSettingsPeer", "updateSvcEpPropogateEpTimeZoneSettingsToAdaptorsLocal", "updateSvcEpPropogateEpTimeZoneSettingsToAdaptorsPeer", "updateSvcEpPropogateEpTimeZoneSettingsToFexIomLocal", "updateSvcEpPropogateEpTimeZoneSettingsToFexIomPeer", "updateSvcEpSetEpLocal", "updateSvcEpSetEpPeer", "updateSvcEpSuccess"], []),
        "order": MoPropertyMeta("order", "order", "ushort", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "retry": MoPropertyMeta("retry", "retry", "byte", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "stage_status": MoPropertyMeta("stage_status", "stageStatus", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["fail", "inProgress", "nop", "pending", "skip", "success", "throttled"], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "lastUpdateTime": "last_update_time", 
        "name": "name", 
        "order": "order", 
        "retry": "retry", 
        "rn": "rn", 
        "sacl": "sacl", 
        "stageStatus": "stage_status", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.last_update_time = None
        self.order = None
        self.retry = None
        self.sacl = None
        self.stage_status = None
        self.status = None

        ManagedObject.__init__(self, "CommSvcEpFsmStage", parent_mo_or_dn, **kwargs)
