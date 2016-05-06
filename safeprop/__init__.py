# -*- coding: utf-8 -*-
"""safeprop

Wrappers for CoolProp for safe property calculations.

:copyright: (c) 2016 by Andrew Hjortland
:licence: MIT, see LICENCE for more details

"""
from __future__ import absolute_import, unicode_literals

from .nomenclature import AirProperties, RefProperties
from .safeprop import airprop, phase, refprop

__banner__ = r"""
   ____     ___    ___
  / __/__ _/ _/__ / _ \_______  ___
 _\ \/ _ `/ _/ -_) ___/ __/ _ \/ _ \
/___/\_,_/_/ \__/_/  /_/  \___/ .__/
                             /_/      by Andrew Hjortland
"""

__title__ = 'safeprop'
__summary__ = 'Wrappers for CoolProp for safe property calculations.'
__uri__ = 'https://github.com/ahjortland/safeprop'

__version__ = '0.0.1'

__author__ = 'Andrew Hjortland'
__email__ = 'andrew.hjortland@gmail.com'

__license__ = 'MIT'
__copyright__ = 'Copyright 2016 Andrew Hjortland'
