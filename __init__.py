# -*- coding: UTF-8 -*-
# Copyright (C) 2013 Armel FORTUN <armel.fortun@tchack.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from subprocess import Popen, PIPE
from re import search
import sys

# Import from itools
from itools.core import get_version, get_abspath

# Import from ikaaro
from ikaaro.skins import register_skin, Skin

from tchacker.utils import which

# Keep it, even if Pyflakes would remove it
from root import Root
import config_about_us

# The version
__version__ = get_version()

register_skin('tchack', Skin(get_abspath('ui/tchack/')))
register_skin('upload', Skin(get_abspath('ui/upload/')))


###########################################################################
# Check required software
###########################################################################
for name, cli in [
            ("ffmpeg", "ffmpeg")
            ]:
    if(which(cli)) is None:
        print 'You need to install "%s".' % name


def error_exit(message):
    #http://pydoc.net/Python/ngxtop/0.0.2/ngxtop.utils/
    sys.stderr.write(message)
    sys.exit(1)


def detect_nginx():
    #cmd = ["nginx", "-V"]
    #data = get_pipe(cmd)
    #print("detect_nginx() = %s" % data)
    try:
        proc = Popen(['/usr/sbin/nginx', '-V'], stderr=PIPE)
    except OSError:
        error_exit('Nginx not found. Perhaps Nginx is not in your PATH?\n')
    stdout, stderr = proc.communicate()
    version_output = stderr.decode('utf-8')
    upload_module_match = search(r'--add-module=.*(nginx-upload-module)', version_output)
    #conf_path_match = re.search(r'--conf-path=(\S*)', version_output)
    if upload_module_match is None:
        #print upload_module_match.group(1)
        print 'You need to install the Nginx module called: "upload-module".'


detect_nginx()


# For Pyflakes, shuut!
Root
