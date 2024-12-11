import os
import shutil

def separate_images_by_extension(source_dir):
    # Names of destination folders
    train_dir = os.path.join(source_dir, 'train')
    train_mask_dir = os.path.join(source_dir, 'train_mask')
    
    # Create destination folders
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(train_mask_dir, exist_ok=True)
    
    # Traverse files in source directory
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        
        # Check file?
        if os.path.isfile(file_path):
            # Check by extension
            if filename.lower().endswith('.jpg'):
                print(f"Moving: {filename} -> {train_dir}")
                shutil.move(file_path, os.path.join(train_dir, filename))
            elif filename.lower().endswith('.png'):
                print(f"Moving: {filename} -> {train_mask_dir}")
                shutil.move(file_path, os.path.join(train_mask_dir, filename))
            else:
                print(f"Skipping (incompatible extension): {filename}")
        else:
            print(f"Skipping (not a file): {filename}")
    
    print("The images were separated SUCCESFULLY.")

# The path to the source directory (for example, './dataset')
source_directory = './data/train'
separate_images_by_extension(source_directory)
