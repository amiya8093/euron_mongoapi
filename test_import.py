#!/usr/bin/env python
import traceback
try:
    print("Attempting to import main...")
    import main
    print("✓ main imported successfully")
    print(f"✓ app exists: {hasattr(main, 'app')}")
    print(f"✓ app type: {type(main.app)}")
except Exception as e:
    print(f"✗ Error importing main:")
    traceback.print_exc()
