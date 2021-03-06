#
# Chris Lumens <clumens@redhat.com>
#
# Copyright 2010 Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use, modify,
# copy, or redistribute it subject to the terms and conditions of the GNU
# General Public License v.2.  This program is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY expressed or implied, including the
# implied warranties of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.  Any Red Hat
# trademarks that are incorporated in the source code or documentation are not
# subject to the GNU General Public License and may only be used or replicated
# with the express permission of Red Hat, Inc. 
#
__all__ = ["RHEL6Handler"]

from pykickstart import commands
from pykickstart.base import BaseHandler
from pykickstart.version import RHEL6

class RHEL6Handler(BaseHandler):
    version = RHEL6

    commandMap = {
        "auth": commands.authconfig.FC3_Authconfig,
        "authconfig": commands.authconfig.FC3_Authconfig,
        "autopart": commands.autopart.RHEL6_AutoPart,
        "autostep": commands.autostep.FC3_AutoStep,
        "bootloader": commands.bootloader.RHEL6_Bootloader,
        "cdrom": commands.cdrom.FC3_Cdrom,
        "clearpart": commands.clearpart.FC3_ClearPart,
        "cmdline": commands.displaymode.FC3_DisplayMode,
        "device": commands.device.F8_Device,
        "deviceprobe": commands.deviceprobe.FC3_DeviceProbe,
        "dmraid": commands.dmraid.FC6_DmRaid,
        "driverdisk": commands.driverdisk.F12_DriverDisk,
        "fcoe": commands.fcoe.F13_Fcoe,
        "firewall": commands.firewall.F10_Firewall,
        "firstboot": commands.firstboot.FC3_Firstboot,
        "graphical": commands.displaymode.FC3_DisplayMode,
        "group": commands.group.F12_Group,
        "halt": commands.reboot.FC6_Reboot,
        "harddrive": commands.harddrive.FC3_HardDrive,
        "ignoredisk": commands.ignoredisk.RHEL6_IgnoreDisk,
        "install": commands.upgrade.F11_Upgrade,
        "interactive": commands.interactive.FC3_Interactive,
        "iscsi": commands.iscsi.RHEL6_Iscsi,
        "iscsiname": commands.iscsiname.FC6_IscsiName,
        "key": commands.key.RHEL5_Key,
        "keyboard": commands.keyboard.FC3_Keyboard,
        "lang": commands.lang.FC3_Lang,
        "logging": commands.logging.FC6_Logging,
        "logvol": commands.logvol.RHEL6_LogVol,
        "mediacheck": commands.mediacheck.FC4_MediaCheck,
        "method": commands.method.F13_Method,
        "monitor": commands.monitor.F10_Monitor,
        "multipath": commands.multipath.FC6_MultiPath,
        "network": commands.network.RHEL6_Network,
        "nfs": commands.nfs.FC6_NFS,
        "part": commands.partition.RHEL6_Partition,
        "partition": commands.partition.RHEL6_Partition,
        "poweroff": commands.reboot.FC6_Reboot,
        "raid": commands.raid.RHEL6_Raid,
        "reboot": commands.reboot.FC6_Reboot,
        "repo": commands.repo.RHEL6_Repo,
        "rescue": commands.rescue.F10_Rescue,
        "rootpw": commands.rootpw.F8_RootPw,
        "selinux": commands.selinux.FC3_SELinux,
        "services": commands.services.FC6_Services,
        "shutdown": commands.reboot.FC6_Reboot,
        "skipx": commands.skipx.FC3_SkipX,
        "sshpw": commands.sshpw.F13_SshPw,
        "text": commands.displaymode.FC3_DisplayMode,
        "timezone": commands.timezone.FC6_Timezone,
        "unsupported_hardware": commands.unsupported_hardware.RHEL6_UnsupportedHardware,
        "updates": commands.updates.F7_Updates,
        "upgrade": commands.upgrade.F11_Upgrade,
        "url": commands.url.RHEL6_Url,
        "user": commands.user.F12_User,
        "vnc": commands.vnc.F9_Vnc,
        "volgroup": commands.volgroup.FC16_VolGroup,
        "xconfig": commands.xconfig.F10_XConfig,
        "zerombr": commands.zerombr.F9_ZeroMbr,
        "zfcp": commands.zfcp.F12_ZFCP,
    }

    dataMap = {
        "DriverDiskData": commands.driverdisk.F12_DriverDiskData,
        "DeviceData": commands.device.F8_DeviceData,
        "DmRaidData": commands.dmraid.FC6_DmRaidData,
        "FcoeData": commands.fcoe.F13_FcoeData,
        "GroupData": commands.group.F12_GroupData,
        "IscsiData": commands.iscsi.RHEL6_IscsiData,
        "LogVolData": commands.logvol.RHEL6_LogVolData,
        "MultiPathData": commands.multipath.FC6_MultiPathData,
        "NetworkData": commands.network.RHEL6_NetworkData,
        "PartData": commands.partition.RHEL6_PartData,
        "RaidData": commands.raid.RHEL6_RaidData,
        "RepoData": commands.repo.RHEL6_RepoData,
        "SshPwData": commands.sshpw.F13_SshPwData,
        "UserData": commands.user.F12_UserData,
        "VolGroupData": commands.volgroup.FC16_VolGroupData,
        "ZFCPData": commands.zfcp.F12_ZFCPData,
    }
