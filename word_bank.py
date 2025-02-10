words = [
    "a", "I", "is", "at", "to", "by", "in", "on", "of", "up", "we", "me", "be", "it",
    "its", "rum", "hum", "if", "no", "yes", "for", "cat", "dog", "fox", "hat", "run", "top",
    "van", "rat", "sun", "toy", "book", "fish", "blue", "rose", "star", "lock", "bike", "work",
    "tree", "zone", "apple", "bread", "clock", "dance", "earth", "flame", "grape", "house", "jewel",
    "kite", "market", "planet", "singer", "spring", "mango", "piano", "candy", "bridge", "stone",
    "tiger", "bicycle", "famous", "journey", "sunshine", "airport", "desert", "victory", "capture",
    "fortune", "glimpse", "boy", "man", "map", "tap", "cap", "car", "bag", "box", "pen", "fan", "kit",
    "bun", "pin", "lip", "bell", "salt", "pipe", "camp", "mark", "neck", "trip", "swim", "path", "race",
    "walk", "clue", "trap", "hill", "turn", "snow", "moon", "rain", "call", "milk", "hand", "hope", "wrap",
    "hook", "sew", "spine", "dive", "sleep", "play", "stop", "gold", "push", "seat", "ring", "lead", "snap",
    "clear", "face", "iron", "stem", "will", "rope", "cart", "surf", "oak", "pull", "fast", "wind", "mask",
    "coat", "smile", "wood", "palm", "bake", "rush", "kick", "lane", "mute", "help", "oak", "task", "grid",
    "wish", "show", "zoom", "hall", "bite", "club", "more", "home", "sound", "roll", "vibe", "step", "dust",
    "mood", "zap", "glow", "head", "warm", "chat", "puzzle", "tune", "cast", "draw", "fall", "gear", "leaf",
    "click", "loud", "file", "pick", "burn", "care", "bore", "stab", "slow", "grip", "case", "belt", "mist",
    "dash", "clay", "ball", "trick", "drop", "beam", "kill", "hit", "note", "move", "chill", "bright",
    "clamp", "best", "yell", "dice", "spot", "whip", "quick", "start", "maze", "fix", "tool", "hop", "set",
    "life", "pool", "loop", "shine", "lift", "trail", "mark", "golf", "cup", "shot", "block", "chime", "roam",
    "drum", "smile", "lock", "wind", "bar", "pin", "bed", "cage", "gray", "brush", "look", "sip", "dot", "slip",
    "coin", "trek", "fog", "wall", "drip", "pan", "jog", "ride", "land", "gap", "win", "blue", "hook", "peak",
    "hold", "sand", "bird", "dock", "new", "foot", "cart", "sew", "snap", "dove", "page", "call", "coat", "turn",
    "mix", "shine", "risk", "glue", "skip", "drop", "jog", "ride", "dash", "pipe", "hill", "side", "park",
    "luck", "rose", "snail", "bell", "deer", "cup", "hook", "child", "straw", "money", "pot", "knee", "love",
    "clash", "kite", "smack", "note", "race", "stone", "rays", "trap", "rise", "cup", "bottle", "stitch",
    "bone", "silver", "blue", "dream", "split", "spoon", "boxer", "frame", "load", "tool", "gear", "mood",
    "hood", "card", "skirt", "fall", "bowl", "grass", "grip", "blow", "burn", "snap", "grip", "grow",
    "double", "flower", "pearl", "neon", "teal", "coin", "rub", "pine", "tour", "candy", "soft",
    "plume", "flame", "size", "hike", "burn", "peel", "cup", "goat", "match", "talk", "mine",
    "world", "clasp", "hunt", "stem", "cross", "water", "south", "mirror", "quick", "prize", "straw",
    "fact", "leaf", "ship", "stock", "sword", "quick", "lotus", "rack", "pit", "loud", "fall",
    "swim", "dust", "flip", "speed", "track", "fish", "fix", "sail", "seat", "space", "jump", "jump",
    "luck", "pit", "smooth", "flash", "sit", "wind", "trust", "slap", "dash", "jump", "trap",
    "force", "tiger", "beach", "pillow", "stone", "map", "drill", "pink", "love", "deck", "snap",
    "field", "rock", "smile", "bright", "late", "goat", "swear", "hope", "kit", "race", "mist",
    "sit", "play", "trap", "goat", "pan", "tick", "plow", "cast", "jump", "wave", "pale", "shine"
]

character_total = 0

for word in words:
    word_count = len(word) + 1
    character_total += word_count

character_average = character_total / len(words)
print(f"The average number of characters is {character_average}.")
print(f" The list contains {len(words)} words.")