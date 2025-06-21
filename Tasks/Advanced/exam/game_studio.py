def sort_games(*args, **kwargs):
    console = []
    pc = []

    game_title_to_platform = {title: platform for platform, title in args}

    for release_id, game_title in kwargs.items():
        platform = game_title_to_platform[game_title]
        if not platform:
            continue
        release_date = '_'.join(release_id.split("_")[:-1])
        entry_created = (release_id, release_date, game_title)
        if platform == "console":
            console.append(entry_created)
        elif platform == "pc":
            pc.append(entry_created)

    sorted_console = sorted(console, key=lambda x: x[0])
    sorted_pc = sorted(pc, key=lambda x: x[0], reverse=True)

    result = []

    if sorted_console:
        result.append("Console Games:")
        for _, release_date, title in sorted_console:
            result.append(f">>>{release_date}: {title}")

    if sorted_pc:
        result.append("PC Games:")
        for _, release_date, title in sorted_pc:
            result.append(f"<<<{release_date}: {title}")

    return '\n'.join(result)


print(sort_games(
    ("pc", "Iron Comet"),
    ("console", "Jungle Quest"),
    ("console", "Cyber Realm"),
    ("pc", "Neon Skyline"),
    ("console", "Blade Echo"),
    ("pc", "Sky Frontier"),
    April_12_2025_002="Neon Skyline",
    July_01_2025_004="Cyber Realm",
    July_01_2025_002="Blade Echo",
    December_31_2024_007="Jungle Quest",
    April_12_2025_005="Iron Comet",
    February_14_2025_009="Sky Frontier",
))
