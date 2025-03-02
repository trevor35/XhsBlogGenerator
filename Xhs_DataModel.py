# Title:小红书输出数据模式
# 2025/2/28 21:27
from typing import List

from langchain_core.pydantic_v1 import BaseModel, Field

class Xhs(BaseModel):
    titles: List[str] = Field(description="小红书的5个标题", min_items=5, max_items=5)
    content: str = Field(description="小红书的正文内容")
