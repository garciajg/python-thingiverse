from datetime import datetime
from typing import Optional, Text, TypedDict, List


class Creator(TypedDict):
    id: int
    name: Text
    first_name: Text
    last_name: Text
    url: Text
    public_url: Text
    thumbnail: Text
    count_of_followers: int
    count_of_following: int
    count_of_designs: int
    accepts_tips: bool
    is_following: bool
    location: Text
    cover: Text


class Tag(TypedDict):
    name: Text
    tag: Text
    url: Text
    count: int
    things_url: Text
    absolute_url: Text


class SearchResult(TypedDict):
    id: int
    name: Text
    url: Text
    public_url: Text
    created_at: datetime
    thumbnail: Text
    preview_image: Text
    creator: Creator
    is_private: Optional[bool]
    is_purchased: Optional[bool]
    is_published: Optional[bool]
    comment_count: int
    make_count: int
    like_count: int
    tags: List[Tag]
    is_nsfw: bool


class SearchResponse(TypedDict):
    total: int
    hits: List[SearchResult]

