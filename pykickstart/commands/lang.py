#
# Chris Lumens <clumens@redhat.com>
#
# Copyright 2005, 2006, 2007 Red Hat, Inc.
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
from pykickstart.base import KickstartCommand
from pykickstart.errors import KickstartParseError, formatErrorMsg
from pykickstart.options import KSOptionParser, commaSplit

from pykickstart.i18n import _

class FC3_Lang(KickstartCommand):
    removedKeywords = KickstartCommand.removedKeywords
    removedAttrs = KickstartCommand.removedAttrs

    def __init__(self, writePriority=0, *args, **kwargs):
        KickstartCommand.__init__(self, writePriority, *args, **kwargs)
        self.op = self._getParser()
        self.lang = kwargs.get("lang", "")

    def __str__(self):
        retval = KickstartCommand.__str__(self)

        if self.lang != "":
            retval += "# System language\nlang %s\n" % self.lang

        return retval

    def _getParser(self):
        op = KSOptionParser()
        return op

    def parse(self, args):
        (ns, extra) = self.op.parse_known_args(args=args, lineno=self.lineno)

        if len(extra) != 1:
            raise KickstartParseError(formatErrorMsg(self.lineno, msg=_("Kickstart command %s requires one argument") % "lang"))
        elif any(arg for arg in extra if arg.startswith("-")):
            mapping = {"command": "lang", "options": extra}
            raise KickstartParseError(formatErrorMsg(self.lineno, msg=_("Unexpected arguments to %(command)s command: %(options)s") % mapping))

        self.lang = extra[0]
        self.set_to_self(ns)
        return self

class F19_Lang(FC3_Lang):
    removedKeywords = FC3_Lang.removedKeywords
    removedAttrs = FC3_Lang.removedAttrs

    def __init__(self, writePriority=0, *args, **kwargs):
        FC3_Lang.__init__(self, writePriority, *args, **kwargs)
        self.addsupport = kwargs.get("addsupport", [])

        self.op = self._getParser()

    def __str__(self):
        s = FC3_Lang.__str__(self)
        if s and self.addsupport:
            s = s.rstrip()
            s += " --addsupport=%s\n" % ",".join(self.addsupport)
        return s

    def _getParser(self):
        op = FC3_Lang._getParser(self)
        op.add_argument("--addsupport", type=commaSplit)
        return op
