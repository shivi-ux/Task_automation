import os
import shutil

# Define the directory to organize
TARGET_DIR = 'C:/Users/rakesh sariyam/Downloads'

# Define the file type categories and their corresponding extensions
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Archives': ['.zip', '.tar', '.gz', '.rar'],
}

def organize_files(target_dir):
    # Change the working directory to the target directory
    os.chdir(target_dir)

    # Create subfolders for each category
    for category in FILE_CATEGORIES.keys():
        if not os.path.exists(category):
            os.makedirs(category)

    # Move files into their respective folders
    for filename in os.listdir(target_dir):
        # Skip directories
        if os.path.isdir(filename):
            continue
        
        # Get the file extension
        file_extension = os.path.splitext(filename)[1].lower()
        
        # Determine the category and move the file
        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                shutil.move(filename, os.path.join(category, filename))
                print(f'Moved: {filename} to {category}/')
                moved = True
                break
        
        # If the file doesn't match any category, you can choose to handle it differently
        if not moved:
            print(f'Uncategorized file: {filename}')

if __name__ == '__main__':
    organize_files(TARGET_DIR)