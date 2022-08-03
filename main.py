"""
Latest Earthquake Apps
"""
from earthquake_package import extract_data, visualize_data

if __name__ == '__main__':
    print("Main Apps")
    final_result = extract_data()
    visualize_data(final_result)