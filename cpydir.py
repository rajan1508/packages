import shutil
import os

def copy_files(source_folder, destination_folder):
    try:
        # Create the destination folder if it doesn't exist
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Iterate over files in the source folder
        for filename in os.listdir(source_folder):
            source_file = os.path.join(source_folder, filename)
            destination_file = os.path.join(destination_folder, filename)

            # Check if the file already exists in the destination folder
            if os.path.exists(destination_file):
                print(f"File '{filename}' already exists in the destination folder. Skipping...")
            else:
                # Copy the file from source to destination
                shutil.copy2(source_file, destination_file)
                print(f"File '{filename}' copied successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
source_folder = "/path/to/source_folder"
destination_folder = "/path/to/destination_folder"

copy_files(source_folder, destination_folder)
