# -*- coding: utf-8 -*-
# Copyright 2016 OpenMarket Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ._base import BaseSlavedStore
from ._slaved_id_tracker import SlavedIdTracker
from synapse.storage import DataStore


class SlavedDeviceInboxStore(BaseSlavedStore):
    def __init__(self, db_conn, hs):
        super(SlavedDeviceInboxStore, self).__init__(db_conn, hs)
        self._device_inbox_id_gen = SlavedIdTracker(
            db_conn, "device_inbox", "stream_id",
        )

    get_to_device_stream_token = DataStore.get_to_device_stream_token.__func__
    get_new_messages_for_device = DataStore.get_new_messages_for_device.__func__
    delete_messages_for_device = DataStore.delete_messages_for_device.__func__
