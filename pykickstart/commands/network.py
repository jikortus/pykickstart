#
# Chris Lumens <clumens@redhat.com>
#
# Copyright 2005, 2006, 2007 Red Hat, Inc.
#
# This software may be freely redistributed under the terms of the GNU
# general public license.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
from pykickstart.base import *
from pykickstart.constants import *
from pykickstart.errors import *
from pykickstart.options import *

from rhpl.translate import _
import rhpl.translate as translate

translate.textdomain("pykickstart")

class FC3NetworkData(BaseData):
    def __init__(self, bootProto=BOOTPROTO_DHCP, dhcpclass="", device="",
                 essid="", ethtool="", gateway="", hostname="", ip="",
                 mtu="", nameserver="", netmask="", nodns=False,
                 onboot=True, wepkey=""):
        BaseData.__init__(self)
        self.bootProto = bootProto
        self.dhcpclass = dhcpclass
        self.device = device
        self.essid = essid
        self.ethtool = ethtool
        self.gateway = gateway
        self.hostname = hostname
        self.ip = ip
        self.mtu = mtu
        self.nameserver = nameserver
        self.netmask = netmask
        self.nodns = nodns
        self.onboot = onboot
        self.wepkey = wepkey

    def __str__(self):
        retval = "network"

        if self.bootProto != "":
            retval += " --bootproto=%s" % self.bootProto
        if self.dhcpclass != "":
            retval += " --dhcpclass=%s" % self.dhcpclass
        if self.device != "":
            retval += " --device=%s" % self.device
        if self.essid != "":
            retval += " --essid=\"%s\"" % self.essid
        if self.ethtool != "":
            retval += " --ethtool=\"%s\"" % self.ethtool
        if self.gateway != "":
            retval += " --gateway=%s" % self.gateway
        if self.hostname != "":
            retval += " --hostname=%s" % self.hostname
        if self.ip != "":
            retval += " --ip=%s" % self.ip
        if self.mtu != "":
            retval += " --mtu=%s" % self.mtu
        if self.nameserver != "":
            retval += " --nameserver=%s" % self.nameserver
        if self.netmask != "":
            retval += " --netmask=%s" % self.netmask
        if self.nodns:
            retval += " --nodns"
        if self.onboot:
            retval += " --onboot=on"
        if self.wepkey != "":
            retval += " --wepkey=%s" % self.wepkey

        return retval + "\n"

class FC4NetworkData(FC3NetworkData):
    def __init__(self, bootProto=BOOTPROTO_DHCP, dhcpclass="", device="",
                 essid="", ethtool="", gateway="", hostname="", ip="",
                 mtu="", nameserver="", netmask="", nodns=False,
                 notksdevice=False, onboot=True, wepkey=""):
        FC3NetworkData.__init__(self, bootProto=bootProto,
                                dhcpclass=dhcpclass, device=device,
                                essid=essid, ethtool=ethtool,
                                gateway=gateway, hostname=hostname,
                                ip=ip, mtu=mtu, netmask=netmask,
                                nameserver=nameserver, nodns=nodns,
                                onboot=onboot, wepkey=wepkey)
        self.notksdevice = notksdevice

    def __str__(self):
        retval = FC3NetworkData.__str__(self).strip()

        if self.notksdevice:
            retval += " --notksdevice"

        return retval + "\n"

class FC6NetworkData(FC4NetworkData):
    def __init__(self, bootProto=BOOTPROTO_DHCP, dhcpclass="", device="",
                 essid="", ethtool="", gateway="", hostname="", ip="",
                 ipv4=True, ipv6=True, mtu="", nameserver="", netmask="",
                 nodns=False, notksdevice=False, onboot=True, wepkey=""):
        FC4NetworkData.__init__(self, bootProto=bootProto,
                                dhcpclass=dhcpclass, device=device,
                                essid=essid, ethtool=ethtool,
                                gateway=gateway, hostname=hostname,
                                ip=ip, mtu=mtu, netmask=netmask,
                                nameserver=nameserver, nodns=nodns,
                                notksdevice=notksdevice,
                                onboot=onboot, wepkey=wepkey)
        self.ipv4 = ipv4
        self.ipv6 = ipv6

    def __str__(self):
        retval = "network"

        if self.bootProto != "":
            retval += " --bootproto=%s" % self.bootProto
        if self.dhcpclass != "":
            retval += " --dhcpclass=%s" % self.dhcpclass
        if self.device != "":
            retval += " --device=%s" % self.device
        if self.essid != "":
            retval += " --essid=\"%s\"" % self.essid
        if self.ethtool != "":
            retval += " --ethtool=\"%s\"" % self.ethtool
        if self.gateway != "":
            retval += " --gateway=%s" % self.gateway
        if self.hostname != "":
            retval += " --hostname=%s" % self.hostname
        if self.ip != "":
            retval += " --ip=%s" % self.ip
        if not self.ipv4:
            retval += " --noipv4"
        if not self.ipv6:
            retval += " --noipv6"
        if self.mtu != "":
            retval += " --mtu=%s" % self.mtu
        if self.nameserver != "":
            retval += " --nameserver=%s" % self.nameserver
        if self.netmask != "":
            retval += " --netmask=%s" % self.netmask
        if self.nodns:
            retval += " --nodns"
        if self.notksdevice:
            retval += " --notksdevice"
        if self.onboot:
            retval += " --onboot=on"
        if self.wepkey != "":
            retval += " --wepkey=%s" % self.wepkey

        return retval + "\n"

class RHEL4NetworkData(FC3NetworkData):
    def __init__(self, bootProto=BOOTPROTO_DHCP, dhcpclass="", device="",
                 essid="", ethtool="", gateway="", hostname="", ip="",
                 mtu="", nameserver="", netmask="", nodns=False,
                 notksdevice=False, onboot=True, wepkey=""):
        FC3NetworkData.__init__(self, bootProto=bootProto,
                                dhcpclass=dhcpclass, device=device,
                                essid=essid, ethtool=ethtool,
                                gateway=gateway, hostname=hostname,
                                ip=ip, mtu=mtu, netmask=netmask,
                                nameserver=nameserver, nodns=nodns,
                                onboot=onboot, wepkey=wepkey)
        self.notksdevice = notksdevice

    def __str__(self):
        retval = FC3NetworkData.__str__(self).strip()

        if self.notksdevice:
            retval += " --notksdevice"

        return retval + "\n"

class FC3Network(KickstartCommand):
    def __init__(self, writePriority=0, network=None):
        KickstartCommand.__init__(self, writePriority)

        if network == None:
            network = []

        self.network = network

    def __str__(self):
        retval = ""

        for nic in self.network:
            retval += nic.__str__()

        if retval != "":
            return "# Network information\n" + retval
        else:
            return ""

    def parse(self, args):
        op = KSOptionParser(lineno=self.lineno)
        op.add_option("--bootproto", dest="bootProto",
                      default=BOOTPROTO_DHCP,
                      choices=[BOOTPROTO_DHCP, BOOTPROTO_BOOTP,
                               BOOTPROTO_STATIC])
        op.add_option("--class", dest="dhcpclass")
        op.add_option("--device", dest="device")
        op.add_option("--essid", dest="essid")
        op.add_option("--ethtool", dest="ethtool")
        op.add_option("--gateway", dest="gateway")
        op.add_option("--hostname", dest="hostname")
        op.add_option("--ip", dest="ip")
        op.add_option("--mtu", dest="mtu")
        op.add_option("--nameserver", dest="nameserver")
        op.add_option("--netmask", dest="netmask")
        op.add_option("--nodns", dest="nodns", action="store_true",
                      default=False)
        op.add_option("--onboot", dest="onboot", action="store",
                      type="ksboolean")
        op.add_option("--wepkey", dest="wepkey")

        (opts, extra) = op.parse_args(args=args)
        nd = FC3NetworkData()
        self._setToObj(op, opts, nd)
        self.add(nd)

    def add(self, newObj):
        self.network.append(newObj)

class FC4Network(FC3Network):
    def __init__(self, writePriority=0, network=None):
        FC3Network.__init__(self, writePriority, network)

    def parse(self, args):
        op = KSOptionParser(lineno=self.lineno)
        op.add_option("--bootproto", dest="bootProto",
                      default=BOOTPROTO_DHCP,
                      choices=[BOOTPROTO_DHCP, BOOTPROTO_BOOTP,
                               BOOTPROTO_STATIC])
        op.add_option("--class", dest="dhcpclass")
        op.add_option("--device", dest="device")
        op.add_option("--essid", dest="essid")
        op.add_option("--ethtool", dest="ethtool")
        op.add_option("--gateway", dest="gateway")
        op.add_option("--hostname", dest="hostname")
        op.add_option("--ip", dest="ip")
        op.add_option("--mtu", dest="mtu")
        op.add_option("--nameserver", dest="nameserver")
        op.add_option("--netmask", dest="netmask")
        op.add_option("--nodns", dest="nodns", action="store_true",
                      default=False)
        op.add_option("--notksdevice", dest="notksdevice", action="store_true",
                      default=False)
        op.add_option("--onboot", dest="onboot", action="store",
                      type="ksboolean")
        op.add_option("--wepkey", dest="wepkey")

        (opts, extra) = op.parse_args(args=args)
        nd = FC4NetworkData()
        self._setToObj(op, opts, nd)
        self.add(nd)

class FC6Network(FC4Network):
    def __init__(self, writePriority=0, network=None):
        FC4Network.__init__(self, writePriority, network)

    def parse(self, args):
        op = KSOptionParser(lineno=self.lineno)
        op.add_option("--bootproto", dest="bootProto",
                      default=BOOTPROTO_DHCP,
                      choices=[BOOTPROTO_DHCP, BOOTPROTO_BOOTP,
                               BOOTPROTO_STATIC])
        op.add_option("--class", dest="dhcpclass")
        op.add_option("--device", dest="device")
        op.add_option("--essid", dest="essid")
        op.add_option("--ethtool", dest="ethtool")
        op.add_option("--gateway", dest="gateway")
        op.add_option("--hostname", dest="hostname")
        op.add_option("--ip", dest="ip")
        op.add_option("--noipv4", dest="ipv4", action="store_false",
                      default=True)
        op.add_option("--noipv6", dest="ipv6", action="store_false",
                      default=True)
        op.add_option("--mtu", dest="mtu")
        op.add_option("--nameserver", dest="nameserver")
        op.add_option("--netmask", dest="netmask")
        op.add_option("--nodns", dest="nodns", action="store_true",
                      default=False)
        op.add_option("--notksdevice", dest="notksdevice", action="store_true",
                      default=False)
        op.add_option("--onboot", dest="onboot", action="store",
                      type="ksboolean")
        op.add_option("--wepkey", dest="wepkey")

        (opts, extra) = op.parse_args(args=args)
        nd = FC6NetworkData()
        self._setToObj(op, opts, nd)
        self.add(nd)

class RHEL4Network(FC3Network):
    def __init__(self, writePriority=0, network=None):
        FC3Network.__init__(self, writePriority, network)

    def parse(self, args):
        op = KSOptionParser(lineno=self.lineno)
        op.add_option("--bootproto", dest="bootProto",
                      default=BOOTPROTO_DHCP,
                      choices=[BOOTPROTO_DHCP, BOOTPROTO_BOOTP,
                               BOOTPROTO_STATIC])
        op.add_option("--class", dest="dhcpclass")
        op.add_option("--device", dest="device")
        op.add_option("--essid", dest="essid")
        op.add_option("--ethtool", dest="ethtool")
        op.add_option("--gateway", dest="gateway")
        op.add_option("--hostname", dest="hostname")
        op.add_option("--ip", dest="ip")
        op.add_option("--mtu", dest="mtu")
        op.add_option("--nameserver", dest="nameserver")
        op.add_option("--netmask", dest="netmask")
        op.add_option("--nodns", dest="nodns", action="store_true",
                      default=False)
        op.add_option("--notksdevice", dest="notksdevice", action="store_true",
                      default=False)
        op.add_option("--onboot", dest="onboot", action="store",
                      type="ksboolean")
        op.add_option("--wepkey", dest="wepkey")

        (opts, extra) = op.parse_args(args=args)
        nd = RHEL4NetworkData()
        self._setToObj(op, opts, nd)
        self.add(nd)