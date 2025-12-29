#!/usr/bin/env python3
"""
Modular Blueprint Generator
Generate blueprints in different layouts using reusable panel modules.

Usage:
    python generate_modular_blueprint.py 1                  # Generate UC-001 standard layout
    python generate_modular_blueprint.py 1 technical        # Generate UC-001 technical layout
    python generate_modular_blueprint.py 1 business         # Generate UC-001 business layout
    python generate_modular_blueprint.py                    # Generate all use cases, all layouts
    python generate_modular_blueprint.py all standard       # Generate all use cases, standard layout
"""

import sys
from blueprint_panels.assembler import BlueprintAssembler


def generate_single(use_case_id: int, layout: str = "standard"):
    """Generate single blueprint."""
    print(f"Generating UC-{use_case_id:03d} [{layout} layout]...", end=" ")
    
    try:
        assembler = BlueprintAssembler()
        filename = assembler.save_blueprint(use_case_id, layout)
        print(f"OK: {filename}")
        return True
    except Exception as e:
        print(f"ERROR: {e}")
        return False


def generate_all(layout: str = None):
    """Generate all use cases."""
    layouts = [layout] if layout else ["standard", "technical", "business"]
    
    print("=" * 60)
    print(f"Modular Blueprint Generator")
    print(f"Generating {len(layouts)} layout(s) for 24 use cases")
    print("=" * 60)
    
    total = 0
    success = 0
    
    for uc_id in range(1, 25):
        for layout_name in layouts:
            total += 1
            if generate_single(uc_id, layout_name):
                success += 1
    
    print("=" * 60)
    print(f"Completed: {success}/{total} blueprints generated")
    print("=" * 60)


def main():
    """Main entry point."""
    if len(sys.argv) == 1:
        # No arguments: generate all
        generate_all()
    
    elif sys.argv[1].lower() == "all":
        # "all [layout]": generate all use cases
        layout = sys.argv[2] if len(sys.argv) > 2 else None
        generate_all(layout)
    
    elif sys.argv[1].isdigit():
        # "<id> [layout]": generate single use case
        uc_id = int(sys.argv[1])
        layout = sys.argv[2] if len(sys.argv) > 2 else "standard"
        
        if uc_id < 1 or uc_id > 24:
            print("ERROR: Use case ID must be between 1 and 24")
            sys.exit(1)
        
        generate_single(uc_id, layout)
    
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == '__main__':
    main()

