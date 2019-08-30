# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft import intent_handler


__author__ = 'l'

LOGGER = getLogger(__name__)


class ComedianSkill(MycroftSkill):
    def __init__(self):
        super(ComedianSkill, self).__init__(name="ComedianSkill")
    """
    # This is replaced by the @intent_handler
    def initialize(self):
        mitch_intent = IntentBuilder("MitchHedbergIntent"). \
            require("MitchKeyword").build()
        self.register_intent(mitch_intent,
                             self.handle_mitch_intent)
    """
    @intent_handler(IntentBuilder("mitchIntent").require("MitchKeyword"))  # noqa
    def handle_mitch_intent(self, message):
        self.speak_dialog("mitch")

    @intent_handler(IntentBuilder("stephenIntent").require("StephenKeyword"))  # noqa
    def handle_stephen_intent(self, message):
        self.speak_dialog("stephen")

    @intent_handler(IntentBuilder("rodneyIntent").require("RodneyKeyword"))  # noqa
    def handle_rodney_intent(self, message):
        self.speak_dialog("rodney")

    def stop(self):
        pass


def create_skill():
    return ComedianSkill()
