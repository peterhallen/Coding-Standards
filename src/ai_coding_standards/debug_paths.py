"""Debug script to help diagnose package data path issues."""

# pylint: disable=all

from pathlib import Path


def main() -> None:
    """Main debug function."""
    print("=" * 60)
    print("Package Data Path Debugging")
    print("=" * 60)

    # Check if package is installed
    try:
        import importlib.util

        spec = importlib.util.find_spec("ai_coding_standards")
        if spec and spec.origin:
            pkg_dir = Path(spec.origin).parent
            print(f"\nPackage location: {pkg_dir}")
            print(f"Is in site-packages: {'site-packages' in str(pkg_dir)}")

            data_dir = pkg_dir / "data"
            print(f"Data directory: {data_dir}")
            print(f"Data directory exists: {data_dir.exists()}")

            if data_dir.exists():
                print("\nFiles in data/:")
                for f in sorted(data_dir.iterdir()):
                    if f.is_file():
                        print(f"  ✅ {f.name}")
                    elif f.is_dir():
                        print(f"  📁 {f.name}/")
                        if f.name == ".cursor":
                            for rf in (f / "rules").iterdir():
                                if rf.is_file():
                                    print(f"      ✅ {rf.name}")

            # Test specific files
            test_files = [".editorconfig", ".flake8", ".cursorrules"]
            print("\nTesting file access:")
            for test_file in test_files:
                file_path = data_dir / test_file
                print(f"  {test_file}: {file_path.exists()} ({file_path})")
    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()

    # Try pkg_resources
    print("\n" + "=" * 60)
    print("Testing pkg_resources:")
    try:
        import pkg_resources

        try:
            path = pkg_resources.resource_filename("ai_coding_standards", "data/.editorconfig")
            print(f"  resource_filename: {path}")
            print(f"  Exists: {Path(path).exists()}")
        except Exception as e:
            print(f"  resource_filename failed: {e}")
    except ImportError:
        print("  pkg_resources not available")

    # Try importlib.resources
    print("\n" + "=" * 60)
    print("Testing importlib.resources:")
    try:
        import importlib.resources as res

        try:
            pkg = res.files("ai_coding_standards")
            data = pkg / "data" / ".editorconfig"
            print(f"  Files object: {pkg}")
            print(f"  Data file object: {data}")
            print(f"  Is file: {data.is_file() if hasattr(data, 'is_file') else 'N/A'}")
            if hasattr(data, "as_path"):
                try:
                    path = data.as_path()
                    print(f"  As path: {path}")
                except Exception as e:
                    print(f"  as_path() failed: {e}")
        except Exception as e:
            print(f"  importlib.resources failed: {e}")
            import traceback

            traceback.print_exc()
    except ImportError:
        print("  importlib.resources not available")

    print("=" * 60)


if __name__ == "__main__":
    main()
