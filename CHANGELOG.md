# 0.0.7.dev (2022-02-17)

- `handle_response_error()` method added
  - raises exception on error responses
  - Model added `thingivers.types.users.ThingiverseUser`
- `get_username_things()` method added (`/users/{username}/things`)
  - Fetches user's list of things
- get_username_favorites() method added (`/users/{username}/favorites`)
  - Fetches user's list of favorites
- get_username_likes() method added (`/users/{username}/likes`)
  - Fetches user's list of likes
- `get_username_copies()` method added (`/users/{username}/copies`)
  - Fetches user's list of copies
- `get_username_collections()` method added (`/users/{username}/collections`)
  - Fetches user's list of collections
- `get_username_downloads()` method added (`/users/{username}/downloads`)
  - Fetches user's list of downloads
- `get_username_collected_things()` method added (`/users/{username}/all-collected-things`)
  - Fetches a list of collected things by a given username
- `get_username_unread_message_count()` method added (`/users/unread-message-count`)
  - Fetches a count of unread messages

# 0.0.6rc1.dev (2022-02-14)

- `.dev` versioning started :)
- `ACCESS_TOKEN` added to tests
- `README.md` updated with documentation link and TODOs
- `get_user_by_username()` method added (`/users/{username}/`)
  - Fetches a user's information
  - Model added `thingivers.types.users.ThingiverseUser`
  - Tests added
- `get_users_data()` method added (`/users/{username}/search/{term?}`)
  - Fetches user's things data
  - Tests added

## 0.0.5 (2022-02-11)

- Version bump

## 0.0.5rc3 (2022-02-11)

- DOCS HOSTED!
- `pyproject.toml` updated

## 0.0.5rc2 (2022-02-10)

- Host-able documentation added
- Endpoints added
  - thing by id
  - thing images by id

## 0.0.5rc1 (2022-02-10)

- Bump version
- Poetry manages package now
- CI/CD for `development` to Test PyPI
- CI/CD from `main` to Official PyPI
- ...Everything in between `0.0.5rc1` and `0.0.2` was testing was testing...

## 0.0.2 (2022-02-10)

- Bump stable-ish version
- Tests added to CI/CD
- Sample files for `/search` endpoint responses
- Tests updated to be up to date (100% :)
- `thingy.authenticate()` delayed
- `term_library` and `autocomplete` delayed. Need to figure out API

## 0.0.2a2 (2022-02-10)

- Github Actions tweak

## 0.0.2a1 (2022-02-10)

- Version bump
- tagging started

## 0.0.1a4 (2022-02-10)

- `access_token` added as part of `Thingiverse` object.

## 0.0.1a3 (2022-02-10)

- `development` branch created,
- Github Actions tweaked to only run on `main` branch.


## 0.0.1a2 (2022-02-10)

- Add CHANGELOG :)
- Version bumped
- Github Actions added
- Github repo created :_)
- Tests setup
- API Setup
- Got requests working
- Sample of search response in `search_res.json`

(Anything before 0.0.1a2 was not recorded.)
