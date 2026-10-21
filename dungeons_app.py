"""
Tiny Epic Dungeons - Interactive Thermal Card Printing Application
"""

import argparse
import sys
from pathlib import Path

from dungeons_data import ITEMS, SPELLS, HEROES

ALL_CARDS = ITEMS + SPELLS + HEROES
from card_renderer import render_dungeon_item_card
from funprint.client import FunPrinter, FunPrintConnectionError, FunPrintJobError

BANNER = r"""
╔══════════════════════════════════════════════════════════════╗
║             TINY EPIC DUNGEONS - ITEM COMPENDIUM             ║
║            Thermal Card Printer for Dized Rules              ║
╚══════════════════════════════════════════════════════════════╝
"""


def list_items(items_subset: list[dict]):
    print("\n" + "─" * 62)
    print(f"{'#':<4} {'NAME':<28} {'SLOT':<10} {'CATEGORY'}")
    print("─" * 62)
    for item in items_subset:
        cat = item['set'] if item.get('set') else item.get('category', 'Loot')
        print(f"[{item['id']:02d}] {item['name']:<28} {item['type']:<10} {cat}")
    print("─" * 62)


def display_item_details(item: dict):
    print("\n" + "═" * 62)
    print(f"  {item['name'].upper()}")
    print("═" * 62)
    slot_info = f"Slot: {item['type']}  |  Category: {item['category']}"
    if item.get('set'):
        slot_info += f"  |  Set: {item['set']}"
    print(slot_info)
    print("─" * 62)
    if item.get("set_bonus"):
        print(f"★ Set Bonus:\n  {item['set_bonus']}\n")
    print(f"★ Rules / Effect:\n  {item['description']}")
    print("═" * 62)


def print_item(item: dict, mac: str = "48:0F:57:28:B4:FD", feed: int = 90):
    print(f"\n[1/3] Generating card image for '{item['name']}'...")
    card_img = render_dungeon_item_card(item)

    print(f"[2/3] Connecting to thermal printer ({mac})...")
    printer = FunPrinter(address=mac)

    print(f"[3/3] Streaming card raster to printer...")
    printer.print_image(card_img, feed=feed, dither=True)
    print(f"\n>>> '{item['name']}' PRINTED SUCCESSFULLY! <<<\n")


def find_item_by_query(query: str) -> list[dict]:
    query_lower = query.strip().lower()
    matches = []
    for it in ALL_CARDS:
        if query_lower == str(it['id']) or (query_lower.startswith("s") and query_lower[1:] == str(it['id']) and it['type'] == "Spell"):
            matches.append(it)
        elif query_lower in it['name'].lower() or (it.get('set') and query_lower in it['set'].lower()):
            matches.append(it)
    return matches


def interactive_loop(mac: str):
    print(BANNER)

    while True:
        print("\nCATEGORIES:")
        print("  [1] All Items (1–38)")
        print("  [2] Base Game Loot (10 items)")
        print("  [3] The Set of the Bear (4 items)")
        print("  [4] The Set of the Lion (4 items)")
        print("  [5] The Set of the Panther (4 items)")
        print("  [6] The Set of the Phoenix (4 items)")
        print("  [7] The Set of the Viper (4 items - Stories)")
        print("  [8] The Set of the Scarab (4 items - Stories)")
        print("  [9] Stories Expansion Loot (4 items)")
        print("  [10] Spell Cards (14 spells)")
        print("  [11] Hero Cards (16 heroes - Base & Stories)")
        print("  [S] Search by Name / Keyword")
        print("  [Q] Quit")
        choice = input("\nSelect an option: ").strip().lower()

        if choice == "q":
            print("\nGoodbye, adventurer!")
            break
        elif choice == "1":
            active_list = ITEMS
        elif choice == "2":
            active_list = [i for i in ITEMS if not i.get('set') and i.get('category') != "Stories Expansion"]
        elif choice == "3":
            active_list = [i for i in ITEMS if i.get('set') == "The Set of the Bear"]
        elif choice == "4":
            active_list = [i for i in ITEMS if i.get('set') == "The Set of the Lion"]
        elif choice == "5":
            active_list = [i for i in ITEMS if i.get('set') == "The Set of the Panther"]
        elif choice == "6":
            active_list = [i for i in ITEMS if i.get('set') == "The Set of the Phoenix"]
        elif choice == "7":
            active_list = [i for i in ITEMS if i.get('set') == "The Set of the Viper"]
        elif choice == "8":
            active_list = [i for i in ITEMS if i.get('set') == "The Set of the Scarab"]
        elif choice == "9":
            active_list = [i for i in ITEMS if not i.get('set') and i.get('category') == "Stories Expansion"]
        elif choice == "10":
            active_list = SPELLS
        elif choice == "11":
            active_list = HEROES
        elif choice == "s":
            q = input("Enter search term (e.g. 'sword', 'axe', 'dragon', 'fireball', 'sorceress'): ").strip()
            active_list = find_item_by_query(q)
            if not active_list:
                print(f"No items found matching '{q}'.")
                continue
        else:
            print("Invalid selection.")
            continue

        # Show list
        list_items(active_list)

        # Select item
        while True:
            sel = input("\nEnter item number to view (or 'b' to go back): ").strip().lower()
            if sel == "b":
                break
            
            selected_item = None
            try:
                item_id = int(sel)
                for it in active_list:
                    if it['id'] == item_id:
                        selected_item = it
                        break
            except ValueError:
                matches = find_item_by_query(sel)
                if matches:
                    selected_item = matches[0]

            if not selected_item:
                print(f"Item '{sel}' not found in current view.")
                continue

            display_item_details(selected_item)

            action = input("Press [P] to PRINT on thermal printer, [B] Back to list, [Q] Quit: ").strip().lower()
            if action == "p":
                try:
                    print_item(selected_item, mac=mac)
                except (FunPrintConnectionError, FunPrintJobError) as e:
                    print(f"\nPrinting error: {e}", file=sys.stderr)
            elif action == "q":
                print("\nGoodbye, adventurer!")
                return


def main():
    parser = argparse.ArgumentParser(description="Tiny Epic Dungeons - Thermal Card Printing CLI")
    parser.add_argument("--list", "-l", action="store_true", help="List all items and exit")
    parser.add_argument("--spells", action="store_true", help="List all spells and exit")
    parser.add_argument("--heroes", action="store_true", help="List all heroes and exit")
    parser.add_argument("--print", "-p", type=str, metavar="CARD", help="Print an item, spell, or hero by ID or name and exit")
    parser.add_argument("--preview", type=str, metavar="CARD", help="Save rendered PNG preview without printing")
    parser.add_argument("--mac", "-m", type=str, default="48:0F:57:28:B4:FD", help="Printer Bluetooth MAC address")
    parser.add_argument("--feed", "-f", type=int, default=90, help="Paper feed lines (default: 90)")
    parser.add_argument("--web", "-w", action="store_true", help="Launch the Web Bluetooth interface in your browser")
    args = parser.parse_args()

    if args.web:
        import http.server
        import socketserver
        import webbrowser
        import os
        from pathlib import Path
        
        web_dir = Path(__file__).resolve().parent / "web"
        port = 8765
        os.chdir(web_dir)
        handler = http.server.SimpleHTTPRequestHandler
        httpd = None
        for p in [port, 8766, 8767, 8768]:
            try:
                socketserver.TCPServer.allow_reuse_address = True
                httpd = socketserver.TCPServer(("", p), handler)
                port = p
                break
            except OSError:
                continue

        if not httpd:
            print("Could not bind to any web port.")
            return

        print(BANNER)
        print(f"🚀 Serving Tiny Epic Dungeons Web App at http://localhost:{port}/")
        print("👉 Opening in your browser (Google Chrome, Edge, or Opera)...")
        webbrowser.open(f"http://localhost:{port}/")
        try:
            with httpd:
                httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nWeb server stopped. Goodbye!")
        return
    if args.list:
        print(BANNER)
        list_items(ITEMS)
        return
    if args.spells:
        print(BANNER)
        print("SPELL CARDS:")
        list_items(SPELLS)
        return
    if args.heroes:
        print(BANNER)
        print("HERO CARDS (STATS & ABILITIES):")
        list_items(HEROES)
        return
    if args.preview:
        matches = find_item_by_query(args.preview)
        if not matches:
            print(f"Error: Item '{args.preview}' not found.")
            sys.exit(1)
        item = matches[0]
        card_img = render_dungeon_item_card(item)
        out_path = f"/tmp/dungeon_item_{item['id']}_{item['name'].replace(' ', '_')}.png"
        card_img.save(out_path)
        print(f"Saved card preview to: {out_path}")
        return

    if args.print:
        matches = find_item_by_query(args.print)
        if not matches:
            print(f"Error: Item '{args.print}' not found.")
            sys.exit(1)
        item = matches[0]
        display_item_details(item)
        try:
            print_item(item, mac=args.mac, feed=args.feed)
        except (FunPrintConnectionError, FunPrintJobError) as e:
            print(f"Printing failed: {e}", file=sys.stderr)
            sys.exit(1)
        return

    # Default to interactive mode
    try:
        interactive_loop(mac=args.mac)
    except KeyboardInterrupt:
        print("\n\nOperation cancelled. Goodbye!")


if __name__ == "__main__":
    main()
