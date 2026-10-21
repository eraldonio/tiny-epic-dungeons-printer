"""
Database of all items from Tiny Epic Dungeons (Dized Rules).
"""

ITEMS = [
    # --- REGULAR LOOT CARDS ---
    {
        "id": 1,
        "name": "Amethyst Figurine",
        "type": "Trinket",
        "category": "Loot Card",
        "set": None,
        "description": "Anytime you perform an Intellect check, roll 1 additional die (3 dice limit applies).",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/9c7dd44b-01bd-4f3c-ab7e-9a3ed80d1824-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 2,
        "name": "Crossbow",
        "type": "Hand",
        "category": "Loot Card",
        "set": None,
        "description": "Perform a Missile Attack using Agility at a target up to 3 spaces away from you in a straight path (target cannot be in your space), and add 1 to your die total.\n\nWhenever you perform a Missile Attack, immediately gain 1 focus.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/e9f156ac-1a1e-4ce1-8f69-36f1ff977e73-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 3,
        "name": "Cursed Dragonscale",
        "type": "Garb",
        "category": "Loot Card",
        "set": None,
        "description": "Your Defense is decreased by 1.\nAnytime you perform a Strength, Agility, or Intellect check, add 1 to your die result.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/b52f60ec-12f2-444a-af80-54014af4e15c-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 4,
        "name": "Elven Chain",
        "type": "Garb",
        "category": "Loot Card",
        "set": None,
        "description": "Your Defense and Speed are both increased by 1.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/ff73ba95-09c1-4c21-a28a-c32d01dd013b-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 5,
        "name": "Hook Shot",
        "type": "Hand",
        "category": "Loot Card",
        "set": None,
        "description": "Perform a Melee Attack using Strength and add 1 to your die result...\nOR, perform a Missile Attack using Agility at a target 1 space away from you in a straight path (target cannot be in your space) and add 1 to your die result.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/61f717ca-3818-4bcb-ab16-08292809af5f-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 6,
        "name": "Jade Figurine",
        "type": "Trinket",
        "category": "Loot Card",
        "set": None,
        "description": "Anytime you perform an Agility check, roll 1 additional die (3 dice limit applies).",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/a28f5c09-d804-4965-aa5f-d519051a6039-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 7,
        "name": "Ruby Figurine",
        "type": "Trinket",
        "category": "Loot Card",
        "set": None,
        "description": "Anytime you perform a Strength check, roll 1 additional die (3 dice limit applies).",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/8c9f5c94-c60d-4287-8316-1df919ccfd89-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 8,
        "name": "Spiked Buckler",
        "type": "Hand",
        "category": "Loot Card",
        "set": None,
        "description": "Whenever you perform a Melee Attack, your Defense is increased by 1 and add 1 to your die total if performing a Strength check for the attack.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/d69fb2c3-5773-4210-b14e-8ca3efe35c18-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 9,
        "name": "Sun Hammer",
        "type": "Hand",
        "category": "Loot Card",
        "set": None,
        "description": "Perform a Melee Attack using Strength and add 1 to your die result.\n\nWhenever you perform a Melee Attack, immediately gain 1 focus.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/e0e07dc5-5828-441e-93cd-9c35aa4e60ca-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 10,
        "name": "Violet Cape",
        "type": "Garb",
        "category": "Loot Card",
        "set": None,
        "description": "Whenever you perform a Missile Attack or Cast a Spell, your Defense is increased by 1.\nAnytime you perform an Intellect check, add 1 to your die result.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/4dc3d57d-476b-4543-9136-1b1221485ab2-d41d8cd98f00b204e9800998ecf8427e.png"
    },

    # --- SET OF THE BEAR ---
    {
        "id": 11,
        "name": "Great Axe of the Bear",
        "type": "Hand",
        "category": "Legendary Item",
        "set": "The Set of the Bear",
        "set_bonus": "Whenever you perform a Melee Attack, add (1/2/3) to your die total if you have (2/3/4) pieces of the set equipped.",
        "description": "Perform a Melee Attack using Strength and add 2 to your result.\nYour Speed is decreased by 1.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/3bbe35c6-4e3e-4958-b11a-645f0dfb8202-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 12,
        "name": "Studded Jerkin of the Bear",
        "type": "Garb",
        "category": "Legendary Item",
        "set": "The Set of the Bear",
        "set_bonus": "Whenever you perform a Melee Attack, add (1/2/3) to your die total if you have (2/3/4) pieces of the set equipped.",
        "description": "Whenever you perform a Melee Attack, your Defense is increased by 1.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/e26c8e71-f20d-40f4-8b49-8d33517d6278-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 13,
        "name": "Throwing Axes of the Bear",
        "type": "Hand",
        "category": "Legendary Item",
        "set": "The Set of the Bear",
        "set_bonus": "Whenever you perform a Melee Attack, add (1/2/3) to your die total if you have (2/3/4) pieces of the set equipped.",
        "description": "Perform a Missile Attack using Strength at a target 2 spaces away from you in a straight path (target cannot be in your space) and add 2 to your result.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/63d6089f-14da-4b03-9e3a-c9c295fedcfc-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 14,
        "name": "War Horn of the Bear",
        "type": "Trinket",
        "category": "Legendary Item",
        "set": "The Set of the Bear",
        "set_bonus": "Whenever you perform a Melee Attack, add (1/2/3) to your die total if you have (2/3/4) pieces of the set equipped.",
        "description": "Free Action: Spend 2 focus to move all enemies within 4 spaces, up to 2 spaces each, with you controlling their movement.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/794c8adf-fc7d-4fa0-b796-3291cb0d7da8-d41d8cd98f00b204e9800998ecf8427e.png"
    },

    # --- SET OF THE LION ---
    {
        "id": 15,
        "name": "Greaves of the Lion",
        "type": "Trinket",
        "category": "Legendary Item",
        "set": "The Set of the Lion",
        "set_bonus": "Whenever you perform a Melee Attack, you heal (1/2/3) health if you have (2/3/4) pieces of the set equipped.",
        "description": "Your Speed is increased by 1.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/4bfbbbd4-b3d0-4bb6-942d-4b9435f3e2b3-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 16,
        "name": "Long Sword of the Lion",
        "type": "Hand",
        "category": "Legendary Item",
        "set": "The Set of the Lion",
        "set_bonus": "Whenever you perform a Melee Attack, you heal (1/2/3) health if you have (2/3/4) pieces of the set equipped.",
        "description": "Perform a Melee Attack using Strength and add 1 to your result.\nWhenever you perform a Melee Attack, you may spend 2 focus to add 1 to your die result.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/0ba9bd19-3755-432c-ba4a-563ea9c24ef2-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 17,
        "name": "Platemail of the Lion",
        "type": "Garb",
        "category": "Legendary Item",
        "set": "The Set of the Lion",
        "set_bonus": "Whenever you perform a Melee Attack, you heal (1/2/3) health if you have (2/3/4) pieces of the set equipped.",
        "description": "Your Defense is increased by 1.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/586fda16-816f-4763-b106-f1f4f9119368-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 18,
        "name": "Shield of the Lion",
        "type": "Hand",
        "category": "Legendary Item",
        "set": "The Set of the Lion",
        "set_bonus": "Whenever you perform a Melee Attack, you heal (1/2/3) health if you have (2/3/4) pieces of the set equipped.",
        "description": "Whenever you perform a Melee Attack your Defense is increased by 1.\nWhenever you perform a Melee Attack, you may reroll one of your Hero Dice (only once per attack).",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/e05e05b6-829c-49b5-8405-0a91091df3a4-d41d8cd98f00b204e9800998ecf8427e.png"
    },

    # --- SET OF THE PANTHER ---
    {
        "id": 19,
        "name": "Claw of the Panther",
        "type": "Hand",
        "category": "Legendary Item",
        "set": "The Set of the Panther",
        "set_bonus": "Whenever you perform a Missile Attack, add (1/2/3) to your die result if you have (2/3/4) pieces of the set equipped.",
        "description": "Perform a Melee Attack using Agility and add 1 to your die result.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/34035e9c-f70f-4dbf-903b-654f381e0186-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 20,
        "name": "Cloak of the Panther",
        "type": "Garb",
        "category": "Legendary Item",
        "set": "The Set of the Panther",
        "set_bonus": "Whenever you perform a Missile Attack, add (1/2/3) to your die result if you have (2/3/4) pieces of the set equipped.",
        "description": "Stealth: While moving, you may move through enemies (instead of stopping).",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/0aafa6bc-0fdb-4b1c-9622-2562a2bfc752-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 21,
        "name": "Glove of the Panther",
        "type": "Trinket",
        "category": "Legendary Item",
        "set": "The Set of the Panther",
        "set_bonus": "Whenever you perform a Missile Attack, add (1/2/3) to your die result if you have (2/3/4) pieces of the set equipped.",
        "description": "Anytime you perform an Agility check, add 1 to your die result.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/13a3d148-8071-4142-a7f1-a113275daa40-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 22,
        "name": "Long Bow of the Panther",
        "type": "Hand",
        "category": "Legendary Item",
        "set": "The Set of the Panther",
        "set_bonus": "Whenever you perform a Missile Attack, add (1/2/3) to your die result if you have (2/3/4) pieces of the set equipped.",
        "description": "Perform a Missile Attack using Agility at a target up to 4 spaces away in a straight path (target cannot be in your space)...\nOR, spend 3 Focus to perform a Missile Attack targeting all enemies within 1 space of you (including your own space).",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/0544d2eb-755d-4250-a7f4-d05587463982-d41d8cd98f00b204e9800998ecf8427e.png"
    },

    # --- SET OF THE PHOENIX ---
    {
        "id": 23,
        "name": "Great Staff of the Phoenix",
        "type": "Hand",
        "category": "Legendary Item",
        "set": "The Set of the Phoenix",
        "set_bonus": "Whenever you Cast a Spell, immediately gain (1/2/3) focus if you have (2/3/4) pieces of the set equipped.",
        "description": "Perform a Missile Attack using Intellect at a target up to 3 spaces away in a straight path (target cannot be in your space).",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/c0fc5c0c-6615-4bb7-986c-2c9072565fec-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 24,
        "name": "Ring of the Phoenix",
        "type": "Trinket",
        "category": "Legendary Item",
        "set": "The Set of the Phoenix",
        "set_bonus": "Whenever you Cast a Spell, immediately gain (1/2/3) focus if you have (2/3/4) pieces of the set equipped.",
        "description": "When you Cast a Spell that deals damage, you deal 1 additional damage to a target of the attack. If it targets multiple enemies, increase the damage dealt by 1 to a single target of your choice.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/8f79b639-fbb1-4af1-a8c6-1ad6c10742e3-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 25,
        "name": "Robes of the Phoenix",
        "type": "Garb",
        "category": "Legendary Item",
        "set": "The Set of the Phoenix",
        "set_bonus": "Whenever you Cast a Spell, immediately gain (1/2/3) focus if you have (2/3/4) pieces of the set equipped.",
        "description": "Free Action: Spend 2 Focus to place your hero to any revealed room in the Dungeon (cannot teleport onto Boss Mat).",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/abe67c7d-228d-4b39-af88-3fb45d65629c-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 26,
        "name": "Spell Tome of the Phoenix",
        "type": "Hand",
        "category": "Legendary Item",
        "set": "The Set of the Phoenix",
        "set_bonus": "Whenever you Cast a Spell, immediately gain (1/2/3) focus if you have (2/3/4) pieces of the set equipped.",
        "description": "Anytime you perform a Intellect check, add 1 to your die result.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/19a6280b-561c-481a-aaca-13846ec0eec0-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    # --- STORIES EXPANSION: SET OF THE VIPER ---
    {
        "id": 27,
        "name": "Eyes of the Viper",
        "type": "Trinket",
        "category": "Stories Expansion",
        "set": "The Set of the Viper",
        "set_bonus": "Whenever the Torch reaches an Enemy Actions space, immediately deal (1/2/3) damage to all enemies in your space.",
        "description": "Free Action: Spend 3 focus to reveal an unexplored room anywhere in the dungeon.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/9c7dd44b-01bd-4f3c-ab7e-9a3ed80d1824-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 28,
        "name": "Shadow Gi of the Viper",
        "type": "Garb",
        "category": "Stories Expansion",
        "set": "The Set of the Viper",
        "set_bonus": "Whenever the Torch reaches an Enemy Actions space, immediately deal (1/2/3) damage to all enemies in your space.",
        "description": "Your Speed is increased by 1.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/ff73ba95-09c1-4c21-a28a-c32d01dd013b-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 29,
        "name": "Smoke Bombs of the Viper",
        "type": "Hand",
        "category": "Stories Expansion",
        "set": "The Set of the Viper",
        "set_bonus": "Whenever the Torch reaches an Enemy Actions space, immediately deal (1/2/3) damage to all enemies in your space.",
        "description": "Perform a Melee Attack using Agility.\nAfter performing a melee attack, you may perform one additional melee attack without rolling the enemy die (-1 from your die result).",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/61f717ca-3818-4bcb-ab16-08292809af5f-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 30,
        "name": "Fangs of the Viper",
        "type": "Hand",
        "category": "Stories Expansion",
        "set": "The Set of the Viper",
        "set_bonus": "Whenever the Torch reaches an Enemy Actions space, immediately deal (1/2/3) damage to all enemies in your space.",
        "description": "Limit 1x per turn: Perform a Melee Attack using Agility.\nAfter a successful attack (dealing 1+ damage), place your hero in any revealed room (except Boss Mat).",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/0aafa6bc-0fdb-4b1c-9622-2562a2bfc752-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    # --- STORIES EXPANSION: SET OF THE SCARAB ---
    {
        "id": 31,
        "name": "Mage Blade of the Scarab",
        "type": "Hand",
        "category": "Stories Expansion",
        "set": "The Set of the Scarab",
        "set_bonus": "Whenever you perform a Melee Attack, gain +(1/2/3) Defense for that attack if you have (2/3/4) pieces equipped.",
        "description": "Perform a Melee Attack using Agility and add 1 to your die result.\nLimit 1x per turn: When you perform a melee attack, immediately gain 2 focus.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/0ba9bd19-3755-432c-ba4a-563ea9c24ef2-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 32,
        "name": "Vestment of the Scarab",
        "type": "Garb",
        "category": "Stories Expansion",
        "set": "The Set of the Scarab",
        "set_bonus": "Whenever you perform a Melee Attack, gain +(1/2/3) Defense for that attack if you have (2/3/4) pieces equipped.",
        "description": "Anytime you perform an Intellect check, add 1 to your die result.\nWhenever you Cast a Spell, your Defense is increased by 1.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/586fda16-816f-4763-b106-f1f4f9119368-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 33,
        "name": "Orbs of the Scarab",
        "type": "Trinket",
        "category": "Stories Expansion",
        "set": "The Set of the Scarab",
        "set_bonus": "Whenever you perform a Melee Attack, gain +(1/2/3) Defense for that attack if you have (2/3/4) pieces equipped.",
        "description": "Whenever you perform a Rest Action, gain an additional 2 health, 3 focus, and gain a new Spell from the deck or discard row.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/a28f5c09-d804-4965-aa5f-d519051a6039-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    {
        "id": 34,
        "name": "Ward of the Scarab",
        "type": "Hand",
        "category": "Stories Expansion",
        "set": "The Set of the Scarab",
        "set_bonus": "Whenever you perform a Melee Attack, gain +(1/2/3) Defense for that attack if you have (2/3/4) pieces equipped.",
        "description": "Anytime you perform a Strength check, add 1 to your die result.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/e05e05b6-829c-49b5-8405-0a91091df3a4-d41d8cd98f00b204e9800998ecf8427e.png"
    },
    # --- STORIES EXPANSION: MISCELLANEOUS LOOT ---
    {
        "id": 35,
        "name": "Dungeon Map",
        "type": "Trinket",
        "category": "Stories Expansion",
        "set": None,
        "description": "Your Speed is increased by 1.\nWhenever you perform a Rest Action, you may reveal any unexplored dungeon rooms within 1 space of you.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/f1795cb3-ab3f-448c-8263-42ba69178e3b-765cfa56e0cb183b0d9ed3179b221af3.png"
    },
    {
        "id": 36,
        "name": "Bedrolls",
        "type": "Trinket",
        "category": "Stories Expansion",
        "set": None,
        "description": "Whenever you perform a Rest Action, all heroes within 2 spaces of you (including yourself) also gain 2 health and 3 focus.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/c3083c09-58e7-4ea3-a0b3-5ba88cfc4e12-765cfa56e0cb183b0d9ed3179b221af3.png"
    },
    {
        "id": 37,
        "name": "Everlit Torch",
        "type": "Trinket",
        "category": "Stories Expansion",
        "set": None,
        "description": "Whenever the Torch reaches an 'Enemy Actions' space on the torch track, you may reveal an adjacent unexplored room tile.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/868abb6d-342f-43b6-9f94-bcd136ed52f8-765cfa56e0cb183b0d9ed3179b221af3.png"
    },
    {
        "id": 38,
        "name": "Ceremonial Spear",
        "type": "Hand",
        "category": "Stories Expansion",
        "set": None,
        "description": "Perform a Melee Attack using Strength or a Missile Attack using Agility at a target 1 space away in a straight path.\nAdds +1 to Skill Checks and Intellect checks.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/21156874-67b1-4158-9b68-efd5a3f2a681-765cfa56e0cb183b0d9ed3179b221af3.png"
    }
]

SPELLS = [
    {
        "id": 1,
        "name": "Chain Lightning",
        "type": "Spell",
        "category": "Spell Card",
        "set": None,
        "description": "Perform an Intellect check of 6. If successful, spend 3 focus to deal 1 damage to up to 2 different targets, each which are within 2 spaces of you along any path (cannot target the same enemy twice).",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/8d3e5981-25ab-4768-a07e-1cbcd16e93fa-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/spell_1.png"
    },
    {
        "id": 2,
        "name": "Claw of Darkness",
        "type": "Spell",
        "category": "Spell Card",
        "set": None,
        "description": "Perform an Intellect check of 6. If successful, spend 4 focus and deal 3 damage to a target up to 2 spaces away along any path. If unsuccessful, move the torch down 1 space on the torch track.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/a0b6e9ff-4c11-49a5-8401-513736692053-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/spell_2.png"
    },
    {
        "id": 3,
        "name": "Conjurer’s Gambit",
        "type": "Spell",
        "category": "Spell Card",
        "set": None,
        "description": "Perform an Intellect check of 7. If successful, spend 5 focus and deal 1 damage to every enemy that is in your space and adjacent spaces.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/c38de80d-c89c-40b2-ab38-032f01dd4481-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/spell_3.png"
    },
    {
        "id": 4,
        "name": "Cloud of Death",
        "type": "Spell",
        "category": "Spell Card",
        "set": None,
        "description": "Perform an Intellect check of 6. If successful, spend 4 focus and deal 2 damage to all enemies in your space.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/be11a6c2-76ee-4070-9f8a-07f05c7fd1c5-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/spell_4.png"
    },
    {
        "id": 5,
        "name": "Dark Bargain",
        "type": "Spell",
        "category": "Spell Card",
        "set": None,
        "description": "Perform an Intellect check of 7. If successful, spend 4 focus for all heroes to immediately gain full health and full focus, then move the torch down 2 spaces on the torch track.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/2273806d-1535-45fe-b5a9-b3eda33bb4d5-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/spell_5.png"
    },
    {
        "id": 6,
        "name": "Delver’s Luck",
        "type": "Spell",
        "category": "Spell Card",
        "set": None,
        "description": "Perform a skill check of 7 using the skill of your choice. If successful, draw 3 Loot cards, keep 1, and place the other 2 on the bottom of the loot deck.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/06e72388-b1a4-428d-804a-0e131b40aefa-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/spell_6.png"
    },
    {
        "id": 7,
        "name": "Dungeon Scry",
        "type": "Spell",
        "category": "Spell Card",
        "set": None,
        "description": "Perform a skill check of 5 using a skill of your choice. If successful, spend 2 focus to look at the top 3 cards of the Dungeon deck and return them in any order you choose.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/31719fe1-d977-4e37-8c1b-ac01afc445ab-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/spell_7.png"
    },
    {
        "id": 8,
        "name": "Eagle’s Swiftness",
        "type": "Spell",
        "category": "Spell Card",
        "set": None,
        "description": "Perform an Intellect check of 3. If successful, spend 3 focus to perform a free Move action with +2 Speed.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/41eacde0-80e8-4acd-a194-302f15e04cd6-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/spell_8.png"
    },
    {
        "id": 9,
        "name": "Elemental Charge",
        "type": "Spell",
        "category": "Spell Card",
        "set": None,
        "description": "Perform a skill check of 5 using a skill of your choice. If successful, spend 2 focus to add 2 additional dice of the chosen skill to your next attack this turn.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/a96f1dc4-16cc-4d1d-8474-52f8f0def258-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/spell_9.png"
    },
    {
        "id": 10,
        "name": "Fireball",
        "type": "Spell",
        "category": "Spell Card",
        "set": None,
        "description": "Perform an Intellect check of 7. If successful, spend 6 focus and deal 3 damage to all enemies in a target space up to 2 spaces away along any path.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/b2f1946a-fc4c-40b9-b7c1-49c12ae8a688-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/spell_10.png"
    },
    {
        "id": 11,
        "name": "Giant’s Strength",
        "type": "Spell",
        "category": "Spell Card",
        "set": None,
        "description": "Perform a Intellect check of 3. If successful, spend 3 focus to perform a Melee Attack using Strength at a target in your space. Add 2 to your die total and gain 1 focus for the attack.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/644ca2b5-6996-47c3-9ad5-6c2939877c8a-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/spell_11.png"
    },
    {
        "id": 12,
        "name": "Holy Abundance",
        "type": "Spell",
        "category": "Spell Card",
        "set": None,
        "description": "Perform an Intellect check of 5. If successful, spend 4 focus for all heroes within 1 space of you (including yourself) to gain 3 health and 2 focus.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/bca2b63e-b08c-408b-ada0-237f5c00d95b-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/spell_12.png"
    },
    {
        "id": 13,
        "name": "Invisibility",
        "type": "Spell",
        "category": "Spell Card",
        "set": None,
        "description": "Perform a skill check of 5 using a skill of your choice. If successful, spend 2 focus. Until the start of your next turn, you cannot be targeted by enemy attacks and may freely move through rooms with enemies without checking for danger.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/6c46e86c-b191-4899-aed7-f86b6b344916-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/spell_13.png"
    },
    {
        "id": 14,
        "name": "Tempest of Arrows",
        "type": "Spell",
        "category": "Spell Card",
        "set": None,
        "description": "Perform an Intellect check of 6. If successful, spend 5 focus to deal 2 damage to up to 2 different targets within 3 spaces of you in a straight path (target cannot be in your space).",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/d110b531-3b19-41b8-9ed1-44ac2db2791a-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/spell_14.png"
    }
]

HEROES = [
    {
        "id": 1,
        "name": "Ethairna",
        "type": "Hero",
        "title": "Elf Sorceress",
        "category": "Hero Mat",
        "set": "Elf Sorceress",
        "edition": "Base Game",
        "health": 6, "focus": 8, "speed": 4, "defense": 3,
        "dice": {"strength": 1, "agility": 2, "intellect": 3},
        "primary_ability": "Seeking Bolt: Perform an Intellect check of 5. If successful, spend 2 focus and deal 1 damage to a target within 4 spaces along any path.",
        "weapon": "Dagger: Perform a Melee Attack using Strength and subtract 1 from your dice roll result.",
        "secondary_ability": "Research (Free Action): Spend 4 focus to discover a Spell from the deck or from the discard row.",
        "description": "Max HP: 6  |  Max Focus: 8  |  Speed: 4  |  Def: 3\nDice: [STR 1]  [AGI 2]  [INT 3]\n\n★ PRIMARY ABILITY:\nSeeking Bolt: Perform an Intellect check of 5. If successful, spend 2 focus and deal 1 damage to a target within 4 spaces along any path.\n\n⚔ WEAPONS / ACTIONS:\nDagger: Perform a Melee Attack using Strength and subtract 1 from your dice roll result.\n\n⚡ SPECIAL ACTION:\nResearch (Free Action): Spend 4 focus to discover a Spell from the deck or from the discard row.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/797a2a38-16e2-4f95-ba01-45cef2d302c1-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/hero_1.png"
    },
    {
        "id": 2,
        "name": "Gerrund the Blue",
        "type": "Hero",
        "title": "Ancient Wizard",
        "category": "Hero Mat",
        "set": "Ancient Wizard",
        "edition": "Base Game",
        "health": 5, "focus": 8, "speed": 3, "defense": 4,
        "dice": {"strength": 1, "agility": 2, "intellect": 3},
        "primary_ability": "Magic Arrow: Perform an Intellect check of 6. If successful, spend 2 focus and deal 2 damage to a target within 2 spaces along any path.",
        "weapon": "Dagger: Perform a Melee Attack using Strength and subtract 1 from your dice roll result.",
        "secondary_ability": "Research (Free Action): Spend 4 focus to discover a Spell from the deck or from the discard row.",
        "description": "Max HP: 5  |  Max Focus: 8  |  Speed: 3  |  Def: 4\nDice: [STR 1]  [AGI 2]  [INT 3]\n\n★ PRIMARY ABILITY:\nMagic Arrow: Perform an Intellect check of 6. If successful, spend 2 focus and deal 2 damage to a target within 2 spaces along any path.\n\n⚔ WEAPONS / ACTIONS:\nDagger: Perform a Melee Attack using Strength and subtract 1 from your dice roll result.\n\n⚡ SPECIAL ACTION:\nResearch (Free Action): Spend 4 focus to discover a Spell from the deck or from the discard row.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/e00959eb-76a4-4ea0-8179-71abe73ed329-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/hero_2.png"
    },
    {
        "id": 3,
        "name": "Grok U’ll",
        "type": "Hero",
        "title": "Half-Orc Barbarian",
        "category": "Hero Mat",
        "set": "Half-Orc Barbarian",
        "edition": "Base Game",
        "health": 8, "focus": 4, "speed": 3, "defense": 2,
        "dice": {"strength": 3, "agility": 2, "intellect": 1},
        "primary_ability": "Battle Rage: Whenever you perform a Melee or Missile Attack action, you may spend 3 focus to add 2 to your die result.",
        "weapon": "Axe: Perform a Melee Attack using Strength and add 1 to your dice roll result.",
        "secondary_ability": "Sprint (Free Action): Spend 1 focus to increase your Speed by 1 for the turn.",
        "description": "Max HP: 8  |  Max Focus: 4  |  Speed: 3  |  Def: 2\nDice: [STR 3]  [AGI 2]  [INT 1]\n\n★ PRIMARY ABILITY:\nBattle Rage: Whenever you perform a Melee or Missile Attack action, you may spend 3 focus to add 2 to your die result.\n\n⚔ WEAPONS / ACTIONS:\nAxe: Perform a Melee Attack using Strength and add 1 to your dice roll result.\n\n⚡ SPECIAL ACTION:\nSprint (Free Action): Spend 1 focus to increase your Speed by 1 for the turn.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/464c4bd2-0e24-4dfd-b9d6-cd8f925d828c-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/hero_3.png"
    },
    {
        "id": 4,
        "name": "Moonblade",
        "type": "Hero",
        "title": "Wood Elf Rogue",
        "category": "Hero Mat",
        "set": "Wood Elf Rogue",
        "edition": "Base Game",
        "health": 6, "focus": 5, "speed": 5, "defense": 3,
        "dice": {"strength": 2, "agility": 3, "intellect": 1},
        "primary_ability": "Shadow Walk: Perform an Agility check of 6. If successful, spend 3 focus to move up to your speed, ignoring enemies, and deal 1 damage to all targets in the space where your movement ends.",
        "weapon": "Dagger: Perform a Melee Attack using Strength and subtract 1 from your dice roll result.",
        "secondary_ability": "Lockpick (Free Action): Spend 2 focus to perform a Disarm Trap Action.",
        "description": "Max HP: 6  |  Max Focus: 5  |  Speed: 5  |  Def: 3\nDice: [STR 2]  [AGI 3]  [INT 1]\n\n★ PRIMARY ABILITY:\nShadow Walk: Perform an Agility check of 6. If successful, spend 3 focus to move up to your speed, ignoring enemies, and deal 1 damage to all targets in the space where your movement ends.\n\n⚔ WEAPONS / ACTIONS:\nDagger: Perform a Melee Attack using Strength and subtract 1 from your dice roll result.\n\n⚡ SPECIAL ACTION:\nLockpick (Free Action): Spend 2 focus to perform a Disarm Trap Action.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/694da3bd-0dac-4f76-840f-1483090bc2ed-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/hero_4.png"
    },
    {
        "id": 5,
        "name": "Sir Lanon",
        "type": "Hero",
        "title": "Human Paladin",
        "category": "Hero Mat",
        "set": "Human Paladin",
        "edition": "Base Game",
        "health": 8, "focus": 5, "speed": 3, "defense": 5,
        "dice": {"strength": 3, "agility": 1, "intellect": 2},
        "primary_ability": "Divine Might: Perform an Intellect check of 4. If successful, spend 2 focus to perform a Melee Attack and add 2 to your die result.",
        "weapon": "Hammer: Perform a Melee Attack using Strength.",
        "secondary_ability": "Healing Hands (Free Action): Spend 2 focus to heal 1 Hero within 1 room (can be self) 2 health.",
        "description": "Max HP: 8  |  Max Focus: 5  |  Speed: 3  |  Def: 5\nDice: [STR 3]  [AGI 1]  [INT 2]\n\n★ PRIMARY ABILITY:\nDivine Might: Perform an Intellect check of 4. If successful, spend 2 focus to perform a Melee Attack and add 2 to your die result.\n\n⚔ WEAPONS / ACTIONS:\nHammer: Perform a Melee Attack using Strength.\n\n⚡ SPECIAL ACTION:\nHealing Hands (Free Action): Spend 2 focus to heal 1 Hero within 1 room (can be self) 2 health.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/9ec692ef-4e54-4e80-8ea1-d48d23bf6b20-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/hero_5.png"
    },
    {
        "id": 6,
        "name": "Thordin Firebraid",
        "type": "Hero",
        "title": "Dwarf Fighter",
        "category": "Hero Mat",
        "set": "Dwarf Fighter",
        "edition": "Base Game",
        "health": 7, "focus": 5, "speed": 3, "defense": 4,
        "dice": {"strength": 3, "agility": 2, "intellect": 1},
        "primary_ability": "Stone Stance: While performing a Melee Attack, you may spend 2 focus to increase your Defense by 2 (may do this after the Enemy Die roll).",
        "weapon": "Hammer: Perform a Melee Attack using Strength.",
        "secondary_ability": "Shield Bash (Free Action): Spend 5 focus to instantly kill 1 Goblin in your room.",
        "description": "Max HP: 7  |  Max Focus: 5  |  Speed: 3  |  Def: 4\nDice: [STR 3]  [AGI 2]  [INT 1]\n\n★ PRIMARY ABILITY:\nStone Stance: While performing a Melee Attack, you may spend 2 focus to increase your Defense by 2 (may do this after the Enemy Die roll).\n\n⚔ WEAPONS / ACTIONS:\nHammer: Perform a Melee Attack using Strength.\n\n⚡ SPECIAL ACTION:\nShield Bash (Free Action): Spend 5 focus to instantly kill 1 Goblin in your room.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/563fd40c-d8ed-4d63-9b64-4115ddbae203-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/hero_6.png"
    },
    {
        "id": 7,
        "name": "Uliessa",
        "type": "Hero",
        "title": "Dwarf Cleric",
        "category": "Hero Mat",
        "set": "Dwarf Cleric",
        "edition": "Base Game",
        "health": 6, "focus": 7, "speed": 4, "defense": 5,
        "dice": {"strength": 2, "agility": 1, "intellect": 3},
        "primary_ability": "Heal: Whenever you Cast a Spell, you may also spend 2 focus to heal 1 Hero up to 3 rooms away 4 health (can be self).",
        "weapon": "Hammer: Perform a Melee Attack using Strength.",
        "secondary_ability": "Research (Free Action): Spend 4 focus to discover a Spell from the deck or from the discard row.",
        "description": "Max HP: 6  |  Max Focus: 7  |  Speed: 4  |  Def: 5\nDice: [STR 2]  [AGI 1]  [INT 3]\n\n★ PRIMARY ABILITY:\nHeal: Whenever you Cast a Spell, you may also spend 2 focus to heal 1 Hero up to 3 rooms away 4 health (can be self).\n\n⚔ WEAPONS / ACTIONS:\nHammer: Perform a Melee Attack using Strength.\n\n⚡ SPECIAL ACTION:\nResearch (Free Action): Spend 4 focus to discover a Spell from the deck or from the discard row.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/4416a2d6-2c60-47bb-98a9-606be9b0d150-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/hero_7.png"
    },
    {
        "id": 8,
        "name": "Wyn Keleas",
        "type": "Hero",
        "title": "Elf Ranger",
        "category": "Hero Mat",
        "set": "Elf Ranger",
        "edition": "Base Game",
        "health": 7, "focus": 5, "speed": 4, "defense": 3,
        "dice": {"strength": 2, "agility": 3, "intellect": 1},
        "primary_ability": "Stealth (Free Action): Spend 2 focus to move through enemies (instead of stopping).",
        "weapon": "Dagger: Perform a Melee Attack using Strength and subtract 1 from your dice roll result.\nBow: Perform a Missile Attack using Agility, targeting an enemy up to 2 rooms away in a straight path (not same room) and subtract 1 from your die result.",
        "secondary_ability": None,
        "description": "Max HP: 7  |  Max Focus: 5  |  Speed: 4  |  Def: 3\nDice: [STR 2]  [AGI 3]  [INT 1]\n\n★ PRIMARY ABILITY:\nStealth (Free Action): Spend 2 focus to move through enemies (instead of stopping).\n\n⚔ WEAPONS / ACTIONS:\nDagger: Perform a Melee Attack using Strength and subtract 1 from your dice roll result.\nBow: Perform a Missile Attack using Agility, targeting an enemy up to 2 rooms away in a straight path (not same room) and subtract 1 from your die result.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/c04df1d6-e8f4-49fc-86da-33e500415fc9-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/hero_8.png"
    },
    {
        "id": 9,
        "name": "Zui Xiong",
        "type": "Hero",
        "title": "Pandakin Brewmaster",
        "category": "Hero Mat",
        "set": "Pandakin Brewmaster",
        "edition": "Stories Expansion",
        "health": 8, "focus": 6, "speed": 4, "defense": 4,
        "dice": {"strength": 1, "agility": 1, "intellect": 1},
        "primary_ability": "Intoxication (Free Action): Lose 1 health to roll 2 additional dice for any skill check (3 dice limit still applies).",
        "weapon": "Spiked Tankard: Perform a Melee Attack using Strength.",
        "secondary_ability": "Hair o’ the Dog (Free Action): Spend 2 focus to heal yourself 1 hit point.",
        "description": "Max HP: 8  |  Max Focus: 6  |  Speed: 4  |  Def: 4\nDice: [STR 1]  [AGI 1]  [INT 1]\n\n★ PRIMARY ABILITY:\nIntoxication (Free Action): Lose 1 health to roll 2 additional dice for any skill check (3 dice limit still applies).\n\n⚔ WEAPONS / ACTIONS:\nSpiked Tankard: Perform a Melee Attack using Strength.\n\n⚡ SPECIAL ACTION:\nHair o’ the Dog (Free Action): Spend 2 focus to heal yourself 1 hit point.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/797a2a38-16e2-4f95-ba01-45cef2d302c1-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/hero_9.png"
    },
    {
        "id": 10,
        "name": "Nili Songheart",
        "type": "Hero",
        "title": "Bard",
        "category": "Hero Mat",
        "set": "Bard",
        "edition": "Stories Expansion",
        "health": 6, "focus": 7, "speed": 5, "defense": 4,
        "dice": {"strength": 2, "agility": 2, "intellect": 2},
        "primary_ability": "Inspire (Free Action): Spend 2 focus to roll 1 additional die for any skill check (3 dice limit still applies).",
        "weapon": "Rapier: Perform a Melee Attack using Strength.",
        "secondary_ability": "Terrify (Free Action): Spend 1 focus to move 1 enemy (within 3 rooms of you) 1 room through an open corridor.",
        "description": "Max HP: 6  |  Max Focus: 7  |  Speed: 5  |  Def: 4\nDice: [STR 2]  [AGI 2]  [INT 2]\n\n★ PRIMARY ABILITY:\nInspire (Free Action): Spend 2 focus to roll 1 additional die for any skill check (3 dice limit still applies).\n\n⚔ WEAPONS / ACTIONS:\nRapier: Perform a Melee Attack using Strength.\n\n⚡ SPECIAL ACTION:\nTerrify (Free Action): Spend 1 focus to move 1 enemy (within 3 rooms of you) 1 room through an open corridor.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/c04df1d6-e8f4-49fc-86da-33e500415fc9-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/hero_10.png"
    },
    {
        "id": 11,
        "name": "Sir Gamelyn",
        "type": "Hero",
        "title": "Grand Marshal",
        "category": "Hero Mat",
        "set": "Grand Marshal",
        "edition": "Stories Expansion",
        "health": 8, "focus": 5, "speed": 3, "defense": 5,
        "dice": {"strength": 2, "agility": 2, "intellect": 2},
        "primary_ability": "Zeal: Whenever you perform a Melee Attack, you may spend 2 focus to add 1 to your die result and increase your Defense by 1.",
        "weapon": "Sword: Perform a Melee Attack using Strength.",
        "secondary_ability": "Inspiration (Free Action): Spend 1 focus to have another hero within 3 rooms gain 1 focus.",
        "description": "Max HP: 8  |  Max Focus: 5  |  Speed: 3  |  Def: 5\nDice: [STR 2]  [AGI 2]  [INT 2]\n\n★ PRIMARY ABILITY:\nZeal: Whenever you perform a Melee Attack, you may spend 2 focus to add 1 to your die result and increase your Defense by 1.\n\n⚔ WEAPONS / ACTIONS:\nSword: Perform a Melee Attack using Strength.\n\n⚡ SPECIAL ACTION:\nInspiration (Free Action): Spend 1 focus to have another hero within 3 rooms gain 1 focus.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/9ec692ef-4e54-4e80-8ea1-d48d23bf6b20-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/hero_11.png"
    },
    {
        "id": 12,
        "name": "Zezili",
        "type": "Hero",
        "title": "Monk",
        "category": "Hero Mat",
        "set": "Monk",
        "edition": "Stories Expansion",
        "health": 7, "focus": 6, "speed": 4, "defense": 4,
        "dice": {"strength": 2, "agility": 2, "intellect": 2},
        "primary_ability": "Tiger Strike: Perform an Intellect check of 4. If successful, kill 1 Goblin in your space and gain 2 focus.",
        "weapon": "Bo Staff: Perform a Melee Attack using Agility and subtract 1 from your dice roll result.",
        "secondary_ability": "Inner Focus (Free Action): Spend 6 focus to perform 1 additional action during your turn (limit 1x per turn).",
        "description": "Max HP: 7  |  Max Focus: 6  |  Speed: 4  |  Def: 4\nDice: [STR 2]  [AGI 2]  [INT 2]\n\n★ PRIMARY ABILITY:\nTiger Strike: Perform an Intellect check of 4. If successful, kill 1 Goblin in your space and gain 2 focus.\n\n⚔ WEAPONS / ACTIONS:\nBo Staff: Perform a Melee Attack using Agility and subtract 1 from your dice roll result.\n\n⚡ SPECIAL ACTION:\nInner Focus (Free Action): Spend 6 focus to perform 1 additional action during your turn (limit 1x per turn).",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/563fd40c-d8ed-4d63-9b64-4115ddbae203-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/hero_12.png"
    },
    {
        "id": 13,
        "name": "Lara Gambit",
        "type": "Hero",
        "title": "Adventurer",
        "category": "Hero Mat",
        "set": "Adventurer",
        "edition": "Stories Expansion",
        "health": 7, "focus": 6, "speed": 4, "defense": 4,
        "dice": {"strength": 2, "agility": 2, "intellect": 2},
        "primary_ability": "Treasure Heist (Free Action): Spend 2 focus to pick up 1 Loot/Spell from the discard row.",
        "weapon": "Dagger: Perform a Melee Attack using Strength and subtract 1 from your dice roll result.\nBullwhip: Perform a Missile Attack using Agility, targeting an enemy up to 1 room away in a straight line (not same room) and subtract 1 from your die result.",
        "secondary_ability": None,
        "description": "Max HP: 7  |  Max Focus: 6  |  Speed: 4  |  Def: 4\nDice: [STR 2]  [AGI 2]  [INT 2]\n\n★ PRIMARY ABILITY:\nTreasure Heist (Free Action): Spend 2 focus to pick up 1 Loot/Spell from the discard row.\n\n⚔ WEAPONS / ACTIONS:\nDagger: Perform a Melee Attack using Strength and subtract 1 from your dice roll result.\nBullwhip: Perform a Missile Attack using Agility, targeting an enemy up to 1 room away in a straight line (not same room) and subtract 1 from your die result.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/694da3bd-0dac-4f76-840f-1483090bc2ed-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/hero_13.png"
    },
    {
        "id": 14,
        "name": "Evelynn",
        "type": "Hero",
        "title": "Druid",
        "category": "Hero Mat",
        "set": "Druid",
        "edition": "Stories Expansion",
        "health": 6, "focus": 8, "speed": 4, "defense": 4,
        "dice": {"strength": 1, "agility": 2, "intellect": 3},
        "primary_ability": "Healing Wind: Whenever you Cast a Spell, you may also spend 2 focus to heal all Heroes up to 2 rooms away 2 health (including yourself).",
        "weapon": "Shillelagh: Perform a Melee Attack using Strength.",
        "secondary_ability": "Research (Free Action): Spend 4 focus to discover a Spell from the deck or from the discard row.",
        "description": "Max HP: 6  |  Max Focus: 8  |  Speed: 4  |  Def: 4\nDice: [STR 1]  [AGI 2]  [INT 3]\n\n★ PRIMARY ABILITY:\nHealing Wind: Whenever you Cast a Spell, you may also spend 2 focus to heal all Heroes up to 2 rooms away 2 health (including yourself).\n\n⚔ WEAPONS / ACTIONS:\nShillelagh: Perform a Melee Attack using Strength.\n\n⚡ SPECIAL ACTION:\nResearch (Free Action): Spend 4 focus to discover a Spell from the deck or from the discard row.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/4416a2d6-2c60-47bb-98a9-606be9b0d150-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/hero_14.png"
    },
    {
        "id": 15,
        "name": "Aetoris",
        "type": "Hero",
        "title": "Necromancer",
        "category": "Hero Mat",
        "set": "Necromancer",
        "edition": "Stories Expansion",
        "health": 6, "focus": 7, "speed": 3, "defense": 5,
        "dice": {"strength": 1, "agility": 2, "intellect": 3},
        "primary_ability": "Life Steal: Perform an Intellect check of 5. If successful, spend 3 focus to deal 1 damage to 1 enemy, up to 2 rooms away from you using any path and heal 1 damage from any hero (including yourself) also within 2 rooms of you using any path.",
        "weapon": "Dagger: Perform a Melee Attack using Strength and subtract 1 from your dice roll result.",
        "secondary_ability": "Research (Free Action): Spend 4 focus to discover a Spell from the deck or from the discard row.",
        "description": "Max HP: 6  |  Max Focus: 7  |  Speed: 3  |  Def: 5\nDice: [STR 1]  [AGI 2]  [INT 3]\n\n★ PRIMARY ABILITY:\nLife Steal: Perform an Intellect check of 5. If successful, spend 3 focus to deal 1 damage to 1 enemy, up to 2 rooms away from you using any path and heal 1 damage from any hero (including yourself) also within 2 rooms of you using any path.\n\n⚔ WEAPONS / ACTIONS:\nDagger: Perform a Melee Attack using Strength and subtract 1 from your dice roll result.\n\n⚡ SPECIAL ACTION:\nResearch (Free Action): Spend 4 focus to discover a Spell from the deck or from the discard row.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/e00959eb-76a4-4ea0-8179-71abe73ed329-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/hero_15.png"
    },
    {
        "id": 16,
        "name": "Clotho",
        "type": "Hero",
        "title": "Psychic",
        "category": "Hero Mat",
        "set": "Psychic",
        "edition": "Stories Expansion",
        "health": 5, "focus": 8, "speed": 4, "defense": 4,
        "dice": {"strength": 1, "agility": 2, "intellect": 3},
        "primary_ability": "Psychic Blast: Perform an Intellect check of 5. If successful, spend 2 focus to deal 1 damage to all enemies in your space and 1 space away from you.",
        "weapon": "Dagger: Perform a Melee Attack using Strength and subtract 1 from your dice roll result.",
        "secondary_ability": "Research (Free Action): Spend 4 focus to discover a Spell from the deck or from the discard row.",
        "description": "Max HP: 5  |  Max Focus: 8  |  Speed: 4  |  Def: 4\nDice: [STR 1]  [AGI 2]  [INT 3]\n\n★ PRIMARY ABILITY:\nPsychic Blast: Perform an Intellect check of 5. If successful, spend 2 focus to deal 1 damage to all enemies in your space and 1 space away from you.\n\n⚔ WEAPONS / ACTIONS:\nDagger: Perform a Melee Attack using Strength and subtract 1 from your dice roll result.\n\n⚡ SPECIAL ACTION:\nResearch (Free Action): Spend 4 focus to discover a Spell from the deck or from the discard row.",
        "image_url": "https://assets.dized.app/project/29a0b155-919c-446c-8545-48f47f448305/en-US/eb51938ff9a3aaa135a6ae051260d1ab/797a2a38-16e2-4f95-ba01-45cef2d302c1-d41d8cd98f00b204e9800998ecf8427e.png",
        "local_image": "images/hero_16.png"
    }
]
