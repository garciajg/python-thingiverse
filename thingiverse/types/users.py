
from datetime import datetime
from typing import Optional, Text, TypedDict, List
from thingiverse.types.search import Creator


class CurrentApp(TypedDict):
    id: int
    name: Text
    url: Text
    public_url: Text
    thumbnail: Text
    creator: Creator
    is_published: bool
    is_approved: bool


class ThingiverseUser(TypedDict):
    """Thingiverse User model"""
    id: int
    name: Text
    first_name: Text
    last_name: Text
    full_name: Text
    url: Text
    public_url: Text
    thumbnail: Text
    bio: Text
    bio_html: Text
    location: Text
    country: Text
    industry: Text
    subindustry: Text
    registered: datetime
    last_active: datetime
    cover_image: Text
    things_url: Text
    copies_url: Text
    likes_url: Text
    printers: List[Optional[Text]]
    programs: List[Optional[Text]]
    types: List[Optional[Text]]
    skill_level: Text
    accepts_tips: bool
    groups: List[Optional[Text]]
    website: Optional[Text]
    twitter: Optional[Text]
    count_of_followers: int
    count_of_following: int
    count_of_designs: int
    collection_count: int
    make_count: int
    like_count: int
    has_favorite: bool
    favorite_count: int
    is_admin: bool
    default_license: Text
    current_app: CurrentApp
