from __future__ import annotations
#annotations
from typing import Any, Dict, Optional
#  从类型提示里面导入 任意，字典，可选择

# 就是说如果有大模型服务商 而且是openai兼容的即可使用这个parse_service
class AskMessageParseService:
    def __init__(self, *, generation_service: Optional[Any] = None) -> None:
        self.generation_service = generation_service

    def parse_message_action(self, *, message: str, working_context: Dict[str, Any]) -> Dict[str, Any]:
        if self.generation_service is None:
            return {}
        if getattr(self.generation_service, "mode", "disabled") != "openai-compatible":
            return {}
        try:
            payload = self.generation_service.generate_message_action_parse(
                message=message,
                working_context=working_context,
            )
        except Exception:
            return {}
        return payload if isinstance(payload, dict) else {}
