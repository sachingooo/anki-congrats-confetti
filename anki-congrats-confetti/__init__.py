# Congrats Confetti
#
# Copyright (C) 2022  Sachin Govind
#
# The main confetti of this addon (the confetti) was not written by me - that fantastic functionality is all thanks to loonywizard (https://github.com/loonywizard)
# All this addon does is call that confetti code in the right place on the overview screen!
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from aqt import mw
from aqt.overview import Overview

from anki.hooks import wrap
from . import externalJs


def _confetti(ov: Overview):
    jsToEvaluate = externalJs.confettiJs  # all credit to loonywizard for this
    jsToEvaluate += "\n\n" + """
        const confetti = new JSConfetti();
        confetti.addConfetti();
    """

    mw.web.eval(jsToEvaluate)


Overview._show_finished_screen = wrap(
    Overview._show_finished_screen, _confetti, "after")
