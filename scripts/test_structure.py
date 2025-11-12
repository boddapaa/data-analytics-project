"""
Test Script to Verify Project Structure
This script checks that all required directories and files exist.
"""

import os
import sys


def check_structure():
    """Verify the project structure is correct"""
    
    # Get project root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    print("=" * 60)
    print("Data Analytics Project - Structure Verification")
    print("=" * 60)
    print(f"\nProject Root: {project_root}\n")
    
    # Required directories
    required_dirs = ['data', 'notebooks', 'scripts', 'plots']
    
    # Required files
    required_files = [
        'README.md',
        'requirements.txt',
        'data/sample_sales_data.csv',
        'scripts/generate_plots.py',
        'scripts/sql_queries.py',
        'scripts/export_for_bi.py',
        'scripts/dashboard.py',
        'notebooks/exploratory_analysis.ipynb'
    ]
    
    all_passed = True
    
    # Check directories
    print("Checking directories...")
    for dir_name in required_dirs:
        dir_path = os.path.join(project_root, dir_name)
        if os.path.isdir(dir_path):
            print(f"  ✓ {dir_name}/")
        else:
            print(f"  ✗ {dir_name}/ (MISSING)")
            all_passed = False
    
    # Check files
    print("\nChecking required files...")
    for file_path in required_files:
        full_path = os.path.join(project_root, file_path)
        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)
            print(f"  ✓ {file_path} ({size:,} bytes)")
        else:
            print(f"  ✗ {file_path} (MISSING)")
            all_passed = False
    
    # Check if plots exist
    print("\nChecking generated plots...")
    plots_dir = os.path.join(project_root, 'plots')
    if os.path.isdir(plots_dir):
        plot_files = [f for f in os.listdir(plots_dir) if f.endswith('.png')]
        if plot_files:
            print(f"  ✓ Found {len(plot_files)} plot(s):")
            for plot in sorted(plot_files):
                print(f"    - {plot}")
        else:
            print(f"  ℹ No plots generated yet (run generate_plots.py)")
    
    # Summary
    print("\n" + "=" * 60)
    if all_passed:
        print("✅ Project structure verification PASSED")
        print("=" * 60)
        print("\nNext steps:")
        print("  1. Run: python generate_plots.py")
        print("  2. Run: python sql_queries.py")
        print("  3. Run: python export_for_bi.py")
        print("  4. Run: streamlit run dashboard.py")
        return 0
    else:
        print("❌ Project structure verification FAILED")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    sys.exit(check_structure())
