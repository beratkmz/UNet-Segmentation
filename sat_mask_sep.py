import os
import shutil

def separate_images_by_extension(source_dir):
    # Hedef klasörlerin adları
    train_sat_dir = os.path.join(source_dir, 'train_sat')
    train_mask_dir = os.path.join(source_dir, 'train_mask')
    
    # Hedef klasörleri oluştur
    os.makedirs(train_sat_dir, exist_ok=True)
    os.makedirs(train_mask_dir, exist_ok=True)
    
    # Kaynak dizinindeki dosyaları gez
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        
        # Dosya mı kontrol et
        if os.path.isfile(file_path):
            # Uzantısına göre kontrol et
            if filename.lower().endswith('.jpg'):
                print(f"Taşınıyor: {filename} -> {train_sat_dir}")
                shutil.move(file_path, os.path.join(train_sat_dir, filename))
            elif filename.lower().endswith('.png'):
                print(f"Taşınıyor: {filename} -> {train_mask_dir}")
                shutil.move(file_path, os.path.join(train_mask_dir, filename))
            else:
                print(f"Atlanıyor (uyumsuz uzantı): {filename}")
        else:
            print(f"Atlanıyor (dosya değil): {filename}")
    
    print("Resimler başarıyla ayrıldı.")

# Kaynak dizinin yolu (örneğin, './dataset' gibi)
source_directory = './src/data/train'
separate_images_by_extension(source_directory)
