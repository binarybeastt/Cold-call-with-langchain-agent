from typing import Optional
from replit import db
from vocode.streaming.models.telephony import CallConfig
from vocode.streaming.telephony.config_manager.base_config_manager import (
    BaseConfigManager,
)


class ReplitConfigManager(BaseConfigManager):
    def __init__(self):
        self.configs = db

    def save_config(self, conversation_id: str, config: CallConfig):
        self.configs[conversation_id] = config.json()

    def get_config(self, conversation_id) -> Optional[CallConfig]:
        raw_config = self.configs.get(conversation_id)
        if raw_config:
            return CallConfig.parse_raw(raw_config)

    def delete_config(self, conversation_id):
        if conversation_id in self.configs:
            del self.configs[conversation_id]
